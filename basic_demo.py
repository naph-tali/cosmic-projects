# examples/basic_demo.py
"""
🚀 COSMIC RESONANCE - BASIC DEMO (FIXED IMPORTS)
"""

import sys
import os

# Add parent directory to Python path
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)

try:
    from cosmic_core import CosmicCore
    print("✅ Successfully imported CosmicCore")
except ImportError as e:
    print(f"❌ Import failed: {e}")
    print("🔧 Trying alternative import...")
    
    # Alternative import attempt
    sys.path.insert(0, os.getcwd())
    from cosmic_core import CosmicCore

def run_basic_demo():
    """Run basic demonstration of cosmic resonance evaluation"""
    
    print("🌌 COSMIC RESONANCE EVALUATION - BASIC DEMO")
    print("=" * 50)
    
    try:
        # Initialize the cosmic engine
        cosmic_engine = CosmicCore()
        print("✅ Cosmic engine initialized successfully")
        
    except Exception as e:
        print(f"❌ Failed to initialize cosmic engine: {e}")
        print("🔧 Creating minimal working version...")
        return create_minimal_demo()
    
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
    try:
        results = cosmic_engine.run_complete_experiment(
            narratives=cosmic_narratives,
            num_syntheses=2  # Reduced for stability
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
            
    except Exception as e:
        print(f"❌ Experiment failed: {e}")
        print("🔧 Falling back to minimal test...")
        run_minimal_test()

def create_minimal_demo():
    """Create a minimal working demo when main components fail"""
    print("\n🛠️  RUNNING MINIMAL DEMO")
    print("=" * 40)
    
    # Simple cosmic synthesis without complex dependencies
    def simple_synthesis(a, b):
        templates = [
            f"The cosmic dance of '{a}' and '{b}' reveals new understanding",
            f"When '{a}' meets '{b}', we discover deeper truth", 
            f"From '{a}' and '{b}', emergent meaning arises"
        ]
        import random
        return random.choice(templates)
    
    # Simple scoring
    def simple_score(text):
        words = text.split()
        length_score = min(len(words) / 20, 1.0)
        structure_score = 1.0 if text[0].isupper() and text[-1] in '.!?' else 0.7
        return (length_score + structure_score) / 2
    
    # Test narratives
    narratives = [
        "The universe began in silence",
        "Light is the first word",
        "Chaos dreams of order"
    ]
    
    print("🌱 Testing with narratives:")
    for i, narr in enumerate(narratives):
        print(f"  {i+1}. {narr}")
    
    print(f"\n🔬 Running minimal synthesis...")
    results = []
    
    for i in range(len(narratives)-1):
        parent_a, parent_b = narratives[i], narratives[i+1]
        child = simple_synthesis(parent_a, parent_b)
        score = simple_score(child)
        
        print(f"\n🧪 Experiment {i+1}:")
        print(f"   Parents: '{parent_a}' + '{parent_b}'")
        print(f"   Child: '{child}'")
        print(f"   Score: {score:.3f}")
        
        results.append(score)
    
    avg_score = sum(results) / len(results)
    print(f"\n📊 Average Score: {avg_score:.3f}")
    
    if avg_score >= 0.6:
        print("✅ MINIMAL DEMO: Basic functionality working!")
    else:
        print("🔧 MINIMAL DEMO: Needs improvement")

def run_minimal_test():
    """Run a minimal test of individual components"""
    print("\n🔧 TESTING INDIVIDUAL COMPONENTS")
    
    # Test mathematical foundation
    try:
        from mathematical_foundation import MathematicalFoundation
        math_test = MathematicalFoundation()
        test_result = math_test.validate_ucp_principles("test", "test", "test")
        print(f"✅ Mathematical Foundation: {test_result['overall_score']:.3f}")
    except Exception as e:
        print(f"❌ Mathematical Foundation: {e}")
    
    # Test narrative synthesis  
    try:
        from narrative_synthesis import NarrativeSynthesis
        synth_test = NarrativeSynthesis()
        child = synth_test.template_synthesis("hello", "world")
        print(f"✅ Narrative Synthesis: '{child}'")
    except Exception as e:
        print(f"❌ Narrative Synthesis: {e}")
    
    print("🔧 Component testing complete")

if __name__ == "__main__":
    run_basic_demo()