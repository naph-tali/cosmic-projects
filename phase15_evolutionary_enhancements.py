#  PHASE 1.5: EVOLUTIONARY ALGORITHM ENHANCEMENTS
# Testing the enhanced evolutionary engine with advanced algorithms

import sys
import os
sys.path.insert(0, os.path.dirname(__file__))

from typing import List, Dict, Any
from dataclasses import dataclass
import json

@dataclass
class CorpusDocument:
    """Enhanced document representation"""
    doc_type: str
    content: str
    concepts: List[str]
    coherence_potential: float = 0.0

class EvolutionaryEnhancements:
    """Test enhanced evolutionary algorithms"""
    
    def __init__(self):
        self.corpus_documents = self._load_corpus()
        self.hilbert_space = None
        self.evolutionary_engine = None
        self.enhanced_cre = None
        
    def _load_corpus(self) -> List[CorpusDocument]:
        """Load test corpus"""
        return [
            CorpusDocument(
                "mathematics", 
                "Lagrangian symmetry principles govern cosmic evolution through conservation laws.",
                ["lagrangian", "symmetry", "conservation", "cosmic", "evolution"],
                0.8
            ),
            CorpusDocument(
                "theology",
                "Kenotic love represents divine self-emptying as creative foundation.",
                ["kenosis", "love", "divine", "creation", "self-emptying"],
                0.9
            )
        ]
    
    def test_enhanced_evolution(self):
        """Test the enhanced evolutionary algorithms"""
        print("🧬 Testing Enhanced Evolutionary Algorithms...")
        
        from genesis_engine.core.consciousness_space import ConsciousnessHilbertSpace
        from genesis_engine.core.evolutionary_engine import GenerativeEvolutionaryAlgorithm
        from genesis_engine.core.physics_of_meaning import EnhancedCRE
        
        # Initialize systems
        self.hilbert_space = ConsciousnessHilbertSpace()
        self.hilbert_space.initialize_from_corpus(self.corpus_documents)
        
        self.enhanced_cre = EnhancedCRE()
        self.evolutionary_engine = GenerativeEvolutionaryAlgorithm(
            self.hilbert_space, 
            self.enhanced_cre
        )
        
        # Configure evolutionary parameters
        self.evolutionary_engine.population_size = 30
        self.evolutionary_engine.elitism_count = 3
        self.evolutionary_engine.mutation_rate = 0.4
        
        print("\\n Evolutionary Parameters:")
        print(f"   Population Size: {self.evolutionary_engine.population_size}")
        print(f"   Elitism Count: {self.evolutionary_engine.elitism_count}")
        print(f"   Mutation Rate: {self.evolutionary_engine.mutation_rate}")
        print(f"   Crossover Rate: {self.evolutionary_engine.crossover_rate}")
        
        # Initialize population
        self.evolutionary_engine.initialize_population()
        initial_report = self.evolutionary_engine.get_evolutionary_report()
        print(f"\\n Initial Population: {initial_report['current_population']} narratives")
        print(f"   Initial Best Fitness: {initial_report['best_fitness']:.3f}")
        
        # Run enhanced evolution
        print("\\n🔄 Running Enhanced Evolution...")
        best_narrative = self.evolutionary_engine.evolve_narrative(generations=50)
        
        # Get final report
        final_report = self.evolutionary_engine.get_evolutionary_report()
        
        print("\\n EVOLUTIONARY RESULTS:")
        print("=" * 50)
        print(f" Best Narrative: \"{best_narrative.content}\"")
        print(f" Final Fitness: {best_narrative.fitness_score:.3f}")
        print(f" Concepts: {', '.join(best_narrative.concepts)}")
        print(f" Generations: {final_report['total_generations']}")
        print(f" Population Diversity: {final_report['population_diversity']:.3f}")
        
        # Show fitness progression
        if final_report['fitness_progression']:
            initial_fitness = final_report['fitness_progression'][0]
            final_fitness = final_report['fitness_progression'][-1]
            improvement = final_fitness - initial_fitness
            print(f" Fitness Improvement: {improvement:+.3f}")
        
        return best_narrative
    
    def demonstrate_mutation_operators(self):
        """Demonstrate different mutation operators"""
        print("\\n Demonstrating Mutation Operators...")
        
        from genesis_engine.core.evolutionary_engine import NarrativeState
        
        # Create test narrative
        test_narrative = NarrativeState(
            state_id="test_mutation",
            content="Consciousness evolves through love and resonance.",
            concepts=["consciousness", "evolution", "love", "resonance"],
            coherence=0.7,
            fitness_score=0.6
        )
        
        print(f"   Original: \"{test_narrative.content}\"")
        print(f"   Concepts: {test_narrative.concepts}")
        
        # Test each mutation operator
        mutation_operators = [
            ("Concept Mutation", self.evolutionary_engine._concept_mutation),
            ("Sentence Structure", self.evolutionary_engine._sentence_structure_mutation),
            ("Semantic Expansion", self.evolutionary_engine._semantic_expansion_mutation),
            ("Conceptual Inversion", self.evolutionary_engine._conceptual_inversion_mutation)
        ]
        
        for name, operator in mutation_operators:
            mutated = operator(test_narrative)
            print(f"   {name}: \"{mutated.content}\"")
    
    def analyze_evolutionary_dynamics(self):
        """Analyze evolutionary dynamics and metrics"""
        print("\\n Analyzing Evolutionary Dynamics...")
        
        if not self.evolutionary_engine or not self.evolutionary_engine.metrics_history:
            print("   No evolutionary data available")
            return
        
        metrics = self.evolutionary_engine.metrics_history
        
        print("\\n Evolutionary Metrics Analysis:")
        print("   Generation | Avg Fitness | Max Fitness | Diversity | Sel Pressure")
        print("   " + "-" * 65)
        
        for i, metric in enumerate(metrics[::5]):  # Show every 5th generation
            if i % 3 == 0:  # Show sample generations
                print(f"   {metric.generation:10d} | {metric.avg_fitness:11.3f} | {metric.max_fitness:11.3f} | {metric.diversity:9.3f} | {metric.selection_pressure:13.3f}")
        
        # Show evolutionary trends
        if len(metrics) > 1:
            first = metrics[0]
            last = metrics[-1]
            
            print(f"\\n Evolutionary Trends:")
            print(f"   Fitness Growth: {last.avg_fitness - first.avg_fitness:+.3f}")
            print(f"   Diversity Change: {last.diversity - first.diversity:+.3f}")
            print(f"   Generations Completed: {last.generation}")

def main():
    """Main evolutionary enhancements demonstration"""
    print(" PHASE 1.5: EVOLUTIONARY ALGORITHM ENHANCEMENTS")
    print("=" * 60)
    
    enhancer = EvolutionaryEnhancements()
    
    # 1. Test enhanced evolution
    best_narrative = enhancer.test_enhanced_evolution()
    
    # 2. Demonstrate mutation operators
    enhancer.demonstrate_mutation_operators()
    
    # 3. Analyze evolutionary dynamics
    enhancer.analyze_evolutionary_dynamics()
    
    print("\\n" + "=" * 60)
    print(" EVOLUTIONARY ALGORITHM ENHANCEMENTS COMPLETE!")
    print(" Genesis Engine now features:")
    print("    Fitness-proportionate selection")
    print("    Multiple mutation operators") 
    print("    Environmental pressure simulation")
    print("    Elitism and generational memory")
    print("    Comprehensive metrics tracking")
    print("    Early stopping conditions")
    
    print("\\n Next: Enhance Resonant Crossover with semantic similarity")
    print(" Focus: Word embeddings and emergent property generation")

if __name__ == "__main__":
    main()
