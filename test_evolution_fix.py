#  QUICK FIX TEST FOR EVOLUTIONARY ENGINE
# Test the fixed evolutionary engine with proper stopping conditions

import sys
import os
sys.path.insert(0, os.path.dirname(__file__))

print(" QUICK FIX TEST FOR EVOLUTIONARY ENGINE")
print("=" * 45)

try:
    from genesis_engine.core.consciousness_space import ConsciousnessHilbertSpace
    from genesis_engine.core.evolutionary_engine import GenerativeEvolutionaryAlgorithm
    from genesis_engine.core.physics_of_meaning import EnhancedCRE
    
    print(" All imports successful")
    
    # Quick setup
    class SimpleDoc:
        def __init__(self, doc_type, content, concepts, coherence_potential=0.5):
            self.doc_type = doc_type
            self.content = content
            self.concepts = concepts
            self.coherence_potential = coherence_potential
    
    # Simple corpus
    corpus = [
        SimpleDoc("math", "Symmetry creates conservation", ["symmetry", "conservation"], 0.7),
        SimpleDoc("theology", "Love enables creation", ["love", "creation"], 0.8)
    ]
    
    # Initialize systems
    hilbert = ConsciousnessHilbertSpace()
    hilbert.initialize_from_corpus(corpus)
    
    cre = EnhancedCRE()
    evolutionary = GenerativeEvolutionaryAlgorithm(hilbert, cre)
    
    # Configure for quick test
    evolutionary.population_size = 20
    evolutionary.elitism_count = 2
    evolutionary.mutation_rate = 0.3
    
    print("\\n🧬 Running quick evolution test (10 generations max)...")
    evolutionary.initialize_population()
    
    # Run evolution with timeout protection
    result = evolutionary.evolve_narrative(generations=10)
    
    print(f"\\n🎯 Evolution completed successfully!")
    print(f"   Best narrative: \"{result.content}\"")
    print(f"   Fitness: {result.fitness_score:.3f}")
    print(f"   Generations: {evolutionary.generation}")
    
    # Show metrics
    if evolutionary.metrics_history:
        final_metrics = evolutionary.metrics_history[-1]
        print(f"   Final fitness: {final_metrics.max_fitness:.3f}")
        print(f"   Diversity: {final_metrics.diversity:.3f}")
    
    print("\\n EVOLUTIONARY ENGINE FIX VERIFIED - NO INFINITE LOOP!")
    
except Exception as e:
    print(f" Test failed: {e}")
    import traceback
    traceback.print_exc()
