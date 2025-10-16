# ========================================
# FakeNews + Deepfake Detector Setup Script
# ========================================

Write-Host "============================================" -ForegroundColor Cyan
Write-Host "  FakeNews + Deepfake Detector - Setup" -ForegroundColor Cyan
Write-Host "============================================" -ForegroundColor Cyan
Write-Host ""

# Check Python installation
Write-Host "[1/6] Checking Python installation..." -ForegroundColor Yellow
$pythonVersion = python --version 2>&1
if ($LASTEXITCODE -ne 0) {
    Write-Host "ERROR: Python is not installed or not in PATH!" -ForegroundColor Red
    Write-Host "Please install Python 3.8+ from https://www.python.org" -ForegroundColor Red
    exit 1
}
Write-Host "  ✓ Found: $pythonVersion" -ForegroundColor Green
Write-Host ""

# Create virtual environment
Write-Host "[2/6] Creating virtual environment..." -ForegroundColor Yellow
if (Test-Path "venv") {
    Write-Host "  ⚠ Virtual environment already exists, skipping..." -ForegroundColor Yellow
} else {
    python -m venv venv
    if ($LASTEXITCODE -eq 0) {
        Write-Host "  ✓ Virtual environment created" -ForegroundColor Green
    } else {
        Write-Host "  ✗ Failed to create virtual environment" -ForegroundColor Red
        exit 1
    }
}
Write-Host ""

# Activate virtual environment
Write-Host "[3/6] Activating virtual environment..." -ForegroundColor Yellow
& ".\venv\Scripts\Activate.ps1"
if ($LASTEXITCODE -eq 0) {
    Write-Host "  ✓ Virtual environment activated" -ForegroundColor Green
} else {
    Write-Host "  ⚠ Could not activate automatically" -ForegroundColor Yellow
    Write-Host "  Please run: .\venv\Scripts\Activate.ps1" -ForegroundColor Yellow
}
Write-Host ""

# Upgrade pip
Write-Host "[4/6] Upgrading pip..." -ForegroundColor Yellow
python -m pip install --upgrade pip --quiet
Write-Host "  ✓ Pip upgraded" -ForegroundColor Green
Write-Host ""

# Install dependencies
Write-Host "[5/6] Installing dependencies..." -ForegroundColor Yellow
Write-Host "  ⏳ This may take 5-10 minutes (downloading ~2GB)..." -ForegroundColor Cyan
python -m pip install -r requirements.txt
if ($LASTEXITCODE -eq 0) {
    Write-Host "  ✓ All dependencies installed" -ForegroundColor Green
} else {
    Write-Host "  ✗ Failed to install dependencies" -ForegroundColor Red
    exit 1
}
Write-Host ""

# Verify installation
Write-Host "[6/6] Verifying installation..." -ForegroundColor Yellow
$packages = @("streamlit", "transformers", "torch", "opencv-python", "newspaper3k")
$allInstalled = $true
foreach ($package in $packages) {
    python -c "import $($package.Replace('-', '_').Replace('3k', ''))" 2>&1 | Out-Null
    if ($LASTEXITCODE -eq 0) {
        Write-Host "  ✓ $package" -ForegroundColor Green
    } else {
        Write-Host "  ✗ $package (not found)" -ForegroundColor Red
        $allInstalled = $false
    }
}
Write-Host ""

# Final message
if ($allInstalled) {
    Write-Host "============================================" -ForegroundColor Cyan
    Write-Host "  ✓ Setup Complete!" -ForegroundColor Green
    Write-Host "============================================" -ForegroundColor Cyan
    Write-Host ""
    Write-Host "To run the app:" -ForegroundColor Yellow
    Write-Host "  1. Ensure venv is activated:" -ForegroundColor White
    Write-Host "     .\venv\Scripts\Activate.ps1" -ForegroundColor Cyan
    Write-Host ""
    Write-Host "  2. Run the Streamlit app:" -ForegroundColor White
    Write-Host "     streamlit run app.py" -ForegroundColor Cyan
    Write-Host ""
    Write-Host "The app will open in your browser at http://localhost:8501" -ForegroundColor White
    Write-Host ""
} else {
    Write-Host "============================================" -ForegroundColor Red
    Write-Host "  ⚠ Setup completed with warnings" -ForegroundColor Yellow
    Write-Host "============================================" -ForegroundColor Red
    Write-Host "Some packages failed to install. Please check the errors above." -ForegroundColor Yellow
}
