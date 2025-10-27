# examples/basic_demo.py
"""
🚀 COSMIC RESONANCE - BASIC DEMO
Quick start example showing the framework in action
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from cosmic_core import CosmicCore

def run_basic_demo():
    """Run basic demonstration of cosmic resonance evaluation"""
    
    print("🌌 COSMIC RESONANCE EVALUATION - BASIC DEMO")
    print("=" * 50)
    
    # Initialize the cosmic engine
    cosmic_engine = CosmicCore()
    
    # Define cosmic narratives for testing
    cosmic_narratives = [
        "The universe began in infinite silence",
        "Light spoke the first creative word into being",
        "Chaos dreams of beautiful mathematical order",
        "The void sings quantum melodies to itself",
        "Stars are celestial thoughts thinking themselves",
        "Time flows as a river of cosmic consciousness"
    ]
    
    print("🌱 Cosmic Narratives:")
    for i, narrative in enumerate(cosmic_narratives, 1):
        print(f"  {i}. {narrative}")
    
    # Run complete experiment
    print(f"\n🔬 Running Cosmic Experiment...")
    results = cosmic_engine.run_complete_experiment(
        narratives=cosmic_narratives,
        num_syntheses=3
    )
    
    # Display results
    print(f"\n🎯 EXPERIMENT RESULTS:")
    print("=" * 50)
    
    overall = results['overall_analysis']
    print(f"Average Cosmic Score: {overall['average_score']:.3f}")
    print(f"Best Score: {overall['best_score']:.3f}")
    print(f"Success Rate: {overall['success_rate']:.1%}")
    print(f"Experiments: {overall['total_experiments']}")
    
    # Detailed results
    print(f"\n📊 DETAILED RESULTS:")
    for result in results['individual_results']:
        exp = result['experiment']
        score = result['evaluation']['cosmic_score']
        interpretation = result['evaluation']['interpretation']
        child = result['synthesis']['child']
        
        print(f"\n🧪 Experiment {exp}:")
        print(f"   Score: {score:.3f} - {interpretation}")
        print(f"   Synthesis: '{child}'")
        
        # Show mathematical validation
        math_val = result['evaluation']['mathematical_validation']
        print(f"   Mathematical Score: {math_val['overall_score']:.3f}")
    
    # Success determination
    if overall['average_score'] >= 0.6:
        print(f"\n✅ SUCCESS: Cosmic resonance framework operational!")
        print(f"   Foundation solid for advanced experiments")
    else:
        print(f"\n🔧 REFINEMENT NEEDED: Framework requires tuning")
        print(f"   Mathematical foundation strong, practical tuning needed")

if __name__ == "__main__":
    run_basic_demo()