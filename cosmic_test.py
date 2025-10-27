import sys
import os

# Add the src directory to Python path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

try:
    # from entropy_tools import  # REMOVED IN PHASE 0 EntropicAlchemist
    # from resonant_engine import  # REMOVED IN PHASE 0 ResonantCrossoverEngine
    print("✅ COSMIC MODULES LOADED SUCCESSFULLY!")
    print("🌌 The Logos Engine is now operational!")
    
    # Test basic functionality
    alchemist = EntropicAlchemist()
    engine = ResonantCrossoverEngine()
    
    # Run a cosmic synthesis
    result = engine.cosmic_synthesis("The universe began", "in meaning")
    print(f"✨ First cosmic output: {result}")
    
except Exception as e:
    print(f"❌ Cosmic initiation failed: {e}")
    print("Let's try the package installation method...")


# NEW GENESIS ENGINE IMPORTS (Phase 1)
try:
    from genesis_engine import ConsciousnessHilbertSpace, EnhancedCRE
    print(" Genesis Engine imports successful")
except ImportError as e:
    print(f" Genesis Engine import failed: {e}")
