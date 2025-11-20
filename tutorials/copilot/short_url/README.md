# URL Shortener

A simple URL shortener service built with FastAPI and SQLite.

## Features

- Shorten long URLs to compact codes
- Redirect short URLs to original destinations
- Click tracking and statistics
- Web interface and REST API
- SQLite database for persistence

## Setup

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Run the application:
```bash
python main.py
```

Or use uvicorn directly:
```bash
uvicorn main:app --reload
```

## Usage

### Web Interface
Visit `http://localhost:8000` to use the web interface.

### API Endpoints

- `POST /api/shorten` - Shorten a URL
- `GET /{short_code}` - Redirect to original URL
- `GET /stats/{short_code}` - Get URL statistics

### Example API Usage

```bash
# Shorten a URL
curl -X POST "http://localhost:8000/api/shorten" \
     -H "Content-Type: application/json" \
     -d '{"url": "https://www.example.com"}'

# Get statistics
curl "http://localhost:8000/stats/abc123"
```

## Database

The application uses SQLite database (`shortener.db`) to store:
- Original URLs
- Short codes
- Creation timestamps
- Click counts
