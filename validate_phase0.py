#  PHASE 0 VALIDATION SCRIPT
# Tests the new Genesis Engine structure

import sys
import os

def validate_structure():
    """Validate the new Phase 0 structure"""
    print(" Validating Phase 0 Restructuring...")
    
    # Check core directories exist
    required_dirs = [
        "genesis_engine",
        "genesis_engine/core", 
        "genesis_engine/mathematics",
        "genesis_engine/theology",
        "genesis_engine/integration",
        "genesis_engine/tests"
    ]
    
    for dir_path in required_dirs:
        if not os.path.exists(dir_path):
            print(f" Missing directory: {dir_path}")
            return False
        print(f" Directory exists: {dir_path}")
    
    # Check core files exist
    required_files = [
        "genesis_engine/__init__.py",
        "genesis_engine/core/__init__.py", 
        "genesis_engine/core/consciousness_space.py",
        "genesis_engine/core/evolutionary_engine.py",
        "genesis_engine/core/physics_of_meaning.py", 
        "genesis_engine/core/resonant_crossover.py",
        "requirements.txt"
    ]
    
    for file_path in required_files:
        if not os.path.exists(file_path):
            print(f"❌ Missing file: {file_path}")
            return False
        print(f"✅ File exists: {file_path}")
    
    # Test imports
    try:
        from genesis_engine import ConsciousnessHilbertSpace, GenerativeEvolutionaryAlgorithm
        from genesis_engine.core.physics_of_meaning import EnhancedCRE
        print("✅ All imports successful")
    except ImportError as e:
        print(f"❌ Import failed: {e}")
        return False
    
    print("🎉 Phase 0 validation PASSED!")
    print("🚀 Ready for Phase 1: Genesis Engine Implementation")
    return True

if __name__ == "__main__":
    success = validate_structure()
    sys.exit(0 if success else 1)
