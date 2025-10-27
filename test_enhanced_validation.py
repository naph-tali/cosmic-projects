#  ENHANCED CORPUS VALIDATION TEST
# Testing the improved cross-domain connections and coherence

import sys
import os
sys.path.insert(0, os.path.dirname(__file__))

print(" ENHANCED CORPUS VALIDATION TEST")
print("=" * 45)

try:
    # Test enhanced imports
    print("\\n Testing Enhanced System Components...")
    from genesis_engine.core.enhanced_consciousness_space import EnhancedConsciousnessHilbertSpace
    from genesis_engine.core.enhanced_cross_domain import EnhancedCrossDomainDetector
    from genesis_engine.core.physics_of_meaning import EnhancedCRE
    from genesis_engine.core.advanced_evolution import AdvancedEvolutionaryEngine
    
    print(" All enhanced components imported successfully")
    
    # Test 1: Enhanced Cross-Domain Detection
    print("\\n Testing Enhanced Cross-Domain Detection...")
    detector = EnhancedCrossDomainDetector()
    
    # Create test domain vectors with overlapping concepts
    test_domains = {
        'mathematics': [
            type('Vector', (), {'concepts': ['symmetry', 'balance', 'evolution', 'consciousness']})(),
            type('Vector', (), {'concepts': ['resonance', 'vibration', 'pattern']})()
        ],
        'theology': [
            type('Vector', (), {'concepts': ['love', 'divine', 'consciousness', 'sacred']})(),
            type('Vector', (), {'concepts': ['compassion', 'kindness', 'evolution']})()
        ],
        'philosophy': [
            type('Vector', (), {'concepts': ['reality', 'existence', 'consciousness', 'being']})(),
            type('Vector', (), {'concepts': ['truth', 'awareness', 'mind']})()
        ]
    }
    
    cross_connections = detector.detect_cross_domain_connections(test_domains)
    print(f"   Test cross-domain connections: {len(cross_connections)} concepts")
    
    # Test 2: Enhanced Consciousness Space
    print("\\n Testing Enhanced Consciousness Space with Improved Detection...")
    enhanced_hilbert = EnhancedConsciousnessHilbertSpace()
    enhanced_hilbert.initialize_from_integrated_corpus()
    
    domain_analysis = enhanced_hilbert.get_domain_analysis()
    print(f"   Enhanced Hilbert Space: {domain_analysis['total_vectors']} state vectors")
    print(f"   Cross-Domain Bridges: {len(domain_analysis['cross_domain_bridges'])}")
    
    # Show some cross-domain connections
    if domain_analysis['cross_domain_bridges']:
        print("   Sample Cross-Domain Concepts:")
        for concept, domains in list(domain_analysis['cross_domain_bridges'].items())[:3]:
            print(f"     - '{concept}': {domains}")
    
    # Test 3: Enhanced Evolution with Cross-Domain Concepts
    print("\\n Testing Enhanced Evolutionary Integration...")
    cre_system = EnhancedCRE()
    enhanced_evolution = AdvancedEvolutionaryEngine(enhanced_hilbert, cre_system)
    
    enhanced_evolution.population_size = 20
    enhanced_evolution.max_generations = 10
    
    print("\\n Running Enhanced Evolution...")
    enhanced_evolution.initialize_population()
    
    # Run evolution with cross-domain enhancement
    best_narrative = enhanced_evolution.evolve_narrative(generations=8)
    
    # Enhanced results analysis
    integration_report = enhanced_hilbert.get_corpus_integration_report()
    
    print("\\n ENHANCED SYSTEM RESULTS:")
    print("=" * 40)
    print(f" Best Narrative: \"{best_narrative.content}\"")
    print(f" Fitness Score: {best_narrative.fitness_score:.3f}")
    print(f" Semantic Quality: {best_narrative.semantic_quality:.3f}")
    print(f" Cross-Domain Concepts: {', '.join(best_narrative.concepts)}")
    
    # Cross-domain impact analysis
    print(f"\\n CROSS-DOMAIN INTEGRATION IMPACT:")
    print(f"   Total Documents: {integration_report['corpus_integration']['total_documents']}")
    print(f"   Domains Integrated: {len(integration_report['consciousness_space_analysis']['domain_breakdown'])}")
    print(f"   Cross-Domain Concepts: {integration_report['system_status']['cross_domain_concepts']}")
    print(f"   System Coherence: {integration_report['system_status']['current_coherence']:.3f}")
    
    # Check if we improved from baseline
    baseline_coherence = 0.480
    current_coherence = integration_report['system_status']['current_coherence']
    improvement = ((current_coherence - baseline_coherence) / baseline_coherence) * 100
    
    print(f"   Coherence Improvement: {improvement:+.1f}% from baseline")
    
    if integration_report['system_status']['cross_domain_concepts'] > 0:
        print("\\n CROSS-DOMAIN CONNECTION ISSUE: RESOLVED!")
        print(" System now detecting conceptual bridges between domains")
    else:
        print("\\n  Cross-domain connections still need refinement")
    
    print("\\n ENHANCED VALIDATION COMPLETE!")
    
except Exception as e:
    print(f" Enhanced validation failed: {e}")
    import traceback
    traceback.print_exc()

print("\\n ENHANCEMENT PROTOCOL EXECUTION COMPLETE")
