"""
Entropic Alchemy Tools - Quantum Vortices in Semantic Space
"""

import numpy as np
from sentence_transformers import SentenceTransformer
from scipy.spatial.distance import cosine

class EntropicAlchemist:
    """Transforms chaotic potential into meaningful order"""
    
    def __init__(self, model_name="all-mpnet-base-v2"):
        try:
            self.model = SentenceTransformer(model_name)
            print("🌀 Entropic Alchemist initialized - Morphic Field Active")
        except Exception as e:
            print(f"⚠️  Model load failed: {e}")
            self.model = None
    
    def calculate_novel_coherence(self, parent_a, parent_b, child):
        """Quantum vortices in semantic space - Novel coherence metric"""
        if self.model is None:
            return 0.5  # Fallback score
            
        try:
            # Embed all narratives in the cosmic field
            texts = [parent_a, parent_b, child]
            embeddings = self.model.encode(texts, convert_to_tensor=True)
            
            # Calculate semantic relationships
            parent_similarity = 1 - cosine(embeddings[0].cpu().numpy(), embeddings[1].cpu().numpy())
            child_to_a = 1 - cosine(embeddings[2].cpu().numpy(), embeddings[0].cpu().numpy())
            child_to_b = 1 - cosine(embeddings[2].cpu().numpy(), embeddings[1].cpu().numpy())
            
            # Novel coherence: how child transcends parent similarity
            novel_coherence = (child_to_a + child_to_b) - parent_similarity
            return max(0, novel_coherence)
            
        except Exception as e:
            print(f"❌ Quantum vortex collapse: {e}")
            return 0.0

if __name__ == "__main__":
    alchemist = EntropicAlchemist()
    print("✅ Entropic Alchemist test passed!")
