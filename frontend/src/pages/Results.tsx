import { useEffect, useState } from 'react'
import { useLocation, useNavigate } from 'react-router-dom'
import { motion } from 'framer-motion'
import { ArrowLeft, AlertTriangle, CheckCircle, Shield, Activity, Globe } from 'lucide-react'
import HolographicCard from '@/components/HolographicCard'
import LoadingSpinner from '@/components/LoadingSpinner'
import GlowButton from '@/components/GlowButton'
import RadarChart from '@/components/RadarChart'
import { useAnalyzeAPI } from '@/hooks/useAnalyzeAPI'

/**
 * Results Page Component
 * 
 * Displays analysis results with:
 * - Trust score radar chart
 * - Claim reviews section
 * - ClaimBuster sentences
 * - Source reputation data
 * - Error handling with glitch effect
 */
const Results = () => {
  const location = useLocation()
  const navigate = useNavigate()
  const url = location.state?.url

  const { data, loading, error, analyze } = useAnalyzeAPI()

  useEffect(() => {
    if (!url) {
      navigate('/')
      return
    }

    // Trigger analysis
    analyze(url)
  }, [url])

  if (!url) {
    return null
  }

  // Loading State
  if (loading) {
    return (
      <div className="min-h-screen flex items-center justify-center">
        <LoadingSpinner />
      </div>
    )
  }

  // Error State
  if (error) {
    return (
      <div className="min-h-screen flex items-center justify-center px-4">
        <HolographicCard className="max-w-2xl w-full p-8 border-cyber-red/50">
          <div className="text-center space-y-6">
            <motion.div
              animate={{ rotate: [0, 5, -5, 0] }}
              transition={{ duration: 0.3, repeat: Infinity }}
            >
              <AlertTriangle className="w-24 h-24 mx-auto text-cyber-red" />
            </motion.div>

            <h2 className="font-orbitron text-3xl font-bold text-cyber-red">
              SYSTEM ALERT
            </h2>

            <p className="text-gray-300 font-rajdhani text-lg">
              {error}
            </p>

            <GlowButton onClick={() => navigate('/')} variant="danger">
              <ArrowLeft className="w-5 h-5" />
              RETURN TO HOME
            </GlowButton>
          </div>
        </HolographicCard>
      </div>
    )
  }

  // Success State
  const trustScore = data?.trustScore || 0
  const isCredible = trustScore >= 60

  return (
    <div className="min-h-screen px-4 py-12">
      <div className="max-w-7xl mx-auto space-y-8">
        {/* Header */}
        <motion.div
          initial={{ opacity: 0, y: -20 }}
          animate={{ opacity: 1, y: 0 }}
          className="flex items-center justify-between"
        >
          <GlowButton onClick={() => navigate('/')} variant="secondary">
            <ArrowLeft className="w-5 h-5" />
            NEW SCAN
          </GlowButton>

          <h1 className="font-orbitron text-2xl md:text-4xl font-bold text-cyber-cyan neon-text">
            ANALYSIS COMPLETE
          </h1>
        </motion.div>

        {/* URL Display */}
        <HolographicCard delay={0.1}>
          <div className="flex items-center gap-3">
            <Globe className="w-5 h-5 text-cyber-blue flex-shrink-0" />
            <p className="text-gray-300 font-mono text-sm break-all">{url}</p>
          </div>
        </HolographicCard>

        {/* Trust Score Radar */}
        <HolographicCard delay={0.2} className="p-8">
          <h2 className="font-orbitron text-2xl font-bold mb-6 text-cyber-cyan flex items-center gap-3">
            <Shield className="w-6 h-6" />
            TRUST SCORE ANALYSIS
          </h2>

          <div className="grid grid-cols-1 lg:grid-cols-2 gap-8 items-center">
            <RadarChart score={trustScore} />

            <div className="space-y-4">
              <div className={`text-6xl font-black font-orbitron ${isCredible ? 'text-cyber-green' : 'text-cyber-red'}`}>
                {trustScore}%
              </div>

              <div className={`inline-flex items-center gap-2 px-4 py-2 rounded-full ${
                isCredible ? 'bg-cyber-green/20 text-cyber-green' : 'bg-cyber-red/20 text-cyber-red'
              }`}>
                {isCredible ? <CheckCircle className="w-5 h-5" /> : <AlertTriangle className="w-5 h-5" />}
                <span className="font-orbitron font-bold">
                  {isCredible ? 'LIKELY CREDIBLE' : 'POTENTIALLY FAKE'}
                </span>
              </div>

              <p className="text-gray-400 text-sm">
                {isCredible 
                  ? 'This source shows strong indicators of reliability based on our verification protocols.'
                  : 'Multiple red flags detected. Exercise caution and verify with additional sources.'}
              </p>
            </div>
          </div>
        </HolographicCard>

        {/* Three Column Grid */}
        <div className="grid grid-cols-1 lg:grid-cols-3 gap-6">
          {/* Claim Reviews */}
          <HolographicCard delay={0.3} className="lg:col-span-1">
            <h3 className="font-orbitron text-xl font-bold mb-4 text-cyber-cyan flex items-center gap-2">
              <Activity className="w-5 h-5" />
              CLAIM REVIEWS
            </h3>

            <div className="space-y-3">
              {data?.claimReviews?.slice(0, 5).map((claim: any, idx: number) => (
                <motion.div
                  key={idx}
                  initial={{ opacity: 0, x: -20 }}
                  animate={{ opacity: 1, x: 0 }}
                  transition={{ delay: idx * 0.1 }}
                  className="p-3 bg-cyber-dark/50 rounded-lg border border-cyber-blue/20"
                >
                  <div className="flex items-start justify-between gap-2 mb-2">
                    <span className={`text-xs font-bold px-2 py-1 rounded ${
                      claim.verdict?.toLowerCase().includes('false') 
                        ? 'bg-cyber-red/20 text-cyber-red'
                        : 'bg-cyber-green/20 text-cyber-green'
                    }`}>
                      {claim.verdict || 'UNVERIFIED'}
                    </span>
                  </div>
                  <p className="text-gray-300 text-sm line-clamp-3">{claim.claim}</p>
                  {claim.source && (
                    <p className="text-cyber-blue text-xs mt-2">Source: {claim.source}</p>
                  )}
                </motion.div>
              )) || (
                <p className="text-gray-500 text-sm">No claim reviews available</p>
              )}
            </div>
          </HolographicCard>

          {/* ClaimBuster Sentences */}
          <HolographicCard delay={0.4} className="lg:col-span-1">
            <h3 className="font-orbitron text-xl font-bold mb-4 text-cyber-cyan flex items-center gap-2">
              <Activity className="w-5 h-5" />
              CHECKWORTHY CLAIMS
            </h3>

            <div className="space-y-3">
              {data?.claimbuster?.sentences?.slice(0, 5).map((item: any, idx: number) => (
                <motion.div
                  key={idx}
                  initial={{ opacity: 0, x: -20 }}
                  animate={{ opacity: 1, x: 0 }}
                  transition={{ delay: idx * 0.1 }}
                  className="space-y-2"
                >
                  <p className="text-gray-300 text-sm">{item.sentence}</p>
                  <div className="flex items-center gap-2">
                    <div className="flex-1 h-2 bg-cyber-dark rounded-full overflow-hidden">
                      <motion.div
                        initial={{ width: 0 }}
                        animate={{ width: `${item.score * 100}%` }}
                        transition={{ duration: 1, delay: idx * 0.1 }}
                        className={`h-full ${
                          item.score > 0.7 ? 'bg-cyber-red' : item.score > 0.4 ? 'bg-cyber-purple' : 'bg-cyber-blue'
                        }`}
                      />
                    </div>
                    <span className="text-xs text-cyber-cyan font-mono">
                      {(item.score * 100).toFixed(0)}%
                    </span>
                  </div>
                </motion.div>
              )) || (
                <p className="text-gray-500 text-sm">No checkworthy claims detected</p>
              )}
            </div>
          </HolographicCard>

          {/* Source Reputation */}
          <HolographicCard delay={0.5} className="lg:col-span-1">
            <h3 className="font-orbitron text-xl font-bold mb-4 text-cyber-cyan flex items-center gap-2">
              <Shield className="w-5 h-5" />
              SOURCE REPUTATION
            </h3>

            <div className="space-y-4">
              {data?.virusTotal && (
                <div className="p-4 bg-cyber-dark/50 rounded-lg border border-cyber-blue/20">
                  <h4 className="text-sm font-bold text-cyber-blue mb-3">VirusTotal Scan</h4>
                  
                  <div className="grid grid-cols-3 gap-3 text-center">
                    <div>
                      <div className="text-2xl font-bold text-cyber-red">
                        {data.virusTotal.malicious || 0}
                      </div>
                      <div className="text-xs text-gray-400">Malicious</div>
                    </div>
                    <div>
                      <div className="text-2xl font-bold text-cyber-purple">
                        {data.virusTotal.suspicious || 0}
                      </div>
                      <div className="text-xs text-gray-400">Suspicious</div>
                    </div>
                    <div>
                      <div className="text-2xl font-bold text-cyber-green">
                        {data.virusTotal.harmless || 0}
                      </div>
                      <div className="text-xs text-gray-400">Harmless</div>
                    </div>
                  </div>

                  <div className={`mt-3 text-center text-sm font-bold ${
                    data.virusTotal.verdict === 'clean' ? 'text-cyber-green' : 'text-cyber-red'
                  }`}>
                    {data.virusTotal.verdict?.toUpperCase() || 'UNKNOWN'}
                  </div>
                </div>
              )}

              {data?.domain && (
                <div className="p-4 bg-cyber-dark/50 rounded-lg border border-cyber-blue/20">
                  <h4 className="text-sm font-bold text-cyber-blue mb-2">Domain Info</h4>
                  <div className="space-y-1 text-sm">
                    <p className="text-gray-300">
                      <span className="text-gray-500">Domain:</span> {data.domain.name}
                    </p>
                    {data.domain.age && (
                      <p className="text-gray-300">
                        <span className="text-gray-500">Age:</span> {data.domain.age}
                      </p>
                    )}
                  </div>
                </div>
              )}

              {!data?.virusTotal && !data?.domain && (
                <p className="text-gray-500 text-sm">No reputation data available</p>
              )}
            </div>
          </HolographicCard>
        </div>
      </div>
    </div>
  )
}

export default Results
