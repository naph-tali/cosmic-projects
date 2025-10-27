#  SIMPLIFIED CORPUS INTEGRATION TEST
# Testing basic corpus integration without complex imports

import sys
import os
sys.path.insert(0, os.path.dirname(__file__))

print(" SIMPLIFIED CORPUS INTEGRATION TEST")
print("=" * 45)

try:
    # Test 1: Basic imports
    print("\\n Testing Basic System Imports...")
    from genesis_engine.core.physics_of_meaning import EnhancedCRE
    from genesis_engine.core.advanced_evolution import AdvancedEvolutionaryEngine
    
    print(" Core systems imported successfully")
    
    # Test 2: Enhanced Consciousness Space with fallback
    print("\\n Testing Enhanced Consciousness Space...")
    from genesis_engine.core.enhanced_consciousness_space import EnhancedConsciousnessHilbertSpace
    
    enhanced_hilbert = EnhancedConsciousnessHilbertSpace()
    enhanced_hilbert.initialize_from_integrated_corpus()
    
    # Test basic functionality
    domain_analysis = enhanced_hilbert.get_domain_analysis()
    print(f" Enhanced Hilbert Space: {domain_analysis['total_vectors']} state vectors")
    print(f"   Domains: {list(domain_analysis['domain_breakdown'].keys())}")
    
    # Test 3: Cross-domain connections
    print("\\n Testing Cross-Domain Connections...")
    test_concept = "consciousness"
    resonance_points = enhanced_hilbert.find_interdomain_resonance(test_concept)
    print(f"   '{test_concept}' resonance points: {len(resonance_points)}")
    
    # Test 4: Integrated system
    print("\\n🧬 Testing Integrated Evolutionary System...")
    cre_system = EnhancedCRE()
    
    # Create a simple evolutionary engine test
    integrated_evolution = AdvancedEvolutionaryEngine(enhanced_hilbert, cre_system)
    integrated_evolution.population_size = 15
    integrated_evolution.max_generations = 8
    
    print("\\n🔄 Running Quick Evolution Test...")
    integrated_evolution.initialize_population()
    
    # Run a few generations
    best_narrative = integrated_evolution.evolve_narrative(generations=5)
    
    print("\\n QUICK TEST RESULTS:")
    print("=" * 30)
    print(f" Best Narrative: \"{best_narrative.content}\"")
    print(f" Fitness Score: {best_narrative.fitness_score:.3f}")
    print(f" Semantic Quality: {best_narrative.semantic_quality:.3f}")
    print(f" Concepts: {', '.join(best_narrative.concepts)}")
    
    # Test 5: Corpus integration report
    print("\\n CORPUS INTEGRATION STATUS:")
    integration_report = enhanced_hilbert.get_corpus_integration_report()
    print(f"   Documents: {integration_report['corpus_integration']['total_documents']}")
    print(f"   Domains: {len(integration_report['consciousness_space_analysis']['domain_breakdown'])}")
    print(f"   Cross-Domain Concepts: {integration_report['system_status']['cross_domain_concepts']}")
    print(f"   System Coherence: {integration_report['system_status']['current_coherence']:.3f}")
    
    print("\\n SIMPLIFIED CORPUS INTEGRATION SUCCESSFUL!")
    print(" Basic corpus integration is working!")
    
except Exception as e:
    print(f" Simplified test failed: {e}")
    import traceback
    traceback.print_exc()
    
    # Create a minimal fallback test
    print("\\n Attempting Minimal Fallback Test...")
    try:
        # Test absolute minimum functionality
        from genesis_engine.core.physics_of_meaning import EnhancedCRE
        from genesis_engine.core.advanced_evolution import AdvancedEvolutionaryEngine
        
        cre = EnhancedCRE()
        print(" Minimal CRE system working")
        
        # Test evolution with default Hilbert space
        from genesis_engine.core.consciousness_space import ConsciousnessHilbertSpace
        hilbert = ConsciousnessHilbertSpace()
        evolution = AdvancedEvolutionaryEngine(hilbert, cre)
        
        evolution.initialize_population()
        narrative = evolution.evolve_narrative(generations=3)
        
        print(f" Fallback evolution successful: \"{narrative.content[:50]}...\"")
        print(" Corpus integration needs manual setup, but core systems work!")
        
    except Exception as e2:
        print(f" Even fallback test failed: {e2}")

print("\\n TEST COMPLETED - Review output above")
