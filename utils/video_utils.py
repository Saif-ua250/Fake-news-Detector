"""
Video Processing Utilities Module

This module provides functionality to extract frames from video files for deepfake analysis.
Uses OpenCV (cv2) for video processing.
"""

import logging
import os
import tempfile
from typing import List
from pathlib import Path
import cv2

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def extract_sample_frames(video_path: str, sample_rate: int = 1) -> List[str]:
    """
    Extract sample frames from a video file.
    
    Args:
        video_path (str): Path to the video file
        sample_rate (int): Number of frames to extract per second (default: 1)
                          Higher values extract more frames but increase processing time
    
    Returns:
        List[str]: List of file paths to extracted frame images
    
    Raises:
        FileNotFoundError: If video file doesn't exist
        Exception: If video cannot be opened or processed
    
    Example:
        >>> frames = extract_sample_frames("video.mp4", sample_rate=2)
        >>> print(f"Extracted {len(frames)} frames")
    """
    # Validate video file exists
    if not os.path.exists(video_path):
        raise FileNotFoundError(f"Video file not found: {video_path}")
    
    try:
        logger.info(f"Opening video: {video_path}")
        
        # Open video file
        cap = cv2.VideoCapture(video_path)
        
        if not cap.isOpened():
            raise Exception("Could not open video file")
        
        # Get video properties
        fps = cap.get(cv2.CAP_PROP_FPS)
        total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
        duration = total_frames / fps if fps > 0 else 0
        
        logger.info(f"Video info: {fps:.2f} fps, {total_frames} frames, {duration:.2f}s duration")
        
        # Calculate frame interval based on sample rate
        # sample_rate = frames per second to extract
        frame_interval = max(1, int(fps / sample_rate)) if fps > 0 else 1
        
        logger.info(f"Extracting 1 frame every {frame_interval} frames (≈{sample_rate} fps)")
        
        # Extract frames
        frame_paths = []
        frame_count = 0
        saved_count = 0
        
        # Create temp directory for frames
        temp_dir = tempfile.mkdtemp(prefix="video_frames_")
        
        while True:
            ret, frame = cap.read()
            
            if not ret:
                break
            
            # Save frame at specified interval
            if frame_count % frame_interval == 0:
                frame_filename = os.path.join(temp_dir, f"frame_{saved_count:04d}.jpg")
                cv2.imwrite(frame_filename, frame)
                frame_paths.append(frame_filename)
                saved_count += 1
                
                # Limit to reasonable number of frames (max 100)
                if saved_count >= 100:
                    logger.warning("Reached maximum of 100 frames, stopping extraction")
                    break
            
            frame_count += 1
        
        cap.release()
        
        logger.info(f"✓ Extracted {len(frame_paths)} frames to {temp_dir}")
        
        if not frame_paths:
            raise Exception("No frames could be extracted from video")
        
        return frame_paths
        
    except Exception as e:
        logger.error(f"Failed to extract frames: {e}")
        raise Exception(f"Could not extract frames from video: {str(e)}")


def cleanup_frames(frame_paths: List[str]):
    """
    Clean up temporary frame files.
    
    Args:
        frame_paths (List[str]): List of frame file paths to delete
    
    Example:
        >>> cleanup_frames(frame_paths)
    """
    for frame_path in frame_paths:
        try:
            if os.path.exists(frame_path):
                os.unlink(frame_path)
        except Exception as e:
            logger.warning(f"Could not delete frame {frame_path}: {e}")
    
    # Try to remove parent directory if empty
    if frame_paths:
        try:
            parent_dir = os.path.dirname(frame_paths[0])
            if os.path.exists(parent_dir) and not os.listdir(parent_dir):
                os.rmdir(parent_dir)
                logger.info(f"Cleaned up temp directory: {parent_dir}")
        except Exception as e:
            logger.warning(f"Could not remove temp directory: {e}")


def get_video_info(video_path: str) -> dict:
    """
    Get basic information about a video file.
    
    Args:
        video_path (str): Path to the video file
    
    Returns:
        dict: Video information including fps, frame count, duration, resolution
    
    Example:
        >>> info = get_video_info("video.mp4")
        >>> print(f"Duration: {info['duration']:.2f}s")
    """
    if not os.path.exists(video_path):
        raise FileNotFoundError(f"Video file not found: {video_path}")
    
    try:
        cap = cv2.VideoCapture(video_path)
        
        if not cap.isOpened():
            raise Exception("Could not open video file")
        
        info = {
            "fps": cap.get(cv2.CAP_PROP_FPS),
            "frame_count": int(cap.get(cv2.CAP_PROP_FRAME_COUNT)),
            "width": int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)),
            "height": int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)),
        }
        
        info["duration"] = info["frame_count"] / info["fps"] if info["fps"] > 0 else 0
        info["resolution"] = f"{info['width']}x{info['height']}"
        
        cap.release()
        
        return info
        
    except Exception as e:
        logger.error(f"Failed to get video info: {e}")
        raise


# Demo code
if __name__ == "__main__":
    print("=" * 60)
    print("Video Processing Utilities - Demo")
    print("=" * 60)
    
    print("\n⚠️  Note: Requires a video file for testing")
    print("\nExample usage:")
    print("-" * 60)
    
    print("""
# Extract frames from video
frames = extract_sample_frames("sample_video.mp4", sample_rate=1)
print(f"Extracted {len(frames)} frames")

# Get video info
info = get_video_info("sample_video.mp4")
print(f"Video: {info['resolution']}, {info['fps']:.2f} fps, {info['duration']:.2f}s")

# Clean up after processing
cleanup_frames(frames)
    """)
    
    print("\n" + "=" * 60)
    print("✓ Module loaded successfully")
    print("=" * 60)
