#  ADVANCED ALGORITHM DEVELOPMENT TEST
# Testing semantic similarity and advanced evolutionary algorithms

import sys
import os
sys.path.insert(0, os.path.dirname(__file__))

print(" ADVANCED ALGORITHM DEVELOPMENT TEST")
print("=" * 45)

try:
    from genesis_engine.core.consciousness_space import ConsciousnessHilbertSpace
    from genesis_engine.core.advanced_evolution import AdvancedEvolutionaryEngine
    from genesis_engine.core.advanced_crossover import AdvancedResonantCrossoverEngine
    from genesis_engine.core.physics_of_meaning import EnhancedCRE
    
    print(" Advanced systems imported successfully")
    
    # Test semantic crossover engine
    print("\\n Testing Advanced Resonant Crossover...")
    crossover_engine = AdvancedResonantCrossoverEngine()
    
    # Test semantic relationships
    test_concepts_a = ["consciousness", "evolution", "love"]
    test_concepts_b = ["resonance", "divine", "mathematics"]
    
    resonance_points = crossover_engine._advanced_resonance_detection(test_concepts_a, test_concepts_b)
    relationships = crossover_engine._analyze_semantic_relationships(test_concepts_a, test_concepts_b)
    
    print(f"   Found {len(resonance_points)} resonance points")
    print(f"   Found {len(relationships)} semantic relationships")
    
    for i, point in enumerate(resonance_points[:3]):
        print(f"     Resonance {i+1}: {point.concept_a} + {point.concept_b} = {point.resonance_strength:.3f} ({point.relationship_type})")
    
    # Test advanced evolutionary engine
    print("\\n🧬 Testing Advanced Evolutionary Engine...")
    
    class SimpleDoc:
        def __init__(self, doc_type, content, concepts, coherence_potential=0.5):
            self.doc_type = doc_type
            self.content = content
            self.concepts = concepts
            self.coherence_potential = coherence_potential
    
    # Enhanced corpus with semantic richness
    corpus = [
        SimpleDoc("mathematics", "Symmetry principles govern cosmic evolution through mathematical resonance.", 
                 ["symmetry", "cosmic", "evolution", "mathematics", "resonance"], 0.8),
        SimpleDoc("theology", "Kenotic love enables divine creation through self-emptying resonance.", 
                 ["kenosis", "love", "divine", "creation", "resonance"], 0.9),
        SimpleDoc("philosophy", "Consciousness participates in reality through observational resonance.", 
                 ["consciousness", "reality", "observation", "participation", "resonance"], 0.7)
    ]
    
    # Initialize advanced systems
    hilbert = ConsciousnessHilbertSpace()
    hilbert.initialize_from_corpus(corpus)
    
    cre = EnhancedCRE()
    advanced_evolution = AdvancedEvolutionaryEngine(hilbert, cre)
    
    # Configure for advanced testing
    advanced_evolution.population_size = 18
    advanced_evolution.max_generations = 20
    
    print("\\n Advanced Evolutionary Parameters:")
    print(f"   Population: {advanced_evolution.population_size}")
    print(f"   Max Generations: {advanced_evolution.max_generations}")
    print(f"   Semantic Integration: ENABLED")
    
    # Run advanced evolution
    print("\\n Running Advanced Evolution with Semantic Integration...")
    advanced_evolution.initialize_population()
    
    initial_report = advanced_evolution.get_advanced_report()
    print(f"   Initial Fitness: {initial_report['best_fitness']:.3f}")
    print(f"   Initial Semantic Quality: {initial_report['best_semantic_quality']:.3f}")
    
    # Evolve with advanced algorithms
    best_narrative = advanced_evolution.evolve_narrative(generations=15)
    
    # Advanced results
    final_report = advanced_evolution.get_advanced_report()
    
    print("\\n ADVANCED EVOLUTION RESULTS:")
    print("=" * 50)
    print(f" Best Narrative: \"{best_narrative.content}\"")
    print(f" Final Fitness: {best_narrative.fitness_score:.3f}")
    print(f" Semantic Quality: {best_narrative.semantic_quality:.3f}")
    print(f" Key Concepts: {', '.join(best_narrative.concepts)}")
    print(f" Generations: {final_report['total_generations']}")
    
    # Show progression
    if final_report['fitness_progression']:
        initial_fitness = final_report['fitness_progression'][0]
        final_fitness = final_report['fitness_progression'][-1]
        improvement = final_fitness - initial_fitness
        print(f" Fitness Improvement: {improvement:+.3f}")
    
    if final_report['semantic_progression']:
        initial_semantic = final_report['semantic_progression'][0]
        final_semantic = final_report['semantic_progression'][-1]
        semantic_improvement = final_semantic - initial_semantic
        print(f" Semantic Improvement: {semantic_improvement:+.3f}")
    
    print("\\n ADVANCED ALGORITHMS WORKING SUCCESSFULLY!")
    print(" Semantic integration and advanced evolution operational!")
    
except Exception as e:
    print(f" Advanced algorithm test failed: {e}")
    import traceback
    traceback.print_exc()
    sys.exit(1)
