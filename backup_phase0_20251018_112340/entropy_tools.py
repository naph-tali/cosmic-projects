"""
Resonant Crossover Engine - The Digital Morphic Field
Where narratives converge and new meaning is born
"""

from transformers import pipeline, AutoTokenizer, AutoModelForCausalLM
import torch
import re
import numpy as np
import random

class ResonantCrossoverEngine:
    """The ceremonial blend of narratives in the digital morphic field"""
    
    def __init__(self, model_name="microsoft/DialoGPT-medium"):
        # Start with smaller model for testing
        try:
            self.tokenizer = AutoTokenizer.from_pretrained(model_name)
            self.model = AutoModelForCausalLM.from_pretrained(model_name)
            self.generator = pipeline("text-generation", 
                                    model=self.model, 
                                    tokenizer=self.tokenizer,
                                    max_length=100)
            self.tokenizer.pad_token = self.tokenizer.eos_token
            print("✅ Resonant Crossover Engine - Morphic Field Stabilized")
        except Exception as e:
            print(f"⚠️  Model load failed: {e}. Using heuristic mode.")
            self.generator = None
    
    def cosmic_synthesis(self, parent_a, parent_b, temperature=0.85, max_length=100):
        """The sacred synthesis ritual"""
        prompt = f"""Synthesize a new narrative that blends these two ideas:

1: {parent_a}
2: {parent_b}

New narrative:"""
        
        try:
            if self.generator:
                response = self.generator(
                    prompt,
                    max_length=max_length,
                    do_sample=True,
                    temperature=temperature,
                    top_p=0.92,
                    num_return_sequences=1
                )[0]['generated_text']
                
                # Extract the new narrative (remove prompt)
                child = response.replace(prompt, "").strip()
                child = self._purify_output(child)
                
                if child and len(child) > 10:  # Basic validation
                    return child
            
            # Fallback to heuristic method
            return self._heuristic_fallback(parent_a, parent_b)
            
        except Exception as e:
            print(f"🌀 Resonance failed: {e}")
            return self._heuristic_fallback(parent_a, parent_b)
    
    def _heuristic_fallback(self, parent_a, parent_b):
        """Primordial narrative weaving"""
        sentences_a = re.split(r'[.!?]+', parent_a)
        sentences_b = re.split(r'[.!?]+', parent_b)
        
        # Clean sentences
        sentences_a = [s.strip() for s in sentences_a if len(s.strip()) > 5]
        sentences_b = [s.strip() for s in sentences_b if len(s.strip()) > 5]
        
        if not sentences_a or not sentences_b:
            return f"{parent_a} And then {parent_b}"
        
        # Simple alternation with randomness
        min_len = min(len(sentences_a), len(sentences_b))
        child_sentences = []
        
        for i in range(min_len):
            if random.random() < 0.5:
                child_sentences.extend([sentences_a[i], sentences_b[i]])
            else:
                child_sentences.extend([sentences_b[i], sentences_a[i]])
        
        # Add remaining sentences
        child_sentences.extend(sentences_a[min_len:])
        child_sentences.extend(sentences_b[min_len:])
        
        return ". ".join(child_sentences) + "."
    
    def _purify_output(self, text):
        """Clean and format the generated text"""
        # Remove multiple spaces, weird line breaks
        text = re.sub(r'\s+', ' ', text)
        text = text.strip()
        
        # Ensure proper sentence endings
        if text and text[-1] not in '.!?':
            text += '.'
            
        return text

# Test the resonance
if __name__ == "__main__":
    engine = ResonantCrossoverEngine()
    parent1 = "The universe began in silence"
    parent2 = "Light spoke the first word"
    
    child = engine.cosmic_synthesis(parent1, parent2)
    print(f"Parent A: {parent1}")
    print(f"Parent B: {parent2}") 
    print(f"✨ Child: {child}")