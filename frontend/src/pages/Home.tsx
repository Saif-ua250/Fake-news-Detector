import { useState } from 'react'
import { useNavigate } from 'react-router-dom'
import { motion } from 'framer-motion'
import { Search, Shield, Zap } from 'lucide-react'
import GlowButton from '@/components/GlowButton'
import HolographicCard from '@/components/HolographicCard'
import GlitchText from '@/components/GlitchText'

/**
 * Home Page Component
 * 
 * Landing page featuring:
 * - NEURO-VERIFY AI branding
 * - URL input with validation
 * - Feature highlights
 * - Futuristic animations
 */
const Home = () => {
  const [url, setUrl] = useState('')
  const [isValidating, setIsValidating] = useState(false)
  const navigate = useNavigate()

  const handleAnalyze = async () => {
    if (!url.trim()) {
      alert('Please enter a URL')
      return
    }

    // Basic URL validation
    try {
      new URL(url)
    } catch {
      alert('Please enter a valid URL (e.g., https://example.com)')
      return
    }

    setIsValidating(true)
    
    // Navigate to results page with URL as state
    setTimeout(() => {
      navigate('/results', { state: { url } })
    }, 1000)
  }

  return (
    <div className="relative min-h-screen flex items-center justify-center px-4 py-12">
      <div className="max-w-4xl w-full space-y-12">
        {/* Hero Section */}
        <motion.div
          initial={{ opacity: 0, y: -50 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ duration: 0.8 }}
          className="text-center space-y-6"
        >
          {/* Logo/Badge */}
          <motion.div
            className="inline-block"
            animate={{ 
              rotate: [0, 5, -5, 0],
              scale: [1, 1.05, 1]
            }}
            transition={{ duration: 4, repeat: Infinity }}
          >
            <div className="w-24 h-24 mx-auto bg-gradient-to-br from-cyber-blue to-cyber-purple rounded-full flex items-center justify-center shadow-neon-blue">
              <Shield className="w-12 h-12 text-white" />
            </div>
          </motion.div>

          {/* Title */}
          <h1 className="font-orbitron text-6xl md:text-8xl font-black">
            <GlitchText text="NEURO-VERIFY" className="neon-text" />
            <span className="text-cyber-blue"> AI</span>
          </h1>

          {/* Tagline */}
          <motion.p
            className="font-exo text-xl md:text-2xl text-cyber-cyan tracking-wider"
            initial={{ opacity: 0 }}
            animate={{ opacity: 1 }}
            transition={{ delay: 0.5 }}
          >
            DETECT FAKE NEWS LIKE A CYBORG
          </motion.p>

          {/* Divider */}
          <div className="w-64 h-1 mx-auto bg-gradient-to-r from-transparent via-cyber-blue to-transparent" />
        </motion.div>

        {/* URL Input Section */}
        <HolographicCard className="p-8">
          <div className="space-y-6">
            <div className="flex items-center gap-3 text-cyber-cyan mb-4">
              <Search className="w-6 h-6" />
              <h2 className="font-orbitron text-xl font-bold tracking-wide">
                ENTER URL TO ANALYZE
              </h2>
            </div>

            <div className="relative">
              <input
                type="text"
                value={url}
                onChange={(e) => setUrl(e.target.value)}
                onKeyPress={(e) => e.key === 'Enter' && handleAnalyze()}
                placeholder="https://example.com/news-article"
                className="w-full px-6 py-4 bg-cyber-dark/50 border-2 border-cyber-blue/30 rounded-lg
                         text-white placeholder-cyber-blue/40 font-rajdhani text-lg
                         focus:border-cyber-cyan focus:outline-none focus:ring-2 focus:ring-cyber-cyan/30
                         transition-all duration-300"
                disabled={isValidating}
              />
              
              {/* Input glow effect */}
              <div className="absolute inset-0 rounded-lg bg-gradient-to-r from-cyber-blue/10 to-cyber-cyan/10 opacity-0 hover:opacity-100 transition-opacity duration-300 pointer-events-none" />
            </div>

            <GlowButton
              onClick={handleAnalyze}
              isLoading={isValidating}
              className="w-full"
              variant="primary"
            >
              <Zap className="w-5 h-5" />
              {isValidating ? 'INITIALIZING SCAN' : 'ANALYZE NOW'}
            </GlowButton>
          </div>
        </HolographicCard>

        {/* Feature Grid */}
        <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
          <HolographicCard delay={0.2} className="text-center p-6">
            <div className="w-16 h-16 mx-auto mb-4 bg-cyber-blue/20 rounded-full flex items-center justify-center">
              <Shield className="w-8 h-8 text-cyber-blue" />
            </div>
            <h3 className="font-orbitron text-lg font-bold mb-2 text-cyber-cyan">
              CLAIM VERIFICATION
            </h3>
            <p className="text-gray-400 text-sm">
              Cross-reference claims with trusted fact-checking databases
            </p>
          </HolographicCard>

          <HolographicCard delay={0.4} className="text-center p-6">
            <div className="w-16 h-16 mx-auto mb-4 bg-cyber-purple/20 rounded-full flex items-center justify-center">
              <Zap className="w-8 h-8 text-cyber-purple" />
            </div>
            <h3 className="font-orbitron text-lg font-bold mb-2 text-cyber-cyan">
              AI ANALYSIS
            </h3>
            <p className="text-gray-400 text-sm">
              Advanced NLP algorithms detect misleading content patterns
            </p>
          </HolographicCard>

          <HolographicCard delay={0.6} className="text-center p-6">
            <div className="w-16 h-16 mx-auto mb-4 bg-cyber-cyan/20 rounded-full flex items-center justify-center">
              <Search className="w-8 h-8 text-cyber-cyan" />
            </div>
            <h3 className="font-orbitron text-lg font-bold mb-2 text-cyber-cyan">
              SOURCE CHECK
            </h3>
            <p className="text-gray-400 text-sm">
              Reputation scanning via VirusTotal and domain verification
            </p>
          </HolographicCard>
        </div>

        {/* Footer */}
        <motion.div
          className="text-center text-gray-500 font-rajdhani text-sm"
          initial={{ opacity: 0 }}
          animate={{ opacity: 1 }}
          transition={{ delay: 1 }}
        >
          <p>POWERED BY AI VERITAS PROTOCOL</p>
          <div className="flex items-center justify-center gap-4 mt-2">
            <span>v1.0.0</span>
            <span>•</span>
            <span>QUANTUM SECURE</span>
            <span>•</span>
            <span>NEURAL NET ENABLED</span>
          </div>
        </motion.div>
      </div>
    </div>
  )
}

export default Home
