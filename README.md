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