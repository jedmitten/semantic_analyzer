from gensim.models import KeyedVectors
from pathlib import Path
import os

# Default path to the word vectors file
DEFAULT_VECTOR_PATH = os.path.expanduser("~/Downloads/archive/GoogleNews-vectors-negative300.bin")

def get_word_vectors(vector_path: str | None = None) -> KeyedVectors:
    """
    Get or load the word vectors model.
    
    Args:
        vector_path: Optional path to the word vectors file. If None, uses DEFAULT_VECTOR_PATH
        
    Returns:
        Loaded KeyedVectors model
        
    Raises:
        FileNotFoundError: If the vector file is not found at the specified path
    """
    path = vector_path or DEFAULT_VECTOR_PATH
    
    if not os.path.exists(path):
        raise FileNotFoundError(
            f"Word vectors file not found at {path}. "
            "Please download the Google News Word2Vec model and update the path."
        )
    
    return KeyedVectors.load_word2vec_format(path, binary=True) 