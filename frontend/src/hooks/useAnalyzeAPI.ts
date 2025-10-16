import { useState } from 'react'
import axios from 'axios'

/**
 * API Response Type
 * Defines the structure of the /api/analyze response
 */
export interface AnalysisResponse {
  ok: boolean
  trustScore: number
  claimReviews?: Array<{
    claim: string
    verdict: string
    source?: string
    url?: string
  }>
  claimbuster?: {
    sentences: Array<{
      sentence: string
      score: number
    }>
  }
  virusTotal?: {
    verdict: string
    malicious: number
    suspicious: number
    harmless: number
  }
  domain?: {
    name: string
    age?: string
  }
  error?: string
}

/**
 * useAnalyzeAPI Hook
 * 
 * Custom hook for interacting with /api/analyze endpoint
 * Handles:
 * - POST request to backend
 * - Loading states
 * - Error handling
 * - Response typing
 */
export const useAnalyzeAPI = () => {
  const [data, setData] = useState<AnalysisResponse | null>(null)
  const [loading, setLoading] = useState(false)
  const [error, setError] = useState<string | null>(null)

  const analyze = async (url: string) => {
    setLoading(true)
    setError(null)
    setData(null)

    try {
      const response = await axios.post<AnalysisResponse>('/api/analyze', {
        url,
      }, {
        timeout: 30000, // 30 second timeout
      })

      if (response.data.ok) {
        setData(response.data)
      } else {
        setError(response.data.error || 'Analysis failed')
      }
    } catch (err: any) {
      if (err.code === 'ECONNABORTED') {
        setError('Request timeout. The analysis is taking too long.')
      } else if (err.response) {
        setError(err.response.data?.error || 'Server error occurred')
      } else if (err.request) {
        setError('Network error. Please check your connection.')
      } else {
        setError('An unexpected error occurred')
      }
    } finally {
      setLoading(false)
    }
  }

  return {
    data,
    loading,
    error,
    analyze,
  }
}
