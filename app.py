"""
FakeNews + Deepfake Detector - Professional Edition
Nothing Phone Inspired UI with 3D Elements

A comprehensive web app for detecting fake news in text/URLs and deep
Uses pre-trained Hugging Face models for analysis.
"""

import streamlit as st
import os
import tempfile
from pathlib import Path
import logging
import time
from datetime import datetime
from dotenv import load_dotenv

# Load environment variables from .env file (for Hugging Face token)
load_dotenv()

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Import detection modules with better error handling
try:
    from detectors import fake_news, deepfake
    from utils import scraper, video_utils, newsapi_client
    from utils import virustotal_client, gemini_client
    IMPORTS_SUCCESS = True
    NEWSAPI_AVAILABLE = newsapi_client.is_newsapi_configured()
    VT_AVAILABLE = virustotal_client.is_configured()
    GEMINI_AVAILABLE = gemini_client.is_configured()
except ImportError as e:
    IMPORTS_SUCCESS = False
    IMPORT_ERROR = str(e)
    NEWSAPI_AVAILABLE = False
    VT_AVAILABLE = False
    GEMINI_AVAILABLE = False


# ============================================================================
# PAGE CONFIGURATION
# ============================================================================

st.set_page_config(
    page_title="Truth Lens - AI Detector",
    page_icon="🔍",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ============================================================================
# MODERN CSS STYLING - Nothing Phone Inspired
# ============================================================================

def load_custom_css():
    """Load custom CSS for professional Nothing Phone-inspired UI."""
    st.markdown("""
    <style>
    /* Import Google Fonts */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&display=swap');
    
    /* Global Styles */
    * {
        font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
    }
    
    /* Main Background with gradient and 3D honeycomb */
    .stApp {
        background: linear-gradient(135deg, #0a0a0a 0%, #1a1a1a 50%, #0f0f0f 100%);
        color: #ffffff;
        position: relative;
        min-height: 100vh;
        overflow-x: hidden;
        overflow-y: auto;
    }
    
    /* Make sure all content is above background effects */
    .main .block-container {
        position: relative;
        z-index: 10;
        opacity: 1 !important;
        visibility: visible !important;
        padding-top: 2rem;
        padding-bottom: 3rem;
        max-width: 1200px;
    }
    
    /* Ensure main content area is visible */
    section.main {
        z-index: 10;
        opacity: 1 !important;
        visibility: visible !important;
        display: block !important;
    }
    
    /* Honeycomb SVG Pattern Overlay - Behind ALL content */
    .stApp::before {
        content: '';
        position: fixed;
        inset: 0;
        z-index: -2;
        pointer-events: none;
        opacity: 0.06;
        background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='100' height='87' viewBox='0 0 100 87'%3E%3Cg fill='none' stroke='%2300d4ff' stroke-width='1.5'%3E%3Cpath d='M50,0 L100,25 L100,62 L50,87 L0,62 L0,25 Z'/%3E%3C/g%3E%3C/svg%3E");
        background-size: 70px 60px;
        animation: honeycombFloat 30s ease-in-out infinite;
    }
    
    /* Grid Lines Effect - Behind ALL content */
    .stApp::after {
        content: '';
        position: fixed;
        inset: 0;
        z-index: -1;
        pointer-events: none;
        background-image: 
            linear-gradient(rgba(0, 212, 255, 0.02) 1px, transparent 1px),
            linear-gradient(90deg, rgba(0, 212, 255, 0.02) 1px, transparent 1px);
        background-size: 50px 50px;
    }
    
    @keyframes honeycombFloat {
        0%, 100% { transform: translate(0, 0); opacity: 0.06; }
        50% { transform: translate(20px, -20px); opacity: 0.1; }
    }
    
    /* Header Styling - Enhanced with 3D depth */
    .main-header {
        background: linear-gradient(135deg, rgba(255,255,255,0.05) 0%, rgba(255,255,255,0.02) 100%);
        backdrop-filter: blur(20px);
        border: 1px solid rgba(0, 212, 255, 0.2);
        border-radius: 24px;
        padding: 2rem 2.5rem;
        margin-bottom: 2rem;
        box-shadow: 
            0 8px 32px rgba(0,0,0,0.3),
            0 0 30px rgba(0, 212, 255, 0.1),
            inset 0 1px 0 rgba(255,255,255,0.1);
        position: relative;
        overflow: hidden;
        z-index: 100;
        animation: headerPulse 4s ease-in-out infinite;
    }
    
    @keyframes headerPulse {
        0%, 100% { box-shadow: 0 8px 32px rgba(0,0,0,0.3), 0 0 30px rgba(0, 212, 255, 0.1), inset 0 1px 0 rgba(255,255,255,0.1); }
        50% { box-shadow: 0 8px 32px rgba(0,0,0,0.3), 0 0 50px rgba(0, 212, 255, 0.2), inset 0 1px 0 rgba(255,255,255,0.1); }
    }
    
    .main-title {
        font-size: 3.5rem;
        font-weight: 900;
        background: linear-gradient(135deg, #00d4ff 0%, #ffffff 50%, #b537ff 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin: 0;
        letter-spacing: -0.05em;
        text-shadow: 0 0 40px rgba(0, 212, 255, 0.3);
        animation: titleShimmer 3s ease-in-out infinite;
        position: relative;
        z-index: 1;
    }
    
    @keyframes titleShimmer {
        0%, 100% { filter: brightness(1) drop-shadow(0 0 10px rgba(0, 212, 255, 0.3)); }
        50% { filter: brightness(1.2) drop-shadow(0 0 20px rgba(0, 212, 255, 0.5)); }
    }
    
    .main-subtitle {
        font-size: 1.2rem;
        color: #888;
        margin-top: 0.5rem;
        font-weight: 400;
        letter-spacing: 0.05em;
    }
    
    /* Card Styling - 3D Effect with Holographic Border */
    .glass-card {
        background: linear-gradient(135deg, rgba(255,255,255,0.08) 0%, rgba(255,255,255,0.04) 100%);
        backdrop-filter: blur(20px);
        border: 1px solid rgba(0, 212, 255, 0.2);
        border-radius: 20px;
        padding: 2rem;
        margin: 1.5rem 0;
        box-shadow: 
            0 8px 32px rgba(0,0,0,0.4),
            0 0 20px rgba(0, 212, 255, 0.1);
        transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
        position: relative;
        z-index: 100;
        transform-style: preserve-3d;
    }
    
    .glass-card:hover {
        transform: translateY(-5px) rotateX(2deg);
        box-shadow: 
            0 12px 48px rgba(0,0,0,0.5),
            0 0 40px rgba(0, 212, 255, 0.3),
            inset 0 1px 0 rgba(255,255,255,0.1);
        border-color: rgba(0, 255, 255, 0.4);
    }
    
    /* Animated border glow */
    .glass-card::before {
        content: '';
        position: absolute;
        inset: -1px;
        border-radius: 20px;
        padding: 1px;
        background: linear-gradient(45deg, 
            transparent 30%, 
            rgba(0, 212, 255, 0.4) 50%, 
            transparent 70%);
        -webkit-mask: linear-gradient(#fff 0 0) content-box, linear-gradient(#fff 0 0);
        -webkit-mask-composite: xor;
        mask-composite: exclude;
        opacity: 0;
        transition: opacity 0.4s;
        pointer-events: none;
        animation: borderGlow 3s linear infinite;
    }
    
    .glass-card:hover::before {
        opacity: 1;
    }
    
    @keyframes borderGlow {
        0% { background-position: 0% 50%; }
        100% { background-position: 200% 50%; }
    }


    
    /* Result Cards */
    .result-card-fake {
        background: linear-gradient(135deg, rgba(255,68,68,0.15) 0%, rgba(255,68,68,0.05) 100%);
        border: 2px solid rgba(255,68,68,0.4);
        border-radius: 20px;
        padding: 2rem;
        margin: 1rem 0;
        backdrop-filter: blur(10px);
        animation: slideIn 0.5s ease-out;
    }
    
    .result-card-real {
        background: linear-gradient(135deg, rgba(68,255,68,0.15) 0%, rgba(68,255,68,0.05) 100%);
        border: 2px solid rgba(68,255,68,0.4);
        border-radius: 20px;
        padding: 2rem;
        margin: 1rem 0;
        backdrop-filter: blur(10px);
        animation: slideIn 0.5s ease-out;
    }
    
    @keyframes slideIn {
        from {
            opacity: 0;
            transform: translateY(20px);
        }
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }
    
    /* Buttons - Futuristic with 3D press effect */
    .stButton > button {
        background: linear-gradient(135deg, #00d4ff 0%, #0088cc 100%);
        color: white;
        border: 1px solid rgba(0, 212, 255, 0.5);
        border-radius: 16px;
        padding: 1rem 2.5rem;
        font-size: 1.1rem;
        font-weight: 600;
        letter-spacing: 0.1em;
        box-shadow: 
            0 8px 24px rgba(0, 212, 255, 0.4),
            0 0 30px rgba(0, 212, 255, 0.2),
            inset 0 1px 0 rgba(255,255,255,0.2);
        transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
        text-transform: uppercase;
        position: relative;
        overflow: hidden;
        transform-style: preserve-3d;
    }
    
    .stButton > button::before {
        content: '';
        position: absolute;
        top: 50%;
        left: 50%;
        width: 0;
        height: 0;
        border-radius: 50%;
        background: rgba(255,255,255,0.3);
        transform: translate(-50%, -50%);
        transition: width 0.6s, height 0.6s;
    }
    
    .stButton > button:hover::before {
        width: 300px;
        height: 300px;
    }
    
    .stButton > button:hover {
        transform: translateY(-3px) scale(1.02);
        box-shadow: 
            0 12px 36px rgba(0, 212, 255, 0.6),
            0 0 50px rgba(0, 212, 255, 0.4),
            inset 0 1px 0 rgba(255,255,255,0.3);
        background: linear-gradient(135deg, #00ffff 0%, #00aaff 100%);
        border-color: rgba(0, 255, 255, 0.8);
    }
    
    .stButton > button:active {
        transform: translateY(-1px) scale(0.98);
        box-shadow: 
            0 4px 12px rgba(0, 212, 255, 0.3),
            inset 0 2px 4px rgba(0,0,0,0.2);
    }
    
    /* Sidebar Styling */
    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, #0f0f0f 0%, #1a1a1a 100%);
        border-right: 1px solid rgba(0, 212, 255, 0.2);
        z-index: 100;
    }
    
    [data-testid="stSidebar"] .element-container {
        backdrop-filter: blur(10px);
        position: relative;
        z-index: 100;
    }
    
    /* Radio Buttons */
    .stRadio > div {
        background: rgba(0, 20, 40, 0.4);
        border-radius: 12px;
        padding: 1rem;
        border: 1px solid rgba(0, 212, 255, 0.2);
        position: relative;
        z-index: 100;
    }
    
    /* File Uploader */
    [data-testid="stFileUploader"] {
        background: rgba(0, 20, 40, 0.4);
        border: 2px dashed rgba(0, 212, 255, 0.3);
        border-radius: 16px;
        padding: 2rem;
        transition: all 0.3s ease;
        position: relative;
        z-index: 100;
    }
    
    [data-testid="stFileUploader"]:hover {
        border-color: rgba(0, 255, 255, 0.6);
        background: rgba(0, 30, 50, 0.5);
        box-shadow: 0 0 20px rgba(0, 212, 255, 0.2);
    }
    
    /* Text Input - Holographic with neon glow */
    .stTextInput > div > div > input,
    .stTextArea > div > div > textarea {
        background: rgba(0,20,40,0.6);
        border: 1px solid rgba(0, 212, 255, 0.3);
        border-radius: 12px;
        color: white;
        padding: 1rem;
        font-size: 1rem;
        box-shadow: 
            inset 0 2px 4px rgba(0,0,0,0.3),
            0 0 10px rgba(0, 212, 255, 0.1);
        transition: all 0.3s ease;
    }
    
    .stTextInput > div > div > input:focus,
    .stTextArea > div > div > textarea:focus {
        border-color: rgba(0, 255, 255, 0.8);
        background: rgba(0,30,50,0.7);
        box-shadow: 
            inset 0 2px 4px rgba(0,0,0,0.3),
            0 0 20px rgba(0, 255, 255, 0.4),
            0 0 40px rgba(0, 255, 255, 0.2);
        outline: none;
    }
    
    .stTextInput > div > div > input::placeholder,
    .stTextArea > div > div > textarea::placeholder {
        color: rgba(0, 212, 255, 0.5);
    }
    
    /* Progress Bar - Animated neon flow */
    .stProgress > div > div > div > div {
        background: linear-gradient(90deg, 
            #00d4ff 0%, 
            #00ffff 25%, 
            #b537ff 50%, 
            #00ffff 75%, 
            #00d4ff 100%);
        background-size: 200% 100%;
        animation: progress-flow 2s linear infinite;
        filter: drop-shadow(0 0 10px rgba(0, 212, 255, 0.6));
        box-shadow: 0 0 20px rgba(0, 212, 255, 0.4);
    }
    
    @keyframes progress-flow {
        0% { background-position: 0% 50%; }
        100% { background-position: 200% 50%; }
    }
    
    /* Metric Cards */
    [data-testid="stMetricValue"] {
        font-size: 2.5rem;
        font-weight: 800;
        background: linear-gradient(135deg, #00d4ff 0%, #ffffff 50%, #b537ff 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        filter: drop-shadow(0 0 10px rgba(0, 212, 255, 0.3));
    }
    
    /* Expander */
    .streamlit-expanderHeader {
        background: rgba(0, 20, 40, 0.4);
        border-radius: 12px;
        border: 1px solid rgba(0, 212, 255, 0.2);
        font-weight: 600;
        padding: 1rem 1.5rem;
        position: relative;
        z-index: 100;
    }
    
    .streamlit-expanderHeader:hover {
        background: rgba(0, 30, 50, 0.5);
        border-color: rgba(0, 255, 255, 0.4);
        box-shadow: 0 0 15px rgba(0, 212, 255, 0.2);
    }
    
    /* Success/Error Messages */
    .stSuccess {
        background: linear-gradient(135deg, rgba(68,255,68,0.2) 0%, rgba(68,255,68,0.1) 100%);
        border-left: 4px solid #44ff44;
        border-radius: 12px;
        padding: 1rem;
        backdrop-filter: blur(10px);
    }
    
    .stError {
        background: linear-gradient(135deg, rgba(255,68,68,0.2) 0%, rgba(255,68,68,0.1) 100%);
        border-left: 4px solid #ff4444;
        border-radius: 12px;
        padding: 1rem;
        backdrop-filter: blur(10px);
    }
    
    .stWarning {
        background: linear-gradient(135deg, rgba(255,204,68,0.2) 0%, rgba(255,204,68,0.1) 100%);
        border-left: 4px solid #ffcc44;
        border-radius: 12px;
        padding: 1rem;
        backdrop-filter: blur(10px);
    }
    
    .stInfo {
        background: linear-gradient(135deg, rgba(68,136,255,0.2) 0%, rgba(68,136,255,0.1) 100%);
        border-left: 4px solid #4488ff;
        border-radius: 12px;
        padding: 1rem;
        backdrop-filter: blur(10px);
    }
    
    /* Selectbox */
    .stSelectbox > div > div {
        background: rgba(0, 20, 40, 0.6);
        border: 1px solid rgba(0, 212, 255, 0.3);
        border-radius: 12px;
        position: relative;
        z-index: 100;
    }
    
    /* Slider */
    .stSlider > div > div > div {
        background: rgba(255,255,255,0.1);
    }
    
    /* Divider */
    hr {
        border: none;
        height: 1px;
        background: linear-gradient(90deg, transparent, rgba(255,255,255,0.2), transparent);
        margin: 2rem 0;
    }
    
    /* Loading Spinner - Cyber rings */
    .stSpinner > div {
        border-top-color: #00d4ff !important;
        border-right-color: #00ffff !important;
        filter: drop-shadow(0 0 15px rgba(0, 212, 255, 0.8));
        animation: spinnerGlow 1.5s ease-in-out infinite;
    }
    
    @keyframes spinnerGlow {
        0%, 100% { 
            filter: drop-shadow(0 0 15px rgba(0, 212, 255, 0.8)); 
            transform: scale(1);
        }
        50% { 
            filter: drop-shadow(0 0 25px rgba(0, 255, 255, 1)); 
            transform: scale(1.05);
        }
    }
    
    /* Footer */
    .footer {
        text-align: center;
        padding: 2rem;
        margin-top: 4rem;
        border-top: 1px solid rgba(255,255,255,0.1);
        color: #666;
        font-size: 0.9rem;
    }
    
    /* Pulse Animation for Icons */
    @keyframes pulse {
        0%, 100% {
            opacity: 1;
            transform: scale(1);
        }
        50% {
            opacity: 0.8;
            transform: scale(1.05);
        }
    }
    
    .pulse-icon {
        animation: pulse 2s ease-in-out infinite;
    }
    
    /* 3D Card Effect */
    .card-3d {
        transform-style: preserve-3d;
        transition: transform 0.6s;
    }
    
    .card-3d:hover {
        transform: rotateY(5deg) rotateX(5deg);
    }
    
    /* Scrollbar */
    ::-webkit-scrollbar {
        width: 10px;
        height: 10px;
    }
    
    ::-webkit-scrollbar-track {
        background: rgba(255,255,255,0.05);
    }
    
    ::-webkit-scrollbar-thumb {
        background: linear-gradient(180deg, #ff4444, #cc0000);
        border-radius: 5px;
    }
    
    ::-webkit-scrollbar-thumb:hover {
        background: linear-gradient(180deg, #ff5555, #dd0000);
    }
    
    /* Hide Streamlit Branding - Keep header visible */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    /* header visibility: visible to show content */
    
    /* Checkbox */
    .stCheckbox {
        background: rgba(255,255,255,0.05);
        border-radius: 8px;
        padding: 0.5rem;
    }
    
    /* Custom Cursor - Removed for better usability */
    /* Using default cursor for better UX */
    
    /* Ensure main content is always visible */
    [data-testid="stAppViewContainer"] {
        position: relative;
        z-index: 1;
        opacity: 1 !important;
        visibility: visible !important;
    }
    
    /* Ensure all Streamlit elements are visible */
    [data-testid="stVerticalBlock"] {
        opacity: 1 !important;
        visibility: visible !important;
    }
    
    /* Remove pseudo-elements that block content */
    /* Scan line and grid moved to body::after and body::before */
    
    /* Holographic Corner Accents */
    .glass-card::after {
        content: '';
        position: absolute;
        top: 0;
        right: 0;
        width: 40px;
        height: 40px;
        border-top: 2px solid rgba(0, 212, 255, 0.5);
        border-right: 2px solid rgba(0, 212, 255, 0.5);
        border-radius: 0 20px 0 0;
        opacity: 0;
        transition: opacity 0.3s;
    }
    
    .glass-card:hover::after {
        opacity: 1;
    }
    
    /* Particle Effect on Hover */
    @keyframes particleFloat {
        0%, 100% { transform: translateY(0) translateX(0); opacity: 0; }
        10% { opacity: 1; }
        90% { opacity: 1; }
        100% { transform: translateY(-100px) translateX(10px); opacity: 0; }
    }
    
    /* Neon Text Glow */
    h1, h2, h3 {
        text-shadow: 
            0 0 10px rgba(0, 212, 255, 0.5),
            0 0 20px rgba(0, 212, 255, 0.3),
            0 0 30px rgba(0, 212, 255, 0.2);
    }
    
    /* Success/Error Message Enhancement */
    .stSuccess, .stError, .stWarning, .stInfo {
        animation: slideInGlow 0.5s ease-out;
    }
    
    @keyframes slideInGlow {
        from {
            transform: translateX(-20px);
            opacity: 0;
            filter: blur(5px);
        }
        to {
            transform: translateX(0);
            opacity: 1;
            filter: blur(0);
        }
    }

    </style>
    """, unsafe_allow_html=True)
# ============================================================================
# SESSION STATE INITIALIZATION
# ============================================================================

def init_session_state():
    """Initialize session state variables for caching models."""
    if 'text_model' not in st.session_state:
        st.session_state.text_model = None
    if 'image_model' not in st.session_state:
        st.session_state.image_model = None
    if 'show_instructions' not in st.session_state:
        st.session_state.show_instructions = False
    if 'analysis_count' not in st.session_state:
        st.session_state.analysis_count = 0
    if 'theme' not in st.session_state:
        st.session_state.theme = 'dark'


# ============================================================================
# MODEL LOADING FUNCTIONS (WITH CACHING)
# ============================================================================

@st.cache_resource(show_spinner=False)
def load_fake_news_model():
    """Load and cache the fake news detection model with fallback."""
    try:
        if not IMPORTS_SUCCESS:
            raise ImportError(f"Module import failed: {IMPORT_ERROR}")
        
        logger.info("Loading fake news model...")
        # Try to load with fallback support
        try:
            from detectors import fake_news_offline
            model = fake_news_offline.load_text_model_with_fallback(device=-1)
            if model['type'] == 'offline':
                logger.warning("Using offline rule-based detection (Hugging Face unavailable)")
            else:
                logger.info("✓ Fake news AI model loaded")
            return model
        except:
            # Fallback to original method
            model = fake_news.load_text_model(device=-1)
            logger.info("✓ Fake news model loaded")
            return {'type': 'huggingface', 'model': model}
    except Exception as e:
        logger.error(f"Failed to load fake news model: {e}")
        # Return offline mode as last resort
        logger.warning("Using offline detection mode")
        return {'type': 'offline', 'model': None}


@st.cache_resource(show_spinner=False)
def load_deepfake_model():
    """Load and cache the deepfake detection model."""
    try:
        if not IMPORTS_SUCCESS:
            raise ImportError(f"Module import failed: {IMPORT_ERROR}")
            
        logger.info("Loading deepfake model...")
        model = deepfake.load_image_model(device=-1)
        logger.info("✓ Deepfake model loaded")
        return model
    except Exception as e:
        logger.error(f"Failed to load deepfake model: {e}")
        raise Exception(f"Model loading failed: {str(e)}\n\nPlease ensure dependencies are installed:\npip install -r requirements.txt")


# ============================================================================
# HELPER FUNCTIONS
# ============================================================================

def retry_model_download(model_name: str, task: str, retries: int = 3) -> bool:
    """
    Attempt to download a Hugging Face model with retry logic.
    
    Args:
        model_name: Name of the Hugging Face model
        task: Task type (e.g., "text-classification", "image-classification")
        retries: Number of retry attempts
        
    Returns:
        bool: True if successful, False otherwise
    """
    from transformers import pipeline
    
    for i in range(retries):
        try:
            st.info(f"📥 Downloading {model_name}... (Attempt {i+1}/{retries})")
            pipeline(task, model=model_name)
            st.success(f"✅ Successfully downloaded {model_name}")
            return True
        except Exception as e:
            if i < retries - 1:
                st.warning(f"⚠️ Download failed (attempt {i+1}/{retries}): {str(e)[:100]}...")
                time.sleep(2)
            else:
                st.error(f"❌ Failed to download {model_name} after {retries} attempts: {str(e)[:100]}...")
    return False


def display_result(result: dict, result_type: str = "text"):
    """
    Display classification results in a modern, professional format.
    
    Args:
        result: Dictionary containing label, score, and raw output
        result_type: Type of analysis ("text", "image", "video")
    """
    label = result.get("label", "Unknown")
    score = result.get("score", 0.0)
    
    # Determine color and styling based on label
    if "fake" in label.lower() or "deepfake" in label.lower():
        card_class = "result-card-fake"
        icon = "🚩"
        status_emoji = "⚠️"
        status_text = "POTENTIALLY FAKE"
    else:
        card_class = "result-card-real"
        icon = "✅"
        status_emoji = "✓"
        status_text = "LIKELY AUTHENTIC"
    
    # Animated result card
    st.markdown(f"""
    <div class="{card_class}" style="animation: slideIn 0.6s ease-out;">
        <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 1.5rem;">
            <div>
                <h2 style="margin: 0; font-size: 2.5rem; font-weight: 900;">
                    {icon} {label.upper()}
                </h2>
                <p style="margin: 0.5rem 0 0 0; color: #888; font-size: 1.1rem; letter-spacing: 0.1em;">
                    {status_emoji} {status_text}
                </p>
            </div>
            <div style="text-align: right;">
                <div style="font-size: 3rem; font-weight: 900; background: linear-gradient(135deg, #ffffff 0%, #888888 100%); -webkit-background-clip: text; -webkit-text-fill-color: transparent;">
                    {score:.1%}
                </div>
                <div style="color: #666; font-size: 0.9rem; text-transform: uppercase; letter-spacing: 0.1em;">
                    CONFIDENCE
                </div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Animated progress bar
    st.progress(score, text=f"Analysis Confidence: {score:.1%}")
    
    # Explanation based on result type and label
    with st.expander("ℹ️ What does this mean?"):
        if result_type == "text":
            if "fake" in label.lower():
                st.warning("""
                **Fake News Detected**
                
                The AI model believes this text contains characteristics commonly 
                found in fake news articles, such as:
                - Sensationalized language
                - Lack of credible sources
                - Misleading or false claims
                - Emotional manipulation tactics
                
                ⚠️ **Recommendation**: Verify this information with trusted news sources 
                before sharing or believing it.
                """)
            else:
                st.success("""
                **Likely Real News**
                
                The AI model believes this text contains characteristics commonly 
                found in legitimate news articles, such as:
                - Factual reporting style
                - Balanced language
                - Credible information patterns
                
                ✓ **Note**: While the model suggests this is real, always practice 
                media literacy and verify important information.
                """)
        
        elif result_type in ["image", "video"]:
            if "fake" in label.lower() or "deepfake" in label.lower():
                st.warning("""
                **Deepfake Detected**
                
                The AI model has identified manipulation patterns in this media, including:
                - Facial inconsistencies
                - Unnatural textures or artifacts
                - AI-generated features
                
                ⚠️ **Recommendation**: This media may have been altered or generated 
                by AI. Verify authenticity before trusting or sharing.
                """)
            else:
                st.success("""
                **Likely Authentic Media**
                
                The AI model believes this media is authentic and shows:
                - Natural features and textures
                - Consistent lighting and shadows
                - No obvious signs of manipulation
                
                ✓ **Note**: No detection system is 100% accurate. Use critical 
                thinking when evaluating media authenticity.
                """)


def display_raw_output(result: dict):
    """Display raw model output for advanced users."""
    if st.checkbox("🔧 Show raw model output (for advanced users)"):
        st.json(result)


# ============================================================================
# TEXT/URL ANALYSIS SECTION
# ============================================================================

def text_analysis_section():
    """Handle text and URL analysis interface with modern UI."""
    st.markdown("""
    <div class="glass-card">
        <h2 style="font-size: 2rem; font-weight: 800; margin: 0 0 0.5rem 0; background: linear-gradient(135deg, #ffffff 0%, #888888 100%); -webkit-background-clip: text; -webkit-text-fill-color: transparent;">
            📝 TEXT & URL ANALYSIS
        </h2>
        <p style="color: #888; margin: 0; font-size: 1rem;">
            Analyze news articles and web content for misinformation using advanced NLP
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("<div style='height: 1.5rem;'></div>", unsafe_allow_html=True)
    
    # Input method selection with tabs-like design
    if NEWSAPI_AVAILABLE:
        col1, col2, col3 = st.columns(3)
        with col1:
            paste_button = st.button("📄 PASTE TEXT", use_container_width=True, type="secondary")
        with col2:
            url_button = st.button("🔗 ENTER URL", use_container_width=True, type="secondary")
        with col3:
            news_button = st.button("📰 FETCH NEWS", use_container_width=True, type="secondary")
    else:
        col1, col2 = st.columns(2)
        with col1:
            paste_button = st.button("📄 PASTE TEXT", use_container_width=True, type="secondary")
        with col2:
            url_button = st.button("🔗 ENTER URL", use_container_width=True, type="secondary")
        news_button = False
    
    # Determine input method
    if 'input_method' not in st.session_state:
        st.session_state.input_method = "text"
    
    if paste_button:
        st.session_state.input_method = "text"
    elif url_button:
        st.session_state.input_method = "url"
    elif news_button:
        st.session_state.input_method = "news"
    
    input_method = st.session_state.input_method
    
    st.markdown("<div style='height: 1rem;'></div>", unsafe_allow_html=True)
    
    text_to_analyze = None
    
    if input_method == "text":
        st.markdown("""
        <div style="color: #888; font-size: 0.9rem; margin-bottom: 0.5rem; text-transform: uppercase; letter-spacing: 0.1em;">
            📄 Paste Article Text
        </div>
        """, unsafe_allow_html=True)
        text_to_analyze = st.text_area(
            "text_input",
            height=250,
            placeholder="Paste the news article or text you want to analyze here...\n\nTip: Include at least 3-4 paragraphs for best results.",
            label_visibility="collapsed"
        )
    elif input_method == "url":
        st.markdown("""
        <div style="color: #888; font-size: 0.9rem; margin-bottom: 0.5rem; text-transform: uppercase; letter-spacing: 0.1em;">
            🔗 Enter Article URL
        </div>
        """, unsafe_allow_html=True)
        url = st.text_input(
            "url_input",
            placeholder="https://example.com/news-article",
            label_visibility="collapsed"
        )
        
        if url:
            st.info("👆 Click 'ANALYZE' to fetch and verify the article from this URL")
            # Optional: quick VirusTotal check button
            if VT_AVAILABLE:
                if st.button("🛡️ Quick URL Reputation Check (VirusTotal)", use_container_width=True):
                    with st.spinner("Submitting URL to VirusTotal..."):
                        vt_res = virustotal_client.url_analyze(url)
                    if vt_res.get("ok"):
                        verdict = vt_res.get("verdict", "unknown").title()
                        st.success(f"VirusTotal verdict: {verdict} | Malicious: {vt_res.get('malicious',0)} | Suspicious: {vt_res.get('suspicious',0)} | Harmless: {vt_res.get('harmless',0)}")
                        with st.expander("View raw VT result"):
                            st.json(vt_res.get("raw", {}))
                    else:
                        st.warning(f"VirusTotal check failed: {vt_res.get('error', 'Unknown error')}")
    
    elif input_method == "news":
        st.markdown("""
        <div style="color: #888; font-size: 0.9rem; margin-bottom: 0.5rem; text-transform: uppercase; letter-spacing: 0.1em;">
            📰 Search Real News Articles (Powered by NewsAPI.org)
        </div>
        """, unsafe_allow_html=True)
        
        search_col1, search_col2 = st.columns([3, 1])
        with search_col1:
            news_query = st.text_input(
                "news_query",
                placeholder="Search: politics, technology, health, sports...",
                label_visibility="collapsed"
            )
        with search_col2:
            search_button = st.button("🔍 SEARCH", use_container_width=True)
        
        if search_button and news_query:
            with st.spinner(f"🔎 Searching for '{news_query}'..."):
                results = newsapi_client.search_news(news_query, page_size=10)
                
                if results.get("status") == "ok":
                    articles = results.get("articles", [])
                    
                    if articles:
                        st.success(f"✓ Found {results.get('totalResults', 0)} articles (showing {len(articles)})")
                        st.session_state.news_articles = articles
                    else:
                        st.warning("No articles found. Try a different search term.")
                else:
                    st.error(f"Error: {results.get('message', 'Failed to search news')}")
        
        # Display found articles
        if 'news_articles' in st.session_state and st.session_state.news_articles:
            st.markdown("---")
            st.markdown("### 📰 Select an Article to Analyze:")
            
            for idx, article in enumerate(st.session_state.news_articles):
                formatted = newsapi_client.format_article_for_display(article)
                
                with st.expander(f"📄 {formatted['title']}", expanded=(idx==0)):
                    col1, col2 = st.columns([3, 1])
                    
                    with col1:
                        st.markdown(f"**Source:** {formatted['source']}")
                        st.markdown(f"**Author:** {formatted['author']}")
                        st.markdown(f"**Published:** {formatted['published'][:10]}")
                        st.markdown(f"**Description:** {formatted['description']}")
                        
                        if formatted['image']:
                            st.image(formatted['image'], use_column_width=True)
                    
                    with col2:
                        if st.button(f"✅ Analyze This", key=f"analyze_{idx}", use_container_width=True):
                            text_to_analyze = newsapi_client.extract_article_text(article)
                            st.session_state.selected_news_text = text_to_analyze
                            st.session_state.selected_news_url = formatted['url']
                            st.rerun()
        
        # Use selected article
        if 'selected_news_text' in st.session_state:
            text_to_analyze = st.session_state.selected_news_text
            st.info(f"✓ Article selected! Click 'ANALYZE NOW' below.")
    
    st.markdown("<div style='height: 1rem;'></div>", unsafe_allow_html=True)
    
    # Analyze button with modern styling
    analyze_col1, analyze_col2, analyze_col3 = st.columns([1, 2, 1])
    with analyze_col2:
        analyze_button = st.button("🔍 ANALYZE NOW", type="primary", use_container_width=True)
    
    if analyze_button:
        try:
            # Fetch text from URL if needed
            if input_method == "url":
                if not url or not url.strip():
                    st.error("⚠️ Please enter a valid URL")
                    return
                
                with st.spinner("📡 Fetching article from URL..."):
                    text_to_analyze = scraper.get_text_from_url(url)
                    
                    if not text_to_analyze or len(text_to_analyze.strip()) < 50:
                        st.error("⚠️ Could not extract sufficient text from the URL. Please try another URL or paste the text directly.")
                        return
                    
                    st.success(f"✓ Fetched {len(text_to_analyze)} characters")
                    
                    # Show preview
                    with st.expander("📄 Article Preview"):
                        st.text(text_to_analyze[:500] + "..." if len(text_to_analyze) > 500 else text_to_analyze)

                    # Optional Gemini cross-check
                    if GEMINI_AVAILABLE and st.toggle("Use Gemini to cross-check (summary & verdict)", value=False):
                        with st.spinner("Asking Gemini for a quick summary and sanity check..."):
                            g = gemini_client.summarize_and_verify(text_to_analyze)
                        if g.get("ok"):
                            st.markdown("### 🤝 Gemini Summary")
                            st.write(g.get("text", ""))
                        else:
                            st.warning(f"Gemini check failed: {g.get('error', 'Unknown error')}")
            
            # Validate text input
            if not text_to_analyze or not text_to_analyze.strip():
                st.error("⚠️ Please enter some text to analyze")
                return
            
            if len(text_to_analyze.strip()) < 20:
                st.warning("⚠️ Text is too short for reliable analysis. Please provide at least a few sentences.")
                return
            
            # Load model and classify with better UI feedback
            progress_placeholder = st.empty()
            status_placeholder = st.empty()
            
            try:
                # Step 1: Load model
                progress_placeholder.progress(0.2, text="Loading AI model...")
                status_placeholder.info("🤖 Initializing BERT Neural Network...")
                time.sleep(0.5)
                text_model = load_fake_news_model()
                
                # Step 2: Analyze
                progress_placeholder.progress(0.6, text="Analyzing content...")
                status_placeholder.info("🔎 Running deep analysis on text patterns...")
                time.sleep(0.5)
                
                # Use fallback-aware classification
                if text_model.get('type') == 'offline':
                    status_placeholder.warning("🔎 Using offline rule-based analysis (AI model unavailable)...")
                
                try:
                    from detectors import fake_news_offline
                    result = fake_news_offline.classify_text_with_fallback(text_model, text_to_analyze, max_length=1024)
                except:
                    # Fallback to original method
                    model = text_model.get('model', text_model)
                    result = fake_news.classify_text(model, text_to_analyze, max_length=1024)
                
                # Step 3: Complete
                progress_placeholder.progress(1.0, text="Analysis complete!")
                status_placeholder.success("✅ Analysis completed successfully!")
                time.sleep(0.5)
                
                # Clear progress indicators
                progress_placeholder.empty()
                status_placeholder.empty()
                
                # Increment analysis counter
                st.session_state.analysis_count += 1
                
                # Display results with animation
                st.markdown("<div style='height: 1rem;'></div>", unsafe_allow_html=True)
                st.markdown("### 📊 ANALYSIS RESULTS")
                st.markdown("<div style='height: 0.5rem;'></div>", unsafe_allow_html=True)
                
                display_result(result, result_type="text")
                
                # Show additional details
                with st.expander("📈 Detailed Analysis"):
                    col1, col2, col3 = st.columns(3)
                    with col1:
                        st.metric("Text Length", f"{len(text_to_analyze)} chars")
                    with col2:
                        st.metric("Words", f"{len(text_to_analyze.split())} words")
                    with col3:
                        st.metric("Analyzed At", datetime.now().strftime("%H:%M:%S"))
                
                display_raw_output(result)
                
            finally:
                progress_placeholder.empty()
                status_placeholder.empty()
            
        except Exception as e:
            st.error(f"""
            ### ❌ Analysis Failed
            
            **Error:** {str(e)}
            
            **Troubleshooting:**
            - Ensure text is at least 20 characters long
            - Check your internet connection (for URL fetching)
            - Verify dependencies are installed: `pip install -r requirements.txt`
            """)
            logger.exception("Text analysis failed")


# ============================================================================
# IMAGE ANALYSIS SECTION
# ============================================================================

def image_analysis_section():
    """Handle image deepfake detection interface with modern UI."""
    st.markdown("""
    <div class="glass-card">
        <h2 style="font-size: 2rem; font-weight: 800; margin: 0 0 0.5rem 0; background: linear-gradient(135deg, #ffffff 0%, #888888 100%); -webkit-background-clip: text; -webkit-text-fill-color: transparent;">
            🖼️ IMAGE DEEPFAKE DETECTION
        </h2>
        <p style="color: #888; margin: 0; font-size: 1rem;">
            Advanced computer vision analysis to detect AI-generated or manipulated images
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("<div style='height: 1.5rem;'></div>", unsafe_allow_html=True)
    
    # File uploader with modern styling
    st.markdown("""
    <div style="color: #888; font-size: 0.9rem; margin-bottom: 0.5rem; text-transform: uppercase; letter-spacing: 0.1em;">
        📤 Upload Image File
    </div>
    """, unsafe_allow_html=True)
    
    uploaded_file = st.file_uploader(
        "image_uploader",
        type=["jpg", "jpeg", "png", "webp"],
        help="Supported formats: JPG, JPEG, PNG, WEBP",
        label_visibility="collapsed"
    )
    
    if uploaded_file is not None:
        st.markdown("<div style='height: 1rem;'></div>", unsafe_allow_html=True)
        
        # Display uploaded image with modern card
        col1, col2 = st.columns([3, 2])
        
        with col1:
            st.markdown("""
            <div class="glass-card">
                <h3 style="margin: 0 0 1rem 0; color: #888; font-size: 0.9rem; text-transform: uppercase; letter-spacing: 0.1em;">
                    📸 Uploaded Image
                </h3>
            </div>
            """, unsafe_allow_html=True)
            st.image(uploaded_file, use_container_width=True)
        
        with col2:
            file_size_kb = uploaded_file.size / 1024
            file_size_mb = file_size_kb / 1024
            size_display = f"{file_size_mb:.2f} MB" if file_size_mb >= 1 else f"{file_size_kb:.2f} KB"
            
            st.markdown(f"""
            <div class="glass-card">
                <h3 style="margin: 0 0 1rem 0; color: #888; font-size: 0.9rem; text-transform: uppercase; letter-spacing: 0.1em;">
                    📋 File Information
                </h3>
                <div style="margin-bottom: 1rem;">
                    <div style="color: #666; font-size: 0.85rem; margin-bottom: 0.25rem;">FILE NAME</div>
                    <div style="font-weight: 600; word-break: break-all;">{uploaded_file.name}</div>
                </div>
                <div style="margin-bottom: 1rem;">
                    <div style="color: #666; font-size: 0.85rem; margin-bottom: 0.25rem;">FILE SIZE</div>
                    <div style="font-weight: 600;">{size_display}</div>
                </div>
                <div>
                    <div style="color: #666; font-size: 0.85rem; margin-bottom: 0.25rem;">FILE TYPE</div>
                    <div style="font-weight: 600;">{uploaded_file.type}</div>
                </div>
            </div>
            """, unsafe_allow_html=True)
        
        st.markdown("<div style='height: 1.5rem;'></div>", unsafe_allow_html=True)
        
        # Analyze button
        analyze_col1, analyze_col2, analyze_col3 = st.columns([1, 2, 1])
        with analyze_col2:
            analyze_button = st.button("🔍 ANALYZE IMAGE", type="primary", use_container_width=True)
        
        if analyze_button:
            progress_placeholder = st.empty()
            status_placeholder = st.empty()
            
            try:
                # Save uploaded file temporarily
                with tempfile.NamedTemporaryFile(delete=False, suffix=Path(uploaded_file.name).suffix) as tmp_file:
                    tmp_file.write(uploaded_file.getvalue())
                    tmp_path = tmp_file.name
                
                try:
                    # Step 1: Load model
                    progress_placeholder.progress(0.2, text="Loading AI model...")
                    status_placeholder.info("🤖 Initializing Computer Vision Model...")
                    time.sleep(0.5)
                    image_model = load_deepfake_model()
                    
                    # Step 2: Analyze
                    progress_placeholder.progress(0.6, text="Analyzing image...")
                    status_placeholder.info("🔎 Scanning for manipulation patterns...")
                    time.sleep(0.5)
                    result = deepfake.classify_image(image_model, tmp_path)
                    
                    # Step 3: Complete
                    progress_placeholder.progress(1.0, text="Analysis complete!")
                    status_placeholder.success("✅ Image analysis completed!")
                    time.sleep(0.5)
                    
                    # Clear progress indicators
                    progress_placeholder.empty()
                    status_placeholder.empty()
                    
                    # Increment counter
                    st.session_state.analysis_count += 1
                    
                    # Display results
                    st.markdown("<div style='height: 1rem;'></div>", unsafe_allow_html=True)
                    st.markdown("### 📊 ANALYSIS RESULTS")
                    st.markdown("<div style='height: 0.5rem;'></div>", unsafe_allow_html=True)
                    
                    display_result(result, result_type="image")
                    
                    # Show additional details
                    with st.expander("📈 Detailed Analysis"):
                        col1, col2, col3 = st.columns(3)
                        with col1:
                            st.metric("File Size", size_display)
                        with col2:
                            st.metric("Format", uploaded_file.type.split('/')[-1].upper())
                        with col3:
                            st.metric("Analyzed At", datetime.now().strftime("%H:%M:%S"))
                    
                    display_raw_output(result)
                    
                finally:
                    # Clean up temp file
                    try:
                        os.unlink(tmp_path)
                    except:
                        pass
                    progress_placeholder.empty()
                    status_placeholder.empty()
                
            except Exception as e:
                st.error(f"""
                ### ❌ Analysis Failed
                
                **Error:** {str(e)}
                
                **Troubleshooting:**
                - Ensure image file is valid and not corrupted
                - Try a different image format (JPG, PNG)
                - Reduce image size if it's very large
                - Check internet connection for model download
                """)
                logger.exception("Image analysis failed")
    else:
        st.markdown("""
        <div class="glass-card" style="text-align: center; padding: 3rem;">
            <div style="font-size: 4rem; margin-bottom: 1rem; opacity: 0.5;">🖼️</div>
            <h3 style="color: #888; font-weight: 600; margin: 0;">Upload an image to begin analysis</h3>
            <p style="color: #666; margin-top: 0.5rem;">Supported formats: JPG, JPEG, PNG, WEBP</p>
        </div>
        """, unsafe_allow_html=True)


# ============================================================================
# VIDEO ANALYSIS SECTION
# ============================================================================

def video_analysis_section():
    """Handle video deepfake detection interface."""
    st.header("🎥 Video Deepfake Detection")
    st.markdown("Upload a video to analyze frames for deepfake detection.")
    
    # File uploader
    uploaded_file = st.file_uploader(
        "Choose a video file:",
        type=["mp4", "avi", "mov"],
        help="Supported formats: MP4, AVI, MOV"
    )
    
    if uploaded_file is not None:
        st.info(f"""
        **File Details:**
        - Name: {uploaded_file.name}
        - Size: {uploaded_file.size / (1024*1024):.2f} MB
        - Type: {uploaded_file.type}
        """)
        
        # Sample rate configuration
        sample_rate = st.slider(
            "Frame sampling rate (frames per second):",
            min_value=1,
            max_value=5,
            value=1,
            help="Higher values analyze more frames but take longer"
        )
        
        st.warning("""
        ⚠️ **Note**: Video analysis may take several minutes depending on video length 
        and sampling rate. The app will extract frames and analyze each one.
        """)
        
        # Analyze button
        if st.button("🔍 Analyze Video", type="primary", use_container_width=True):
            try:
                # Save uploaded file temporarily
                with tempfile.NamedTemporaryFile(delete=False, suffix=Path(uploaded_file.name).suffix) as tmp_file:
                    tmp_file.write(uploaded_file.getvalue())
                    tmp_path = tmp_file.name
                
                # Extract frames
                with st.spinner(f"🎞️ Extracting frames (sampling at {sample_rate} fps)..."):
                    frame_paths = video_utils.extract_sample_frames(tmp_path, sample_rate=sample_rate)
                    st.success(f"✓ Extracted {len(frame_paths)} frames")
                
                if not frame_paths:
                    st.error("⚠️ Could not extract frames from video. Please try another file.")
                    os.unlink(tmp_path)
                    return
                
                # Load model
                with st.spinner("🤖 Loading deepfake detection model..."):
                    image_model = load_deepfake_model()
                
                # Analyze video (all frames)
                with st.spinner(f"🔎 Analyzing {len(frame_paths)} frames..."):
                    result = deepfake.classify_video(image_model, tmp_path, sample_rate=sample_rate)
                
                # Clean up temp files
                try:
                    os.unlink(tmp_path)
                    for frame_path in frame_paths:
                        try:
                            os.unlink(frame_path)
                        except:
                            pass
                except:
                    pass
                
                # Display overall result
                st.divider()
                st.subheader("📊 Overall Video Analysis")
                display_result(result, result_type="video")
                
                # Display per-frame results
                if "frame_results" in result:
                    with st.expander(f"🎞️ Per-Frame Results ({len(result['frame_results'])} frames)"):
                        frame_results = result["frame_results"]
                        
                        # Show frame analysis summary
                        cols = st.columns(min(4, len(frame_results)))
                        for idx, (col, frame_result) in enumerate(zip(cols, frame_results[:8])):
                            with col:
                                st.metric(
                                    f"Frame {idx+1}",
                                    frame_result.get("label", "Unknown"),
                                    f"{frame_result.get('score', 0):.1%}"
                                )
                        
                        if len(frame_results) > 8:
                            st.info(f"Showing first 8 of {len(frame_results)} frames")
                
                display_raw_output(result)
                
            except Exception as e:
                st.error(f"❌ Error during analysis: {str(e)}")
                logger.exception("Video analysis failed")
    else:
        st.info("👆 Upload a video file to begin analysis")


# ========================# INSTRUCTIONS PANEL====================================================

# ============================================================================

def show_instructions():
    """Display setup and usage instructions."""
    st.sidebar.markdown("---")
    st.sidebar.subheader("📚 Setup Instructions")
    
    if st.sidebar.button("📖 Show/Hide Instructions"):
        st.session_state.show_instructions = not st.session_state.show_instructions
    
    if st.session_state.show_instructions:
        with st.expander("🚀 How to Run Locally", expanded=True):
            st.markdown("""
            ### Setup Steps
            
            1. **Create a virtual environment:**
            ```bash
            python -m venv venv
            ```
            
            2. **Activate the virtual environment:**
            
            **Windows (PowerShell):**
            ```powershell
            .\\venv\\Scripts\\Activate.ps1
            ```
            
            **Windows (CMD):**
            ```cmd
            venv\\Scripts\\activate.bat
            ```
            
            **Linux/Mac:**
            ```bash
            source venv/bin/activate
            ```
            
            3. **Install dependencies:**
            ```bash
            pip install -r requirements.txt
            ```
            
            4. **Run the application:**
            ```bash
            streamlit run app.py
            ```
            
            ### Troubleshooting
            
            **Out of Memory Errors:**
            - Use smaller images/videos
            - Reduce video sampling rate
            - Close other applications
            - Use CPU-only mode (models are set to CPU by default)
            
            **GPU Not Available:**
            - The app uses CPU by default (`device=-1`)
            - For GPU: install `torch` with CUDA support
            - Models will automatically use available hardware
            
            **Slow Performance:**
            - First-time model downloads take time
            - Subsequent runs use cached models
            - Video analysis is computationally intensive
            
            **Import Errors:**
            - Ensure all dependencies are installed
            - Check Python version (3.8+ recommended)
            - Verify virtual environment is activated
            """)


# ============================================================================
# MAIN APP
# ============================================================================

def main():
    """Main application entry point."""
    
    # Check if imports were successful
    if not IMPORTS_SUCCESS:
        st.error(f"""
        ### ⚠️ Setup Required
        
        The application modules could not be imported. 
        
        **Error:** {IMPORT_ERROR}
        
        **Please run the setup:**
        ```powershell
        .\\setup.ps1
        ```
        
        Or install dependencies manually:
        ```powershell
        pip install -r requirements.txt
        ```
        """)
        st.stop()
    
    # Load custom CSS
    load_custom_css()
    
    # Initialize session state
    init_session_state()
    
    # Modern Header with Nothing Phone aesthetic
    st.markdown("""
    <div class="main-header">
        <h1 class="main-title pulse-icon">🔍 TRUTH LENS</h1>
        <p class="main-subtitle">AI-POWERED FAKE NEWS & DEEPFAKE DETECTION SYSTEM</p>
        <div style="display: flex; gap: 1.5rem; margin-top: 1.5rem; flex-wrap: wrap;">
            <div style="display: flex; align-items: center; gap: 0.5rem;">
                <span style="color: #ff4444; font-size: 1.2rem;">●</span>
                <span style="color: #888; font-size: 0.9rem;">BERT NLP Model</span>
            </div>
            <div style="display: flex; align-items: center; gap: 0.5rem;">
                <span style="color: #44ff44; font-size: 1.2rem;">●</span>
                <span style="color: #888; font-size: 0.9rem;">Vision AI Model</span>
            </div>
            <div style="display: flex; align-items: center; gap: 0.5rem;">
                <span style="color: #4444ff; font-size: 1.2rem;">●</span>
                <span style="color: #888; font-size: 0.9rem;">Real-time Analysis</span>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Sidebar with modern design
    with st.sidebar:
        st.markdown("""
        <div style="text-align: center; padding: 1.5rem 0; border-bottom: 1px solid rgba(255,255,255,0.1);">
            <h2 style="font-size: 1.8rem; font-weight: 800; margin: 0; background: linear-gradient(135deg, #ff4444 0%, #ffffff 100%); -webkit-background-clip: text; -webkit-text-fill-color: transparent;">
                ANALYSIS MODE
            </h2>
            <p style="color: #666; font-size: 0.85rem; margin-top: 0.5rem; letter-spacing: 0.1em;">
                SELECT YOUR DETECTION TYPE
            </p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("<div style='height: 1.5rem;'></div>", unsafe_allow_html=True)
        
        analysis_mode = st.radio(
            "Detection Mode",
            ["📝 Text & URL Analysis", "🖼️ Image Deepfake Detection", "🎥 Video Deepfake Detection"],
            label_visibility="collapsed"
        )
        
        st.markdown("<div style='height: 2rem;'></div>", unsafe_allow_html=True)
        
        # Stats display
        st.markdown(f"""
        <div class="glass-card" style="padding: 1.5rem; text-align: center;">
            <div style="font-size: 2.5rem; font-weight: 900; background: linear-gradient(135deg, #ffffff 0%, #888888 100%); -webkit-background-clip: text; -webkit-text-fill-color: transparent;">
                {st.session_state.analysis_count}
            </div>
            <div style="color: #666; font-size: 0.85rem; text-transform: uppercase; letter-spacing: 0.1em; margin-top: 0.5rem;">
                Analyses Completed
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    # Show instructions
    with st.sidebar:
        show_instructions()
        
        st.markdown("<div style='height: 1.5rem;'></div>", unsafe_allow_html=True)
        
        # Model info with modern design
        newsapi_status = "✅ Active" if NEWSAPI_AVAILABLE else "⚠️ Not Configured"
        newsapi_color = "#44ff44" if NEWSAPI_AVAILABLE else "#ffaa44"
        
        st.markdown(f"""
        <div class="glass-card" style="padding: 1.5rem;">
            <h4 style="margin: 0 0 1rem 0; color: #888; font-size: 0.85rem; text-transform: uppercase; letter-spacing: 0.1em;">
                🤖 AI Models & APIs
            </h4>
            <div style="margin-bottom: 1rem;">
                <div style="color: #ff4444; font-weight: 600; margin-bottom: 0.25rem;">● Text Analysis</div>
                <div style="color: #888; font-size: 0.85rem; font-family: monospace;">Fake-News-BERT</div>
            </div>
            <div style="margin-bottom: 1rem;">
                <div style="color: #44ff44; font-weight: 600; margin-bottom: 0.25rem;">● Vision Analysis</div>
                <div style="color: #888; font-size: 0.85rem; font-family: monospace;">Deep-Fake-Detector-v2</div>
            </div>
            <div style="margin-bottom: 1rem;">
                <div style="color: {newsapi_color}; font-weight: 600; margin-bottom: 0.25rem;">● NewsAPI</div>
                <div style="color: #888; font-size: 0.85rem; font-family: monospace;">{newsapi_status}</div>
            </div>
            <div style="margin-bottom: 1rem;">
                <div style="color: {'#44ff44' if VT_AVAILABLE else '#ffaa44'}; font-weight: 600; margin-bottom: 0.25rem;">● VirusTotal</div>
                <div style="color: #888; font-size: 0.85rem; font-family: monospace;">{'✅ Active' if VT_AVAILABLE else '⚠️ Not Configured'}</div>
            </div>
            <div>
                <div style="color: {'#44ff44' if GEMINI_AVAILABLE else '#ffaa44'}; font-weight: 600; margin-bottom: 0.25rem;">● Google Gemini</div>
                <div style="color: #888; font-size: 0.85rem; font-family: monospace;">{'✅ Active' if GEMINI_AVAILABLE else '⚠️ Not Configured'}</div>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("<div style='height: 1rem;'></div>", unsafe_allow_html=True)
        
        # Manual model download button
        if st.button("🔄 Download AI Models", use_container_width=True, help="Manually download Hugging Face models for offline use"):
            with st.expander("📥 Model Download Progress", expanded=True):
                text_model = os.getenv("TEXT_MODEL", "jy46604790/Fake-News-Bert-Detect")
                image_model = os.getenv("IMAGE_MODEL", "prithivMLmods/Deep-Fake-Detector-v2-Model")
                
                st.markdown("### 📝 Text Analysis Model")
                success1 = retry_model_download(text_model, "text-classification", retries=3)
                
                st.markdown("---")
                st.markdown("### 🖼️ Image Analysis Model")
                success2 = retry_model_download(image_model, "image-classification", retries=3)
                
                if success1 and success2:
                    st.balloons()
                    st.success("🎉 All models downloaded successfully! You can now use the app offline.")
                elif success1 or success2:
                    st.warning("⚠️ Some models downloaded successfully. Check the messages above.")
                else:
                    st.error("❌ Model download failed. Please check your internet connection and try again.")
        
        st.markdown("<div style='height: 1rem;'></div>", unsafe_allow_html=True)
        
        # Disclaimer with modern design
        st.markdown("""
        <div class="glass-card" style="padding: 1.5rem; border-left: 3px solid #ffcc44;">
            <h4 style="margin: 0 0 0.75rem 0; color: #ffcc44; font-size: 0.9rem; font-weight: 700;">
                ⚠️ IMPORTANT NOTICE
            </h4>
            <p style="margin: 0; color: #888; font-size: 0.85rem; line-height: 1.6;">
                AI models are not 100% accurate. Always verify important information with 
                multiple trusted sources and use critical thinking.
            </p>
        </div>
        """, unsafe_allow_html=True)
    
    # Main content area
    st.markdown("<div style='height: 1rem;'></div>", unsafe_allow_html=True)
    
    # Route to appropriate section based on mode
    if "Text" in analysis_mode:
        text_analysis_section()
    elif "Image" in analysis_mode:
        image_analysis_section()
    elif "Video" in analysis_mode:
        video_analysis_section()
    
    # Modern Footer
    st.markdown("<div style='height: 3rem;'></div>", unsafe_allow_html=True)
    st.markdown("""
    <div class="footer">
        <div style="max-width: 800px; margin: 0 auto;">
            <div style="display: flex; justify-content: center; gap: 2rem; margin-bottom: 1.5rem; flex-wrap: wrap;">
                <div style="text-align: center;">
                    <div style="font-size: 1.5rem; margin-bottom: 0.25rem;">🤖</div>
                    <div style="font-size: 0.75rem; color: #888; text-transform: uppercase; letter-spacing: 0.1em;">AI-Powered</div>
                </div>
                <div style="text-align: center;">
                    <div style="font-size: 1.5rem; margin-bottom: 0.25rem;">⚡</div>
                    <div style="font-size: 0.75rem; color: #888; text-transform: uppercase; letter-spacing: 0.1em;">Real-Time</div>
                </div>
                <div style="text-align: center;">
                    <div style="font-size: 1.5rem; margin-bottom: 0.25rem;">🔒</div>
                    <div style="font-size: 0.75rem; color: #888; text-transform: uppercase; letter-spacing: 0.1em;">Secure</div>
                </div>
                <div style="text-align: center;">
                    <div style="font-size: 1.5rem; margin-bottom: 0.25rem;">🌐</div>
                    <div style="font-size: 0.75rem; color: #888; text-transform: uppercase; letter-spacing: 0.1em;">Open Source</div>
                </div>
            </div>
            <div style="height: 1px; background: linear-gradient(90deg, transparent, rgba(255,255,255,0.1), transparent); margin: 1.5rem 0;"></div>
            <div style="text-align: center; color: #666; font-size: 0.85rem;">
                <p style="margin: 0.5rem 0;">Built with <span style="color: #ff4444;">❤</span> using Streamlit</p>
                <p style="margin: 0.5rem 0;">Powered by Hugging Face Transformers • PyTorch • OpenCV</p>
                <p style="margin: 0.5rem 0; font-size: 0.75rem; color: #555;">
                    © 2025 Truth Lens - AI Detection System
                </p>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)


# ============================================================================
# RUN APP
# ============================================================================

if __name__ == "__main__":
    main()
