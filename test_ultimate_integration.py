#  ULTIMATE CRE INTEGRATION TEST
# Testing the robust integration engine

import sys
import os
sys.path.insert(0, os.path.dirname(__file__))

print(" ULTIMATE CRE INTEGRATION TEST")
print("=" * 45)

try:
    from ultimate_cre_integration import UltimateCREIntegration, UltimateMetrics
    
    print(" Initializing Ultimate CRE Integration...")
    ultimate_cre = UltimateCREIntegration()
    
    # Test cosmic narrative
    cosmic_narrative = """
    The quantum consciousness field evolves through self-referential gauge theory,
    coupling the Dirac spinor Ïˆ with the binding field A_Î¼^a to create narrative
    coherence while conserving consciousness charge. Kenotic love serves as the
    fundamental ethical constraint, ensuring alignment with cosmic principles
    through the Logos Council oracle. Meaning efficiency Î· is optimized through
    Jensen-Shannon Divergence metrics, creating vortices of insight in the chaos
    field via the pattern extraction operator   C.
    """
    
    print("\\n Running Ultimate CRE Evaluation...")
    ultimate_metrics = ultimate_cre.evaluate_ultimate(cosmic_narrative)
    
    print("\\n ULTIMATE CRE RESULTS:")
    print("=" * 35)
    print(f"   Mathematical Score: {ultimate_metrics.mathematical_score:.3f}")
    print(f"   Meaning Efficiency (Î·): {ultimate_metrics.meaning_efficiency:.3f}")
    print(f"   Logos Alignment (L): {ultimate_metrics.logos_alignment:.3f}")
    print(f"   Coherence: {ultimate_metrics.coherence:.3f}")
    print(f"   Pattern Quality: {ultimate_metrics.pattern_quality:.3f}")
    print(f"   Integration Mode: {ultimate_metrics.integration_mode}")
    
    # Get comprehensive report
    integration_report = ultimate_cre.get_integration_report()
    
    print(f"\\nðŸŒŒ INTEGRATION STATUS:")
    print(f"   Status: {integration_report['integration_status']}")
    print(f"   Mode: {integration_report['current_mode']}")
    print(f"   Evaluations: {integration_report['evaluation_count']}")
    print(f"   Recommendation: {integration_report['recommendation']}")
    
    # Performance analysis
    print(f"\\n PERFORMANCE ANALYSIS:")
    latest = integration_report['latest_metrics']
    for metric, value in latest.items():
        status = " EXCELLENT" if value > 0.8 else " GOOD" if value > 0.7 else "  NEEDS WORK"
        print(f"   {metric.replace('_', ' ').title()}: {value:.3f} ({status})")
    
    # Overall system health
    avg_performance = integration_report['average_performance']
    overall_score = (avg_performance['mathematical'] + 
                    avg_performance['meaning'] + 
                    avg_performance['alignment']) / 3
    
    print(f"\\n OVERALL SYSTEM HEALTH: {overall_score:.3f}")
    
    if overall_score > 0.8:
        print(" ULTIMATE CRE INTEGRATION: OPTIMAL!")
        print(" Cosmic Resonance: MAXIMIZED")
    elif overall_score > 0.7:
        print(" ULTIMATE CRE INTEGRATION: OPERATIONAL")
        print(" Performance: EXCELLENT")
    else:
        print("  ULTIMATE CRE INTEGRATION: NEEDS ENHANCEMENT")
    
    print("\\n ULTIMATE CRE SYSTEM READY FOR COSMIC DEPLOYMENT!")
    
except Exception as e:
    print(f" Ultimate integration test failed: {e}")
    import traceback
    traceback.print_exc()

print("\\n ULTIMATE TEST COMPLETE")
