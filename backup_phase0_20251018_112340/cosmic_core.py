# cosmic_core.py
"""
🌌 COSMIC RESONANCE EVALUATION - CORE ENGINE
Main framework combining mathematical foundations with practical evaluation
"""

import numpy as np
from sentence_transformers import SentenceTransformer
import networkx as nx
from scipy.spatial.distance import cosine
import json

class CosmicCore:
    """
    WHAT: Main cosmic resonance evaluation engine
    HOW-TO: Initialize and run cosmic synthesis + evaluation
    MATHEMATICAL: Integrates UCP principles with practical scoring
    """
    
    def __init__(self, model_name='all-mpnet-base-v2'):
        # Core components
        self.embedding_model = SentenceTransformer(model_name)
        self.mathematical_foundation = MathematicalFoundation()
        self.synthesis_engine = NarrativeSynthesis()
        self.evaluation_metrics = CosmicMetrics()
        
        print("🌌 Cosmic Resonance Engine Initialized")
        print("✅ Mathematical Foundation: ACTIVE")
        print("🌀 Synthesis Engine: READY")
        print("📊 Evaluation Metrics: OPERATIONAL")
    
    def cosmic_synthesis(self, parent_a, parent_b, method='hybrid'):
        """
        Perform cosmic narrative synthesis
        
        Args:
            parent_a, parent_b: Input narratives
            method: 'template', 'adjoint', or 'hybrid'
        
        Returns:
            Dictionary with synthesis results
        """
        print(f"🌀 Performing cosmic synthesis ({method} method)...")
        
        if method == 'template':
            child = self.synthesis_engine.template_synthesis(parent_a, parent_b)
        elif method == 'adjoint':
            child = self.synthesis_engine.adjoint_synthesis(parent_a, parent_b)
        else:  # hybrid
            child = self.synthesis_engine.hybrid_synthesis(parent_a, parent_b)
        
        return {
            'parent_a': parent_a,
            'parent_b': parent_b, 
            'child': child,
            'synthesis_method': method
        }
    
    def evaluate_resonance(self, parent_a, parent_b, child):
        """
        Comprehensive cosmic resonance evaluation
        
        Returns multi-dimensional scoring with mathematical validation
        """
        print("📊 Evaluating cosmic resonance...")
        
        # Traditional multi-dimensional scoring
        traditional_scores = self.evaluation_metrics.multi_dimensional_scoring(
            parent_a, parent_b, child
        )
        
        # Mathematical UCP validation
        mathematical_validation = self.mathematical_foundation.validate_ucp_principles(
            parent_a, parent_b, child
        )
        
        # Combined cosmic score
        cosmic_score = self._calculate_cosmic_score(
            traditional_scores, 
            mathematical_validation
        )
        
        return {
            'cosmic_score': cosmic_score,
            'traditional_scores': traditional_scores,
            'mathematical_validation': mathematical_validation,
            'interpretation': self._interpret_cosmic_score(cosmic_score)
        }
    
    def run_complete_experiment(self, narratives, num_syntheses=3):
        """
        Run complete cosmic experiment with multiple syntheses
        
        Args:
            narratives: List of input narratives
            num_syntheses: Number of synthesis experiments to run
        """
        print("🔬 Running Complete Cosmic Experiment...")
        print("=" * 60)
        
        results = []
        
        for i in range(min(num_syntheses, len(narratives) - 1)):
            print(f"\n🧪 Experiment {i+1}:")
            
            # Select parents
            parent_a, parent_b = narratives[i], narratives[i+1]
            print(f"   Parent A: {parent_a}")
            print(f"   Parent B: {parent_a}")
            
            # Perform synthesis
            synthesis_result = self.cosmic_synthesis(parent_a, parent_b, method='hybrid')
            child = synthesis_result['child']
            print(f"   Child: {child}")
            
            # Evaluate resonance
            evaluation = self.evaluate_resonance(parent_a, parent_b, child)
            
            experiment_result = {
                'experiment': i+1,
                'synthesis': synthesis_result,
                'evaluation': evaluation
            }
            
            results.append(experiment_result)
            
            print(f"   Cosmic Score: {evaluation['cosmic_score']:.3f}")
            print(f"   Interpretation: {evaluation['interpretation']}")
        
        # Overall analysis
        overall_analysis = self._analyze_experiment_results(results)
        
        return {
            'individual_results': results,
            'overall_analysis': overall_analysis
        }
    
    def _calculate_cosmic_score(self, traditional_scores, mathematical_validation):
        """Calculate combined cosmic score"""
        # Weight traditional scores 60%, mathematical 40%
        traditional_avg = np.mean(list(traditional_scores.values()))
        math_avg = mathematical_validation.get('overall_score', 0.5)
        
        cosmic_score = 0.6 * traditional_avg + 0.4 * math_avg
        return min(1.0, cosmic_score)  # Cap at 1.0
    
    def _interpret_cosmic_score(self, score):
        """Interpret cosmic score"""
        if score >= 0.8:
            return "🌟 COSMIC MASTERPIECE"
        elif score >= 0.7:
            return "✨ EXCELLENT SYNTHESIS" 
        elif score >= 0.6:
            return "💫 STRONG RESONANCE"
        elif score >= 0.5:
            return "🌱 PROMISING CREATION"
        else:
            return "🌀 EMERGING MEANING"
    
    def _analyze_experiment_results(self, results):
        """Analyze overall experiment results"""
        scores = [r['evaluation']['cosmic_score'] for r in results]
        
        return {
            'average_score': np.mean(scores),
            'best_score': max(scores),
            'consistency': np.std(scores),
            'total_experiments': len(results),
            'success_rate': len([s for s in scores if s >= 0.6]) / len(scores)
        }