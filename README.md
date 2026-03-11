# Token Auth API

This project is a backend REST API developed with **Python** and **Django** that implements **token-based authentication**.

## Features

* User authentication with tokens
* Secure API endpoints
* Environment variable configuration
* Automated tests for authentication and API endpoints

---

# Project Setup

## 1. Clone the repository

```bash
git clone https://github.com/cerencilt/token-auth-api.git
cd token-auth-api
```

## 2. Create and activate a virtual environment

```bash
python -m venv venv
```

Activate the virtual environment:

Windows:

```bash
venv\Scripts\activate
```

Mac / Linux:

```bash
source venv/bin/activate
```

## 3. Install dependencies

```bash
pip install -r requirements.txt
```

## 4. Setup environment variables

Copy the sample environment file:

```powershell
copy .env.sample .env
```

Open the `.env` file and replace the following value with your own Django secret key:

```
SECRET_KEY=your-secret-key-goes-here
```

## 5. Run the project

```bash
python manage.py runserver
```

The API will be available at:

```
http://127.0.0.1:8000/
```

---

# Running Tests

The project includes automated tests to verify authentication and API endpoints.

Run the tests with:

```bash
python manage.py test
```

---

# Technologies Used

* Python
* Django
* Django REST Framework
* Token Authentication
