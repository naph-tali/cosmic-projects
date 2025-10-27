#  CORPUS INTEGRATION TEST
# Testing the integration of actual documents into Genesis Engine

import sys
import os
sys.path.insert(0, os.path.dirname(__file__))

print(" CORPUS INTEGRATION TEST")
print("=" * 40)

try:
    from genesis_engine.integration.corpus_integrator import CorpusIntegrator
    from genesis_engine.core.enhanced_consciousness_space import EnhancedConsciousnessHilbertSpace
    from genesis_engine.core.advanced_evolution import AdvancedEvolutionaryEngine
    from genesis_engine.core.physics_of_meaning import EnhancedCRE
    
    print(" Corpus integration systems imported successfully")
    
    # Test 1: Corpus Integration
    print("\\n Testing Corpus Integration...")
    integrator = CorpusIntegrator()
    corpus_documents = integrator.integrate_cosmic_corpus()
    
    corpus_report = integrator.get_corpus_report()
    print(f"   Integrated Documents: {corpus_report['total_documents']}")
    print(f"   Domain Breakdown:")
    for domain, stats in corpus_report['domain_breakdown'].items():
        print(f"     - {domain}: {stats['count']} documents ({stats['percentage']:.1f}%)")
    
    print(f"   Quality Metrics:")
    print(f"     - Average Coherence: {corpus_report['quality_metrics']['average_coherence']:.3f}")
    print(f"     - Concept Density: {corpus_report['quality_metrics']['concept_density']:.3f}")
    
    # Test 2: Enhanced Consciousness Space
    print("\\n Testing Enhanced Consciousness Space...")
    enhanced_hilbert = EnhancedConsciousnessHilbertSpace()
    enhanced_hilbert.initialize_from_integrated_corpus()
    
    domain_analysis = enhanced_hilbert.get_domain_analysis()
    print(f"   State Vectors: {domain_analysis['total_vectors']}")
    print(f"   Domain Analysis:")
    for domain, stats in domain_analysis['domain_breakdown'].items():
        print(f"     - {domain}: {stats['vector_count']} vectors, Coherence: {stats['average_coherence']:.3f}")
    
    print(f"   Cross-Domain Bridges: {len(domain_analysis['cross_domain_bridges'])}")
    
    # Test 3: Cross-Domain Resonance
    print("\\n Testing Cross-Domain Resonance...")
    test_concepts = ['consciousness', 'love', 'evolution', 'resonance']
    
    for concept in test_concepts:
        resonance_points = enhanced_hilbert.find_interdomain_resonance(concept)
        if resonance_points:
            print(f"   '{concept}' connects {len(resonance_points)} domains")
            for point in resonance_points[:2]:  # Show first 2
                print(f"     - {point['domain']}: {point['content_sample']}")
    
    # Test 4: Integrated Evolutionary System
    print("\\n Testing Integrated Evolutionary System...")
    cre_system = EnhancedCRE()
    integrated_evolution = AdvancedEvolutionaryEngine(enhanced_hilbert, cre_system)
    
    # Configure for integrated evolution
    integrated_evolution.population_size = 20
    integrated_evolution.max_generations = 15
    
    print("\\n🔄 Running Integrated Evolution with Actual Corpus...")
    integrated_evolution.initialize_population()
    
    initial_report = integrated_evolution.get_advanced_report()
    print(f"   Initial Fitness: {initial_report['best_fitness']:.3f}")
    print(f"   Initial Semantic Quality: {initial_report['best_semantic_quality']:.3f}")
    
    # Run integrated evolution
    best_narrative = integrated_evolution.evolve_narrative(generations=10)
    
    # Integrated results
    final_report = integrated_evolution.get_advanced_report()
    corpus_integration_report = enhanced_hilbert.get_corpus_integration_report()
    
    print("\\n INTEGRATED SYSTEM RESULTS:")
    print("=" * 50)
    print(f" Best Narrative: \"{best_narrative.content}\"")
    print(f" Final Fitness: {best_narrative.fitness_score:.3f}")
    print(f" Semantic Quality: {best_narrative.semantic_quality:.3f}")
    print(f" Cross-Domain Concepts: {', '.join(best_narrative.concepts)}")
    print(f" Generations: {final_report['total_generations']}")
    
    # Show corpus integration impact
    print(f"\\n CORPUS INTEGRATION IMPACT:")
    print(f"   Total Documents: {corpus_integration_report['corpus_integration']['total_documents']}")
    print(f"   Domain Coverage: {len(corpus_integration_report['consciousness_space_analysis']['domain_breakdown'])} domains")
    print(f"   Cross-Domain Concepts: {corpus_integration_report['system_status']['cross_domain_concepts']}")
    print(f"   System Coherence: {corpus_integration_report['system_status']['current_coherence']:.3f}")
    
    print("\\n CORPUS INTEGRATION SUCCESSFUL!")
    print(" Genesis Engine now operates on actual cosmic knowledge!")
    
except Exception as e:
    print(f" Corpus integration test failed: {e}")
    import traceback
    traceback.print_exc()
    sys.exit(1)
