"""
Quick Test Script for FakeNews + Deepfake Detector

This script tests the core functionality without the Streamlit UI.
Run this to verify your installation before starting the web app.
"""

import sys
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')
logger = logging.getLogger(__name__)

def test_imports():
    """Test that all required packages are installed."""
    print("=" * 60)
    print("TEST 1: Checking Package Imports")
    print("=" * 60)
    
    packages = [
        ("streamlit", "Streamlit web framework"),
        ("transformers", "Hugging Face Transformers"),
        ("torch", "PyTorch"),
        ("cv2", "OpenCV"),
        ("newspaper", "Newspaper3k web scraper"),
    ]
    
    failed = []
    for package, description in packages:
        try:
            __import__(package)
            print(f"✓ {package:20} - {description}")
        except ImportError as e:
            print(f"✗ {package:20} - FAILED: {e}")
            failed.append(package)
    
    print()
    if failed:
        print(f"⚠️  {len(failed)} package(s) failed to import: {', '.join(failed)}")
        print("Run: pip install -r requirements.txt")
        return False
    else:
        print("✓ All packages imported successfully!")
    
    return True


def test_modules():
    """Test that project modules can be imported."""
    print("\n" + "=" * 60)
    print("TEST 2: Checking Project Modules")
    print("=" * 60)
    
    modules = [
        ("detectors.fake_news", "Fake news detector"),
        ("detectors.deepfake", "Deepfake detector"),
        ("utils.scraper", "Web scraper"),
        ("utils.video_utils", "Video utilities"),
    ]
    
    failed = []
    for module, description in modules:
        try:
            __import__(module)
            print(f"✓ {module:25} - {description}")
        except ImportError as e:
            print(f"✗ {module:25} - FAILED: {e}")
            failed.append(module)
    
    print()
    if failed:
        print(f"⚠️  {len(failed)} module(s) failed to import")
        return False
    else:
        print("✓ All project modules imported successfully!")
    
    return True


def test_text_model():
    """Test loading the fake news detection model."""
    print("\n" + "=" * 60)
    print("TEST 3: Testing Fake News Model")
    print("=" * 60)
    
    try:
        from detectors import fake_news
        
        print("Loading model (this may take a few minutes on first run)...")
        model = fake_news.load_text_model(device=-1)
        print("✓ Model loaded successfully!")
        
        # Test classification
        test_text = "Scientists discover new breakthrough in renewable energy technology."
        print(f"\nTesting with sample text: '{test_text[:50]}...'")
        
        result = fake_news.classify_text(model, test_text)
        
        print(f"\nResult:")
        print(f"  Label: {result['label']}")
        print(f"  Confidence: {result['score']:.2%}")
        print(f"  Raw: {result['raw']}")
        
        print("\n✓ Fake news detection is working!")
        return True
        
    except Exception as e:
        print(f"\n✗ Failed to test fake news model: {e}")
        import traceback
        traceback.print_exc()
        return False


def test_image_model():
    """Test loading the deepfake detection model."""
    print("\n" + "=" * 60)
    print("TEST 4: Testing Deepfake Model")
    print("=" * 60)
    
    try:
        from detectors import deepfake
        
        print("Loading model (this may take a few minutes on first run)...")
        model = deepfake.load_image_model(device=-1)
        print("✓ Model loaded successfully!")
        
        print("\n✓ Deepfake detection model is ready!")
        print("  (Image/video testing requires actual media files)")
        return True
        
    except Exception as e:
        print(f"\n✗ Failed to test deepfake model: {e}")
        import traceback
        traceback.print_exc()
        return False


def main():
    """Run all tests."""
    print("\n" + "=" * 60)
    print("🔍 FakeNews + Deepfake Detector - System Test")
    print("=" * 60)
    print()
    
    tests = [
        ("Package Imports", test_imports),
        ("Project Modules", test_modules),
        ("Fake News Model", test_text_model),
        ("Deepfake Model", test_image_model),
    ]
    
    results = []
    for test_name, test_func in tests:
        try:
            passed = test_func()
            results.append((test_name, passed))
        except Exception as e:
            print(f"\n✗ Test '{test_name}' crashed: {e}")
            results.append((test_name, False))
    
    # Summary
    print("\n" + "=" * 60)
    print("TEST SUMMARY")
    print("=" * 60)
    
    passed_count = sum(1 for _, passed in results if passed)
    total_count = len(results)
    
    for test_name, passed in results:
        status = "✓ PASSED" if passed else "✗ FAILED"
        color = "\033[92m" if passed else "\033[91m"
        reset = "\033[0m"
        print(f"{color}{status}{reset} - {test_name}")
    
    print("\n" + "=" * 60)
    print(f"Result: {passed_count}/{total_count} tests passed")
    print("=" * 60)
    
    if passed_count == total_count:
        print("\n🎉 All tests passed! Your app is ready to use.")
        print("\nTo start the web app, run:")
        print("  streamlit run app.py")
        print("\nOr use the convenience script:")
        print("  .\\run.ps1")
        return 0
    else:
        print("\n⚠️  Some tests failed. Please fix the issues above.")
        print("\nCommon fixes:")
        print("  1. Install dependencies: pip install -r requirements.txt")
        print("  2. Check Python version: python --version (need 3.8+)")
        print("  3. Ensure virtual environment is activated")
        return 1


if __name__ == "__main__":
    sys.exit(main())
