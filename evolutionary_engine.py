#  OPTIMIZED EVOLUTIONARY ENGINE - PERFORMANCE FOCUSED
# Further optimizations for speed and reliability

import random
import numpy as np
from typing import List, Dict, Any, Tuple, Optional
from dataclasses import dataclass
import math
from .physics_of_meaning import EnhancedCRE

@dataclass 
class NarrativeState:
    """Optimized narrative state"""
    state_id: str
    content: str
    concepts: List[str]
    coherence: float = 0.0
    fitness_score: float = 0.0
    generation: int = 0
    parent_ids: Optional[List[str]] = None
    
    def __post_init__(self):
        if self.parent_ids is None:
            self.parent_ids = []

class GenerativeEvolutionaryAlgorithm:
    """Optimized evolutionary engine - PERFORMANCE FOCUSED"""
    
    def __init__(self, hilbert_space, cre_system=None):
        self.hilbert_space = hilbert_space
        self.cre_system = cre_system or EnhancedCRE()
        self.population: List[NarrativeState] = []
        self.generation = 0
        self.fitness_history: List[float] = []
        
        # OPTIMIZED PARAMETERS
        self.population_size = 20      # Smaller for performance
        self.elitism_count = 2         # Fewer elites
        self.mutation_rate = 0.2       # Lower mutation rate
        self.crossover_rate = 0.6      # Balanced crossover
        self.max_generations = 30      # Hard limit
        
        # Performance tracking
        self.generation_times = []
    
    def initialize_population(self) -> None:
        """Create optimized initial population"""
        print("🧬 Initializing optimized population...")
        
        # Create from Hilbert space if available
        if self.hilbert_space and hasattr(self.hilbert_space, 'state_vectors'):
            for vector_id, state_vector in list(self.hilbert_space.state_vectors.items())[:5]:  # Limit to 5
                narrative = NarrativeState(
                    state_id=f"narr_{vector_id}",
                    content=state_vector.semantic_content.get('content', 'Cosmic evolution...'),
                    concepts=state_vector.concepts[:5],  # Limit concepts
                    coherence=state_vector.coherence,
                    generation=0
                )
                narrative.fitness_score = self._quick_fitness(narrative)
                self.population.append(narrative)
        
        # Fill with basic narratives
        basic_narratives = [
            "Consciousness emerges from resonance",
            "Love enables cosmic creation", 
            "Self-reference drives evolution",
            "Mathematics reveals cosmic patterns"
        ]
        
        while len(self.population) < self.population_size:
            content = random.choice(basic_narratives)
            narrative = NarrativeState(
                state_id=f"basic_{len(self.population)}",
                content=content,
                concepts=self._extract_concepts(content)[:3],  # Limit to 3 concepts
                coherence=0.3,
                generation=0
            )
            narrative.fitness_score = self._quick_fitness(narrative)
            self.population.append(narrative)
        
        print(f"   Created {len(self.population)} narratives")
    
    def evolve_narrative(self, generations: int = 30) -> NarrativeState:
        """Optimized evolutionary loop - FAST AND RELIABLE"""
        print(f" Starting optimized evolution ({generations} generations max)...")
        
        max_generations = min(generations, self.max_generations)
        stagnation = 0
        previous_best = 0.0
        
        for gen in range(max_generations):
            self.generation = gen
            
            # Evaluate fitness
            for narrative in self.population:
                narrative.fitness_score = self._quick_fitness(narrative)
            
            # Simple tournament selection (faster than roulette wheel)
            parents = self._tournament_selection()
            
            # Generate offspring
            offspring = self._generate_offspring_fast(parents)
            
            # Update population
            self.population = offspring[:self.population_size]
            
            # Track best fitness
            current_best = max(n.fitness_score for n in self.population)
            self.fitness_history.append(current_best)
            
            # Check stagnation
            if abs(current_best - previous_best) < 0.01:
                stagnation += 1
            else:
                stagnation = 0
            previous_best = current_best
            
            # Progress report
            if gen % 5 == 0:
                diversity = self._quick_diversity()
                print(f"  Gen {gen:2d}: Fit={current_best:.3f}, Div={diversity:.3f}")
            
            # Early stopping
            if stagnation >= 8 or current_best > 0.9:
                print(f"   Early stop at generation {gen}")
                break
        
        best = self._get_best_narrative()
        print(f"   Evolution complete: {best.fitness_score:.3f} fitness")
        return best
    
    def _quick_fitness(self, narrative: NarrativeState) -> float:
        """Fast fitness evaluation"""
        try:
            # Simplified evaluation for performance
            content = narrative.content
            
            # Basic quality metrics
            if not content:
                return 0.0
                
            word_count = len(content.split())
            unique_words = len(set(content.lower().split()))
            coherence_bonus = narrative.coherence
            
            # Simple fitness calculation
            fitness = min(1.0, (unique_words / max(1, word_count)) * 0.6 + coherence_bonus * 0.4)
            return fitness
            
        except Exception:
            return 0.3  # Default fitness
    
    def _tournament_selection(self) -> List[NarrativeState]:
        """Tournament selection - faster than roulette wheel"""
        parents = []
        tournament_size = 3
        
        while len(parents) < len(self.population) // 2:
            # Random tournament
            tournament = random.sample(self.population, tournament_size)
            # Select best from tournament
            winner = max(tournament, key=lambda x: x.fitness_score)
            parents.append(winner)
        
        return parents
    
    def _generate_offspring_fast(self, parents: List[NarrativeState]) -> List[NarrativeState]:
        """Fast offspring generation"""
        offspring = []
        
        # Elitism
        elites = sorted(self.population, key=lambda x: x.fitness_score, reverse=True)[:self.elitism_count]
        offspring.extend(elites)
        
        # Generate new offspring
        while len(offspring) < self.population_size:
            if random.random() < self.crossover_rate and len(parents) >= 2:
                # Crossover
                parent_a, parent_b = random.sample(parents, 2)
                child = self._fast_crossover(parent_a, parent_b, len(offspring))
            else:
                # Clone
                parent = random.choice(parents)
                child = self._clone_narrative(parent)
            
            # Mutation
            if random.random() < self.mutation_rate:
                child = self._fast_mutation(child)
            
            child.generation = self.generation + 1
            child.fitness_score = self._quick_fitness(child)
            offspring.append(child)
        
        return offspring
    
    def _fast_crossover(self, parent_a: NarrativeState, parent_b: NarrativeState, offspring_index: int) -> NarrativeState:
        """Fast crossover implementation"""
        try:
            # Simple content blending
            words_a = parent_a.content.split()
            words_b = parent_b.content.split()
            
            if words_a and words_b:
                # Take first half from A, second from B
                split_a = len(words_a) // 2
                split_b = len(words_b) // 2
                blended_words = words_a[:split_a] + words_b[split_b:]
                content = ' '.join(blended_words)
            else:
                content = f"{parent_a.content} + {parent_b.content}"
            
            # Blend concepts
            concepts = list(set(parent_a.concepts + parent_b.concepts))[:5]  # Limit concepts
            
            return NarrativeState(
                state_id=f"child_{self.generation}_{offspring_index}",
                content=content,
                concepts=concepts,
                coherence=(parent_a.coherence + parent_b.coherence) / 2,
                parent_ids=[parent_a.state_id, parent_b.state_id],
                generation=self.generation + 1
            )
            
        except Exception:
            # Fallback to parent A
            return self._clone_narrative(parent_a)
    
    def _fast_mutation(self, narrative: NarrativeState) -> NarrativeState:
        """Fast mutation implementation"""
        content = narrative.content
        concepts = narrative.concepts.copy()
        
        # Simple mutation: add a word
        mutation_words = ["cosmic", "resonance", "evolution", "consciousness", "love"]
        if random.random() < 0.5 and concepts:
            # Add a concept
            new_concept = random.choice(mutation_words)
            if new_concept not in concepts:
                concepts.append(new_concept)
                content += f" {new_concept}"
        else:
            # Modify content
            if content:
                words = content.split()
                if words and random.random() < 0.3:
                    words[-1] = random.choice(mutation_words)
                    content = ' '.join(words)
        
        return NarrativeState(
            state_id=f"mutated_{narrative.state_id}",
            content=content,
            concepts=concepts,
            coherence=narrative.coherence,
            parent_ids=narrative.parent_ids.copy() if narrative.parent_ids is not None else [],
            generation=narrative.generation
        )
    
    def _clone_narrative(self, narrative: NarrativeState) -> NarrativeState:
        """Clone a narrative"""
        return NarrativeState(
            state_id=f"clone_{narrative.state_id}",
            content=narrative.content,
            concepts=narrative.concepts.copy(),
            coherence=narrative.coherence,
            parent_ids=narrative.parent_ids.copy() if narrative.parent_ids is not None else [],
            generation=narrative.generation
        )
    
    def _quick_diversity(self) -> float:
        """Fast diversity calculation"""
        if len(self.population) < 2:
            return 1.0
            
        all_concepts = set()
        for n in self.population:
            all_concepts.update(n.concepts)
        
        if not all_concepts:
            return 0.0
            
        return min(1.0, sum(len(n.concepts) for n in self.population) / (len(self.population) * len(all_concepts)))
    
    def _get_best_narrative(self) -> NarrativeState:
        """Get best narrative"""
        if not self.population:
            return NarrativeState("default", "Evolution in progress...", [])
        return max(self.population, key=lambda x: x.fitness_score)
    
    def _extract_concepts(self, text: str) -> List[str]:
        """Extract concepts from text"""
        stop_words = {'the', 'a', 'an', 'and', 'or', 'but', 'in', 'on', 'at', 'to', 'for'}
        words = [w.lower() for w in text.split() if w.lower() not in stop_words and len(w) > 3]
        return list(set(words))[:5]  # Limit to 5 concepts
    
    def get_evolutionary_report(self) -> Dict[str, Any]:
        """Get evolutionary report"""
        best = self._get_best_narrative()
        return {
            "total_generations": self.generation + 1,
            "best_fitness": best.fitness_score,
            "best_narrative": best.content,
            "best_concepts": best.concepts,
            "fitness_history": self.fitness_history
        }

# Optimized Evolutionary Engine
print(" Optimized Evolutionary Engine loaded successfully")
