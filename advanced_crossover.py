#  ADVANCED RESONANT CROSSOVER ENGINE
# Enhanced with semantic similarity and word embeddings simulation

import random
import math
from typing import List, Dict, Any, Tuple
from dataclasses import dataclass
import re

@dataclass
class ResonancePoint:
    """Enhanced resonance point with semantic properties"""
    concept_a: str
    concept_b: str 
    resonance_strength: float
    emergent_potential: float
    semantic_similarity: float
    relationship_type: str  # 'synonym', 'antonym', 'related', 'novel'

@dataclass
class SemanticRelationship:
    """Represents semantic relationship between concepts"""
    concept_a: str
    concept_b: str
    similarity: float
    relationship: str
    confidence: float

class AdvancedResonantCrossoverEngine:
    """Advanced crossover with semantic similarity and relationship detection"""
    
    def __init__(self):
        self.resonance_threshold = 0.6
        self.max_concept_pairs = 15
        self.semantic_network = self._build_semantic_network()
        
    def _build_semantic_network(self) -> Dict[str, Dict[str, float]]:
        """Build a simple semantic network for concept relationships"""
        # This simulates a word embedding space with semantic relationships
        # In a full implementation, this would use actual word embeddings
        
        semantic_groups = {
            'consciousness': ['awareness', 'mind', 'cognition', 'sentience', 'perception'],
            'love': ['compassion', 'care', 'empathy', 'kindness', 'devotion'],
            'evolution': ['development', 'growth', 'progress', 'adaptation', 'emergence'],
            'resonance': ['harmony', 'vibration', 'frequency', 'sympathy', 'alignment'],
            'mathematics': ['symmetry', 'logic', 'pattern', 'structure', 'calculation'],
            'divine': ['sacred', 'holy', 'spiritual', 'transcendent', 'eternal'],
            'creation': ['formation', 'generation', 'synthesis', 'production', 'inception'],
            'cosmic': ['universal', 'celestial', 'astral', 'galactic', 'infinite']
        }
        
        network = {}
        
        # Build similarity matrix
        all_concepts = set()
        for group_concepts in semantic_groups.values():
            all_concepts.update(group_concepts)
        
        for concept in all_concepts:
            network[concept] = {}
            for other_concept in all_concepts:
                if concept == other_concept:
                    network[concept][other_concept] = 1.0
                else:
                    # Check if concepts are in same semantic group
                    similarity = 0.1  # Base similarity
                    
                    for group_name, group_concepts in semantic_groups.items():
                        if concept in group_concepts and other_concept in group_concepts:
                            similarity = 0.8  # High similarity within group
                            break
                        elif concept in group_concepts or other_concept in group_concepts:
                            # Check if they share any group
                            for other_group_name, other_group_concepts in semantic_groups.items():
                                if group_name != other_group_name:
                                    if (concept in group_concepts and other_concept in other_group_concepts) or \
                                       (concept in other_group_concepts and other_concept in group_concepts):
                                        similarity = 0.4  # Medium cross-group similarity
                                        break
                    
                    network[concept][other_concept] = similarity
        
        return network
    
    def crossover(self, parent_a, parent_b):
        """Advanced crossover with semantic relationship analysis"""
        try:
            # Extract and validate concepts
            concepts_a = self._safe_get_concepts(parent_a)
            concepts_b = self._safe_get_concepts(parent_b)
            
            # Limit concepts for performance
            concepts_a = concepts_a[:8]
            concepts_b = concepts_b[:8]
            
            # 1. Advanced resonance detection with semantic analysis
            resonance_points = self._advanced_resonance_detection(concepts_a, concepts_b)
            
            # 2. Semantic relationship analysis
            relationships = self._analyze_semantic_relationships(concepts_a, concepts_b)
            
            # 3. Conceptual blending with semantic guidance
            blended_concepts = self._semantic_concept_blending(concepts_a, concepts_b, resonance_points, relationships)
            
            # 4. Content generation with semantic coherence
            content_a = self._safe_get_content(parent_a)
            content_b = self._safe_get_content(parent_b)
            blended_content = self._semantic_content_generation(content_a, content_b, relationships)
            
            # Create enhanced offspring
            offspring = type('AdvancedOffspring', (), {
                'vector_id': f"advanced_{getattr(parent_a, 'vector_id', 'A')}_{getattr(parent_b, 'vector_id', 'B')}",
                'content': blended_content,
                'concepts': blended_concepts,
                'coherence': (getattr(parent_a, 'coherence', 0.3) + getattr(parent_b, 'coherence', 0.3)) / 2,
                'parent_ids': [getattr(parent_a, 'vector_id', 'A'), getattr(parent_b, 'vector_id', 'B')],
                'resonance_points': resonance_points,
                'semantic_relationships': relationships
            })()
            
            return offspring
            
        except Exception as e:
            print(f"   Advanced crossover failed, using fallback: {e}")
            return self._fallback_crossover(parent_a, parent_b)
    
    def _advanced_resonance_detection(self, concepts_a: List[str], concepts_b: List[str]) -> List[ResonancePoint]:
        """Advanced resonance detection with semantic analysis"""
        resonance_points = []
        comparisons = 0
        
        for concept_a in concepts_a:
            for concept_b in concepts_b:
                if comparisons >= self.max_concept_pairs:
                    break
                    
                # Calculate multiple resonance metrics
                lexical_resonance = self._calculate_lexical_resonance(concept_a, concept_b)
                semantic_resonance = self._calculate_semantic_resonance(concept_a, concept_b)
                combined_resonance = (lexical_resonance * 0.3 + semantic_resonance * 0.7)
                
                if combined_resonance > self.resonance_threshold:
                    # Determine relationship type
                    relationship_type = self._determine_relationship_type(concept_a, concept_b, semantic_resonance)
                    
                    # Calculate emergent potential
                    emergent_potential = self._calculate_emergent_potential(concept_a, concept_b, relationship_type)
                    
                    resonance_points.append(
                        ResonancePoint(
                            concept_a=concept_a,
                            concept_b=concept_b,
                            resonance_strength=combined_resonance,
                            emergent_potential=emergent_potential,
                            semantic_similarity=semantic_resonance,
                            relationship_type=relationship_type
                        )
                    )
                
                comparisons += 1
        
        # Sort by resonance strength
        resonance_points.sort(key=lambda x: x.resonance_strength, reverse=True)
        return resonance_points[:5]  # Return top 5 resonance points
    
    def _calculate_lexical_resonance(self, concept_a: str, concept_b: str) -> float:
        """Calculate lexical (word-based) resonance"""
        if not concept_a or not concept_b:
            return 0.0
            
        a_lower = concept_a.lower()
        b_lower = concept_b.lower()
        
        # Exact match
        if a_lower == b_lower:
            return 1.0
        
        # Shared substring
        if a_lower in b_lower or b_lower in a_lower:
            return 0.7
        
        # Shared letters with weighting
        set_a = set(a_lower)
        set_b = set(b_lower)
        
        if not set_a or not set_b:
            return 0.2
            
        shared_letters = len(set_a & set_b)
        total_letters = len(set_a | set_b)
        
        if total_letters > 0:
            base_similarity = shared_letters / total_letters
            
            # Boost for shared prefixes/suffixes
            if a_lower[:3] == b_lower[:3]:
                base_similarity += 0.2
            elif a_lower[-3:] == b_lower[-3:]:
                base_similarity += 0.1
                
            return min(1.0, base_similarity)
        
        return 0.2
    
    def _calculate_semantic_resonance(self, concept_a: str, concept_b: str) -> float:
        """Calculate semantic resonance using the semantic network"""
        if concept_a not in self.semantic_network or concept_b not in self.semantic_network:
            return self._calculate_lexical_resonance(concept_a, concept_b) * 0.5
            
        return self.semantic_network[concept_a].get(concept_b, 0.1)
    
    def _determine_relationship_type(self, concept_a: str, concept_b: str, semantic_similarity: float) -> str:
        """Determine the type of semantic relationship"""
        if semantic_similarity > 0.8:
            return 'synonym'
        elif semantic_similarity > 0.6:
            return 'related'
        elif semantic_similarity < 0.3:
            return 'novel'  # Novel combination
        else:
            return 'related'
    
    def _calculate_emergent_potential(self, concept_a: str, concept_b: str, relationship_type: str) -> float:
        """Calculate the potential for emergent properties"""
        base_potential = random.uniform(0.3, 0.8)
        
        # Adjust based on relationship type
        if relationship_type == 'novel':
            base_potential += 0.3  # Novel combinations have higher emergent potential
        elif relationship_type == 'synonym':
            base_potential -= 0.2  # Similar concepts have lower emergent potential
            
        return min(1.0, base_potential)
    
    def _analyze_semantic_relationships(self, concepts_a: List[str], concepts_b: List[str]) -> List[SemanticRelationship]:
        """Analyze semantic relationships between concept sets"""
        relationships = []
        
        for concept_a in concepts_a[:5]:  # Limit analysis
            for concept_b in concepts_b[:5]:
                similarity = self._calculate_semantic_resonance(concept_a, concept_b)
                relationship_type = self._determine_relationship_type(concept_a, concept_b, similarity)
                
                # Calculate confidence based on similarity strength
                confidence = min(1.0, similarity * 1.2)
                
                relationships.append(
                    SemanticRelationship(
                        concept_a=concept_a,
                        concept_b=concept_b,
                        similarity=similarity,
                        relationship=relationship_type,
                        confidence=confidence
                    )
                )
        
        # Return most significant relationships
        relationships.sort(key=lambda x: x.similarity, reverse=True)
        return relationships[:8]
    
    def _semantic_concept_blending(self, concepts_a: List[str], concepts_b: List[str], 
                                 resonance_points: List[ResonancePoint], 
                                 relationships: List[SemanticRelationship]) -> List[str]:
        """Blend concepts using semantic guidance"""
        blended = set(concepts_a + concepts_b)
        
        # Add emergent concepts from high-resonance pairs
        for point in resonance_points[:3]:
            if point.emergent_potential > 0.7:
                if point.relationship_type == 'novel':
                    emergent_concept = f"{point.concept_a}-{point.concept_b}"
                else:
                    emergent_concept = f"{point.concept_a}_{point.concept_b}"
                blended.add(emergent_concept)
        
        # Add concepts from strong semantic relationships
        for rel in relationships[:3]:
            if rel.similarity > 0.7 and rel.confidence > 0.8:
                blended_concept = f"{rel.concept_a}-{rel.concept_b}"
                blended.add(blended_concept)
        
        return list(blended)[:10]  # Limit to 10 concepts
    
    def _semantic_content_generation(self, content_a: str, content_b: str, 
                                   relationships: List[SemanticRelationship]) -> str:
        """Generate content using semantic relationships"""
        if not content_a and not content_b:
            return "Semantic resonance emerging..."
        elif not content_a:
            return content_b
        elif not content_b:
            return content_a
        
        # Extract key phrases
        phrases_a = self._extract_key_phrases(content_a)
        phrases_b = self._extract_key_phrases(content_b)
        
        # Use semantic relationships to guide blending
        if relationships and len(relationships) > 0:
            best_relationship = relationships[0]
            if best_relationship.similarity > 0.6:
                # Use the relationship to create a bridge
                bridge = f" connecting {best_relationship.concept_a} and {best_relationship.concept_b}"
            else:
                bridge = " through cosmic resonance"
        else:
            bridge = " through semantic synthesis"
        
        # Blend phrases
        if phrases_a and phrases_b:
            blended_phrase = f"{phrases_a[0]} {bridge} {phrases_b[0]}"
        else:
            # Fallback blending
            words_a = content_a.split()[:4]
            words_b = content_b.split()[-4:]
            blended_phrase = f"{' '.join(words_a)} {bridge} {' '.join(words_b)}"
        
        return blended_phrase
    
    def _extract_key_phrases(self, text: str) -> List[str]:
        """Extract key phrases from text"""
        if not text:
            return []
        
        # Simple phrase extraction - split by punctuation
        phrases = re.split(r'[.!?]', text)
        phrases = [p.strip() for p in phrases if p.strip()]
        
        # Return non-empty phrases, limited to 3
        return phrases[:3]
    
    def _safe_get_concepts(self, parent) -> List[str]:
        """Safely extract concepts"""
        concepts = getattr(parent, 'concepts', [])
        if concepts is None:
            concepts = []
        return [str(c).strip() for c in concepts if c and str(c).strip()]
    
    def _safe_get_content(self, parent) -> str:
        """Safely extract content"""
        content = getattr(parent, 'content', '')
        if content is None:
            content = ''
        return str(content)
    
    def _fallback_crossover(self, parent_a, parent_b):
        """Fallback crossover method"""
        content_a = self._safe_get_content(parent_a)
        content_b = self._safe_get_content(parent_b)
        concepts_a = self._safe_get_concepts(parent_a)
        concepts_b = self._safe_get_concepts(parent_b)
        
        blended_content = f"{content_a} integrated with {content_b} through resonance"
        blended_concepts = list(set(concepts_a + concepts_b))[:8]
        
        offspring = type('FallbackOffspring', (), {
            'vector_id': f"fallback_{getattr(parent_a, 'vector_id', 'A')}_{getattr(parent_b, 'vector_id', 'B')}",
            'content': blended_content,
            'concepts': blended_concepts,
            'coherence': (getattr(parent_a, 'coherence', 0.3) + getattr(parent_b, 'coherence', 0.3)) / 2,
            'parent_ids': [getattr(parent_a, 'vector_id', 'A'), getattr(parent_b, 'vector_id', 'B')]
        })()
        
        return offspring

# Advanced Resonant Crossover Engine
print(" Advanced Resonant Crossover Engine loaded successfully")
