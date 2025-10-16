import { BrowserRouter as Router, Routes, Route } from 'react-router-dom'
import { motion, AnimatePresence } from 'framer-motion'
import Home from './pages/Home'
import Results from './pages/Results'
import HexGridBackground from './components/HexGridBackground'
import ScanLine from './components/ScanLine'

/**
 * Main App Component
 * 
 * Sci-Fi themed application with:
 * - Animated hex-grid background
 * - Scan-line effect overlay
 * - Page transitions with Framer Motion
 * - Routing between Home and Results pages
 */
function App() {
  return (
    <Router>
      <div className="relative min-h-screen w-full overflow-hidden bg-cyber-darker">
        {/* Animated Hexagon Grid Background */}
        <HexGridBackground />
        
        {/* Scan Line Effect */}
        <ScanLine />
        
        {/* Main Content with Page Transitions */}
        <AnimatePresence mode="wait">
          <Routes>
            <Route path="/" element={<Home />} />
            <Route path="/results" element={<Results />} />
          </Routes>
        </AnimatePresence>
      </div>
    </Router>
  )
}

export default App
