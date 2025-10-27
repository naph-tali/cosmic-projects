#  ENHANCED CROSS-DOMAIN CONNECTION DETECTOR
# Fixed to properly detect shared concepts across domains

import itertools
from typing import List, Dict, Set

class EnhancedCrossDomainDetector:
    """Advanced cross-domain concept mapping with semantic analysis"""
    
    def __init__(self):
        self.shared_concept_threshold = 0.6
        self.concept_synonyms = {
            'consciousness': ['awareness', 'mind', 'cognition', 'sentience'],
            'love': ['compassion', 'care', 'empathy', 'kindness'],
            'evolution': ['development', 'progress', 'growth', 'advancement'],
            'divine': ['sacred', 'holy', 'spiritual', 'transcendent'],
            'symmetry': ['balance', 'harmony', 'proportion', 'equilibrium'],
            'resonance': ['harmony', 'vibration', 'frequency', 'alignment'],
            'reality': ['existence', 'actuality', 'truth', 'being'],
            'existence': ['being', 'reality', 'presence', 'actuality']
        }
    
    def detect_cross_domain_connections(self, domain_vectors: Dict[str, List]) -> Dict[str, List[str]]:
        """Enhanced cross-domain connection detection with semantic expansion"""
        cross_domain_map = {}
        
        # Build concept sets for each domain with semantic expansion
        domain_concept_sets = {}
        for domain, vectors in domain_vectors.items():
            domain_concept_sets[domain] = self._get_expanded_concepts(vectors)
            print(f"   {domain}: {len(domain_concept_sets[domain])} expanded concepts")
        
        # Find intersections between all domain pairs
        domain_pairs = list(itertools.combinations(domain_concept_sets.keys(), 2))
        
        for domain_a, domain_b in domain_pairs:
            concepts_a = domain_concept_sets[domain_a]
            concepts_b = domain_concept_sets[domain_b]
            
            # Find direct matches
            direct_matches = concepts_a.intersection(concepts_b)
            
            # Find semantic matches (using synonyms)
            semantic_matches = self._find_semantic_matches(concepts_a, concepts_b)
            
            all_matches = direct_matches.union(semantic_matches)
            
            for concept in all_matches:
                if concept not in cross_domain_map:
                    cross_domain_map[concept] = []
                
                if domain_a not in cross_domain_map[concept]:
                    cross_domain_map[concept].append(domain_a)
                if domain_b not in cross_domain_map[concept]:
                    cross_domain_map[concept].append(domain_b)
        
        print(f"   Found {len(cross_domain_map)} cross-domain connecting concepts")
        for concept, domains in list(cross_domain_map.items())[:5]:  # Show first 5
            print(f"     - '{concept}': {', '.join(domains)}")
        
        return cross_domain_map
    
    def _get_expanded_concepts(self, vectors: List) -> Set[str]:
        """Get expanded concept set including synonyms"""
        expanded_concepts = set()
        
        for vector in vectors:
            # Add direct concepts
            expanded_concepts.update(vector.concepts)
            
            # Add synonyms for each concept
            for concept in vector.concepts:
                synonyms = self.concept_synonyms.get(concept.lower(), [])
                expanded_concepts.update(synonyms)
        
        return expanded_concepts
    
    def _find_semantic_matches(self, concepts_a: Set[str], concepts_b: Set[str]) -> Set[str]:
        """Find semantic matches between concept sets"""
        semantic_matches = set()
        
        for concept_a in concepts_a:
            for concept_b in concepts_b:
                if self._concepts_are_semantically_related(concept_a, concept_b):
                    # Add both concepts to indicate the connection
                    semantic_matches.add(concept_a)
                    semantic_matches.add(concept_b)
        
        return semantic_matches
    
    def _concepts_are_semantically_related(self, concept_a: str, concept_b: str) -> bool:
        """Check if two concepts are semantically related"""
        # Direct match
        if concept_a.lower() == concept_b.lower():
            return True
        
        # Synonym check
        a_synonyms = self.concept_synonyms.get(concept_a.lower(), [])
        b_synonyms = self.concept_synonyms.get(concept_b.lower(), [])
        
        if concept_a.lower() in b_synonyms or concept_b.lower() in a_synonyms:
            return True
        
        # Check if one is synonym of the other
        if any(syn.lower() == concept_b.lower() for syn in a_synonyms):
            return True
        if any(syn.lower() == concept_a.lower() for syn in b_synonyms):
            return True
        
        return False

print(" Enhanced Cross-Domain Detector loaded successfully")
