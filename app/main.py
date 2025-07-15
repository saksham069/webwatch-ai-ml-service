from fastapi import FastAPI, Query, HTTPException
from app.parser import extract_article_text
from app.summarizer import summarize
from utils.logger import logger

app = FastAPI()


@app.get("/health")
def health_check():
    logger.info("Health check pinged.")
    return {"status": "ok"}


@app.get("/summarize")
def summarize_article(
    url: str = Query(..., description="URL of the article to summarize")
):
    logger.info(f"Incoming summarization request for: {url}")

    article_text = extract_article_text(url)
    if not article_text:
        logger.warning("Article extraction failed.")
        raise HTTPException(status_code=400, detail="Could not extract article text.")

    summary = summarize(article_text)
    if not summary:
        logger.error("Summarization returned empty.")
        raise HTTPException(status_code=500, detail="Summarization failed.")

    logger.info("Summarization successful.")
    return {"summary": summary}
