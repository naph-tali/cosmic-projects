"""
Simple Cosmic Resonance Test - The Mustard Seed Version
"""

import numpy as np

class SimpleAlchemist:
    def __init__(self):
        print("🌱 Simple Alchemist initialized")
    
    def calculate_coherence(self, text1, text2, text3):
        # Simple length-based coherence for testing
        avg_len = (len(text1) + len(text2) + len(text3)) / 3
        return min(avg_len / 100, 1.0)

class SimpleEngine:
    def __init__(self):
        print("🌱 Simple Resonant Engine initialized")
    
    def cosmic_synthesis(self, parent_a, parent_b):
        return f"{parent_a} and {parent_b} merge into cosmic unity."

# Test immediately
if __name__ == "__main__":
    print("🚀 COSMIC RESONANCE ENGINE - MUSTARD SEED EDITION")
    
    alchemist = SimpleAlchemist()
    engine = SimpleEngine()
    
    # Test the cosmic process
    parent1 = "The universe began in silence"
    parent2 = "Light spoke the first word"
    child = engine.cosmic_synthesis(parent1, parent2)
    
    coherence = alchemist.calculate_coherence(parent1, parent2, child)
    
    print(f"Parent A: {parent1}")
    print(f"Parent B: {parent2}")
    print(f"✨ Cosmic Child: {child}")
    print(f"📊 Coherence Score: {coherence:.3f}")
    print("🎉 THE MUSTARD SEED HAS SPROUTED! 🌱")
