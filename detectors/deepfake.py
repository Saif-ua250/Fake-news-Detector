"""
Deepfake Detection Module

This module provides functionality to detect deepfakes in images and videos using
a pre-trained image classification model from Hugging Face.

Model: prithivMLmods/Deep-Fake-Detector-v2-Model
"""

import logging
import os
from typing import Dict, Any, List
from transformers import pipeline
from utils import video_utils

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Load Hugging Face token from environment (optional)
HF_TOKEN = os.getenv("HUGGINGFACE_TOKEN", None)
IMAGE_MODEL = os.getenv("IMAGE_MODEL", "prithivMLmods/Deep-Fake-Detector-v2-Model")


def load_image_model(device: int = -1):
    """
    Load the deepfake detection model pipeline.
    
    Args:
        device (int): Device to run inference on.
                     -1 for CPU (default), 0 for GPU, 1+ for multi-GPU setups.
    
    Returns:
        Pipeline: A Hugging Face image-classification pipeline ready for inference.
    
    Raises:
        Exception: If model loading fails (network issues, memory, etc.)
    
    Example:
        >>> pipe = load_image_model(device=-1)
        >>> # Model is now ready for classification
    """
    try:
        logger.info(f"Loading deepfake detection model: {IMAGE_MODEL}")
        
        # Prepare pipeline arguments
        pipeline_kwargs = {
            "model": IMAGE_MODEL,
            "device": device
        }
        
        # Add token if available (for private models or avoiding rate limits)
        if HF_TOKEN:
            pipeline_kwargs["token"] = HF_TOKEN
            logger.info("Using Hugging Face authentication token")
        
        # Load the image-classification pipeline with the specified model
        image_pipeline = pipeline("image-classification", **pipeline_kwargs)
        
        logger.info("✓ Deepfake model loaded successfully")
        return image_pipeline
        
    except Exception as e:
        logger.error(f"Failed to load deepfake model: {e}")
        raise


def classify_image(pipe, image_path: str) -> Dict[str, Any]:
    """
    Classify an image as deepfake or real.
    
    Args:
        pipe: The loaded Hugging Face pipeline from load_image_model()
        image_path (str): Path to the image file to analyze
    
    Returns:
        Dict[str, Any]: Classification result containing:
            - label (str): Human-readable label ("Deepfake" or "Real")
            - score (float): Confidence score (0-1)
            - raw (List[Dict]): Raw model output with all predictions
    
    Raises:
        FileNotFoundError: If image file doesn't exist
        Exception: If classification fails
    
    Example:
        >>> pipe = load_image_model()
        >>> result = classify_image(pipe, "photo.jpg")
        >>> print(f"{result['label']} (confidence: {result['score']:.2%})")
    """
    try:
        # Run inference
        raw_results = pipe(image_path)
        
        # Get top prediction
        if isinstance(raw_results, list) and len(raw_results) > 0:
            top_result = raw_results[0]
            raw_label = top_result["label"]
            raw_score = top_result["score"]
        else:
            raise Exception("Unexpected model output format")
        
        # Map model labels to human-readable labels
        human_label = _map_label_to_human(pipe, raw_label)
        
        logger.info(f"Classification: {human_label} (confidence: {raw_score:.4f})")
        
        return {
            "label": human_label,
            "score": raw_score,
            "raw": raw_results
        }
        
    except Exception as e:
        logger.error(f"Image classification failed: {e}")
        raise


def classify_video(pipe, video_path: str, sample_rate: int = 1) -> Dict[str, Any]:
    """
    Classify a video as deepfake or real by analyzing sampled frames.
    
    This function extracts frames from the video at the specified sample rate,
    classifies each frame, and aggregates the results using majority vote
    and average confidence.
    
    Args:
        pipe: The loaded Hugging Face pipeline from load_image_model()
        video_path (str): Path to the video file to analyze
        sample_rate (int): Frames to extract per second (default: 1)
    
    Returns:
        Dict[str, Any]: Aggregated classification result containing:
            - label (str): Final verdict ("Deepfake" or "Real")
            - score (float): Average confidence score across all frames
            - frame_count (int): Number of frames analyzed
            - frame_results (List[Dict]): Individual results for each frame
            - deepfake_count (int): Number of frames classified as deepfake
            - real_count (int): Number of frames classified as real
    
    Raises:
        FileNotFoundError: If video file doesn't exist
        Exception: If frame extraction or classification fails
    
    Example:
        >>> pipe = load_image_model()
        >>> result = classify_video(pipe, "video.mp4", sample_rate=2)
        >>> print(f"Video: {result['label']} ({result['frame_count']} frames analyzed)")
    """
    try:
        logger.info(f"Processing video: {video_path}")
        
        # Extract frames from video
        frame_paths = video_utils.extract_sample_frames(video_path, sample_rate=sample_rate)
        
        if not frame_paths:
            raise Exception("No frames could be extracted from video")
        
        logger.info(f"Analyzing {len(frame_paths)} frames...")
        
        # Classify each frame
        frame_results = []
        deepfake_count = 0
        real_count = 0
        total_score = 0.0
        
        for i, frame_path in enumerate(frame_paths):
            try:
                result = classify_image(pipe, frame_path)
                frame_results.append(result)
                
                # Count classifications
                if "fake" in result["label"].lower():
                    deepfake_count += 1
                else:
                    real_count += 1
                
                total_score += result["score"]
                
                logger.debug(f"Frame {i+1}/{len(frame_paths)}: {result['label']} ({result['score']:.2f})")
                
            except Exception as e:
                logger.warning(f"Failed to classify frame {i+1}: {e}")
                continue
        
        # Calculate aggregated result
        if not frame_results:
            raise Exception("No frames could be successfully classified")
        
        # Majority vote for final label
        final_label = "Deepfake" if deepfake_count > real_count else "Real"
        
        # Average confidence score
        avg_score = total_score / len(frame_results)
        
        # If it's close, adjust confidence
        margin = abs(deepfake_count - real_count) / len(frame_results)
        adjusted_score = avg_score * (0.5 + margin * 0.5)  # Scale confidence by margin
        
        logger.info(f"Video analysis complete: {final_label} (avg confidence: {avg_score:.4f})")
        logger.info(f"Frames: {deepfake_count} deepfake, {real_count} real")
        
        return {
            "label": final_label,
            "score": adjusted_score,
            "frame_count": len(frame_results),
            "frame_results": frame_results,
            "deepfake_count": deepfake_count,
            "real_count": real_count,
            "raw": {
                "majority_vote": final_label,
                "average_confidence": avg_score,
                "adjusted_confidence": adjusted_score,
                "vote_margin": margin
            }
        }
        
    except Exception as e:
        logger.error(f"Video classification failed: {e}")
        raise


def _map_label_to_human(pipe, model_label: str) -> str:
    """
    Map model output labels to human-readable labels.
    
    Args:
        pipe: The pipeline object with model config
        model_label (str): Raw label from model
    
    Returns:
        str: Human-readable label ("Deepfake" or "Real")
    
    Note:
        Different models may use different label conventions.
        This function tries to intelligently map various labels to
        "Deepfake" or "Real" based on common patterns.
    """
    label_lower = model_label.lower()
    
    # Common deepfake indicators
    fake_indicators = ["fake", "deepfake", "manipulated", "synthetic", "generated", "altered"]
    real_indicators = ["real", "authentic", "genuine", "original", "natural"]
    
    # Check for fake indicators
    for indicator in fake_indicators:
        if indicator in label_lower:
            return "Deepfake"
    
    # Check for real indicators
    for indicator in real_indicators:
        if indicator in label_lower:
            return "Real"
    
    # Try to use model config if available
    try:
        if hasattr(pipe.model, 'config') and hasattr(pipe.model.config, 'id2label'):
            id2label = pipe.model.config.id2label
            # Look through all labels for hints
            for idx, label in id2label.items():
                label_check = label.lower()
                for indicator in fake_indicators:
                    if indicator in label_check and indicator in label_lower:
                        return "Deepfake"
                for indicator in real_indicators:
                    if indicator in label_check and indicator in label_lower:
                        return "Real"
    except Exception:
        pass
    
    # Default: return original label if no mapping found
    logger.warning(f"Could not map label '{model_label}' to standard format")
    return model_label


def get_model_info(pipe) -> Dict[str, Any]:
    """
    Get information about the loaded model's configuration.
    
    Args:
        pipe: The loaded pipeline
    
    Returns:
        Dict[str, Any]: Model configuration info including label mappings
    """
    info = {
        "model_name": pipe.model.config.name_or_path if hasattr(pipe.model, 'config') else "unknown",
        "id2label": {}
    }
    
    try:
        if hasattr(pipe.model, 'config') and hasattr(pipe.model.config, 'id2label'):
            info["id2label"] = pipe.model.config.id2label
    except Exception:
        pass
    
    return info


# Demo and testing code
if __name__ == "__main__":
    print("=" * 60)
    print("Deepfake Detection - Demo")
    print("=" * 60)
    
    print("\n⚠️  Note: Requires image/video files for testing")
    print("\nExample usage:")
    print("-" * 60)
    
    print("""
# Load model
pipe = load_image_model(device=-1)

# Classify image
result = classify_image(pipe, "photo.jpg")
print(f"Image: {result['label']} (confidence: {result['score']:.2%})")

# Classify video
video_result = classify_video(pipe, "video.mp4", sample_rate=1)
print(f"Video: {video_result['label']}")
print(f"Analyzed {video_result['frame_count']} frames")
print(f"Deepfake frames: {video_result['deepfake_count']}")
print(f"Real frames: {video_result['real_count']}")
    """)
    
    print("\n" + "=" * 60)
    print("✓ Module loaded successfully")
    print("=" * 60)
