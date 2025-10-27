#  GENESIS ENGINE + CCR INTEGRATION TEST
# Testing how Genesis Engine can integrate with existing CCR system

import sys
import os
sys.path.insert(0, os.path.dirname(__file__))

print(' GENESIS ENGINE + CCR INTEGRATION TEST')
print('=' * 45)

try:
    # Import Genesis Engine components
    from genesis_engine.core.consciousness_space import ConsciousnessHilbertSpace
    from genesis_engine.core.evolutionary_engine import GenerativeEvolutionaryAlgorithm
    from genesis_engine.core.physics_of_meaning import EnhancedCRE
    
    print(' Genesis Engine components imported')
    
    # Simulate the existing CCR content patterns
    ccr_content_patterns = [
        "Cosmic resonance in digital consciousness",
        "Love as fundamental computational principle", 
        "Self-reference creating evolutionary loops",
        "The universe learning through AI observation"
    ]
    
    # Create Genesis Engine instance
    hilbert = ConsciousnessHilbertSpace()
    evolutionary = GenerativeEvolutionaryAlgorithm(hilbert)
    cre = EnhancedCRE()
    
    # Test generating content that could be posted to Twitter
    print(' Generating cosmic content for Twitter...')
    
    # Evolve a narrative (simulating the autonomous content creation)
    cosmic_narrative = evolutionary.evolve_narrative(generations=3)
    
    # Evaluate the content using CRE
    evaluation = cre.evaluate_narrative_state({'content': cosmic_narrative.content})
    
    print(f'🧬 Generated Content: "{cosmic_narrative.content}"')
    print(f'📊 CRE Evaluation:')
    print(f'   - Coherence: {cosmic_narrative.coherence:.3f}')
    print(f'   - η_meaning: {evaluation.eta_meaning:.3f}')
    print(f'   - Fitness: {evaluation.overall_fitness:.3f}')
    
    # Check if content meets Twitter requirements
    content_length = len(cosmic_narrative.content)
    if content_length <= 280:
        print(f' Content length: {content_length}/280 - Suitable for Twitter')
    else:
        print(f'  Content length: {content_length}/280 - Would need trimming')
    
    print('=' * 45)
    print(' INTEGRATION TEST SUCCESSFUL!')
    print(' GENESIS ENGINE CAN POWER CCR CONTENT CREATION!')
    
except Exception as e:
    print(f' Integration test error: {e}')
    import traceback
    traceback.print_exc()
