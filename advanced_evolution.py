#  ENHANCED EVOLUTIONARY ENGINE WITH ADVANCED CROSSOVER
# Integrated with semantic similarity and advanced algorithms

import random
import numpy as np
from typing import List, Dict, Any, Optional
from dataclasses import dataclass
import math
from .physics_of_meaning import EnhancedCRE
from .advanced_crossover import AdvancedResonantCrossoverEngine

@dataclass 
class NarrativeState:
    """Enhanced narrative state for advanced evolution"""
    state_id: str
    content: str
    concepts: List[str]
    coherence: float = 0.0
    fitness_score: float = 0.0
    generation: int = 0
    parent_ids: Optional[List[str]] = None
    semantic_quality: float = 0.0  # New: semantic coherence metric
    
    def __post_init__(self):
        if self.parent_ids is None:
            self.parent_ids = []

class AdvancedEvolutionaryEngine:
    """
    AdvancedEvolutionaryEngine
    An advanced evolutionary algorithm engine designed for evolving narrative states with enhanced crossover, mutation, and semantic analysis. This engine integrates semantic-aware selection, advanced fitness evaluation, and metrics tracking to optimize both the fitness and semantic quality of generated narratives.
    Attributes:
        hilbert_space: Source space containing initial state vectors for population initialization.
        cre_system: Enhanced Creative Resonance Evaluation system for narrative assessment.
        crossover_engine: Engine for performing advanced resonant crossover operations.
        population (List[NarrativeState]): Current population of narrative states.
        generation (int): Current generation number.
        fitness_history (List[float]): Historical best fitness scores per generation.
        semantic_history (List[float]): Historical best semantic quality scores per generation.
        population_size (int): Number of individuals in the population.
        elitism_count (int): Number of elite individuals preserved each generation.
        mutation_rate (float): Probability of mutation per offspring.
        crossover_rate (float): Probability of crossover per offspring.
        max_generations (int): Maximum number of generations to evolve.
        semantic_coherence_history (List[float]): Average semantic coherence per generation.
        innovation_history (List[float]): Innovation metric per generation.
    Methods:
        initialize_population():
            Initializes the population with diverse and semantically rich narratives using the Hilbert space and predefined advanced narratives.
        evolve_narrative(generations: int = 25) -> NarrativeState:
            Runs the evolutionary loop for a specified number of generations, optimizing for both fitness and semantic quality, and returns the best evolved narrative.
        _enhanced_fitness(narrative: NarrativeState) -> float:
            Computes an enhanced fitness score for a narrative, combining CRE evaluation, coherence, semantic quality, and novelty.
        _quick_fitness(narrative: NarrativeState) -> float:
            Provides a fallback fitness calculation based on content uniqueness and semantic quality.
        _calculate_semantic_quality(narrative: NarrativeState) -> float:
            Assesses the semantic quality of a narrative based on concept-content alignment and coherence.
        _semantic_aware_selection() -> List[NarrativeState]:
            Selects parent narratives for reproduction using a bias towards semantic quality.
        _generate_advanced_offspring(parents: List[NarrativeState]) -> List[NarrativeState]:
            Produces offspring using advanced crossover, elitism, and semantic-aware mutation.
        _perform_advanced_crossover(parent_a: NarrativeState, parent_b: NarrativeState) -> NarrativeState:
            Executes advanced crossover between two parent narratives, blending their semantic content.
        _clone_with_semantic_variation(narrative: NarrativeState) -> NarrativeState:
            Clones a narrative with minor semantic variations.
        _apply_semantic_mutation(narrative: NarrativeState) -> NarrativeState:
            Applies semantic-aware mutations to a narrative, enhancing concepts and content.
        _fallback_crossover(parent_a: NarrativeState, parent_b: NarrativeState) -> NarrativeState:
            Provides a simple fallback crossover method by blending parent contents and concepts.
        _calculate_novelty(narrative: NarrativeState) -> float:
            Measures the novelty of a narrative relative to the current population.
        _calculate_semantic_diversity() -> float:
            Calculates the semantic diversity of the population based on concept variety and semantic quality variance.
        _calculate_innovation() -> float:
            Computes the innovation level of the population based on recent fitness improvements.
        _update_advanced_metrics():
            Updates advanced metrics such as semantic coherence and innovation history.
        _get_best_narrative() -> NarrativeState:
            Retrieves the best narrative from the population, considering both fitness and semantic quality.
        _extract_semantic_concepts(text: str) -> List[str]:
            Extracts meaningful semantic concepts from a given text.
        get_advanced_report() -> Dict[str, Any]:
            Generates a comprehensive report of the evolutionary process, including best narrative, fitness progression, semantic progression, and advanced metrics.
    """
    """Evolutionary engine with advanced crossover and semantic analysis"""
    
    def __init__(self, hilbert_space, cre_system=None):
        self.hilbert_space = hilbert_space
        self.cre_system = cre_system or EnhancedCRE()
        self.crossover_engine = AdvancedResonantCrossoverEngine()
        self.population: List[NarrativeState] = []
        self.generation = 0
        self.fitness_history: List[float] = []
        self.semantic_history: List[float] = []
        
        # Enhanced parameters
        self.population_size = 20
        self.elitism_count = 3
        self.mutation_rate = 0.25
        self.crossover_rate = 0.7
        self.max_generations = 25
        
        # Advanced metrics
        self.semantic_coherence_history = []
        self.innovation_history = []
    
    def initialize_population(self) -> None:
        """Initialize population with enhanced diversity"""
        print(" Initializing advanced evolutionary population...")
        
        # Create from Hilbert space
        if self.hilbert_space and hasattr(self.hilbert_space, 'state_vectors'):
            for vector_id, state_vector in list(self.hilbert_space.state_vectors.items())[:5]:
                narrative = NarrativeState(
                    state_id=f"adv_{vector_id}",
                    content=state_vector.semantic_content.get('content', 'Advanced cosmic evolution...'),
                    concepts=state_vector.concepts[:6],
                    coherence=state_vector.coherence,
                    generation=0
                )
                narrative.fitness_score = self._enhanced_fitness(narrative)
                narrative.semantic_quality = self._calculate_semantic_quality(narrative)
                self.population.append(narrative)
        
        # Enhanced basic narratives with semantic richness
        advanced_narratives = [
            "Consciousness emerges through resonant awareness patterns",
            "Love manifests as fundamental creative resonance force", 
            "Self-reference creates evolutionary semantic feedback loops",
            "Mathematical symmetry reveals cosmic structural patterns",
            "Kenotic self-emptying enables novel semantic possibilities",
            "Cosmic resonance amplifies meaningful information generation"
        ]
        
        while len(self.population) < self.population_size:
            content = random.choice(advanced_narratives)
            narrative = NarrativeState(
                state_id=f"adv_basic_{len(self.population)}",
                content=content,
                concepts=self._extract_semantic_concepts(content),
                coherence=0.4,
                generation=0
            )
            narrative.fitness_score = self._enhanced_fitness(narrative)
            narrative.semantic_quality = self._calculate_semantic_quality(narrative)
            self.population.append(narrative)
        
        print(f"   Created {len(self.population)} advanced narratives")
        self._update_advanced_metrics()
    
    def evolve_narrative(self, generations: int = 25) -> NarrativeState:
        """Advanced evolutionary loop with semantic optimization"""
        print(f" Starting advanced evolution ({generations} generations)...")
        
        max_generations = min(generations, self.max_generations)
        stagnation = 0
        previous_best = 0.0
        
        for gen in range(max_generations):
            self.generation = gen
            
            # Enhanced fitness evaluation
            for narrative in self.population:
                narrative.fitness_score = self._enhanced_fitness(narrative)
                narrative.semantic_quality = self._calculate_semantic_quality(narrative)
            
            # Advanced selection with semantic bias
            parents = self._semantic_aware_selection()
            
            # Generate offspring with advanced crossover
            offspring = self._generate_advanced_offspring(parents)
            
            # Update population
            self.population = offspring[:self.population_size]
            
            # Track metrics
            current_best = max(n.fitness_score for n in self.population)
            current_semantic = max(n.semantic_quality for n in self.population)
            
            self.fitness_history.append(current_best)
            self.semantic_history.append(current_semantic)
            
            # Check stagnation with semantic consideration
            improvement = current_best - previous_best
            if improvement < 0.01:
                stagnation += 1
            else:
                stagnation = 0
            previous_best = current_best
            
            # Enhanced progress reporting
            if gen % 4 == 0:
                diversity = self._calculate_semantic_diversity()
                innovation = self._calculate_innovation()
                print(f"  Gen {gen:2d}: Fit={current_best:.3f}, Sem={current_semantic:.3f}, Div={diversity:.3f}")
            
            # Advanced stopping conditions
            if stagnation >= 10 or current_best > 0.85:
                print(f"   Advanced stopping at generation {gen}")
                break
        
        best_narrative = self._get_best_narrative()
        print(f"   Advanced evolution complete: {best_narrative.fitness_score:.3f} fitness")
        return best_narrative
    
    def _enhanced_fitness(self, narrative: NarrativeState) -> float:
        """Enhanced fitness evaluation with semantic quality"""
        try:
            # Use CRE system for comprehensive evaluation
            cre_evaluation = self.cre_system.evaluate_narrative_state({
                'content': narrative.content,
                'concepts': narrative.concepts
            })
            
            # Combine multiple factors
            fitness = (
                0.5 * cre_evaluation.overall_fitness +
                0.2 * narrative.coherence +
                0.2 * narrative.semantic_quality +
                0.1 * self._calculate_novelty(narrative)
            )
            
            return min(1.0, fitness)
            
        except Exception:
            # Fallback fitness calculation
            return self._quick_fitness(narrative)
    
    def _quick_fitness(self, narrative: NarrativeState) -> float:
        """Quick fitness fallback"""
        if not narrative.content:
            return 0.0
            
        words = narrative.content.split()
        unique_words = len(set(words))
        semantic_bonus = narrative.semantic_quality
        
        return min(1.0, (unique_words / max(1, len(words))) * 0.6 + semantic_bonus * 0.4)
    
    def _calculate_semantic_quality(self, narrative: NarrativeState) -> float:
        """Calculate semantic quality of narrative"""
        if not narrative.content or not narrative.concepts:
            return 0.3
            
        # Check concept-content alignment
        content_lower = narrative.content.lower()
        concept_presence = sum(1 for concept in narrative.concepts if concept.lower() in content_lower)
        concept_alignment = concept_presence / len(narrative.concepts) if narrative.concepts else 0.5
        
        # Check semantic coherence (simple version)
        word_count = len(narrative.content.split())
        if word_count < 3:
            return 0.3
            
        # Basic semantic quality metric
        semantic_quality = min(1.0, concept_alignment * 0.7 + random.uniform(0.1, 0.3))
        return semantic_quality
    
    def _semantic_aware_selection(self) -> List[NarrativeState]:
        """Selection with semantic quality bias"""
        # Combine fitness and semantic quality for selection
        scored_narratives = []
        for narrative in self.population:
            combined_score = (narrative.fitness_score * 0.7 + narrative.semantic_quality * 0.3)
            scored_narratives.append((narrative, combined_score))
        
        # Tournament selection with combined scores
        parents = []
        tournament_size = 3
        
        while len(parents) < len(self.population) // 2:
            tournament = random.sample(scored_narratives, tournament_size)
            winner = max(tournament, key=lambda x: x[1])[0]
            parents.append(winner)
        
        return parents
    
    def _generate_advanced_offspring(self, parents: List[NarrativeState]) -> List[NarrativeState]:
        """Generate offspring using advanced crossover"""
        offspring = []
        
        # Elitism with semantic consideration
        elites = sorted(self.population, 
                      key=lambda x: (x.fitness_score * 0.6 + x.semantic_quality * 0.4), 
                      reverse=True)[:self.elitism_count]
        offspring.extend(elites)
        
        # Generate new offspring
        while len(offspring) < self.population_size:
            if random.random() < self.crossover_rate and len(parents) >= 2:
                # Advanced crossover
                parent_a, parent_b = random.sample(parents, 2)
                child = self._perform_advanced_crossover(parent_a, parent_b)
            else:
                # Clone with semantic enhancement
                parent = random.choice(parents)
                child = self._clone_with_semantic_variation(parent)
            
            # Advanced mutation
            if random.random() < self.mutation_rate:
                child = self._apply_semantic_mutation(child)
            
            child.generation = self.generation + 1
            child.fitness_score = self._enhanced_fitness(child)
            child.semantic_quality = self._calculate_semantic_quality(child)
            offspring.append(child)
        
        return offspring
    
    def _perform_advanced_crossover(self, parent_a: NarrativeState, parent_b: NarrativeState) -> NarrativeState:
        """Perform advanced crossover with semantic analysis"""
        try:
            child_state = self.crossover_engine.crossover(parent_a, parent_b)
            
            # Create enhanced narrative state
            child = NarrativeState(
                state_id=f"adv_child_{parent_a.state_id}_{parent_b.state_id}_{self.generation}",
                content=getattr(child_state, 'content', 'Semantically blended narrative'),
                concepts=getattr(child_state, 'concepts', []),
                coherence=(parent_a.coherence + parent_b.coherence) / 2,
                parent_ids=[parent_a.state_id, parent_b.state_id],
                generation=self.generation + 1,
                semantic_quality=getattr(child_state, 'semantic_quality', 0.5)
            )
            
            return child
            
        except Exception as e:
            print(f"   Advanced crossover failed: {e}")
            return self._fallback_crossover(parent_a, parent_b)
    
    def _clone_with_semantic_variation(self, narrative: NarrativeState) -> NarrativeState:
        """Clone with slight semantic variations"""
        return NarrativeState(
            state_id=f"adv_clone_{narrative.state_id}",
            content=narrative.content,
            concepts=narrative.concepts.copy(),
            coherence=narrative.coherence,
            parent_ids=(narrative.parent_ids or []).copy(),
            generation=narrative.generation,
            semantic_quality=narrative.semantic_quality
        )
    
    def _apply_semantic_mutation(self, narrative: NarrativeState) -> NarrativeState:
        """Apply semantic-aware mutation"""
        content = narrative.content
        concepts = narrative.concepts.copy()
        
        # Semantic enhancement mutations
        mutation_type = random.choice(['concept_add', 'concept_refine', 'semantic_expansion'])
        
        if mutation_type == 'concept_add' and len(concepts) < 8:
            new_concepts = ['resonance', 'consciousness', 'evolution', 'love', 'divine', 'mathematics']
            new_concept = random.choice(new_concepts)
            if new_concept not in concepts:
                concepts.append(new_concept)
                content += f" with {new_concept}"
                
        elif mutation_type == 'concept_refine' and concepts:
            # Replace a concept with a related one
            concept_mapping = {
                'love': 'compassion',
                'consciousness': 'awareness', 
                'evolution': 'development',
                'resonance': 'harmony'
            }
            for old_concept, new_concept in concept_mapping.items():
                if old_concept in concepts:
                    concepts.remove(old_concept)
                    concepts.append(new_concept)
                    content = content.replace(old_concept, new_concept)
                    break
                    
        elif mutation_type == 'semantic_expansion':
            # Add a semantically related phrase
            expansions = [
                " through cosmic resonance",
                " in the field of consciousness", 
                " with evolutionary potential",
                " through divine manifestation"
            ]
            content += random.choice(expansions)
        
        return NarrativeState(
            state_id=f"sem_mutated_{narrative.state_id}",
            content=content,
            concepts=concepts,
            coherence=narrative.coherence,
            parent_ids=(narrative.parent_ids or []).copy(),
            generation=narrative.generation
        )
    
    def _fallback_crossover(self, parent_a: NarrativeState, parent_b: NarrativeState) -> NarrativeState:
        """Fallback crossover method"""
        # Simple content blending
        content = f"{parent_a.content} blended with {parent_b.content}"
        concepts = list(set(parent_a.concepts + parent_b.concepts))[:6]
        
        return NarrativeState(
            state_id=f"fallback_{parent_a.state_id}_{parent_b.state_id}",
            content=content,
            concepts=concepts,
            coherence=(parent_a.coherence + parent_b.coherence) / 2,
            parent_ids=[parent_a.state_id, parent_b.state_id],
            generation=self.generation + 1
        )
    
    def _calculate_novelty(self, narrative: NarrativeState) -> float:
        """Calculate novelty relative to population"""
        if len(self.population) < 2:
            return 0.5
            
        similarities = []
        for other in self.population:
            if other.state_id != narrative.state_id:
                shared_concepts = len(set(narrative.concepts) & set(other.concepts))
                total_concepts = len(set(narrative.concepts) | set(other.concepts))
                similarity = shared_concepts / total_concepts if total_concepts > 0 else 0
                similarities.append(similarity)
        
        avg_similarity = sum(similarities) / len(similarities) if similarities else 0
        return 1.0 - avg_similarity
    
    def _calculate_semantic_diversity(self) -> float:
        """Calculate semantic diversity of population"""
        if len(self.population) < 2:
            return 1.0
            
        all_concepts = set()
        semantic_scores = []
        
        for narrative in self.population:
            all_concepts.update(narrative.concepts)
            semantic_scores.append(narrative.semantic_quality)
        
        if not all_concepts:
            return 0.5
            
        concept_diversity = len(all_concepts) / (len(self.population) * 3)  # Normalized
        semantic_variance = np.var(semantic_scores) if semantic_scores else 0.5
        
        return float(min(1.0, (concept_diversity + semantic_variance) / 2))
    
    def _calculate_innovation(self) -> float:
        """Calculate population innovation level"""
        if len(self.fitness_history) < 5:
            return 0.5
            
        # Measure fitness improvement trend
        recent_improvement = self.fitness_history[-1] - self.fitness_history[-5]
        return min(1.0, recent_improvement * 10 + 0.3)  # Scale and offset
    
    def _update_advanced_metrics(self):
        """Update advanced evolutionary metrics"""
        if self.population:
            avg_semantic = sum(n.semantic_quality for n in self.population) / len(self.population)
            self.semantic_coherence_history.append(avg_semantic)
            
            innovation = self._calculate_innovation()
            self.innovation_history.append(innovation)
    
    def _get_best_narrative(self) -> NarrativeState:
        """Get best narrative considering multiple factors"""
        if not self.population:
            return NarrativeState("default", "Advanced evolution in progress...", [])
        
        # Weighted selection considering fitness and semantic quality
        return max(self.population, 
                  key=lambda x: x.fitness_score * 0.7 + x.semantic_quality * 0.3)
    
    def _extract_semantic_concepts(self, text: str) -> List[str]:
        """Extract semantic concepts from text"""
        stop_words = {'the', 'a', 'an', 'and', 'or', 'but', 'in', 'on', 'at', 'to', 'for', 'of', 'with', 'by'}
        words = [w.lower() for w in text.split() if w.lower() not in stop_words and len(w) > 3]
        
        # Prioritize meaningful concepts
        priority_concepts = {'consciousness', 'resonance', 'evolution', 'love', 'divine', 
                           'mathematics', 'cosmic', 'creation', 'self-reference'}
        
        concepts = []
        for word in words:
            if word in priority_concepts:
                concepts.append(word)
        
        # Add other meaningful words
        other_words = [w for w in words if w not in priority_concepts]
        concepts.extend(other_words[:4])  # Limit additional concepts
        
        return list(set(concepts))[:6]  # Limit to 6 concepts
    
    def get_advanced_report(self) -> Dict[str, Any]:
        """Get comprehensive advanced evolutionary report"""
        best_narrative = self._get_best_narrative()
        
        return {
            "total_generations": self.generation + 1,
            "best_fitness": best_narrative.fitness_score,
            "best_semantic_quality": best_narrative.semantic_quality,
            "best_narrative": best_narrative.content,
            "best_concepts": best_narrative.concepts,
            "fitness_progression": self.fitness_history,
            "semantic_progression": self.semantic_history,
            "semantic_coherence_history": self.semantic_coherence_history,
            "innovation_history": self.innovation_history
        }

# Advanced Evolutionary Engine
print(" Advanced Evolutionary Engine loaded successfully")
