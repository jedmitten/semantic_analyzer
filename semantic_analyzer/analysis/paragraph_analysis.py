from transformers import pipeline
from ..utils.models import ParagraphAnalysisResult

def analyze_paragraph_qualitative(
    paragraphs: list[str]
) -> ParagraphAnalysisResult:
    """
    Provide qualitative analysis of paragraphs including sentiment, key themes, and content analysis.
    
    Args:
        paragraphs: List of paragraphs to analyze
        
    Returns:
        ParagraphAnalysisResult containing the qualitative analysis
    """
    # Initialize models
    sentiment_analyzer = pipeline("sentiment-analysis")
    summarizer = pipeline("summarization", model="facebook/bart-large-cnn")
    topic_classifier = pipeline("zero-shot-classification")
    
    # Analyze each paragraph
    analyses = []
    for paragraph in paragraphs:
        # Get sentiment
        sentiment = sentiment_analyzer(paragraph)[0]
        
        # Get key themes through summarization
        summary = summarizer(paragraph, max_length=30, min_length=10, do_sample=False)[0]['summary_text']
        
        # Get main topics
        topics = topic_classifier(
            paragraph,
            candidate_labels=["Politics", "Technology", "Science", "Arts", "Business", "Sports", "Health", "Education"]
        )
        
        analyses.append({
            'paragraph': paragraph,
            'sentiment': sentiment,
            'key_themes': summary,
            'main_topics': topics,
            'length': len(paragraph.split()),
            'complexity': len(paragraph.split()) / len(paragraph.split('.')),
            'readability': len(paragraph.split()) / len(paragraph.split('\n'))
        })
    
    return ParagraphAnalysisResult(
        paragraphs=paragraphs,
        analyses=analyses
    ) 