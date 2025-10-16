import { useEffect, useRef } from 'react'

/**
 * HexGridBackground Component
 * 
 * Renders an animated hexagonal grid pattern using Canvas
 * Creates a futuristic honeycomb mesh with glowing lines
 */
const HexGridBackground = () => {
  const canvasRef = useRef<HTMLCanvasElement>(null)

  useEffect(() => {
    const canvas = canvasRef.current
    if (!canvas) return

    const ctx = canvas.getContext('2d')
    if (!ctx) return

    // Set canvas size to window size
    const resizeCanvas = () => {
      canvas.width = window.innerWidth
      canvas.height = window.innerHeight
    }
    resizeCanvas()
    window.addEventListener('resize', resizeCanvas)

    // Hexagon parameters
    const hexRadius = 40
    const hexHeight = hexRadius * 2
    const hexWidth = Math.sqrt(3) * hexRadius
    let offsetX = 0
    let offsetY = 0

    // Animation loop
    const animate = () => {
      ctx.clearRect(0, 0, canvas.width, canvas.height)

      // Animate offset for floating effect
      offsetX = Math.sin(Date.now() / 5000) * 20
      offsetY = Math.cos(Date.now() / 7000) * 20

      // Draw hexagonal grid
      for (let row = -2; row < Math.ceil(canvas.height / (hexHeight * 0.75)) + 2; row++) {
        for (let col = -2; col < Math.ceil(canvas.width / hexWidth) + 2; col++) {
          const x = col * hexWidth + (row % 2) * (hexWidth / 2) + offsetX
          const y = row * (hexHeight * 0.75) + offsetY

          drawHexagon(ctx, x, y, hexRadius)
        }
      }

      requestAnimationFrame(animate)
    }

    // Draw single hexagon
    const drawHexagon = (ctx: CanvasRenderingContext2D, x: number, y: number, radius: number) => {
      ctx.beginPath()
      for (let i = 0; i < 6; i++) {
        const angle = (Math.PI / 3) * i
        const hx = x + radius * Math.cos(angle)
        const hy = y + radius * Math.sin(angle)
        if (i === 0) {
          ctx.moveTo(hx, hy)
        } else {
          ctx.lineTo(hx, hy)
        }
      }
      ctx.closePath()

      // Glowing neon blue stroke
      ctx.strokeStyle = 'rgba(0, 212, 255, 0.15)'
      ctx.lineWidth = 1.5
      ctx.stroke()

      // Add subtle glow effect
      ctx.shadowBlur = 8
      ctx.shadowColor = 'rgba(0, 212, 255, 0.3)'
      ctx.stroke()
      ctx.shadowBlur = 0
    }

    animate()

    return () => {
      window.removeEventListener('resize', resizeCanvas)
    }
  }, [])

  return (
    <canvas
      ref={canvasRef}
      className="fixed inset-0 pointer-events-none opacity-30"
      style={{ zIndex: 0 }}
    />
  )
}

export default HexGridBackground
