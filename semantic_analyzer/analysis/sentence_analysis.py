from typing import Tuple
from sentence_transformers import SentenceTransformer
from ..utils.models import SentenceAnalysisResult

def analyze_sentence_similarity(
    near_sentences: list[str],
    far_sentences: list[str]
) -> SentenceAnalysisResult:
    """
    Analyze sentence similarity based on near and far sentence constraints.
    
    Args:
        near_sentences: List of sentences that should be semantically similar
        far_sentences: List of sentences that should be semantically different
        
    Returns:
        SentenceAnalysisResult containing the analysis results
    """
    # Initialize the sentence transformer model
    model = SentenceTransformer('all-MiniLM-L6-v2')
    
    # Get embeddings for all sentences
    all_sentences = near_sentences + far_sentences
    embeddings = model.encode(all_sentences)
    
    # Calculate similarity scores between all sentences
    similarity_scores = []
    for i, emb1 in enumerate(embeddings):
        for j, emb2 in enumerate(embeddings[i+1:], i+1):
            similarity = model.similarity(emb1, emb2)
            similarity_scores.append((
                (all_sentences[i], all_sentences[j]),
                similarity
            ))
    
    return SentenceAnalysisResult(
        near_sentences=near_sentences,
        far_sentences=far_sentences,
        similarity_scores=similarity_scores
    ) 