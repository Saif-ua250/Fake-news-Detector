"""
Fake News Text Classification Module

This module provides functionality to detect fake news in text using a pre-trained
BERT-based model from Hugging Face.

Model: jy46604790/Fake-News-Bert-Detect
"""

import logging
import os
from typing import Dict, Any, Optional
from transformers import pipeline

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Load Hugging Face token from environment (optional)
HF_TOKEN = os.getenv("HUGGINGFACE_TOKEN", None)
TEXT_MODEL = os.getenv("TEXT_MODEL", "jy46604790/Fake-News-Bert-Detect")


def load_text_model(device: int = -1):
    """
    Load the fake news detection model pipeline.
    
    Args:
        device (int): Device to run inference on.
                     -1 for CPU (default), 0 for GPU, 1+ for multi-GPU setups.
    
    Returns:
        Pipeline: A Hugging Face text-classification pipeline ready for inference.
    
    Raises:
        Exception: If model loading fails (network issues, memory, etc.)
    
    Example:
        >>> pipe = load_text_model(device=-1)
        >>> # Model is now ready for classification
    """
    try:
        logger.info(f"Loading fake news detection model: {TEXT_MODEL}")
        
        # Prepare pipeline arguments
        pipeline_kwargs = {
            "model": TEXT_MODEL,
            "device": device
        }
        
        # Add token if available (for private models or avoiding rate limits)
        if HF_TOKEN:
            pipeline_kwargs["token"] = HF_TOKEN
            logger.info("Using Hugging Face authentication token")
        
        # Load the text-classification pipeline with the specified model
        text_pipeline = pipeline("text-classification", **pipeline_kwargs)
        
        logger.info("✓ Fake news model loaded successfully")
        return text_pipeline
        
    except Exception as e:
        logger.error(f"Failed to load fake news model: {e}")
        raise


def classify_text(pipe, text: str, max_length: int = 1024) -> Dict[str, Any]:
    """
    Classify text as fake or real news.
    
    Args:
        pipe: The loaded Hugging Face pipeline from load_text_model()
        text (str): The news text to classify (article body, headline, etc.)
        max_length (int): Maximum character length to process (default: 1024)
                         Note: BERT models typically support up to 512 tokens
    
    Returns:
        Dict[str, Any]: Classification result containing:
            - label (str): Human-readable label ("Fake" or "Real")
            - score (float): Confidence score (0-1)
            - raw (Dict): Raw model output with original labels
    
    Raises:
        ValueError: If text is empty or None
        Exception: If classification fails
    
    Example:
        >>> pipe = load_text_model()
        >>> result = classify_text(pipe, "Breaking news: extraordinary claim!")
        >>> print(f"{result['label']} (confidence: {result['score']:.2%})")
    """
    # Validate input
    if not text or not text.strip():
        raise ValueError("Input text cannot be empty")
    
    try:
        # Run inference - truncate text to max_length for BERT compatibility
        # Most BERT models have a 512 token limit, but we accept longer text
        # and truncate it here to prevent errors
        truncated_text = text[:max_length]
        raw_result = pipe(truncated_text, truncation=True, max_length=512)
        
        # Extract result (pipeline returns a list with one dict)
        if isinstance(raw_result, list):
            raw_result = raw_result[0]
        
        raw_label = raw_result["label"]
        raw_score = raw_result["score"]
        
        # Map model labels to human-readable labels
        # Try to use model's id2label mapping first
        human_label = _map_label_to_human(pipe, raw_label)
        
        logger.info(f"Classification: {human_label} (confidence: {raw_score:.4f})")
        
        return {
            "label": human_label,
            "score": raw_score,
            "raw": raw_result
        }
        
    except Exception as e:
        logger.error(f"Classification failed: {e}")
        raise


def _map_label_to_human(pipe, model_label: str) -> str:
    """
    Map model output labels (e.g., LABEL_0, LABEL_1) to human-readable labels.
    
    Args:
        pipe: The pipeline object with model config
        model_label (str): Raw label from model (e.g., "LABEL_0")
    
    Returns:
        str: Human-readable label ("Fake" or "Real")
    
    Note:
        This function first tries to use the model's id2label configuration.
        If not available, it falls back to a default mapping where:
        - LABEL_0 typically means "Fake"
        - LABEL_1 typically means "Real"
    """
    try:
        # Try to get id2label from model config
        if hasattr(pipe.model, 'config') and hasattr(pipe.model.config, 'id2label'):
            id2label = pipe.model.config.id2label
            
            # Extract numeric ID from label string (e.g., "LABEL_0" -> 0)
            if model_label.startswith("LABEL_"):
                label_id = int(model_label.split("_")[1])
                if label_id in id2label:
                    config_label = id2label[label_id].lower()
                    # Normalize to "Fake" or "Real"
                    if "fake" in config_label:
                        return "Fake"
                    elif "real" in config_label or "true" in config_label:
                        return "Real"
    except Exception as e:
        logger.debug(f"Could not use model config for label mapping: {e}")
    
    # Fallback mapping based on common conventions
    # For most binary fake news classifiers:
    # LABEL_0 = Fake, LABEL_1 = Real
    label_mapping = {
        "LABEL_0": "Fake",
        "LABEL_1": "Real",
        # Additional fallbacks
        "0": "Fake",
        "1": "Real",
        "fake": "Fake",
        "real": "Real",
    }
    
    return label_mapping.get(model_label, model_label)


def get_model_info(pipe) -> Dict[str, Any]:
    """
    Get information about the loaded model's label configuration.
    
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
    print("Fake News Text Classifier - Demo")
    print("=" * 60)
    
    # Sample texts for testing
    test_texts = [
        "Scientists confirm that drinking water is essential for human health.",
        "BREAKING: Aliens land in major city, government confirms contact!",
        "New study shows moderate exercise improves cardiovascular health.",
        "SHOCKING: Celebrity reveals secret to eternal youth!"
    ]
    
    try:
        # Load model
        print("\n[1] Loading model...")
        text_pipe = load_text_model(device=-1)
        
        # Show model info
        print("\n[2] Model Information:")
        model_info = get_model_info(text_pipe)
        print(f"    Model: {model_info['model_name']}")
        print(f"    Label mapping: {model_info['id2label']}")
        
        # Classify sample texts
        print("\n[3] Classifying sample texts:")
        print("-" * 60)
        
        for i, text in enumerate(test_texts, 1):
            print(f"\nText {i}: \"{text[:60]}...\"" if len(text) > 60 else f"\nText {i}: \"{text}\"")
            
            result = classify_text(text_pipe, text)
            
            print(f"Result: {result['label']}")
            print(f"Confidence: {result['score']:.2%}")
            print(f"Raw label: {result['raw']['label']}")
        
        print("\n" + "=" * 60)
        print("✓ Demo completed successfully!")
        print("=" * 60)
        
    except Exception as e:
        print(f"\n✗ Error during demo: {e}")
        import traceback
        traceback.print_exc()
