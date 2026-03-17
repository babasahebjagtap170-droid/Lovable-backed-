# FastAPI Backend for Lovable Website

This is a simple FastAPI backend project designed to connect with a Lovable website.

## Project Structure

```
/fastapi-backend
├── main.py          # Main FastAPI application
├── requirements.txt # Python dependencies
└── README.md        # This file
```

## Endpoints

- `GET /` - Returns a JSON message confirming the backend is working
- `GET /generate` - Returns a greeting message from the FastAPI backend

## Local Development

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Run the application:
   ```bash
   uvicorn main:app --host 0.0.0.0 --port 10000
   ```

3. Visit `http://localhost:10000` to test the endpoints.

## Deployment on Render

1. Create a new Web Service on Render
2. Connect your GitHub repository
3. Set the following configuration:
   - **Runtime**: Python 3
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `uvicorn main:app --host 0.0.0.0 --port 10000`
4. Deploy the service

## Connecting to Lovable Website

Set the environment variable `FASTAPI_BACKEND_URL` in your Lovable website to point to your deployed Render service URL.

## API Documentation

Once deployed, visit `https://your-render-url/docs` to see the interactive API documentation provided by FastAPI.