
# User Authentication Microservice

The **User Authentication Microservice** is a crucial component of the Habit Tracker App, designed to provide secure user authentication, including registration and login functionality. This microservice is built using FastAPI and ensures secure handling of user credentials.

## Features

- **User Registration:** Allow users to register with a username and password.
- **User Login:** Authenticate users and issue JWT tokens for secure access.
- **Dockerized Deployment:** Easily deploy the microservice using Docker.
- **Kubernetes Deployment:** Ready-to-use Kubernetes configuration for scalable deployments.

## Project Structure

```
user-authentication/
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── controllers/
│   │   ├── __init__.py
│   │   └── auth_controller.py
│   ├── models/
│   │   ├── __init__.py
│   │   └── user.py
│   ├── repositories/
│   │   ├── __init__.py
│   │   └── user_repository.py
│   ├── services/
│   │   ├── __init__.py
│   │   └── auth_service.py
│   ├── config.py
│   └── utils/
│       ├── __init__.py
│       └── logger.py
├── tests/
│   ├── __init__.py
│   └── test_auth_service.py
├── Dockerfile
├── kubernetes/
│   ├── deployment.yaml
│   ├── service.yaml
│   ├── configmap.yaml
│   └── secret.yaml
├── requirements.txt
└── README.md
```

## Getting Started

### Prerequisites

- Python 3.x
- Docker
- Kubernetes (optional, if you want to deploy it on a Kubernetes cluster)

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/user-authentication.git
   cd user-authentication
   ```

2. **Set up a virtual environment and install dependencies:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   pip install -r requirements.txt
   ```

3. **Run the FastAPI application locally:**
   ```bash
   uvicorn app.main:app --reload
   ```

   The application should now be running locally on `http://127.0.0.1:8000`.

### Docker

1. **Build the Docker image:**
   ```bash
   docker build -t user-authentication:latest .
   ```

2. **Run the Docker container:**
   ```bash
   docker run -d -p 8000:8000 user-authentication:latest
   ```

   The application should now be running in a Docker container and accessible at `http://127.0.0.1:8000`.

### Kubernetes

1. **Navigate to the kubernetes directory:**
   ```bash
   cd kubernetes/
   ```

2. **Deploy the application:**
   ```bash
   kubectl apply -f configmap.yaml
   kubectl apply -f secret.yaml
   kubectl apply -f deployment.yaml
   kubectl apply -f service.yaml
   ```

## Usage

### API Endpoints

- **POST /register**
  - Description: Register a new user.
  - Request Body:
    ```json
    {
      "username": "string",
      "password": "string"
    }
    ```

- **POST /login**
  - Description: Authenticate a user and issue a JWT token.
  - Request Body:
    ```json
    {
      "username": "string",
      "password": "string"
    }
    ```

### Example using `curl`

- **Register a new user:**
  ```bash
  curl -X POST "http://127.0.0.1:8000/register" -H "Content-Type: application/json" -d '{
    "username": "testuser",
    "password": "testpassword"
  }'
  ```

- **Login a user:**
  ```bash
  curl -X POST "http://127.0.0.1:8000/login" -H "Content-Type: application/json" -d '{
    "username": "testuser",
    "password": "testpassword"
  }'
  ```

## Testing

Run unit tests with:
```bash
pytest
```

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgements

- [FastAPI](https://fastapi.tiangolo.com/)
- [Docker](https://www.docker.com/)
- [Kubernetes](https://kubernetes.io/)

---
