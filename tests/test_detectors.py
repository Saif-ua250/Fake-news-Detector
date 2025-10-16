"""
Unit Tests for FakeNews + Deepfake Detector

Basic tests for detector modules using pytest.
Uses mocks to avoid downloading models during testing.
"""

import pytest
from unittest.mock import Mock, patch, MagicMock
import sys
import os

# Add parent directory to path for imports
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


# ============================================================================
# FAKE NEWS DETECTOR TESTS
# ============================================================================

class TestFakeNewsDetector:
    """Tests for fake_news detection module."""
    
    @patch('detectors.fake_news.pipeline')
    def test_load_text_model(self, mock_pipeline):
        """Test that text model loads correctly."""
        from detectors import fake_news
        
        # Mock the pipeline
        mock_pipeline.return_value = Mock()
        
        # Load model
        model = fake_news.load_text_model(device=-1)
        
        # Verify pipeline was called with correct parameters
        mock_pipeline.assert_called_once_with(
            "text-classification",
            model="jy46604790/Fake-News-Bert-Detect",
            device=-1
        )
        
        assert model is not None
    
    @patch('detectors.fake_news.pipeline')
    def test_classify_text_valid_input(self, mock_pipeline):
        """Test text classification with valid input."""
        from detectors import fake_news
        
        # Mock pipeline and its return value
        mock_pipe = Mock()
        mock_pipe.return_value = [{"label": "LABEL_0", "score": 0.95}]
        mock_pipe.model = Mock()
        mock_pipe.model.config = Mock()
        mock_pipe.model.config.id2label = {0: "Fake", 1: "Real"}
        
        # Test classification
        result = fake_news.classify_text(mock_pipe, "This is a test article about news.")
        
        # Verify result structure
        assert "label" in result
        assert "score" in result
        assert "raw" in result
        assert result["label"] in ["Fake", "Real"]
        assert 0 <= result["score"] <= 1
    
    def test_classify_text_empty_input(self):
        """Test that empty text raises ValueError."""
        from detectors import fake_news
        
        mock_pipe = Mock()
        
        with pytest.raises(ValueError, match="Input text cannot be empty"):
            fake_news.classify_text(mock_pipe, "")
    
    def test_label_mapping(self):
        """Test label mapping from LABEL_X to human-readable."""
        from detectors.fake_news import _map_label_to_human
        
        mock_pipe = Mock()
        mock_pipe.model = Mock()
        mock_pipe.model.config = Mock()
        mock_pipe.model.config.id2label = {0: "Fake", 1: "Real"}
        
        # Test mapping
        assert _map_label_to_human(mock_pipe, "LABEL_0") == "Fake"
        assert _map_label_to_human(mock_pipe, "LABEL_1") == "Real"


# ============================================================================
# DEEPFAKE DETECTOR TESTS
# ============================================================================

class TestDeepfakeDetector:
    """Tests for deepfake detection module."""
    
    @patch('detectors.deepfake.pipeline')
    def test_load_image_model(self, mock_pipeline):
        """Test that image model loads correctly."""
        from detectors import deepfake
        
        # Mock the pipeline
        mock_pipeline.return_value = Mock()
        
        # Load model
        model = deepfake.load_image_model(device=-1)
        
        # Verify pipeline was called with correct parameters
        mock_pipeline.assert_called_once_with(
            "image-classification",
            model="prithivMLmods/Deep-Fake-Detector-v2-Model",
            device=-1
        )
        
        assert model is not None
    
    @patch('detectors.deepfake.pipeline')
    @patch('os.path.exists')
    def test_classify_image(self, mock_exists, mock_pipeline):
        """Test image classification."""
        from detectors import deepfake
        
        # Mock file existence
        mock_exists.return_value = True
        
        # Mock pipeline
        mock_pipe = Mock()
        mock_pipe.return_value = [{"label": "Real", "score": 0.87}]
        mock_pipe.model = Mock()
        mock_pipe.model.config = Mock()
        
        # Test classification
        result = deepfake.classify_image(mock_pipe, "test_image.jpg")
        
        # Verify result structure
        assert "label" in result
        assert "score" in result
        assert "raw" in result
        assert 0 <= result["score"] <= 1


# ============================================================================
# UTILS TESTS
# ============================================================================

class TestScraper:
    """Tests for web scraper module."""
    
    @patch('utils.scraper.Article')
    def test_get_text_from_url_valid(self, mock_article_class):
        """Test URL scraping with valid input."""
        from utils import scraper
        
        # Mock Article behavior
        mock_article = Mock()
        mock_article.title = "Test Article"
        mock_article.text = "This is the article content."
        mock_article_class.return_value = mock_article
        
        # Test scraping
        result = scraper.get_text_from_url("https://example.com/article")
        
        # Verify Article methods were called
        mock_article.download.assert_called_once()
        mock_article.parse.assert_called_once()
        
        # Verify result
        assert "Test Article" in result
        assert "article content" in result
    
    def test_get_text_from_url_invalid(self):
        """Test that invalid URL raises ValueError."""
        from utils import scraper
        
        with pytest.raises(ValueError):
            scraper.get_text_from_url("")
        
        with pytest.raises(ValueError):
            scraper.get_text_from_url("not-a-url")


class TestVideoUtils:
    """Tests for video processing utilities."""
    
    @patch('cv2.VideoCapture')
    @patch('os.path.exists')
    def test_extract_sample_frames(self, mock_exists, mock_capture_class):
        """Test frame extraction from video."""
        from utils import video_utils
        
        # Mock file existence
        mock_exists.return_value = True
        
        # Mock VideoCapture
        mock_cap = Mock()
        mock_cap.isOpened.return_value = True
        mock_cap.get.side_effect = lambda prop: {
            3: 100,  # CAP_PROP_FRAME_COUNT
            5: 30.0  # CAP_PROP_FPS
        }.get(prop, 0)
        
        # Mock read() to return frames then stop
        mock_cap.read.side_effect = [
            (True, Mock()),  # Frame 1
            (True, Mock()),  # Frame 2
            (False, None)    # End
        ]
        
        mock_capture_class.return_value = mock_cap
        
        # Mock cv2.imwrite
        with patch('cv2.imwrite') as mock_imwrite:
            mock_imwrite.return_value = True
            
            # Test extraction
            frames = video_utils.extract_sample_frames("test.mp4", sample_rate=1)
            
            # Verify frames were extracted
            assert len(frames) > 0


# ============================================================================
# INTEGRATION TESTS
# ============================================================================

class TestIntegration:
    """Integration tests for complete workflows."""
    
    @patch('detectors.fake_news.pipeline')
    def test_text_analysis_workflow(self, mock_pipeline):
        """Test complete text analysis workflow."""
        from detectors import fake_news
        
        # Mock pipeline
        mock_pipe = Mock()
        mock_pipe.return_value = [{"label": "LABEL_1", "score": 0.92}]
        mock_pipe.model = Mock()
        mock_pipe.model.config = Mock()
        mock_pipe.model.config.id2label = {0: "Fake", 1: "Real"}
        mock_pipeline.return_value = mock_pipe
        
        # Load model and classify
        model = fake_news.load_text_model()
        result = fake_news.classify_text(model, "Test news article content here.")
        
        # Verify complete workflow
        assert result["label"] == "Real"
        assert result["score"] == 0.92


# ============================================================================
# FIXTURES
# ============================================================================

@pytest.fixture
def sample_text():
    """Sample text for testing."""
    return "Breaking news: Scientists discover new renewable energy source."


@pytest.fixture
def sample_url():
    """Sample URL for testing."""
    return "https://example.com/news/article"


# ============================================================================
# RUN TESTS
# ============================================================================

if __name__ == "__main__":
    # Run tests with pytest
    pytest.main([__file__, "-v", "--tb=short"])
