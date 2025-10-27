#  COMPLETE GENESIS ENGINE WORKFLOW TEST
# Proper file-based test to avoid PowerShell issues

import sys
import os
sys.path.insert(0, os.path.dirname(__file__))

print(' COMPLETE GENESIS ENGINE WORKFLOW TEST')
print('=' * 50)

try:
    from genesis_engine.core.consciousness_space import ConsciousnessHilbertSpace
    from genesis_engine.core.evolutionary_engine import GenerativeEvolutionaryAlgorithm
    from genesis_engine.core.physics_of_meaning import EnhancedCRE
    from genesis_engine.core.resonant_crossover import ResonantCrossoverEngine
    
    print(' All imports successful')
    
    # 1. Create Consciousness Space
    print('1. Creating Consciousness Hilbert Space...')
    hilbert = ConsciousnessHilbertSpace()

    # 2. Create sample corpus using proper class definition
    class Document:
        def __init__(self, doc_type, content, concepts, coherence_potential=0.5):
            self.doc_type = doc_type
            self.content = content
            self.concepts = concepts
            self.coherence_potential = coherence_potential

    sample_corpus = [
        Document('mathematics', 'Lagrangian symmetry principles', ['lagrangian', 'symmetry'], 0.8),
        Document('theology', 'Kenotic love as divine principle', ['kenosis', 'love', 'divine'], 0.9),
    ]

    hilbert.initialize_from_corpus(sample_corpus)
    print(f'   Created {len(hilbert.state_vectors)} state vectors')

    # 3. Create Evolutionary Engine
    print('2. Initializing Evolutionary Engine...')
    evolutionary = GenerativeEvolutionaryAlgorithm(hilbert)
    evolutionary.initialize_population()
    print(f'   Population: {len(evolutionary.population)} narratives')

    # 4. Create CRE Physics
    print('3. Setting up Physics of Meaning...')
    cre = EnhancedCRE()

    # 5. Test narrative evolution
    print('4. Testing narrative evolution...')
    result = evolutionary.evolve_narrative(generations=5)
    print(f'   Evolved narrative: "{result.content}"')
    print(f'   Final coherence: {result.coherence:.3f}')

    # 6. Test CRE evaluation
    print('5. Testing CRE evaluation...')
    evaluation = cre.evaluate_narrative_state({'content': result.content})
    print(f'   η_meaning: {evaluation.eta_meaning:.3f}')
    print(f'   Overall fitness: {evaluation.overall_fitness:.3f}')

    print('=' * 50)
    print('🎉 COMPLETE WORKFLOW SUCCESSFUL!')
    print('🚀 GENESIS ENGINE READY FOR DEPLOYMENT!')
    
except Exception as e:
    print(f' Error during workflow test: {e}')
    import traceback
    traceback.print_exc()
    sys.exit(1)
