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
class SentenceAnalysisResult:
    near_sentences: list[str]
    far_sentences: list[str]
    similarity_scores: list[Tuple[Tuple[str, str], float]]
    
    def to_json(self) -> str:
        """Convert the result to a JSON string"""
        return json.dumps({
            'near_sentences': self.near_sentences,
            'far_sentences': self.far_sentences,
            'similarity_scores': [
                {
                    'sentence1': pair[0],
                    'sentence2': pair[1],
                    'similarity': score
                }
                for pair, score in self.similarity_scores
            ]
        }, indent=2)
    
    def to_table(self) -> str:
        """Convert the result to a formatted table string"""
        lines = ["Sentence Similarity Analysis", "=" * 50]
        if self.near_sentences:
            lines.append(f"\nNear sentences: {', '.join(self.near_sentences)}")
        if self.far_sentences:
            lines.append(f"Far sentences: {', '.join(self.far_sentences)}")
        lines.append("\nSimilarity Scores:")
        lines.append("-" * 80)
        lines.append(f"{'Sentence 1':<40} {'Sentence 2':<40} {'Score':<10}")
        lines.append("-" * 80)
        for (sent1, sent2), score in self.similarity_scores:
            lines.append(f"{sent1[:37]+'...':<40} {sent2[:37]+'...':<40} {score:.4f}")
        return "\n".join(lines)

@dataclass
class ParagraphAnalysisResult:
    near_paragraphs: list[str]
    far_paragraphs: list[str]
    similarity_scores: list[Tuple[Tuple[str, str], float]]
    
    def to_json(self) -> str:
        """Convert the result to a JSON string"""
        return json.dumps({
            'near_paragraphs': self.near_paragraphs,
            'far_paragraphs': self.far_paragraphs,
            'similarity_scores': [
                {
                    'paragraph1': pair[0],
                    'paragraph2': pair[1],
                    'similarity': score
                }
                for pair, score in self.similarity_scores
            ]
        }, indent=2)
    
    def to_table(self) -> str:
        """Convert the result to a formatted table string"""
        lines = ["Paragraph Similarity Analysis", "=" * 50]
        if self.near_paragraphs:
            lines.append(f"\nNear paragraphs: {', '.join(self.near_paragraphs)}")
        if self.far_paragraphs:
            lines.append(f"Far paragraphs: {', '.join(self.far_paragraphs)}")
        lines.append("\nSimilarity Scores:")
        lines.append("-" * 80)
        lines.append(f"{'Paragraph 1':<40} {'Paragraph 2':<40} {'Score':<10}")
        lines.append("-" * 80)
        for (para1, para2), score in self.similarity_scores:
            lines.append(f"{para1[:37]+'...':<40} {para2[:37]+'...':<40} {score:.4f}")
        return "\n".join(lines) 