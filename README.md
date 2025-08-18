# IntelliDesign AI

This is the monorepo for the IntelliDesign AI project, an AI-native design platform.

## Project Vision

IntelliDesign AI empowers teams to go from idea to high-fidelity, code-ready mockups in minutes. It's a collaborative space where product managers, designers, and developers can seamlessly generate, refine, and export UI/UX designs using natural language, sketches, or existing application screenshots.

## Project Structure

This repository is a monorepo containing the frontend and backend services.

-   `response.json`: The original AI-generated project plan and architecture document.
-   `frontend/`: The Next.js frontend application. This is the main user interface for the design canvas and editor.
-   `backend/`: Contains all the backend microservices.
    -   `api-gateway/`: A NestJS application that acts as the main entry point for all API requests. It routes traffic to the appropriate downstream service.
    -   `ai-service/`: A Python/FastAPI application responsible for all AI-related tasks, including text-to-wireframe generation and AI design suggestions.

## Getting Started

**Note:** The following setup requires Node.js (v18+) and Python (v3.9+) to be installed.

### Frontend Setup

To run the frontend application:

```bash
# Navigate to the frontend directory
cd frontend

# Install dependencies
npm install

# Run the development server
npm run dev
```
The application should now be running on `http://localhost:3000`.

### Backend Setup

Each backend service must be run in its own terminal session.

**1. API Gateway:**
```bash
# Navigate to the API Gateway directory
cd backend/api-gateway

# Install dependencies
npm install

# Run the development server
npm run start:dev
```
The API Gateway will be running on `http://localhost:3001`.

**2. AI Service:**
```bash
# Navigate to the AI Service directory
cd backend/ai-service

# Create a virtual environment (recommended)
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`

# Install dependencies
pip install -r requirements.txt

# Run the development server
uvicorn main:app --reload
```
The AI Service will be running on `http://localhost:8000`.

---

## Getting Started with Docker (Recommended)

For a much simpler setup, you can use Docker to run the entire application with a single command. This is the recommended approach for local development.

### Prerequisites

-   [Docker](https://docs.docker.com/get-docker/)
-   [Docker Compose](https://docs.docker.com/compose/install/)

### Launching the Application

1.  **Clone the repository** (if you haven't already).

2.  **Navigate to the root of the project** and run the following command:
    ```bash
    docker-compose up --build
    ```
    This command will:
    -   Build the Docker images for the `frontend`, `api-gateway`, and `ai-service`.
    -   Start the containers for all three services.
    -   Show the logs from all services in your terminal.

3.  **Access the services:**
    -   **Frontend:** [http://localhost:3000](http://localhost:3000)
    -   **API Gateway:** [http://localhost:3001](http://localhost:3001)
    -   **AI Service:** [http://localhost:8000/docs](http://localhost:8000/docs) (for FastAPI Swagger UI)

To stop the application, press `Ctrl+C` in the terminal where `docker-compose` is running.
