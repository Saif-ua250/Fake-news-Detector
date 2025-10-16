/**
 * Main App Component - NEURO-VERIFY AI
 * Orchestrates the entire application layout and state
 */

import { useState } from 'react';
import Header from './components/Header';
import HeroPanel from './components/HeroPanel';
import ResultsDashboard from './components/ResultsDashboard';
import Footer from './components/Footer';
import BackgroundEffects from './components/BackgroundEffects';
import ErrorModal from './components/ErrorModal';
import { analyzeUrl } from './api/client';
import type { AnalyzeResponse, ApiError, LoadingState } from './types';

function App() {
  // Application state
  const [loadingState, setLoadingState] = useState<LoadingState>('idle');
  const [results, setResults] = useState<AnalyzeResponse | null>(null);
  const [error, setError] = useState<ApiError | null>(null);

  /**
   * Handle URL analysis submission
   * @param url - URL to analyze
   */
  const handleAnalyze = async (url: string) => {
    // Reset previous state
    setError(null);
    setResults(null);
    setLoadingState('loading');

    try {
      const response = await analyzeUrl(url);
      setResults(response);
      setLoadingState('success');
    } catch (err) {
      setError(err as ApiError);
      setLoadingState('error');
    }
  };

  /**
   * Handle error modal close
   */
  const handleErrorClose = () => {
    setError(null);
    setLoadingState('idle');
  };

  /**
   * Handle retry after error
   */
  const handleRetry = () => {
    setError(null);
    setLoadingState('idle');
  };

  return (
    <div className="min-h-screen bg-bg honeycomb-bg relative overflow-x-hidden">
      {/* Background sci-fi effects */}
      <BackgroundEffects />

      {/* Main application layout */}
      <div className="relative z-10">
        {/* Fixed header */}
        <Header />

        {/* Main content container */}
        <main className="container mx-auto px-6 pt-24 pb-16 max-w-7xl">
          {/* Hero input panel */}
          <HeroPanel
            onAnalyze={handleAnalyze}
            isLoading={loadingState === 'loading'}
            disabled={loadingState === 'loading'}
          />

          {/* Results dashboard - only shown when we have results */}
          {(loadingState === 'success' || loadingState === 'loading') && (
            <ResultsDashboard
              results={results}
              isLoading={loadingState === 'loading'}
            />
          )}
        </main>

        {/* Footer */}
        <Footer />
      </div>

      {/* Error modal */}
      {error && (
        <ErrorModal
          error={error}
          onClose={handleErrorClose}
          onRetry={handleRetry}
        />
      )}
    </div>
  );
}

export default App;
