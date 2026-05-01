# Technical Documentation: Django AI-Integrated Profile System

## 1. Project Overview
This project is a Django-based web application developed during the internship program. The primary goal is to implement a complete user authentication lifecycle, integration with a local Large Language Model (LLM) for personalized description generation, and automation of background processes.

## 2. System Architecture
The project is built on a modular principle with a clear separation of concerns:

### A. Client Level
* **Browser**: Interacts with the server via standard HTTP requests.
* **Frontend**: A set of HTML templates utilizing the Django Template Language.

### B. Core System (Django App)
* **Django Engine**: Manages routing and request processing.
* **Logic: Views/Forms**: Implementation of business logic using Function-Based Views (FBVs) with access control decorators.
* **Auth Module**: 
    * **Basic Auth**: Standard registration (Username, Email, Password).
    * **GitHub OAuth**: Integration via `django-allauth` for social media authentication.
    * **Password Reset**: A complete access recovery cycle via SMTP.

### C. Database (SQLite)
* **SQLite** is utilized for development convenience and portability.
* **Models**:
    * `User`: A custom model (`AbstractUser`) for flexible data management.
    * `UserProfile`: A OneToOne-linked model for storing metadata (age, location, interests, AI-generated description).
    * `UserFriends`: A model for implementing social connections between users.
* **Signals**: Automatic profile creation and synchronization upon user registration via `post_save`.

### D. AI Module
* **Ollama (Llama 3.2)**: A local LLM runtime that performs text generation without relying on third-party APIs.
* **LangChain**: Used as an orchestrator to manage system prompts and structure LLM queries.
* **Throttling Logic**: Implemented a backend-level rate-limiting mechanism (3 generations per hour / 1 per 20 min) using Django Cache.

### E. Background Processes
* **Redis**: Acts as the message broker.
* **Celery Worker**: An isolated process for handling "heavy" tasks.
* **Email Service**: Asynchronous delivery of welcome emails and password reset links to ensure a non-blocking user experience.

## 3. Infrastructure and Deployment
The project is fully containerized using **Docker Compose**. The stack includes:
1. **Web**: Django application service (Runserver/Gunicorn).
2. **Redis**: In-memory data store.
3. **Celery**: Task queue worker.
4. **Ollama Connection**: Utilizes a special `host.docker.internal` host to bridge the containerized app with the local AI engine running on the host machine.

## 4. Setup Instructions
1. Install **Ollama** and download the model: `ollama run llama3.2`.
2. Create a `.env` file with necessary configurations (Email SMTP, Redis URL).
3. Execute the command: `docker-compose up --build`.
4. The project will be accessible at: `http://127.0.0.1:8000`.

---
*Documentation prepared by: Vitalii Lylo*