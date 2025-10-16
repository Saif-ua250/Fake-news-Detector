# 🚀 NEURO-VERIFY AI - Sci-Fi Fake News Detector Frontend

A Hollywood-level, futuristic sci-fi web interface for fake news detection, inspired by TRON, Iron Man HUDs, and Blade Runner aesthetics.

![Version](https://img.shields.io/badge/version-1.0.0-blue)
![React](https://img.shields.io/badge/React-18.2-61DAFB?logo=react)
![TypeScript](https://img.shields.io/badge/TypeScript-5.2-3178C6?logo=typescript)
![Tailwind](https://img.shields.io/badge/Tailwind-3.4-38B2AC?logo=tailwind-css)

## ✨ Features

### 🎨 Visual Design
- **Holographic UI** with animated hexagon grid background
- **Neon glow effects** (blue, cyan, purple accents)
- **Glass morphism** cards with backdrop blur
- **Scan line effect** simulating CRT monitors
- **3D-like depth** with layered animations
- **Futuristic fonts** (Orbitron, Exo 2, Rajdhani)
- **Responsive design** (mobile → 4K)

### 🧠 Core Functionality
- **URL Analysis** - Submit news article URLs for verification
- **Trust Score Radar** - Visual pentagon chart showing credibility metrics
- **Claim Reviews** - Display fact-checked claims with verdicts
- **ClaimBuster Integration** - Highlight checkworthy sentences
- **Source Reputation** - VirusTotal scans and domain info
- **Real-time Loading** - Cyber data stream animations
- **Error Handling** - Glitch-effect error states

### 🎭 Animations & Interactions
- **Framer Motion** page transitions
- **Hover glow effects** on all interactive elements
- **Rotating rings** and pulsing backgrounds
- **Data stream** binary code effects
- **Smooth transitions** between states
- **Particle-like** button interactions

## 🛠️ Tech Stack

| Category | Technology |
|----------|-----------|
| **Framework** | React 18 + Vite |
| **Language** | TypeScript 5.2 |
| **Styling** | Tailwind CSS 3.4 |
| **Animations** | Framer Motion 11 |
| **3D Graphics** | Three.js + React Three Fiber |
| **Charts** | Recharts 2.12 |
| **Icons** | Lucide React |
| **HTTP Client** | Axios |
| **Routing** | React Router 6 |

## 📦 Installation

### Prerequisites
- Node.js 18+ and npm/yarn/pnpm
- Backend API running on `http://localhost:8000` (or configure proxy in `vite.config.ts`)

### Quick Start

```bash
# Navigate to frontend directory
cd frontend

# Install dependencies
npm install

# Start development server
npm run dev

# Open browser to http://localhost:3000
```

### Build for Production

```bash
# Create optimized build
npm run build

# Preview production build
npm run preview
```

## 📁 Project Structure

```
frontend/
├── src/
│   ├── components/          # Reusable UI components
│   │   ├── GlowButton.tsx      # Neon button with hover effects
│   │   ├── HolographicCard.tsx # Glass morphism card
│   │   ├── HexGridBackground.tsx # Animated hex canvas
│   │   ├── ScanLine.tsx        # CRT scan effect
│   │   ├── GlitchText.tsx      # Cyberpunk text animation
│   │   ├── LoadingSpinner.tsx  # Futuristic loader
│   │   └── RadarChart.tsx      # Pentagon trust score chart
│   ├── pages/               # Page components
│   │   ├── Home.tsx            # Landing page with URL input
│   │   └── Results.tsx         # Analysis dashboard
│   ├── hooks/               # Custom React hooks
│   │   └── useAnalyzeAPI.ts    # API integration hook
│   ├── lib/                 # Utility functions
│   │   └── utils.ts            # Tailwind class merger
│   ├── App.tsx              # Main app router
│   ├── main.tsx             # React entry point
│   └── index.css            # Global styles + Tailwind
├── public/                  # Static assets
├── index.html               # HTML template
├── package.json             # Dependencies
├── tsconfig.json            # TypeScript config
├── tailwind.config.js       # Tailwind theme (sci-fi palette)
├── vite.config.ts           # Vite configuration
└── README.md                # This file
```

## 🎨 Customization

### Color Palette (Tailwind)

```js
// tailwind.config.js
colors: {
  'cyber-blue': '#00d4ff',    // Primary accent
  'cyber-cyan': '#00ffff',    // Secondary accent
  'cyber-purple': '#b537ff',  // Tertiary accent
  'cyber-pink': '#ff00ff',    // Highlight
  'cyber-red': '#ff0055',     // Errors/warnings
  'cyber-green': '#00ff88',   // Success
  'cyber-dark': '#0a0a0f',    // Background
  'cyber-darker': '#050508',  // Deeper background
}
```

### Animation Timings

```js
// Adjust in tailwind.config.js → theme.extend.keyframes
'glow-pulse': '2s ease-in-out infinite',
'scan-line': '4s linear infinite',
'hex-float': '20s ease-in-out infinite',
```

### API Endpoint

```ts
// vite.config.ts
server: {
  proxy: {
    '/api': {
      target: 'http://localhost:8000', // Change backend URL here
      changeOrigin: true,
    },
  },
}
```

## 🔌 API Integration

### Expected Backend Endpoint

**POST** `/api/analyze`

**Request Body:**
```json
{
  "url": "https://example.com/news-article"
}
```

**Response:**
```json
{
  "ok": true,
  "trustScore": 75,
  "claimReviews": [
    {
      "claim": "...",
      "verdict": "TRUE",
      "source": "FactCheck.org"
    }
  ],
  "claimbuster": {
    "sentences": [
      {
        "sentence": "...",
        "score": 0.85
      }
    ]
  },
  "virusTotal": {
    "verdict": "clean",
    "malicious": 0,
    "suspicious": 0,
    "harmless": 82
  },
  "domain": {
    "name": "example.com",
    "age": "10 years"
  }
}
```

## 🚀 Performance

- **Lighthouse Score Target**: 90+
- **Bundle Size**: ~500KB (gzipped)
- **First Contentful Paint**: < 1.5s
- **Time to Interactive**: < 3s

### Optimization Tips
- Lazy load Three.js components
- Use React.memo for expensive components
- Enable code splitting via dynamic imports
- Compress images/assets with Vite

## 🐛 Troubleshooting

### TypeScript Errors Before Install
- Normal! Run `npm install` first to resolve all imports

### Backend Connection Issues
- Verify backend is running on port 8000
- Check CORS settings on backend
- Adjust proxy in `vite.config.ts`

### Animation Performance
- Reduce `hexRadius` in `HexGridBackground.tsx`
- Disable scan line effect on low-end devices
- Simplify Framer Motion animations

### Build Errors
```bash
# Clear cache and reinstall
rm -rf node_modules package-lock.json
npm install
npm run build
```

## 📝 Scripts

| Command | Description |
|---------|-------------|
| `npm run dev` | Start development server (http://localhost:3000) |
| `npm run build` | Build for production |
| `npm run preview` | Preview production build locally |
| `npm run lint` | Run ESLint |

## 🎯 Roadmap

- [ ] Add sound effects (optional cyber SFX)
- [ ] Three.js particle system for background
- [ ] Dark/light mode toggle (currently dark only)
- [ ] Export analysis reports as PDF
- [ ] Real-time WebSocket updates
- [ ] Mobile app wrapper (React Native)

## 📄 License

MIT License - Free to use for personal and commercial projects.

## 🙏 Credits

- **Fonts**: Orbitron, Exo 2, Rajdhani (Google Fonts)
- **Icons**: Lucide React
- **Inspiration**: TRON, Iron Man, Blade Runner, Cyberpunk 2077

---

**Built with ❤️ and neon dreams** ✨

For backend integration, ensure your FastAPI server is running and accessible at the configured proxy URL.
