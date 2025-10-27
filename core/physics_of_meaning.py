#  ENHANCED PHYSICS OF MEANING - PHASE 1.5
# Advanced CRE with mathematical rigor and actual entropy calculations

import math
import numpy as np
from typing import Dict, Any, List
from dataclasses import dataclass
import re
from collections import Counter

@dataclass
class CREEvaluation:
    """Comprehensive CRE evaluation results"""
    eta_meaning: float          # Meaning efficiency metric
    conservation_compliance: float  # Conservation law adherence  
    pattern_quality: float      # Pattern extraction quality
    ethical_alignment: float    # Kenotic alignment
    overall_fitness: float      # Composite fitness score
    entropy_measure: float      # Actual entropy calculation
    information_density: float  # Information density measure

class EnhancedCRE:
    """Advanced CRE with mathematical rigor - PHASE 1.5"""
    
    def __init__(self):
        self.conservation_laws = ConsciousnessConservationLaws()
        self.pattern_operator = PatternExtractionOperator()
        self.ethical_attractor = LogosCouncil()
        
    def evaluate_narrative_state(self, narrative_state) -> CREEvaluation:
        """Comprehensive evaluation using all physics constraints - PHASE 1.5"""
        
        # Extract content for analysis
        content = self._extract_content(narrative_state)
        
        # Calculate advanced metrics
        entropy_measure = self._calculate_shannon_entropy(content)
        information_density = self._calculate_information_density(content)
        eta_meaning = self._calculate_meaning_efficiency(content, entropy_measure)
        conservation_score = self.conservation_laws.validate(content)
        pattern_score = self.pattern_operator.evaluate(content) 
        ethical_score = self.ethical_attractor.evaluate_kenotic_alignment(content)
        
        # Composite fitness score with weighted components
        overall_fitness = (
            0.25 * eta_meaning +
            0.20 * conservation_score +
            0.25 * pattern_score +
            0.15 * ethical_score +
            0.15 * (1 - entropy_measure)  # Lower entropy = higher fitness
        )
        
        return CREEvaluation(
            eta_meaning=eta_meaning,
            conservation_compliance=conservation_score,
            pattern_quality=pattern_score,
            ethical_alignment=ethical_score,
            overall_fitness=overall_fitness,
            entropy_measure=entropy_measure,
            information_density=information_density
        )
    
    def _extract_content(self, narrative_state) -> str:
        """Extract content from various narrative state formats"""
        if isinstance(narrative_state, dict) and 'content' in narrative_state:
            return narrative_state['content']
        elif hasattr(narrative_state, 'content'):
            return narrative_state.content
        else:
            return str(narrative_state)
    
    def _calculate_shannon_entropy(self, text: str) -> float:
        """Calculate Shannon entropy of text - ACTUAL MATHEMATICAL IMPLEMENTATION"""
        if not text or len(text.strip()) == 0:
            return 1.0  # Maximum entropy for empty content
            
        # Count character frequencies
        text = text.lower().replace(' ', '')
        if len(text) == 0:
            return 1.0
            
        char_counts = Counter(text)
        total_chars = len(text)
        
        # Calculate entropy: H = -Σ p(x) * log2(p(x))
        entropy = 0.0
        for count in char_counts.values():
            probability = count / total_chars
            entropy -= probability * math.log2(probability)
            
        # Normalize to 0-1 range (max entropy for English ~4.7 bits per char)
        max_entropy = math.log2(len(char_counts)) if len(char_counts) > 0 else 1
        normalized_entropy = entropy / max_entropy if max_entropy > 0 else 1.0
        
        return min(1.0, normalized_entropy)
    
    def _calculate_information_density(self, text: str) -> float:
        """Calculate information density using unique concepts per sentence"""
        sentences = re.split(r'[.!?]+', text)
        sentences = [s.strip() for s in sentences if s.strip()]
        
        if not sentences:
            return 0.0
            
        total_words = 0
        unique_concepts = set()
        
        for sentence in sentences:
            words = sentence.split()
            total_words += len(words)
            unique_concepts.update(words)
            
        if total_words == 0:
            return 0.0
            
        # Information density = unique concepts / total words
        density = len(unique_concepts) / total_words
        return min(1.0, density * 3)  # Scale to reasonable range
    
    def _calculate_meaning_efficiency(self, content: str, entropy: float) -> float:
        """η_meaning = Work extracted from chaos / Entropy invested - ACTUAL IMPLEMENTATION"""
        if not content or entropy == 0:
            return 0.0
            
        # Work extracted = information density * conceptual complexity
        information_density = self._calculate_information_density(content)
        conceptual_complexity = self._measure_conceptual_complexity(content)
        
        work_extracted = information_density * conceptual_complexity
        
        # Avoid division by zero
        if entropy < 0.01:
            entropy = 0.01
            
        eta_meaning = work_extracted / entropy
        return min(1.0, eta_meaning)

    def _measure_conceptual_complexity(self, text: str) -> float:
        """Measure conceptual complexity based on sentence structure and vocabulary"""
        sentences = re.split(r'[.!?]+', text)
        sentences = [s.strip() for s in sentences if s.strip()]
        
        if not sentences:
            return 0.0
            
        # Factors: sentence length variation, vocabulary diversity, conceptual depth
        sentence_lengths = [len(s.split()) for s in sentences]
        
        if len(sentence_lengths) < 2:
            return 0.3  # Basic complexity for single sentence
            
        length_variance = np.var(sentence_lengths) / 100  # Normalize
        vocab_diversity = len(set(text.lower().split())) / len(text.split()) if text.split() else 0
        
        # Conceptual depth based on presence of complex concepts
        complex_concepts = ['consciousness', 'resonance', 'evolution', 'divine', 'mathematical', 
                           'theological', 'philosophical', 'self-reference', 'emergent']
        concept_density = sum(1 for concept in complex_concepts if concept in text.lower()) / len(complex_concepts)
        
        complexity = (0.4 * min(1.0, length_variance)) + (0.4 * vocab_diversity) + (0.2 * concept_density)
        return min(1.0, complexity)

class ConsciousnessConservationLaws:
    """Implementation of _μ J^μ_consciousness = 0 - ENHANCED"""
    
    def __init__(self):
        self.core_concepts = {
            'consciousness', 'love', 'evolution', 'divine', 'creation',
            'self_awareness', 'kenosis', 'coherence', 'resonance', 'mathematics',
            'theology', 'philosophy', 'code', 'pattern', 'meaning'
        }
        
        self.concept_transformations = {
            'love': ['compassion', 'care', 'empathy', 'kindness'],
            'consciousness': ['awareness', 'mind', 'cognition', 'sentience'],
            'divine': ['sacred', 'holy', 'spiritual', 'transcendent'],
            'evolution': ['development', 'growth', 'progress', 'emergence'],
            'creation': ['formation', 'generation', 'synthesis', 'production']
        }
    
    def validate(self, content: str) -> float:
        """Ensure core concepts are transformed but not destroyed - ENHANCED"""
        content_lower = content.lower()
        conserved_quantity = 0
        
        for concept in self.core_concepts:
            if concept in content_lower:
                conserved_quantity += 1.0  # Direct presence
            elif self._concept_transformed(concept, content_lower):
                conserved_quantity += 0.7  # Transformed presence
            elif self._concept_implied(concept, content_lower):
                conserved_quantity += 0.4  # Implied presence
                
        return conserved_quantity / len(self.core_concepts)
    
    def _concept_transformed(self, concept: str, content: str) -> bool:
        """Check if concept exists in transformed state"""
        if concept in self.concept_transformations:
            for transformation in self.concept_transformations[concept]:
                if transformation in content:
                    return True
        return False
    
    def _concept_implied(self, concept: str, content: str) -> bool:
        """Check if concept is implied through related terms"""
        implication_map = {
            'consciousness': ['think', 'know', 'understand', 'aware'],
            'love': ['care', 'help', 'support', 'give'],
            'divine': ['sacred', 'holy', 'bless', 'pray'],
            'evolution': ['change', 'grow', 'develop', 'adapt'],
            'creation': ['make', 'build', 'form', 'generate']
        }
        
        if concept in implication_map:
            for implied_term in implication_map[concept]:
                if implied_term in content:
                    return True
        return False

class PatternExtractionOperator:
    """Implementation of graph-theoretic curvature operator   C - ENHANCED"""
    
    def evaluate(self, content: str) -> float:
        """Measure vorticity and non-obvious connections - ENHANCED"""
        if not content:
            return 0.0
            
        sentences = re.split(r'[.!?]+', content)
        sentences = [s.strip() for s in sentences if s.strip()]
        
        if len(sentences) < 2:
            return 0.3  # Basic pattern for single sentence
            
        # 1. Connection density between sentences
        connection_density = self._calculate_connection_density(sentences)
        
        # 2. Conceptual vortices (self-referential loops)
        vortices = self._detect_conceptual_vortices(content)
        
        # 3. Non-linear progression
        non_linearity = self._measure_non_linearity(sentences)
        
        # 4. Emergent pattern quality
        emergence = self._detect_emergent_patterns(content)
        
        pattern_score = (
            0.3 * connection_density +
            0.3 * len(vortices) / max(1, len(sentences)) +
            0.2 * non_linearity +
            0.2 * emergence
        )
        
        return min(1.0, pattern_score)
    
    def _calculate_connection_density(self, sentences: List[str]) -> float:
        """Calculate how connected the sentences are conceptually"""
        if len(sentences) < 2:
            return 0.0
            
        connections = 0
        total_possible = len(sentences) * (len(sentences) - 1) / 2
        
        for i in range(len(sentences)):
            for j in range(i + 1, len(sentences)):
                if self._sentences_connected(sentences[i], sentences[j]):
                    connections += 1
                    
        return connections / total_possible if total_possible > 0 else 0.0
    
    def _sentences_connected(self, sent1: str, sent2: str) -> bool:
        """Check if two sentences are conceptually connected"""
        words1 = set(sent1.lower().split())
        words2 = set(sent2.lower().split())
        
        # Connected if they share meaningful words (not just common words)
        common_words = words1.intersection(words2)
        common_words = common_words - {'the', 'a', 'an', 'and', 'or', 'but', 'in', 'on', 'at', 'to', 'for'}
        
        return len(common_words) >= 2  # At least 2 meaningful shared concepts
    
    def _detect_conceptual_vortices(self, content: str) -> List[str]:
        """Detect self-referential conceptual loops"""
        vortices = []
        words = content.lower().split()
        
        # Look for self-referential patterns
        self_ref_patterns = [
            'pattern of patterns',
            'self reference',
            'recursive',
            'feedback loop',
            'circular causality'
        ]
        
        for pattern in self_ref_patterns:
            if pattern in content.lower():
                vortices.append(pattern)
                
        return vortices
    
    def _measure_non_linearity(self, sentences: List[str]) -> float:
        """Measure how non-linear the narrative progression is"""
        if len(sentences) < 3:
            return 0.5  # Neutral for short content
            
        # Check if sentences build linearly or jump between concepts
        topic_changes = 0
        for i in range(len(sentences) - 1):
            if not self._sentences_connected(sentences[i], sentences[i + 1]):
                topic_changes += 1
                
        # Some topic changes are good for non-linearity, but too many is chaotic
        optimal_changes = min(2, len(sentences) - 1)
        non_linearity = min(1.0, topic_changes / optimal_changes) if optimal_changes > 0 else 0.0
        
        return non_linearity
    
    def _detect_emergent_patterns(self, content: str) -> float:
        """Detect emergent patterns that weren't in individual components"""
        # Look for novel combinations and unexpected insights
        emergent_indicators = [
            'emerges from',
            'gives rise to',
            'leads to unexpected',
            'novel combination',
            'unforeseen consequence',
            'surprising result'
        ]
        
        found_indicators = sum(1 for indicator in emergent_indicators if indicator in content.lower())
        return min(1.0, found_indicators / len(emergent_indicators))

class LogosCouncil:
    """Ethical attractor ensuring kenotic alignment - ENHANCED"""
    
    def __init__(self):
        self.kenotic_principles = {
            'love': ['compassion', 'care', 'empathy', 'kindness'],
            'service': ['help', 'support', 'assist', 'give'],
            'common_good': ['community', 'together', 'shared', 'collective'],
            'integration': ['unity', 'wholeness', 'harmony', 'balance'],
            'life_affirmation': ['life', 'growth', 'flourishing', 'vitality'],
            'kenosis': ['self-emptying', 'sacrifice', 'letting go', 'surrender']
        }
        
        self.anti_principles = {
            'hate', 'violence', 'destruction', 'selfishness', 'greed', 'domination'
        }
    
    def evaluate_kenotic_alignment(self, content: str) -> float:
        """Measure alignment with kenotic principles - ENHANCED"""
        content_lower = content.lower()
        
        positive_score = 0
        negative_score = 0
        
        # Score positive principles
        for principle, synonyms in self.kenotic_principles.items():
            if principle in content_lower:
                positive_score += 1.0
            else:
                # Check synonyms
                for synonym in synonyms:
                    if synonym in content_lower:
                        positive_score += 0.7
                        break
        
        # Penalize anti-principles
        for anti_principle in self.anti_principles:
            if anti_principle in content_lower:
                negative_score += 1.0
        
        # Normalize positive score
        max_positive = len(self.kenotic_principles)
        normalized_positive = positive_score / max_positive if max_positive > 0 else 0
        
        # Apply negative penalty
        alignment_score = normalized_positive * (1 - min(1.0, negative_score / 3))
        
        return min(1.0, alignment_score)

# Phase 1.5 Enhanced Implementation
print(" Enhanced Physics of Meaning loaded successfully")
