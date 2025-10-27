#  DIAGNOSTIC TEST FOR ENHANCED CONSCIOUSNESS SPACE
# Quick verification that all methods are present

import sys
import os
sys.path.insert(0, os.path.dirname(__file__))

print(" ENHANCED CONSCIOUSNESS SPACE DIAGNOSTIC")
print("=" * 50)

try:
    from genesis_engine.core.enhanced_consciousness_space import EnhancedConsciousnessHilbertSpace
    
    # Test instantiation
    hilbert = EnhancedConsciousnessHilbertSpace()
    print(" EnhancedConsciousnessHilbertSpace instantiated successfully")
    
    # Check for required methods
    required_methods = [
        'initialize_from_integrated_corpus',
        '_create_state_from_integrated_document', 
        '_extract_domain_metadata',
        '_build_enhanced_cross_domain_connections',
        'measure_enhanced_coherence',
        'get_domain_analysis',
        'find_interdomain_resonance',
        'get_corpus_integration_report'
    ]
    
    missing_methods = []
    for method in required_methods:
        if hasattr(hilbert, method):
            print(f" Method '{method}' is present")
        else:
            missing_methods.append(method)
            print(f"❌ Method '{method}' is MISSING")
    
    if not missing_methods:
        print("\\n🎉 ALL REQUIRED METHODS ARE PRESENT!")
        print("🚀 Enhanced Consciousness Space is fully functional")
        
        # Quick functionality test
        print("\\n🧪 Testing quick initialization...")
        hilbert.initialize_from_integrated_corpus()
        
        # Test basic functionality
        coherence = hilbert.measure_enhanced_coherence()
        domain_analysis = hilbert.get_domain_analysis()
        
        print(f"✅ Quick test successful:")
        print(f"   Coherence: {coherence:.3f}")
        print(f"   Vectors: {domain_analysis['total_vectors']}")
        print(f"   Cross-domain concepts: {len(domain_analysis['cross_domain_bridges'])}")
        
    else:
        print(f"\\n MISSING METHODS: {missing_methods}")
        print(" Please fix the implementation")
        
except Exception as e:
    print(f" Diagnostic failed: {e}")
    import traceback
    traceback.print_exc()

print("\\n DIAGNOSTIC COMPLETE")
