from transformers import pipeline
from nltk.tokenize import sent_tokenize
import nltk
from utils.logger import logger

nltk.download("punkt", quiet=True)
nltk.download("punkt_tab", quiet=True)

# summarizer pipeline
try:
    summarizer = pipeline("summarization", model="sshleifer/distilbart-cnn-12-6")
    logger.info("Summarizer pipeline loaded successfully.")
except Exception as e:
    logger.critical(f"Error loading summarizer pipeline: {e}")
    summarizer = None


def split_into_chunks(text, max_words=500):
    """
    Splits long texts into manageable chunks of ~max_words each.
    """
    sentences = sent_tokenize(text)
    chunks = []
    current_chunk = ""
    current_length = 0

    for sentence in sentences:
        word_count = len(sentence.split())
        if current_length + word_count <= max_words:
            current_chunk += sentence + " "
            current_length += word_count
        else:
            chunks.append(current_chunk.strip())
            current_chunk = sentence + " "
            current_length = word_count

    if current_chunk:
        chunks.append(current_chunk.strip())

    return chunks


def summarize(text: str) -> str:
    """
    Summarizes input text using pretrained HuggingFace summarizer.

    Args:
        text (str): The full article content.

    Returns:
        str: Concatenated summary across all chunks.
    """
    if not summarizer:
        logger.error("Summarizer not available.")
        return ""

    chunks = split_into_chunks(text)
    logger.info(f"Text split into {len(chunks)} chunk(s).")

    full_summary = ""
    for i, chunk in enumerate(chunks):
        try:
            logger.info(f"Summarizing chunk {i + 1}/{len(chunks)}")
            summary = summarizer(chunk, max_length=120, min_length=30, do_sample=False)
            full_summary += summary[0]["summary_text"].strip() + " "
        except Exception as e:
            logger.error(f"Chunk {i + 1} summarization failed: {e}")
            continue

    return full_summary.strip()
