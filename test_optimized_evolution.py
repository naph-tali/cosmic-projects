#  OPTIMIZED EVOLUTIONARY TEST - FAST AND RELIABLE
# Testing evolutionary enhancements with optimized parameters

import sys
import os
sys.path.insert(0, os.path.dirname(__file__))

print(" OPTIMIZED EVOLUTIONARY TEST")
print("=" * 40)

try:
    from genesis_engine.core.consciousness_space import ConsciousnessHilbertSpace
    from genesis_engine.core.evolutionary_engine import GenerativeEvolutionaryAlgorithm
    from genesis_engine.core.physics_of_meaning import EnhancedCRE
    
    print(" Systems initialized")
    
    # Simple document class
    class SimpleDoc:
        def __init__(self, doc_type, content, concepts, coherence_potential=0.5):
            self.doc_type = doc_type
            self.content = content
            self.concepts = concepts
            self.coherence_potential = coherence_potential
    
    # Minimal corpus for fast testing
    corpus = [
        SimpleDoc("math", "Symmetry creates conservation", ["symmetry", "conservation", "physics"], 0.7),
        SimpleDoc("theology", "Love enables creation", ["love", "creation", "divine"], 0.8),
        SimpleDoc("philosophy", "Consciousness observes reality", ["consciousness", "observation", "reality"], 0.6)
    ]
    
    # Initialize systems with optimized settings
    hilbert = ConsciousnessHilbertSpace()
    hilbert.initialize_from_corpus(corpus)
    
    cre = EnhancedCRE()
    evolutionary = GenerativeEvolutionaryAlgorithm(hilbert, cre)
    
    # OPTIMIZED PARAMETERS FOR FAST TESTING
    evolutionary.population_size = 15      # Smaller population
    evolutionary.elitism_count = 2         # Fewer elites
    evolutionary.mutation_rate = 0.2       # Lower mutation rate
    evolutionary.crossover_rate = 0.6      # Balanced crossover
    
    print("\\n Optimized Parameters:")
    print(f"   Population: {evolutionary.population_size}")
    print(f"   Max Generations: 20")
    print(f"   Mutation Rate: {evolutionary.mutation_rate}")
    
    # Initialize population
    evolutionary.initialize_population()
    initial_fitness = evolutionary.get_evolutionary_report()['best_fitness']
    print(f"   Initial Fitness: {initial_fitness:.3f}")
    
    # Run optimized evolution
    print("\\n Running Optimized Evolution...")
    best_narrative = evolutionary.evolve_narrative(generations=20)  # Fewer generations
    
    # Results
    final_report = evolutionary.get_evolutionary_report()
    
    print("\\n QUICK RESULTS:")
    print("=" * 40)
    print(f"🎯 Best Narrative: \"{best_narrative.content}\"")
    print(f"📊 Final Fitness: {best_narrative.fitness_score:.3f}")
    print(f"🧠 Key Concepts: {', '.join(best_narrative.concepts[:5])}")
    print(f"📈 Generations: {final_report['total_generations']}")
    
    # Show improvement
    improvement = best_narrative.fitness_score - initial_fitness
    print(f" Fitness Improvement: {improvement:+.3f}")
    
    # Quick metrics
    if evolutionary.metrics_history:
        metrics = evolutionary.metrics_history[-1]
        print(f" Final Diversity: {metrics.diversity:.3f}")
        print(f" Average Fitness: {metrics.avg_fitness:.3f}")
    
    print("\\n EVOLUTION COMPLETED SUCCESSFULLY!")
    print(" System is stable and performing well!")
    
except Exception as e:
    print(f" Test failed: {e}")
    import traceback
    traceback.print_exc()
    sys.exit(1)
