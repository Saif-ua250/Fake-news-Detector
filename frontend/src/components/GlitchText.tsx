import { useState, useEffect } from 'react'
import { motion } from 'framer-motion'

interface GlitchTextProps {
  text: string
  className?: string
  isGlitching?: boolean
}

/**
 * GlitchText Component
 * 
 * Creates a cyberpunk glitch text effect
 * Text randomly shifts and distorts when active
 */
const GlitchText = ({ text, className = '', isGlitching = false }: GlitchTextProps) => {
  const [displayText, setDisplayText] = useState(text)

  useEffect(() => {
    if (!isGlitching) {
      setDisplayText(text)
      return
    }

    const glitchChars = '!@#$%^&*()_+-=[]{}|;:,.<>?'
    let interval: NodeJS.Timeout

    interval = setInterval(() => {
      const shouldGlitch = Math.random() > 0.7
      
      if (shouldGlitch) {
        const glitched = text
          .split('')
          .map(char => {
            if (Math.random() > 0.8) {
              return glitchChars[Math.floor(Math.random() * glitchChars.length)]
            }
            return char
          })
          .join('')
        
        setDisplayText(glitched)
        
        // Reset after short delay
        setTimeout(() => setDisplayText(text), 50)
      }
    }, 100)

    return () => clearInterval(interval)
  }, [text, isGlitching])

  return (
    <motion.span
      className={`relative inline-block font-orbitron ${className}`}
      animate={isGlitching ? { x: [-2, 2, -2, 0] } : {}}
      transition={{ duration: 0.2, repeat: isGlitching ? Infinity : 0 }}
    >
      {displayText}
      
      {/* Shadow layers for glitch effect */}
      {isGlitching && (
        <>
          <span 
            className="absolute top-0 left-0 text-cyber-red opacity-70" 
            style={{ transform: 'translate(-2px, 0)' }}
          >
            {displayText}
          </span>
          <span 
            className="absolute top-0 left-0 text-cyber-cyan opacity-70" 
            style={{ transform: 'translate(2px, 0)' }}
          >
            {displayText}
          </span>
        </>
      )}
    </motion.span>
  )
}

export default GlitchText
