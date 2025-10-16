/**
 * API Client for NEURO-VERIFY AI Backend
 * Handles all HTTP requests with error handling and retry logic
 */

import axios, { AxiosError, AxiosInstance } from 'axios';
import type { AnalyzeResponse, ApiError } from '@/types';

/**
 * Base API configuration
 * Update API_BASE_URL to match your backend endpoint
 */
const API_BASE_URL = import.meta.env.VITE_API_BASE_URL || 'http://localhost:8000';

/**
 * Maximum retry attempts for failed requests
 */
const MAX_RETRIES = 3;

/**
 * Create axios instance with default configuration
 */
const apiClient: AxiosInstance = axios.create({
  baseURL: API_BASE_URL,
  timeout: 60000, // 60 seconds timeout for analysis
  headers: {
    'Content-Type': 'application/json',
  },
});

/**
 * Exponential backoff delay calculation
 * @param attempt - Current retry attempt number (1-indexed)
 * @returns Delay in milliseconds
 */
const getRetryDelay = (attempt: number): number => {
  return Math.min(1000 * Math.pow(2, attempt - 1), 10000);
};

/**
 * Sleep helper for retry delays
 * @param ms - Milliseconds to sleep
 */
const sleep = (ms: number): Promise<void> => {
  return new Promise((resolve) => setTimeout(resolve, ms));
};

/**
 * Analyze URL for fake news detection
 * Implements retry logic with exponential backoff
 * 
 * @param url - URL to analyze
 * @returns Promise with analysis results
 * @throws ApiError if all retry attempts fail
 */
export const analyzeUrl = async (url: string): Promise<AnalyzeResponse> => {
  let lastError: AxiosError | Error | null = null;

  // Retry loop with exponential backoff
  for (let attempt = 1; attempt <= MAX_RETRIES; attempt++) {
    try {
      const response = await apiClient.post<AnalyzeResponse>('/api/analyze', { url });
      return response.data;
    } catch (error) {
      lastError = error as AxiosError;

      // Don't retry on client errors (400-499)
      if (axios.isAxiosError(error) && error.response) {
        const status = error.response.status;
        if (status >= 400 && status < 500) {
          throw {
            error: error.response.data?.error || 'Invalid request',
            details: error.response.data?.details,
            code: `HTTP_${status}`,
          } as ApiError;
        }
      }

      // If not last attempt, wait before retrying
      if (attempt < MAX_RETRIES) {
        const delay = getRetryDelay(attempt);
        console.warn(`Request failed (attempt ${attempt}/${MAX_RETRIES}). Retrying in ${delay}ms...`);
        await sleep(delay);
      }
    }
  }

  // All retries failed
  if (axios.isAxiosError(lastError)) {
    if (lastError.code === 'ECONNABORTED') {
      throw {
        error: 'Request timeout',
        details: 'The analysis took too long. Please try again.',
        code: 'TIMEOUT',
      } as ApiError;
    }

    if (lastError.code === 'ERR_NETWORK') {
      throw {
        error: 'Network error',
        details: 'Unable to connect to the server. Please check your connection.',
        code: 'NETWORK_ERROR',
      } as ApiError;
    }

    throw {
      error: 'Analysis failed',
      details: lastError.message,
      code: lastError.code,
    } as ApiError;
  }

  throw {
    error: 'Unknown error',
    details: 'An unexpected error occurred. Please try again.',
    code: 'UNKNOWN',
  } as ApiError;
};

/**
 * Check if backend is healthy
 * @returns Promise<boolean> - true if backend is responding
 */
export const checkHealth = async (): Promise<boolean> => {
  try {
    await apiClient.get('/health', { timeout: 5000 });
    return true;
  } catch {
    return false;
  }
};
