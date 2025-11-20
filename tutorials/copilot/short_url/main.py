from fastapi import FastAPI, Depends, HTTPException, Request, Form
from fastapi.responses import RedirectResponse, HTMLResponse
from sqlalchemy.orm import Session
from database import get_db, URL
from utils import generate_short_code, is_valid_url
from pydantic import BaseModel

app = FastAPI(title="URL Shortener", description="A simple URL shortener service")

class URLRequest(BaseModel):
    url: str

class URLResponse(BaseModel):
    original_url: str
    short_url: str
    short_code: str

@app.get("/", response_class=HTMLResponse)
async def read_root():
    """Serve a simple HTML form for URL shortening."""
    html_content = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>URL Shortener</title>
        <style>
            body { font-family: Arial, sans-serif; max-width: 600px; margin: 50px auto; padding: 20px; }
            input[type="url"] { width: 70%; padding: 10px; margin: 10px 0; }
            input[type="submit"] { padding: 10px 20px; background: #007bff; color: white; border: none; cursor: pointer; }
            .result { margin-top: 20px; padding: 10px; background: #f8f9fa; border-radius: 5px; }
        </style>
    </head>
    <body>
        <h1>URL Shortener</h1>
        <form method="post" action="/shorten">
            <input type="url" name="url" placeholder="Enter URL to shorten" required>
            <input type="submit" value="Shorten">
        </form>
    </body>
    </html>
    """
    return HTMLResponse(content=html_content)

@app.post("/shorten", response_model=URLResponse)
async def shorten_url(
    request: Request,
    url: str = Form(...),
    db: Session = Depends(get_db)
):
    """Shorten a URL and return the short version."""
    if not is_valid_url(url):
        raise HTTPException(status_code=400, detail="Invalid URL format")
    
    # Check if URL already exists
    existing_url = db.query(URL).filter(URL.original_url == url).first()
    if existing_url:
        base_url = f"{request.url.scheme}://{request.url.netloc}"
        return URLResponse(
            original_url=url,
            short_url=f"{base_url}/{existing_url.short_code}",
            short_code=existing_url.short_code
        )
    
    # Generate unique short code
    while True:
        short_code = generate_short_code()
        if not db.query(URL).filter(URL.short_code == short_code).first():
            break
    
    # Create new URL entry
    db_url = URL(original_url=url, short_code=short_code)
    db.add(db_url)
    db.commit()
    db.refresh(db_url)
    
    base_url = f"{request.url.scheme}://{request.url.netloc}"
    return URLResponse(
        original_url=url,
        short_url=f"{base_url}/{short_code}",
        short_code=short_code
    )

@app.post("/api/shorten", response_model=URLResponse)
async def api_shorten_url(
    request: Request,
    url_request: URLRequest,
    db: Session = Depends(get_db)
):
    """API endpoint to shorten a URL."""
    url = url_request.url
    if not is_valid_url(url):
        raise HTTPException(status_code=400, detail="Invalid URL format")
    
    # Check if URL already exists
    existing_url = db.query(URL).filter(URL.original_url == url).first()
    if existing_url:
        base_url = f"{request.url.scheme}://{request.url.netloc}"
        return URLResponse(
            original_url=url,
            short_url=f"{base_url}/{existing_url.short_code}",
            short_code=existing_url.short_code
        )
    
    # Generate unique short code
    while True:
        short_code = generate_short_code()
        if not db.query(URL).filter(URL.short_code == short_code).first():
            break
    
    # Create new URL entry
    db_url = URL(original_url=url, short_code=short_code)
    db.add(db_url)
    db.commit()
    db.refresh(db_url)
    
    base_url = f"{request.url.scheme}://{request.url.netloc}"
    return URLResponse(
        original_url=url,
        short_url=f"{base_url}/{short_code}",
        short_code=short_code
    )

@app.get("/{short_code}")
async def redirect_url(short_code: str, db: Session = Depends(get_db)):
    """Redirect to the original URL using the short code."""
    db_url = db.query(URL).filter(URL.short_code == short_code).first()
    
    if not db_url:
        raise HTTPException(status_code=404, detail="Short URL not found")
    
    # Increment click count
    db_url.click_count += 1
    db.commit()
    
    return RedirectResponse(url=db_url.original_url, status_code=301)

@app.get("/stats/{short_code}")
async def get_stats(short_code: str, db: Session = Depends(get_db)):
    """Get statistics for a shortened URL."""
    db_url = db.query(URL).filter(URL.short_code == short_code).first()
    
    if not db_url:
        raise HTTPException(status_code=404, detail="Short URL not found")
    
    return {
        "short_code": db_url.short_code,
        "original_url": db_url.original_url,
        "created_at": db_url.created_at,
        "click_count": db_url.click_count
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
