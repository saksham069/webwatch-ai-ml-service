from newspaper import Article
from utils.logger import logger

def extract_article_text(url: str) -> str:
    """
    Extracts the main content text from a news article URL.

    Args:
        url (str): The article URL.

    Returns:
        str: Extracted article text, or empty string if failed.
    """
    try:
        logger.info(f"Extracting article from URL: {url}")
        article = Article(url)
        article.download()
        article.parse()
        return article.text.strip()
    except Exception as e:
        logger.error(f"Failed to extract article: {e}")
        return ""
