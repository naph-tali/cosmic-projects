"""
🧪 COSMIC ENVIRONMENT TEST
Verify all components are working
"""

import sys
import os

print("🌌 COSMIC RESONANCE ENVIRONMENT TEST")
print("=" * 50)

# Test imports
try:
    from mathematical_foundation import MathematicalFoundation
    print("✅ MathematicalFoundation import: SUCCESS")
except ImportError as e:
    print(f"❌ MathematicalFoundation import: {e}")

try:
    from narrative_synthesis import NarrativeSynthesis  
    print("✅ NarrativeSynthesis import: SUCCESS")
except ImportError as e:
    print(f"❌ NarrativeSynthesis import: {e}")

try:
    from evaluation_metrics import CosmicMetrics
    print("✅ CosmicMetrics import: SUCCESS") 
except ImportError as e:
    print(f"❌ CosmicMetrics import: {e}")

# Test basic functionality
print("\n🔧 TESTING BASIC FUNCTIONALITY:")
try:
    # Test mathematical foundation
    math_foundation = MathematicalFoundation()
    test_result = math_foundation.validate_ucp_principles(
        "The universe began in silence",
        "Light spoke the first word", 
        "From silence and light, meaning emerges"
    )
    print(f"✅ Mathematical test: {test_result['overall_score']:.3f}")
    
    # Test narrative synthesis
    synthesizer = NarrativeSynthesis()
    child = synthesizer.template_synthesis("Hello", "World")
    print(f"✅ Synthesis test: '{child}'")
    
    print("\n🎉 ENVIRONMENT TEST: ALL SYSTEMS GO!")
    print("Ready for cosmic resonance experiments! 🌌")
    
except Exception as e:
    print(f"❌ Functional test failed: {e}")
    print("🔧 Some components need adjustment")

if __name__ == "__main__":
    pass
