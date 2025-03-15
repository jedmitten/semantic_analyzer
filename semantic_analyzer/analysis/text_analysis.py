from transformers import pipeline
from ..utils.models import TextAnalysisResult

def analyze_text_qualitative(
    texts: list[str]
) -> TextAnalysisResult:
    """
    Provide qualitative analysis of text including sentiment, key themes, and content analysis.
    Works with both sentences and paragraphs.
    
    Args:
        texts: List of text segments to analyze
        
    Returns:
        TextAnalysisResult containing the qualitative analysis
    """
    # Initialize models
    sentiment_analyzer = pipeline("sentiment-analysis")
    summarizer = pipeline("summarization", model="facebook/bart-large-cnn")
    topic_classifier = pipeline("zero-shot-classification")
    
    # Analyze each text segment
    analyses = []
    for text in texts:
        # Get sentiment
        sentiment = sentiment_analyzer(text)[0]
        
        # Get key themes through summarization
        # Use longer summary for longer text
        max_length = 30 if len(text.split()) > 50 else 10
        min_length = 10 if len(text.split()) > 50 else 5
        summary = summarizer(text, max_length=max_length, min_length=min_length, do_sample=False)[0]['summary_text']
        
        # Get main topics
        topics = topic_classifier(
            text,
            candidate_labels=["Politics", "Technology", "Science", "Arts", "Business", "Sports", "Health", "Education"]
        )
        
        # Calculate metrics
        word_count = len(text.split())
        sentence_count = len([s for s in text.split('.') if s.strip()])
        line_count = len([l for l in text.split('\n') if l.strip()])
        
        analyses.append({
            'text': text,
            'sentiment': sentiment,
            'key_themes': summary,
            'main_topics': topics,
            'length': word_count,
            'complexity': word_count / sentence_count if sentence_count > 0 else 0,
            'readability': word_count / line_count if line_count > 0 else 0
        })
    
    return TextAnalysisResult(
        texts=texts,
        analyses=analyses
    ) 