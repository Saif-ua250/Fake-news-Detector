# ========================================
# Run FakeNews + Deepfake Detector
# ========================================

Write-Host "============================================" -ForegroundColor Cyan
Write-Host "  FakeNews + Deepfake Detector" -ForegroundColor Cyan
Write-Host "============================================" -ForegroundColor Cyan
Write-Host ""

# Check if venv exists
if (-Not (Test-Path "venv")) {
    Write-Host "ERROR: Virtual environment not found!" -ForegroundColor Red
    Write-Host "Please run setup.ps1 first:" -ForegroundColor Yellow
    Write-Host "  .\setup.ps1" -ForegroundColor Cyan
    exit 1
}

# Activate venv
Write-Host "Activating virtual environment..." -ForegroundColor Yellow
& ".\venv\Scripts\Activate.ps1"

# Run the app
Write-Host "Starting Streamlit app..." -ForegroundColor Yellow
Write-Host ""
Write-Host "The app will open in your browser at http://localhost:8501" -ForegroundColor Green
Write-Host "Press Ctrl+C to stop the server" -ForegroundColor Yellow
Write-Host ""

streamlit run app.py
