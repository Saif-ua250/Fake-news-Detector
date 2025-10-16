"""
Simple Offline Fake News Detector - Rule-Based Fallback

This module provides a simple rule-based fake news detection system
that works offline when Hugging Face models are not available.
"""

import re
from typing import Dict, Any
import logging

logger = logging.getLogger(__name__)

# Keywords and patterns associated with fake news
FAKE_NEWS_INDICATORS = {
    'sensational_words': [
        'shocking', 'unbelievable', 'you won\'t believe', 'secret', 'exposed',
        'revealed', 'bombshell', 'scandal', 'breaking', 'urgent', 'alert',
        'exclusive', 'leaked', 'cover-up', 'conspiracy', 'hoax'
    ],
    'clickbait_patterns': [
        r'number \d+ will',
        r'what happened next',
        r'doctors hate',
        r'they don\'t want you to know',
        r'this one weird trick',
        r'shocking truth'
    ],
    'excessive_punctuation': r'[!?]{2,}',
    'all_caps': r'\b[A-Z]{4,}\b'
}

REAL_NEWS_INDICATORS = {
    'source_attribution': [
        'according to', 'sources say', 'officials said', 'reported by',
        'confirmed by', 'stated', 'announced', 'published'
    ],
    'formal_language': [
        'however', 'therefore', 'furthermore', 'moreover', 'consequently',
        'additionally', 'meanwhile'
    ]
}


def analyze_text_simple(text: str) -> Dict[str, Any]:
    """
    Perform simple rule-based analysis of text.
    
    Args:
        text: Text to analyze
        
    Returns:
        Dict with label and score
    """
    text_lower = text.lower()
    
    # Count fake news indicators
    fake_score = 0
    real_score = 0
    
    # Check for sensational words
    for word in FAKE_NEWS_INDICATORS['sensational_words']:
        if word in text_lower:
            fake_score += 2
    
    # Check for clickbait patterns
    for pattern in FAKE_NEWS_INDICATORS['clickbait_patterns']:
        if re.search(pattern, text_lower):
            fake_score += 3
    
    # Check for excessive punctuation
    if re.search(FAKE_NEWS_INDICATORS['excessive_punctuation'], text):
        fake_score += 2
    
    # Check for excessive caps
    caps_matches = re.findall(FAKE_NEWS_INDICATORS['all_caps'], text)
    fake_score += len(caps_matches)
    
    # Check for real news indicators
    for phrase in REAL_NEWS_INDICATORS['source_attribution']:
        if phrase in text_lower:
            real_score += 3
    
    for word in REAL_NEWS_INDICATORS['formal_language']:
        if word in text_lower:
            real_score += 1
    
    # Calculate final score
    total_score = fake_score + real_score
    if total_score == 0:
        # Not enough information, default to cautious "Real"
        confidence = 0.55
        label = "Real"
    else:
        fake_probability = fake_score / total_score
        if fake_probability > 0.5:
            label = "Fake"
            confidence = 0.5 + (fake_probability - 0.5) * 0.5  # Scale to 0.5-1.0
        else:
            label = "Real"
            confidence = 0.5 + (1 - fake_probability - 0.5) * 0.5
    
    return {
        'label': label,
        'score': confidence,
        'raw': {
            'fake_score': fake_score,
            'real_score': real_score,
            'method': 'rule-based-offline'
        }
    }


def load_text_model_with_fallback(device: int = -1):
    """
    Load model with fallback to offline mode.
    
    Args:
        device: Device for model (-1 for CPU)
        
    Returns:
        Model pipeline or simple analyzer
    """
    try:
        from transformers import pipeline
        import os
        
        HF_TOKEN = os.getenv("HUGGINGFACE_TOKEN", None)
        TEXT_MODEL = os.getenv("TEXT_MODEL", "hamzab/roberta-fake-news-classification")
        
        logger.info(f"Attempting to load model: {TEXT_MODEL}")
        
        pipeline_kwargs = {
            "model": TEXT_MODEL,
            "device": device
        }
        
        if HF_TOKEN:
            pipeline_kwargs["token"] = HF_TOKEN
        
        model = pipeline("text-classification", **pipeline_kwargs)
        logger.info("✅ Successfully loaded Hugging Face model")
        return {'type': 'huggingface', 'model': model}
        
    except Exception as e:
        logger.warning(f"⚠️ Cannot load Hugging Face model: {str(e)[:100]}")
        logger.info("📋 Falling back to offline rule-based detection")
        return {'type': 'offline', 'model': None}


def classify_text_with_fallback(model_info: dict, text: str, max_length: int = 1024) -> Dict[str, Any]:
    """
    Classify text using available method.
    
    Args:
        model_info: Model information from load_text_model_with_fallback
        text: Text to classify
        max_length: Maximum length
        
    Returns:
        Classification result
    """
    if not text or not text.strip():
        raise ValueError("Input text cannot be empty")
    
    if model_info['type'] == 'huggingface':
        # Use Hugging Face model
        try:
            truncated_text = text[:max_length]
            result = model_info['model'](truncated_text)[0]
            
            # Normalize labels
            label = result['label']
            if 'fake' in label.lower():
                normalized_label = 'Fake'
            elif 'real' in label.lower() or 'true' in label.lower():
                normalized_label = 'Real'
            else:
                normalized_label = label
            
            return {
                'label': normalized_label,
                'score': result['score'],
                'raw': result,
                'method': 'ai-model'
            }
        except Exception as e:
            logger.error(f"Model classification failed: {e}")
            logger.info("Falling back to rule-based detection")
            return analyze_text_simple(text)
    else:
        # Use offline rule-based detection
        result = analyze_text_simple(text)
        result['method'] = 'offline-rules'
        return result
