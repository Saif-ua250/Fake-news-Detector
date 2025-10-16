import { motion } from 'framer-motion'

/**
 * LoadingSpinner Component
 * 
 * Futuristic loading animation with:
 * - Rotating rings
 * - Cyber data stream effect
 * - Pulsing glow
 */
const LoadingSpinner = () => {
  return (
    <div className="flex flex-col items-center justify-center gap-6 py-12">
      {/* Rotating rings */}
      <div className="relative w-24 h-24">
        <motion.div
          className="absolute inset-0 border-4 border-cyber-blue border-t-transparent rounded-full"
          animate={{ rotate: 360 }}
          transition={{ duration: 1, repeat: Infinity, ease: 'linear' }}
        />
        <motion.div
          className="absolute inset-2 border-4 border-cyber-cyan border-b-transparent rounded-full"
          animate={{ rotate: -360 }}
          transition={{ duration: 1.5, repeat: Infinity, ease: 'linear' }}
        />
        <motion.div
          className="absolute inset-4 border-4 border-cyber-purple border-l-transparent rounded-full"
          animate={{ rotate: 360 }}
          transition={{ duration: 2, repeat: Infinity, ease: 'linear' }}
        />
        
        {/* Center pulse */}
        <motion.div
          className="absolute inset-8 bg-cyber-blue rounded-full"
          animate={{ scale: [1, 1.2, 1], opacity: [1, 0.5, 1] }}
          transition={{ duration: 1.5, repeat: Infinity }}
        />
      </div>

      {/* Data stream text */}
      <motion.div
        className="font-rajdhani text-cyber-cyan text-lg tracking-widest"
        animate={{ opacity: [0.5, 1, 0.5] }}
        transition={{ duration: 1.5, repeat: Infinity }}
      >
        ANALYZING DATA STREAM
      </motion.div>

      {/* Binary code stream effect */}
      <div className="flex gap-2 font-mono text-xs text-cyber-blue/50">
        {[...Array(8)].map((_, i) => (
          <motion.span
            key={i}
            animate={{ opacity: [0, 1, 0] }}
            transition={{ 
              duration: 0.8, 
              repeat: Infinity, 
              delay: i * 0.1 
            }}
          >
            {Math.random() > 0.5 ? '1' : '0'}
          </motion.span>
        ))}
      </div>
    </div>
  )
}

export default LoadingSpinner
