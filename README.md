# AI Video Pipeline

An automated pipeline that generates AI-enhanced short videos and manages their upload to YouTube with proper AI content disclosure compliance.

## Overview

This project implements an automated video generation and publishing pipeline with the following key features:

- Topic generation using OpenAI's GPT-3
- Video creation through Fliki AI
- Automated YouTube uploads with AI content disclosure
- Web dashboard for monitoring and management
- Robust queue management system

## Tech Stack

- **Backend**: Python (FastAPI)
- **Frontend**: Next.js dashboard
- **Database**: PostgreSQL
- **Hosting**:
  - Backend: Render (FastAPI service)
  - Frontend: Vercel (Next.js)
  - Database: Render (PostgreSQL)

## Project Structure

```
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
```

## Implementation Phases

### Phase 1 - Core Pipeline Setup

- FastAPI backend implementation with endpoints for:
  - Topic generation
  - Video creation requests
  - Upload management
- PostgreSQL database setup with tables for:
  - Topics queue
  - Video generation queue
  - Upload queue
  - System configuration
- Basic Next.js dashboard featuring:
  - Manual approval interface
  - Pipeline status monitoring
  - Configuration management

### Phase 2 - Integration

- OpenAI API integration for topic generation
- Fliki API integration for video creation
- YouTube API integration with mandatory AI disclosures

### Phase 3 - Automation

- Scheduled pipeline execution
- Error handling and retry mechanisms
- Monitoring and alerting system
- Analytics dashboard

## YouTube AI Policy Compliance

This pipeline adheres to YouTube's responsible AI innovation policies by:

- Implementing mandatory disclosure for AI-generated content
- Adding appropriate labels for synthetic content
- Following YouTube's guidelines for sensitive topics
- Respecting content removal requests for AI-generated material
- Maintaining transparency in the video generation process

## Setup Instructions

1. Clone the repository
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Configure environment variables:
   ```bash
   cp .env.example .env
   # Edit .env with your API keys and configuration
   ```
4. Initialize the database:
   ```bash
   python -m app.database
   ```
5. Start the FastAPI server:
   ```bash
   uvicorn app.main:app --reload
   ```

## Environment Variables

Required environment variables:

```
DATABASE_URL=postgresql://user:password@localhost:5432/dbname
OPENAI_API_KEY=your_openai_key
FLIKI_API_KEY=your_fliki_key
YOUTUBE_API_KEY=your_youtube_key
```

## API Documentation

API documentation is available at `/docs` when running the FastAPI server.

## Contributing

1. Fork the repository
2. Create a feature branch
3. Submit a pull request
