import { motion } from 'framer-motion'
import { RadarChart as RechartsRadar, PolarGrid, PolarAngleAxis, PolarRadiusAxis, Radar, ResponsiveContainer } from 'recharts'

interface RadarChartProps {
  score: number
}

/**
 * RadarChart Component
 * 
 * Displays trust score as a futuristic radar/pentagon chart
 * Uses Recharts for visualization with cyber theme styling
 */
const RadarChart = ({ score }: RadarChartProps) => {
  // Generate radar data based on score
  const data = [
    { subject: 'Credibility', A: score, fullMark: 100 },
    { subject: 'Sources', A: Math.max(0, score - 10), fullMark: 100 },
    { subject: 'Accuracy', A: Math.max(0, score - 5), fullMark: 100 },
    { subject: 'Consistency', A: Math.min(100, score + 5), fullMark: 100 },
    { subject: 'Reputation', A: Math.max(0, score - 8), fullMark: 100 },
  ]

  return (
    <motion.div
      initial={{ scale: 0.8, opacity: 0 }}
      animate={{ scale: 1, opacity: 1 }}
      transition={{ duration: 0.8 }}
      className="relative"
    >
      {/* Pulsing background glow */}
      <motion.div
        className="absolute inset-0 rounded-full bg-cyber-blue/20 blur-3xl"
        animate={{
          scale: [1, 1.2, 1],
          opacity: [0.3, 0.5, 0.3],
        }}
        transition={{
          duration: 3,
          repeat: Infinity,
        }}
      />

      <ResponsiveContainer width="100%" height={300}>
        <RechartsRadar data={data}>
          <PolarGrid stroke="rgba(0, 212, 255, 0.3)" />
          <PolarAngleAxis
            dataKey="subject"
            tick={{ fill: '#00d4ff', fontSize: 12, fontFamily: 'Rajdhani' }}
          />
          <PolarRadiusAxis
            angle={90}
            domain={[0, 100]}
            tick={{ fill: '#00d4ff', fontSize: 10 }}
          />
          <Radar
            name="Trust Score"
            dataKey="A"
            stroke="#00d4ff"
            fill="#00d4ff"
            fillOpacity={0.3}
            strokeWidth={2}
          />
        </RechartsRadar>
      </ResponsiveContainer>

      {/* Rotating ring decoration */}
      <motion.div
        className="absolute inset-0 border-2 border-cyber-cyan/30 rounded-full pointer-events-none"
        animate={{ rotate: 360 }}
        transition={{ duration: 20, repeat: Infinity, ease: 'linear' }}
      />
    </motion.div>
  )
}

export default RadarChart
