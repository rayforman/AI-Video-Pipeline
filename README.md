## Project Structure

ai-video-pipeline/
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── config.py
│   ├── database.py
│   ├── models/
│   │   ├── __init__.py
│   │   └── schemas.py
│   ├── api/
│   │   ├── __init__.py
│   │   ├── topics.py
│   │   ├── videos.py
│   │   └── uploads.py
│   └── services/
│       ├── __init__.py
│       ├── openai_service.py
│       ├── fliki_service.py
│       └── youtube_service.py
├── requirements.txt
├── .env
└── .gitignore