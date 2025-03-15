from dataclasses import dataclass
from typing import Tuple
import json

@dataclass
class WordAnalysisResult:
    near_words: list[str]
    far_words: list[str]
    similar_words: list[Tuple[str, float]]
    
    def to_json(self) -> str:
        """Convert the result to a JSON string"""
        return json.dumps({
            'near_words': self.near_words,
            'far_words': self.far_words,
            'similar_words': [
                {'word': word, 'similarity': score}
                for word, score in self.similar_words
            ]
        }, indent=2)
    
    def to_table(self) -> str:
        """Convert the result to a formatted table string"""
        lines = ["Word Similarity Analysis", "=" * 50]
        if self.near_words:
            lines.append(f"\nNear words: {', '.join(self.near_words)}")
        if self.far_words:
            lines.append(f"Far words: {', '.join(self.far_words)}")
        lines.append("\nSimilar Words:")
        lines.append("-" * 30)
        lines.append(f"{'Word':<20} {'Score':<10}")
        lines.append("-" * 30)
        for word, score in self.similar_words:
            lines.append(f"{word:<20} {score:.4f}")
        return "\n".join(lines)

@dataclass
class TextAnalysisResult:
    texts: list[str]
    analyses: list[dict]
    
    def to_json(self) -> str:
        """Convert the result to a JSON string"""
        return json.dumps({
            'texts': self.texts,
            'analyses': self.analyses
        }, indent=2)
    
    def to_table(self) -> str:
        """Convert the result to a formatted table string"""
        lines = ["Text Qualitative Analysis", "=" * 50]
        
        for analysis in self.analyses:
            lines.append(f"\nText: {analysis['text'][:100]}...")
            lines.append("-" * 50)
            lines.append(f"Sentiment: {analysis['sentiment']['label']} ({analysis['sentiment']['score']:.2f})")
            lines.append(f"Key Themes: {analysis['key_themes']}")
            lines.append(f"Main Topics: {', '.join(analysis['main_topics']['labels'][:3])}")
            lines.append(f"Length: {analysis['length']} words")
            lines.append(f"Complexity: {analysis['complexity']:.2f} words per sentence")
            lines.append(f"Readability: {analysis['readability']:.2f} words per line")
        
        return "\n".join(lines) 