# Complete Installation Script for Truth Lens
# Run this to install ALL dependencies

Write-Host ""
Write-Host "===============================================" -ForegroundColor Cyan
Write-Host " TRUTH LENS - Installing Dependencies" -ForegroundColor Cyan  
Write-Host "===============================================" -ForegroundColor Cyan
Write-Host ""

# Navigate to project directory
	Set-Location "$PSScriptRoot"

# Activate virtual environment
Write-Host "[1/6] Activating virtual environment..." -ForegroundColor Yellow
& ".\venv\Scripts\Activate.ps1"

# Upgrade pip
Write-Host "[2/6] Upgrading pip..." -ForegroundColor Yellow
python -m pip install --upgrade pip

# Install Streamlit
Write-Host "[3/6] Installing Streamlit..." -ForegroundColor Yellow
pip install streamlit

# Install PyTorch (CPU version - faster download)
Write-Host "[4/6] Installing PyTorch (may take 5-10 min)..." -ForegroundColor Yellow
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cpu

# Install Transformers and ML libraries
Write-Host "[5/6] Installing Hugging Face Transformers..." -ForegroundColor Yellow
pip install transformers

# Install remaining packages
Write-Host "[6/6] Installing remaining packages..." -ForegroundColor Yellow
pip install opencv-python pillow newspaper3k lxml beautifulsoup4 requests python-dateutil pytest pytest-cov

Write-Host ""
Write-Host "===============================================" -ForegroundColor Green
Write-Host " Installation Complete!" -ForegroundColor Green
Write-Host "===============================================" -ForegroundColor Green
Write-Host ""

# Test imports
Write-Host "Testing installations..." -ForegroundColor Cyan
python -c "import streamlit; print('OK: Streamlit')"
python -c "import torch; print('OK: PyTorch')"
python -c "import transformers; print('OK: Transformers')"
python -c "import cv2; print('OK: OpenCV')"
python -c "import newspaper; print('OK: Newspaper3k')"
python -c "from utils import newsapi_client; newsapi_client.test_newsapi()"

Write-Host ""
Write-Host "Ready to launch! Run: .\launch.ps1" -ForegroundColor White
Write-Host ""
