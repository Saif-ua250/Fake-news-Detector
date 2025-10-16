"""
Download and Test Models Script
This script downloads the AI models and tests them to ensure they work.
"""

import os
from dotenv import load_dotenv
from transformers import pipeline
import sys

# Load environment variables
load_dotenv()

def download_model(model_name, task, description):
    """Download and test a model."""
    print(f"\n{'='*70}")
    print(f"📥 Downloading {description}")
    print(f"Model: {model_name}")
    print(f"{'='*70}")
    
    try:
        print(f"⏳ Initializing pipeline...")
        model = pipeline(task, model=model_name)
        print(f"✅ Successfully loaded {description}!")
        
        # Test the model
        print(f"🧪 Testing model...")
        if task == "text-classification":
            test_text = "This is a test article about politics and news."
            result = model(test_text)
            print(f"✅ Test successful! Result: {result}")
        elif task == "image-classification":
            print(f"✅ Model loaded successfully (image test requires actual image)")
        
        return True
    except Exception as e:
        print(f"❌ Failed to load {description}")
        print(f"Error: {str(e)}")
        return False


def main():
    print("\n" + "="*70)
    print("🤖 AI MODEL DOWNLOADER & TESTER")
    print("="*70)
    
    # Get models from environment
    text_model = os.getenv("TEXT_MODEL", "hamzab/roberta-fake-news-classification")
    image_model = os.getenv("IMAGE_MODEL", "dima806/deepfake_vs_real_image_detection")
    
    print(f"\n📋 Models to download:")
    print(f"  1. Text Model: {text_model}")
    print(f"  2. Image Model: {image_model}")
    
    # Download text model
    success1 = download_model(text_model, "text-classification", "Text Analysis Model (Fake News Detection)")
    
    # Download image model  
    success2 = download_model(image_model, "image-classification", "Image Analysis Model (Deepfake Detection)")
    
    # Summary
    print(f"\n{'='*70}")
    print("📊 DOWNLOAD SUMMARY")
    print(f"{'='*70}")
    print(f"Text Model: {'✅ Success' if success1 else '❌ Failed'}")
    print(f"Image Model: {'✅ Success' if success2 else '❌ Failed'}")
    
    if success1 and success2:
        print(f"\n🎉 All models downloaded successfully!")
        print(f"✓ You can now run the app with: streamlit run app.py")
        return 0
    else:
        print(f"\n⚠️ Some models failed to download.")
        print(f"Check your internet connection and try again.")
        return 1


if __name__ == "__main__":
    sys.exit(main())
