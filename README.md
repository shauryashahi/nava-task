# Nava Organization Management API Task

## Problem Statement
Create REST APIs in FastAPI for Organization management with dynamic database creation and JWT authentication.

### Required Endpoints

#### 1. Create Organization
- **Endpoint:** `POST /api/v1/org/create`
- **Function:** Creates an organization and its admin user, with a dedicated database
- **Payload:**
  ```json
  {
      "name": "My Organization",
      "admin_email": "admin@example.com",
      "admin_password": "secure_password"
  }
  ```

#### 2. Get Organization
- **Endpoint:** `GET /api/v1/org/{organization_name}`
- **Authentication:** Requires JWT token
- **Headers:** `Authorization: Bearer <token>`

#### 3. Admin Login
- **Endpoint:** `POST /api/v1/admin/login`
- **Payload:**
  ```json
  {
      "email": "admin@example.com",
      "password": "secure_password"
  }
  ```
- **Response:** JWT token

## Implementation Details

### Key Features
- ✨ Separate database for each organization
- 🔐 Secure password hashing
- 🎫 JWT authentication
- 🐳 Docker setup
- 🐘 PostgreSQL database
- 🌐 CORS middleware enabled
- 📚 OpenAPI documentation (Swagger UI)

## Getting Started

### Prerequisites
- Docker
- Docker Compose

### Running the Application
1. Clone the repository
2. Navigate to the project directory
3. Run:
   ```bash
   docker-compose up --build
   ```
4. Access the API at `http://localhost:8000`
5. View API documentation at `http://localhost:8000/docs`

### Testing the APIs
1. Create an organization:
   ```bash
   curl -X POST "http://localhost:8000/api/v1/org/create" \
   -H "Content-Type: application/json" \
   -d '{"name": "My Organization", "admin_email": "admin@example.com", "admin_password": "secure_password"}'
   ```

2. Login as admin:
   ```bash
   curl -X POST "http://localhost:8000/api/v1/admin/login" \
   -H "Content-Type: application/json" \
   -d '{"email": "admin@example.com", "password": "secure_password"}'
   ```

3. Get organization details:
   ```bash
   curl "http://localhost:8000/api/v1/org/My Organization" \
   -H "Authorization: Bearer <your_jwt_token>"
   ```