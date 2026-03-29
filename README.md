# 🏥 Hospital Patient Management System

A robust and lightweight REST API for managing hospital patient records, built with **FastAPI** and **SQLite3**.

## 🚀 Features
- **Full CRUD Support**: Create, Read, Update, and Delete patients.
- **Data Validation**: Strict data typing and validation using Pydantic.
- **Database Integration**: Persistent storage using SQLite.
- **Interactive Documentation**: Auto-generated Swagger UI for testing.

## 🛠️ Tech Stack
- **Backend**: FastAPI (Python)
- **Database**: SQLite3
- **Web Server**: Uvicorn
- **Validation**: Pydantic

## 📂 Project Structure
- `patients.py`: The main entry point containing API routes and server logic.
- `hospital_database.py`: Database configuration and table initialization.
- `requirements.txt`: List of necessary Python libraries.

## ⚙️ Installation & Setup

To get the application up and running, execute the following commands:

```bash
pip install fastapi uvicorn
python patients.py
