# 🔐 Task API Authentication

> A production-style authentication REST API built with **FastAPI** and **Supabase Auth**, implementing user registration, login, Bearer token authentication, protected routes, logout, API health checks, and interactive Swagger documentation.

---

## 🚀 Overview

**Task API Authentication** is a backend authentication project developed using **Python, FastAPI, and Supabase Auth**.

The project demonstrates how to build a secure and structured REST API with authentication and authorization. Users can register and log in through Supabase Authentication, receive an access token, and use that token to access protected API endpoints.

The API also provides automatic **Swagger/OpenAPI documentation**, making it easy to test and understand the available endpoints.

### 🎯 Project Goals

- Build a clean REST API using FastAPI
- Implement user registration and login
- Integrate Supabase Authentication
- Implement Bearer token authentication
- Protect API routes using FastAPI dependencies
- Implement logout functionality
- Manage credentials securely using environment variables
- Test APIs using Swagger UI and PowerShell
- Maintain a professional GitHub-ready backend structure

---

## ✨ Features

- 🔐 User registration with Supabase Auth
- 🔑 Email/password login
- 🎟️ Bearer access-token authentication
- 🛡️ Protected API endpoints
- 👤 Authenticated user profile
- 🚪 Logout functionality
- 🌐 Public API endpoints
- ❤️ Health check endpoint
- 🔌 Supabase connectivity check
- 📚 Interactive Swagger UI
- 📄 Automatic OpenAPI documentation
- ✅ Pydantic request validation
- 🔒 Environment-based configuration
- 🧹 Clean project structure
- 📝 API testing documentation
- 📸 Authentication workflow screenshots

---

## 🛠️ Tech Stack

| Technology | Purpose |
|------------|---------|
| **Python 3.10+** | Backend programming |
| **FastAPI** | REST API framework |
| **Supabase Auth** | Authentication and user management |
| **JWT / Bearer Token** | API authorization |
| **Pydantic** | Request validation |
| **Uvicorn** | ASGI server |
| **python-dotenv** | Environment configuration |
| **Swagger / OpenAPI** | API documentation and testing |
| **Git & GitHub** | Version control |

---

# 📁 Project Structure

```text
task-api-auth-main-clean/
│
├── auth.py
├── config.py
├── dependencies.py
├── main.py
├── requirements.txt
│
├── .env.example
├── .gitignore
├── .gitattributes
├── README.md
│
└── screenshots/
    ├── login_request.png
    ├── login_response.png
    ├── logout.png
    ├── post_logout.png
    ├── protected_profile.png
    ├── signup_request.png
    ├── signup_response.png
    ├── supabase_users.png
    └── swagger_ui.png
```

### 📄 File Responsibilities

| File | Responsibility |
|------|----------------|
| `main.py` | Creates the FastAPI application and defines main API routes |
| `auth.py` | Handles signup, login, and logout operations |
| `config.py` | Loads environment variables and initializes Supabase |
| `dependencies.py` | Verifies Bearer access tokens for protected routes |
| `requirements.txt` | Contains project dependencies |
| `.env.example` | Template for required environment variables |
| `.gitignore` | Prevents sensitive/local files from being committed |
| `screenshots/` | Contains API testing and authentication screenshots |
| `README.md` | Project documentation |

---

# 🔄 Authentication Architecture

```text
                     ┌─────────────────────┐
                     │        Client       │
                     └──────────┬──────────┘
                                │
                                │ POST /signup
                                ▼
                     ┌─────────────────────┐
                     │    FastAPI API      │
                     └──────────┬──────────┘
                                │
                                ▼
                     ┌─────────────────────┐
                     │    Supabase Auth    │
                     │    Create User      │
                     └──────────┬──────────┘
                                │
                                │
                                │ POST /login
                                ▼
                     ┌─────────────────────┐
                     │    Access Token     │
                     └──────────┬──────────┘
                                │
                                │ Authorization:
                                │ Bearer <token>
                                ▼
                     ┌─────────────────────┐
                     │ Protected Endpoint  │
                     │ /protected/profile  │
                     └──────────┬──────────┘
                                │
                                ▼
                     ┌─────────────────────┐
                     │ Authenticated User  │
                     └─────────────────────┘
```

---

# 🌐 API Endpoints

## 🟢 Public Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| `GET` | `/` | API welcome message |
| `GET` | `/health` | API health check |
| `GET` | `/test-supabase` | Supabase connectivity check |
| `POST` | `/signup` | Register a new user |
| `POST` | `/login` | Authenticate a user |
| `GET` | `/public/info` | Public API information |

## 🔴 Protected Endpoints

| Method | Endpoint | Authentication | Description |
|--------|----------|----------------|-------------|
| `GET` | `/protected/profile` | Bearer Token | Returns authenticated user information |
| `POST` | `/logout` | Bearer Token | Logs out the authenticated user |

---

# 🔐 Authentication Flow

### 1️⃣ Signup

The user sends an email and password to:

```text
POST /signup
```

Example request:

```json
{
  "email": "user@example.com",
  "password": "your-password"
}
```

Supabase Auth creates the user account.

---

### 2️⃣ Login

The user authenticates through:

```text
POST /login
```

Example request:

```json
{
  "email": "user@example.com",
  "password": "your-password"
}
```

A successful login returns an authentication session containing an access token.

---

### 3️⃣ Access Protected Route

The access token is sent using the HTTP Authorization header:

```text
Authorization: Bearer <access_token>
```

The protected endpoint is:

```text
GET /protected/profile
```

The API verifies the token before returning the authenticated user's information.

---

### 4️⃣ Logout

The authenticated user can log out through:

```text
POST /logout
```

The request requires a valid Bearer token.

---

# ⚙️ Installation & Setup

## Prerequisites

Make sure you have:

- Python 3.10 or newer
- Git
- VS Code or another code editor
- A Supabase project

---

## 1. Clone the Repository

```powershell
git clone <YOUR_GITHUB_REPOSITORY_URL>
```

Move into the project directory:

```powershell
cd task-api-auth-main-clean
```

---

## 2. Create a Virtual Environment

Create the environment:

```powershell
python -m venv .venv
```

Activate it:

```powershell
.\.venv\Scripts\Activate.ps1
```

After activation, your terminal should show:

```text
(.venv)
```

---

## 3. Install Dependencies

Upgrade pip:

```powershell
python -m pip install --upgrade pip
```

Install the project dependencies:

```powershell
pip install -r requirements.txt
```

---

# 🔑 Supabase Configuration

Create a local `.env` file from the example file:

```powershell
Copy-Item .env.example .env
```

Open `.env` and configure your Supabase project:

```env
SUPABASE_URL=https://your-project.supabase.co
SUPABASE_KEY=your-supabase-key
```

Use the appropriate API key provided by your Supabase project.

### ⚠️ Security Warning

**Never commit `.env` to GitHub.**

The project `.gitignore` is configured to exclude environment files and sensitive credentials.

Do not hard-code Supabase credentials inside Python source files.

---

# ▶️ Running the Application

Start the FastAPI development server:

```powershell
python -m uvicorn main:app --reload
```

The API will run at:

```text
http://127.0.0.1:8000
```

Expected output:

```text
INFO:     Uvicorn running on http://127.0.0.1:8000
```

---

# 📚 Swagger API Documentation

FastAPI automatically generates interactive API documentation.

### Swagger UI

Open:

```text
http://127.0.0.1:8000/docs
```

### OpenAPI JSON

Open:

```text
http://127.0.0.1:8000/openapi.json
```

Swagger UI allows you to:

- View all API endpoints
- Inspect request parameters
- View request/response schemas
- Test API endpoints
- Authenticate using Bearer tokens
- Test protected endpoints
- Explore the OpenAPI specification

---

# 🧪 API Testing

## API Home

```powershell
curl.exe http://127.0.0.1:8000/
```

Expected response:

```json
{
  "message": "Task API Authentication Running"
}
```

---

## Health Check

```powershell
curl.exe http://127.0.0.1:8000/health
```

Expected response:

```json
{
  "status": "healthy"
}
```

---

## Supabase Connectivity

```powershell
curl.exe http://127.0.0.1:8000/test-supabase
```

Expected response:

```json
{
  "message": "Supabase connected"
}
```

---

## Public Information

```powershell
curl.exe http://127.0.0.1:8000/public/info
```

---

## Swagger Status Check

```powershell
curl.exe -s -o NUL -w "HTTP Status: %{http_code}`n" http://127.0.0.1:8000/docs
```

Expected:

```text
HTTP Status: 200
```

---

## OpenAPI Status Check

```powershell
curl.exe -s -o NUL -w "HTTP Status: %{http_code}`n" http://127.0.0.1:8000/openapi.json
```

Expected:

```text
HTTP Status: 200
```

---

# 🧑‍💻 Testing Protected Routes with Swagger

To test the protected profile endpoint:

### Step 1

Open:

```text
http://127.0.0.1:8000/docs
```

### Step 2

Execute:

```text
POST /signup
```

Create a test account.

### Step 3

Execute:

```text
POST /login
```

Copy the returned access token.

### Step 4

Click:

```text
Authorize
```

Enter your Bearer token.

```text
Bearer <access_token>
```

### Step 5

Execute:

```text
GET /protected/profile
```

The API should return the authenticated user's information.

---

# 📸 Project Screenshots

The repository contains screenshots demonstrating the authentication workflow and API testing.

## Swagger UI

![Swagger UI](screenshots/swagger_ui.png)

## Signup Request

![Signup Request](screenshots/signup_request.png)

## Signup Response

![Signup Response](screenshots/signup_response.png)

## Login Request

![Login Request](screenshots/login_request.png)

## Login Response

![Login Response](screenshots/login_response.png)

## Protected Profile

![Protected Profile](screenshots/protected_profile.png)

## Logout

![Logout](screenshots/logout.png)

## Post Logout

![Post Logout](screenshots/post_logout.png)

## Supabase Users

![Supabase Users](screenshots/supabase_users.png)

---

# 🛡️ Security Practices

This project follows basic backend security practices:

- 🔒 Credentials are stored in environment variables.
- 🚫 `.env` is excluded from Git.
- 🔑 Protected routes require Bearer authentication.
- 🎟️ Access tokens are used for authorization.
- 🧩 Authentication logic is separated from the main application.
- 🔐 Supabase manages user authentication.
- 🚫 Sensitive credentials are not hard-coded.
- ⚠️ Supabase service-role keys must never be exposed publicly.
- 🌐 HTTPS should be used in production.
- 🔑 Access tokens should be handled securely.

---

# 🧠 Backend Concepts Demonstrated

This project provides practical experience with:

- REST API development
- FastAPI
- API routing
- HTTP methods
- Request validation
- Pydantic models
- Authentication
- Authorization
- JWT / Bearer tokens
- FastAPI dependency injection
- Supabase Authentication
- Environment variables
- Secure configuration
- Swagger UI
- OpenAPI
- API testing
- Git and GitHub
- Backend project organization

---

# 📈 Learning Outcomes

Through this project, I gained hands-on experience in:

- Building REST APIs with FastAPI
- Structuring a backend application
- Creating authentication endpoints
- Implementing user signup and login
- Working with authentication tokens
- Protecting API routes
- Using FastAPI dependencies
- Integrating Supabase Auth
- Managing environment variables
- Validating API requests
- Testing APIs through Swagger UI
- Working with OpenAPI documentation
- Debugging backend configuration issues
- Managing Python dependencies
- Using Git for version control
- Preparing a professional backend project for GitHub

---

# 🔮 Future Improvements

The project can be extended with:

- [ ] Complete CRUD task management
- [ ] User-specific task ownership
- [ ] Role-based access control
- [ ] Automated unit tests
- [ ] Integration tests
- [ ] API rate limiting
- [ ] Structured logging
- [ ] Docker containerization
- [ ] CI/CD using GitHub Actions
- [ ] Cloud deployment
- [ ] Production monitoring
- [ ] API versioning
- [ ] Improved error handling

---

# 📌 Project Highlights

| Area | Implementation |
|------|----------------|
| Backend Framework | FastAPI |
| Authentication | Supabase Auth |
| Authorization | Bearer Token |
| API Documentation | Swagger / OpenAPI |
| Validation | Pydantic |
| Configuration | Environment Variables |
| Server | Uvicorn |
| Testing | Swagger + cURL |
| Version Control | Git / GitHub |

---

# 👨‍💻 Author

## Kishore R

**B.Tech Information Technology**

Interested in:

**Backend Development • Python • FastAPI • SQL • Data Analytics • Generative AI**

---
