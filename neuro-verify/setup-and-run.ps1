# NEURO-VERIFY AI - Automated Setup Script
# This script will install dependencies and launch the application

Write-Host "========================================" -ForegroundColor Cyan
Write-Host " NEURO-VERIFY AI - Setup & Launch" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""

# Check if Node.js is installed
Write-Host "[1/5] Checking Node.js installation..." -ForegroundColor Yellow
try {
    $nodeVersion = node --version
    Write-Host "  ✓ Node.js found: $nodeVersion" -ForegroundColor Green
} catch {
    Write-Host "  ✗ Node.js not found!" -ForegroundColor Red
    Write-Host "  Please install Node.js from https://nodejs.org/" -ForegroundColor Red
    Read-Host "Press Enter to exit"
    exit 1
}

# Check if npm is installed
Write-Host "[2/5] Checking npm installation..." -ForegroundColor Yellow
try {
    $npmVersion = npm --version
    Write-Host "  ✓ npm found: $npmVersion" -ForegroundColor Green
} catch {
    Write-Host "  ✗ npm not found!" -ForegroundColor Red
    Read-Host "Press Enter to exit"
    exit 1
}

# Install dependencies
Write-Host "[3/5] Installing dependencies..." -ForegroundColor Yellow
Write-Host "  This may take a few minutes..." -ForegroundColor Gray

try {
    npm install
    Write-Host "  ✓ Dependencies installed successfully" -ForegroundColor Green
} catch {
    Write-Host "  ✗ Failed to install dependencies" -ForegroundColor Red
    Write-Host "  Error: $_" -ForegroundColor Red
    Read-Host "Press Enter to exit"
    exit 1
}

# Create .env file if it doesn't exist
Write-Host "[4/5] Configuring environment..." -ForegroundColor Yellow
if (-not (Test-Path ".env")) {
    @"
VITE_API_BASE_URL=http://localhost:8000
"@ | Out-File -FilePath ".env" -Encoding UTF8
    Write-Host "  ✓ Created .env file with default API URL" -ForegroundColor Green
} else {
    Write-Host "  ✓ .env file already exists" -ForegroundColor Green
}

# Display network information
Write-Host "[5/5] Getting network information..." -ForegroundColor Yellow
$ipAddress = (Get-NetIPAddress -AddressFamily IPv4 | Where-Object {$_.InterfaceAlias -like "*Wi-Fi*" -or $_.InterfaceAlias -like "*Ethernet*"} | Select-Object -First 1).IPAddress
Write-Host "  ✓ Local IP Address: $ipAddress" -ForegroundColor Green

Write-Host ""
Write-Host "========================================" -ForegroundColor Green
Write-Host " Setup Complete!" -ForegroundColor Green
Write-Host "========================================" -ForegroundColor Green
Write-Host ""
Write-Host "Starting development server..." -ForegroundColor Cyan
Write-Host ""
Write-Host "Once started, access the app at:" -ForegroundColor White
Write-Host "  Computer: http://localhost:3000" -ForegroundColor Yellow
Write-Host "  Phone:    http://${ipAddress}:3000" -ForegroundColor Yellow
Write-Host ""
Write-Host "Press Ctrl+C to stop the server" -ForegroundColor Gray
Write-Host ""

# Start development server
npm run dev
