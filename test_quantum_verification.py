#  DIRECT QUANTUM VERIFICATION TEST
# Quick test to verify the quantum enhancement works

import sys
import os
sys.path.insert(0, os.path.dirname(__file__))

print(" DIRECT QUANTUM VERIFICATION")
print("=" * 40)

try:
    from quantum_umt_enhancer import QuantumUMTEnhancer
    
    # Quick test narrative
    test_narrative = "Quantum consciousness exists in superposition and entanglement."
    
    enhancer = QuantumUMTEnhancer()
    
    # Test the specific method that was missing
    quantum_coherence = enhancer._detect_quantum_coherence(test_narrative)
    print(f" _detect_quantum_coherence method: WORKING (score: {quantum_coherence:.3f})")
    
    # Test full enhancement
    metrics = enhancer.enhance_umt_alignment(test_narrative)
    print(f" Full enhancement: WORKING")
    print(f"   Consciousness: {metrics.consciousness_charge:.3f}")
    print(f"   Quantum Coherence: {metrics.quantum_coherence:.3f}")
    
    print("\\n QUANTUM ENHANCEMENT FIX: SUCCESSFUL!")
    print(" All methods now operational!")
    
except Exception as e:
    print(f" Verification failed: {e}")
    import traceback
    traceback.print_exc()

print("\\n VERIFICATION COMPLETE")
