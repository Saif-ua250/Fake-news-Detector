/**
 * ScanLine Component
 * 
 * Creates a vertical scanning line effect moving down the screen
 * Simulates a CRT monitor or futuristic HUD interface
 */
const ScanLine = () => {
  return (
    <>
      {/* Animated scan line */}
      <div className="fixed inset-0 pointer-events-none" style={{ zIndex: 50 }}>
        <div className="w-full h-[2px] bg-gradient-to-r from-transparent via-cyber-cyan to-transparent opacity-30 animate-scan-line" />
      </div>
      
      {/* Static scan lines overlay */}
      <div 
        className="fixed inset-0 pointer-events-none opacity-5" 
        style={{ 
          zIndex: 51,
          backgroundImage: 'repeating-linear-gradient(0deg, transparent, transparent 2px, rgba(0, 212, 255, 0.1) 2px, rgba(0, 212, 255, 0.1) 4px)'
        }} 
      />
    </>
  )
}

export default ScanLine
