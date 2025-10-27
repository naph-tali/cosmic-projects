# Simple test of Genesis Engine structure
from genesis_engine import ConsciousnessHilbertSpace, GenerativeEvolutionaryAlgorithm

def test_basic_functionality():
    print(" Testing basic Genesis Engine functionality...")
    
    # Test creating objects
    try:
        hilbert_space = ConsciousnessHilbertSpace()
        evolutionary_engine = GenerativeEvolutionaryAlgorithm(hilbert_space)
        
        print(" Basic object creation successful")
        print(f"   - Hilbert Space: {type(hilbert_space)}")
        print(f"   - Evolutionary Engine: {type(evolutionary_engine)}")
        
        # Test basic methods
        coherence = hilbert_space.measure_coherence()
        print(f"   - Initial coherence: {coherence}")
        
        return True
        
    except Exception as e:
        print(f" Test failed: {e}")
        return False

if __name__ == "__main__":
    success = test_basic_functionality()
    if success:
        print(" Basic functionality test PASSED!")
    else:
        print(" Basic functionality test FAILED!")
