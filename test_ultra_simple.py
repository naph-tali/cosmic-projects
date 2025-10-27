#  ULTRA-SIMPLE EVOLUTION TEST
# Minimal test to verify basic functionality

import sys
import os
sys.path.insert(0, os.path.dirname(__file__))

print(" ULTRA-SIMPLE EVOLUTION TEST")
print("=" * 35)

try:
    from genesis_engine.core.evolutionary_engine import GenerativeEvolutionaryAlgorithm
    from genesis_engine.core.consciousness_space import ConsciousnessHilbertSpace
    
    # Minimal setup
    hilbert = ConsciousnessHilbertSpace()
    evolutionary = GenerativeEvolutionaryAlgorithm(hilbert)
    
    # Ultra-minimal parameters
    evolutionary.population_size = 10
    evolutionary.max_generations = 10
    
    print(" Initializing minimal evolution...")
    evolutionary.initialize_population()
    
    print(" Running minimal evolution (5 generations)...")
    result = evolutionary.evolve_narrative(generations=5)
    
    print(f" Evolution completed!")
    print(f"   Result: \"{result.content}\"")
    print(f"   Fitness: {result.fitness_score:.3f}")
    print(f"   Concepts: {result.concepts}")
    
except Exception as e:
    print(f"❌ Ultra-simple test failed: {e}")
    import traceback
    traceback.print_exc()
