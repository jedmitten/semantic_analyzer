from ..utils.models import WordAnalysisResult
from ..utils.vector_store import get_word_vectors

def analyze_word_similarity(
    near_words: list[str] | None = None,
    far_words: list[str] | None = None,
    top_n: int = 5,
    vector_path: str | None = None
) -> WordAnalysisResult:
    """
    Analyze word similarity based on near and far word constraints.
    
    Args:
        near_words: Optional list of words that should be semantically similar
        far_words: Optional list of words that should be semantically different
        top_n: Number of similar words to return
        vector_path: Optional path to the word vectors file
        
    Returns:
        WordAnalysisResult containing the analysis results
    """
    model = get_word_vectors(vector_path)
    
    # Convert None to empty lists for gensim
    near_words = near_words or []
    far_words = far_words or []
    
    # Find words that are close to near_words but far from far_words
    result = model.most_similar(
        positive=near_words,
        negative=far_words,
        topn=top_n
    )
    
    return WordAnalysisResult(
        near_words=near_words,
        far_words=far_words,
        similar_words=result
    ) 