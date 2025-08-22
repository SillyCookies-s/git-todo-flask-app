# Flask Registration & To-Do Application

A comprehensive Flask application with MongoDB Atlas integration featuring both user registration and to-do list management functionality.

## Architecture

```
┌─────────────────┐    HTTP Requests    ┌─────────────────┐
│                 │ ──────────────────► │                 │
│   Frontend      │                     │   Backend       │
│   (Port 5000)   │ ◄────────────────── │   (Port 3000)   │
│                 │    HTTP Responses   │                 │
└─────────────────┘                     └─────────────────┘
         │                                        │
         │                                        │
         ▼                                        ▼
┌─────────────────┐                     ┌─────────────────┐
│                 │                     │                 │
│   HTML Forms    │                     │   MongoDB       │
│   (index.html)  │                     │   Atlas         │
│                 │                     │   (Cloud DB)    │
└─────────────────┘                     └─────────────────┘
```

## Project Structure

```
to-do-flask-app/
├── backend/
│   ├── app.py                         # Backend Flask application
│   ├── requirements.txt               # Backend dependencies
│   ├── Dockerfile                     # Backend Docker configuration
│   ├── .env                           # Environment variables (not in repo)
│   └── .env.example                   # Environment variables template
├── frontend/   
│   ├── app.py                         # Frontend Flask application
│   ├── requirements.txt               # Frontend dependencies
│   ├── Dockerfile                     # Frontend Docker configuration
│   └── templates/
│       └── index.html                 # Combined registration and to-do form template
├── git_report.docx                    # Report on the Project
├── docker-compose.yml                 # Multi-container Docker setup
└── README.md                          # Project documentation
```

## Setup Instructions

### Prerequisites
- Python 
- MongoDB Atlas account 

### Backend Setup
1. Navigate to backend directory: `cd backend`
2. Install dependencies: `pip3 install -r requirements.txt`
3. Create `.env` file from template: `cp .env.example .env`
4. Configure MongoDB Atlas URI in `.env` file with your credentials
5. Run backend: `python3 app.py` (runs on port 3000)

### Frontend Setup
1. Navigate to frontend directory: `cd frontend`
2. Install dependencies: `pip3 install -r requirements.txt`
3. Run frontend: `python3 app.py` (runs on port 5000)

## Usage

### Local Development
1. Configure MongoDB Atlas connection in `backend/.env` file
2. Run backend server: `python3 backend/app.py`
3. Run frontend server: `python3 frontend/app.py`
4. Access the application at `http://localhost:5000`
5. Use either the registration form or to-do form to submit data

### Docker Deployment
1. Configure MongoDB Atlas connection in `backend/.env` file
2. Build and run with Docker Compose: `docker-compose up --build`
3. Access the application at `http://localhost:5000`

## Features

### Registration Form
- User registration with name and email fields
- Data validation and error handling
- Professional UI design with responsive layout

### To-Do Management
- Add new to-do items with ID, name, and description
- Separate MongoDB collection for to-do items
- Clean and intuitive interface

### Additional Features
- RESTful API endpoints for data retrieval
- CORS enabled for cross-origin requests
- Environment-based configuration
- Docker containerization support

## API Endpoints

### Backend Endpoints
- `GET /` - Backend status check
- `POST /submit` - Submit registration form data to MongoDB
- `POST /add_todo` - Submit to-do item data to MongoDB
- `GET /api` - Retrieve all registration data as JSON

### Frontend Endpoints
- `GET /` - Serve the combined registration and to-do form
- `GET /api` - Proxy to backend API for data retrieval

## Environment Variables

### Backend (.env file)
```
MONGO_URL=your_mongodb_atlas_connection_string
```

### Frontend (optional .env file)
```
BACKEND_URL=http://localhost:3000  # Default if not set
```

## Data Collections

The application uses two MongoDB collections:
1. **form_data** - Stores user registration information (name, email)
2. **todo_items** - Stores to-do items (itemId, itemName, itemDescription)

## Technologies Used

- **Backend**: Flask, PyMongo, Python-dotenv, Flask-CORS
- **Frontend**: Flask, HTML, CSS, Requests
- **Database**: MongoDB Atlas
- **Containerization**: Docker, Docker Compose
- **Styling**: Custom CSS with Google Fonts (Inter)
- **Responsive Design**: Mobile-friendly interface

## Data Flow

1. **User Interface**: Combined form served by frontend Flask application
2. **Form Submission**: 
   - Registration data sent to `/submit` endpoint
   - To-do data sent to `/add_todo` endpoint
3. **Data Storage**: Backend saves data to appropriate MongoDB collections
4. **Data Retrieval**: `/api` endpoint fetches and returns registration data
5. **API Access**: Frontend provides proxy access to backend API

## Development Notes

- The application uses separate collections for different data types
- CORS is enabled to allow frontend-backend communication
- Error handling is implemented for database operations
- Responsive design ensures good user experience on mobile devices
- Environment variables provide flexible configuration

## Future Enhancements

- Add to-do item listing and management functionality
- Implement user authentication
- Add data validation and sanitization
- Include unit tests
- Add delete/update operations for to-do items
- Implement real-time updates with WebSockets
