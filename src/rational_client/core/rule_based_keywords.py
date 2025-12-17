"""
Rule-based keyword extraction using simple NLP techniques.

This module provides a simple approach to keyword extraction based on:
- Stopword removal (using NLTK)
- Lemmatization (using NLTK)
- Word frequency analysis
- Returning the most frequent terms

Supports multiple languages including English and Italian.
"""

import re
from collections import Counter

import nltk
from nltk.corpus import stopwords
from nltk.stem import SnowballStemmer, WordNetLemmatizer

# Download required NLTK data (if not already downloaded)
try:
    nltk.data.find("corpora/stopwords")
except LookupError:
    nltk.download("stopwords", quiet=True)

try:
    nltk.data.find("corpora/wordnet")
except LookupError:
    nltk.download("wordnet", quiet=True)

try:
    nltk.data.find("corpora/omw-1.4")
except LookupError:
    nltk.download("omw-1.4", quiet=True)

# Language detection support
try:
    from langdetect import detect

    LANGDETECT_AVAILABLE = True
except ImportError:
    detect = None  # type: ignore
    LANGDETECT_AVAILABLE = False

# Initialize stopwords and lemmatizers for supported languages
STOPWORDS_BY_LANG = {
    "en": set(stopwords.words("english")),
    "it": set(stopwords.words("italian")),
}

# WordNetLemmatizer only works for English
# For other languages, we'll use SnowballStemmer
LEMMATIZERS = {
    "en": WordNetLemmatizer(),
}

STEMMERS = {
    "en": SnowballStemmer("english"),
    "it": SnowballStemmer("italian"),
}


def detect_language(text: str) -> str:
    """
    Detect the language of the text.

    Args:
        text: The text to detect language from

    Returns:
        Two-letter language code (e.g., 'en', 'it'), defaults to 'en' if detection fails
    """
    if not LANGDETECT_AVAILABLE or detect is None or not text or len(text.strip()) < 20:
        # Default to English if langdetect not available or text too short
        return "en"

    try:
        lang = detect(text)
        # Map to supported languages
        if lang in STOPWORDS_BY_LANG:
            return lang
        # Default to English for unsupported languages
        return "en"
    except Exception:
        return "en"


def extract_keywords_rule_based(text: str, max_keywords: int = 15, language: str | None = None) -> list[str]:
    """
    Extract keywords from text using rule-based approach with NLP.

    This function:
    1. Detects language (if not provided)
    2. Tokenizes the text into words
    3. Converts to lowercase
    4. Removes stopwords for the detected language (using NLTK)
    5. Filters out very short words (< 3 characters)
    6. Lemmatizes/stems words to their base form (using NLTK)
    7. Counts word frequencies
    8. Returns the top N most frequent words

    Supports English and Italian, with automatic language detection.

    Args:
        text: The text to extract keywords from
        max_keywords: Maximum number of keywords to return (default: 15)
        language: Optional language code ('en', 'it'). If None, will auto-detect.

    Returns:
        A list of extracted keywords (lemmatized/stemmed), ordered by frequency (most frequent first)
    """
    if not text or not text.strip():
        return []

    # Detect language if not provided
    if language is None:
        language = detect_language(text)

    # Get stopwords for the detected language (default to English)
    stopwords_set = STOPWORDS_BY_LANG.get(language, STOPWORDS_BY_LANG["en"])

    # Convert to lowercase
    text_lower = text.lower()

    # Tokenize: split on non-alphanumeric characters, keeping words
    # Support Unicode characters for non-English languages
    words = re.findall(r"\b[\w]+\b", text_lower, re.UNICODE)

    # Filter out stopwords and very short words
    filtered_words = [word for word in words if word not in stopwords_set and len(word) >= 3]

    if not filtered_words:
        return []

    # Lemmatize/stem words to get their base form
    # Use language-specific lemmatizer or stemmer
    if language in LEMMATIZERS:
        # Use lemmatizer for English (more accurate)
        lemmatizer = LEMMATIZERS[language]
        processed_words = [lemmatizer.lemmatize(word) for word in filtered_words]
    elif language in STEMMERS:
        # Use stemmer for other languages (Italian, etc.)
        stemmer = STEMMERS[language]
        processed_words = [stemmer.stem(word) for word in filtered_words]
    else:
        # Fallback: no processing
        processed_words = filtered_words

    # Count word frequencies
    word_counts = Counter(processed_words)

    # Get the most common words
    most_common = word_counts.most_common(max_keywords)

    # Return just the words (without counts)
    return [word for word, _count in most_common]
