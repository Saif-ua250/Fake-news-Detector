/**
 * TypeScript Type Definitions for NEURO-VERIFY AI
 * Comprehensive API response interfaces with strict typing
 */

/**
 * Single claim review from fact-checking organizations
 */
export interface ClaimReview {
  publisher: {
    name: string;
    site: string;
    favicon?: string;
  };
  title: string;
  url: string;
  reviewDate?: string;
  verdict?: 'true' | 'false' | 'mixed' | 'unverified';
  summary?: string;
}

/**
 * Individual sentence with check-worthiness score from ClaimBuster
 */
export interface ClaimBusterSentence {
  sentence: string;
  score: number; // 0.0 - 1.0
}

/**
 * VirusTotal domain analysis summary
 */
export interface VirusTotalSummary {
  domain: string;
  last_scans: Record<string, { detected: boolean; result?: string }>;
  suspicious_score: number; // 0 - 100
  domain_age_days?: number;
}

/**
 * Source reputation rating
 */
export type SourceReputationRating = 'trustworthy' | 'mixed' | 'unreliable' | 'satire';

/**
 * Source reputation details
 */
export interface SourceReputation {
  rating: SourceReputationRating;
  details?: string;
}

/**
 * Complete API response from POST /api/analyze
 */
export interface AnalyzeResponse {
  url: string;
  title?: string;
  snippet?: string;
  publish_date?: string;
  author?: string;
  claim_reviews: ClaimReview[];
  claimbuster: {
    top_sentences: ClaimBusterSentence[];
  };
  virustotal: VirusTotalSummary | null;
  source_reputation?: SourceReputation;
  trust_score: number; // 0 - 100
  explanation: string;
}

/**
 * API error response structure
 */
export interface ApiError {
  error: string;
  details?: string;
  code?: string;
}

/**
 * Loading state for async operations
 */
export type LoadingState = 'idle' | 'loading' | 'success' | 'error';

/**
 * Button variant types
 */
export type ButtonVariant = 'primary' | 'secondary' | 'ghost' | 'danger' | 'icon' | 'fab';

/**
 * Button size types
 */
export type ButtonSize = 'sm' | 'md' | 'lg';

/**
 * Animation variant names for Framer Motion
 */
export type AnimationVariant = 'fadeIn' | 'pop' | 'lineDraw' | 'gauge' | 'slideIn';
