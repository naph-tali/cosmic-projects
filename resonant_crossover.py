#  RESONANT CROSSOVER ENGINE - ROBUST VERSION  
# Fixed concept handling and improved performance

from typing import Tuple, List, Dict, Any
from dataclasses import dataclass

@dataclass
class ResonancePoint:
    """A point of conceptual resonance between two states"""
    concept_a: str
    concept_b: str 
    resonance_strength: float
    emergent_potential: float

class ResonantCrossoverEngine:
    """The primary variation operator for creative synthesis - ROBUST VERSION"""
    
    def __init__(self):
        self.resonance_threshold = 0.5  # Lowered threshold for more crossover
        self.max_concept_pairs = 20  # Limit to prevent combinatorial explosion
        
    def crossover(self, parent_a, parent_b):
        """Perform sacred synthesis of two narrative fragments - ROBUST"""
        try:
            # Extract concepts from parents with safety checks
            concepts_a = self._safe_get_concepts(parent_a)
            concepts_b = self._safe_get_concepts(parent_b)
            
            # Limit concepts to prevent combinatorial explosion
            concepts_a = concepts_a[:10]  # Limit to first 10 concepts
            concepts_b = concepts_b[:10]  # Limit to first 10 concepts
            
            # 1. Resonance detection
            resonance_points = self._detect_resonance_points(concepts_a, concepts_b)
            
            # 2. Conceptual blending  
            blended_concepts = self._blend_concepts(concepts_a, concepts_b, resonance_points)
            
            # 3. Create offspring content
            content_a = self._safe_get_content(parent_a)
            content_b = self._safe_get_content(parent_b)
            blended_content = self._blend_content(content_a, content_b)
            
            # Create offspring state
            offspring = type('OffspringState', (), {
                'vector_id': f"offspring_{getattr(parent_a, 'vector_id', 'A')}_{getattr(parent_b, 'vector_id', 'B')}",
                'content': blended_content,
                'concepts': blended_concepts,
                'coherence': (getattr(parent_a, 'coherence', 0.3) + getattr(parent_b, 'coherence', 0.3)) / 2,
                'parent_ids': [getattr(parent_a, 'vector_id', 'A'), getattr(parent_b, 'vector_id', 'B')]
            })()
            
            return offspring
            
        except Exception as e:
            # Fallback: simple concatenation if crossover fails
            return self._fallback_crossover(parent_a, parent_b)
    
    def _safe_get_concepts(self, parent) -> List[str]:
        """Safely extract concepts from parent with validation"""
        concepts = getattr(parent, 'concepts', [])
        if concepts is None:
            concepts = []
        # Ensure all concepts are strings and non-empty
        return [str(c).strip() for c in concepts if c and str(c).strip()]
    
    def _safe_get_content(self, parent) -> str:
        """Safely extract content from parent"""
        content = getattr(parent, 'content', '')
        if content is None:
            content = ''
        return str(content)
    
    def _fallback_crossover(self, parent_a, parent_b):
        """Fallback crossover method if main method fails"""
        content_a = self._safe_get_content(parent_a)
        content_b = self._safe_get_content(parent_b)
        concepts_a = self._safe_get_concepts(parent_a)
        concepts_b = self._safe_get_concepts(parent_b)
        
        # Simple blending as fallback
        blended_content = f"{content_a} integrated with {content_b}"
        blended_concepts = list(set(concepts_a + concepts_b))
        
        offspring = type('OffspringState', (), {
            'vector_id': f"fallback_{getattr(parent_a, 'vector_id', 'A')}_{getattr(parent_b, 'vector_id', 'B')}",
            'content': blended_content,
            'concepts': blended_concepts,
            'coherence': (getattr(parent_a, 'coherence', 0.3) + getattr(parent_b, 'coherence', 0.3)) / 2,
            'parent_ids': [getattr(parent_a, 'vector_id', 'A'), getattr(parent_b, 'vector_id', 'B')]
        })()
        
        return offspring
    
    def _detect_resonance_points(self, concepts_a: List[str], concepts_b: List[str]) -> List[ResonancePoint]:
        """Find conceptual points of maximum resonance - OPTIMIZED"""
        resonance_points = []
        
        # Limit the number of comparisons to prevent slowdown
        max_comparisons = min(len(concepts_a) * len(concepts_b), self.max_concept_pairs)
        comparisons = 0
        
        for concept_a in concepts_a:
            for concept_b in concepts_b:
                if comparisons >= max_comparisons:
                    break
                    
                score = self._calculate_conceptual_resonance(concept_a, concept_b)
                if score > self.resonance_threshold:
                    resonance_points.append(
                        ResonancePoint(
                            concept_a=concept_a,
                            concept_b=concept_b,
                            resonance_strength=score,
                            emergent_potential=score * 1.2
                        )
                    )
                
                comparisons += 1
            if comparisons >= max_comparisons:
                break
        
        return resonance_points
    
    def _calculate_conceptual_resonance(self, concept_a: str, concept_b: str) -> float:
        """Calculate resonance between two concepts - ROBUST"""
        try:
            # Handle None or empty concepts
            if not concept_a or not concept_b:
                return 0.0
                
            a_lower = str(concept_a).lower().strip()
            b_lower = str(concept_b).lower().strip()
            
            if not a_lower or not b_lower:
                return 0.0
            
            # Exact match
            if a_lower == b_lower:
                return 1.0
                
            # Shared substring (quick check)
            if a_lower in b_lower or b_lower in a_lower:
                return 0.8
                
            # Shared letters (faster implementation)
            set_a = set(a_lower)
            set_b = set(b_lower)
            
            if not set_a or not set_b:
                return 0.3
                
            shared_letters = len(set_a & set_b)
            total_letters = len(set_a | set_b)
            
            if total_letters > 0:
                return shared_letters / total_letters
                
            return 0.3  # Default low resonance
            
        except Exception:
            return 0.3  # Safe fallback
    
    def _blend_concepts(self, concepts_a: List[str], concepts_b: List[str], resonance_points: List[ResonancePoint]) -> List[str]:
        """Blend concepts based on resonance points"""
        # Start with all unique concepts
        blended = set(concepts_a + concepts_b)
        
        # Add emergent concepts from high-resonance pairs (limit to 3)
        high_resonance_points = [p for p in resonance_points if p.resonance_strength > 0.8]
        for point in high_resonance_points[:3]:  # Limit to top 3
            emergent_concept = f"{point.concept_a}-{point.concept_b}"
            blended.add(emergent_concept)
        
        return list(blended)
    
    def _blend_content(self, content_a: str, content_b: str) -> str:
        """Blend narrative content from two parents - SIMPLIFIED"""
        if not content_a and not content_b:
            return "Cosmic resonance emerging..."
        elif not content_a:
            return content_b
        elif not content_b:
            return content_a
            
        # Simple blending: take first part from A, second from B
        words_a = content_a.split()
        words_b = content_b.split()
        
        if not words_a or not words_b:
            return f"{content_a} synthesized with {content_b}"
            
        # Take first 3 words from A, last 3 words from B
        part_a = ' '.join(words_a[:3])
        part_b = ' '.join(words_b[-3:]) if len(words_b) > 3 else ' '.join(words_b)
        
        return f"{part_a} {part_b} through resonance"

# Robust Resonant Crossover Engine
print(" Robust Resonant Crossover Engine loaded successfully")
