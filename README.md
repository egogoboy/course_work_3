# Examination System

A web-based examination management system developed as a second-year Software Engineering coursework project.

## Overview

### Project Objective

The objective of the project was to design and implement a web-based examination system that supports the complete examination workflow:

- examination creation and management by instructors;
- examination participation by students;
- automatic evaluation of objective questions;
- manual review and grading where required;
- role-based access to system functionality.

The system was developed as a university-oriented application with separate workflows for administrators, instructors, and students.

## Technologies

### Backend

- Python 3.10
- FastAPI
- SQLAlchemy
- Pydantic

### Frontend

- HTML
- CSS
- JavaScript

### Database

- SQLite

## Architecture

The application follows a client-server architecture. The frontend communicates with the backend through a REST API implemented with FastAPI.

```text
┌──────────────────────┐
│       Frontend       │
│    HTML/CSS/JS       │
└──────────┬───────────┘
           │ REST API
           ▼
┌──────────────────────┐
│       FastAPI        │
│      API Layer       │
├──────────────────────┤
│ Authentication / RBAC│
├──────────────────────┤
│     CRUD Layer       │
├──────────────────────┤
│      SQLAlchemy      │
└──────────┬───────────┘
           │
           ▼
┌──────────────────────┐
│       SQLite         │
└──────────────────────┘
```

The backend is organized into several logical layers and modules:

```text
backend/app/
├── crud/          # Database operations
├── database/      # Database configuration and initialization
├── models/        # ORM models and validation schemas
├── routes/
│   ├── api/       # REST API endpoints
│   └── frontend/  # Frontend-related routes
├── security/      # Authentication and role-based access control
├── utils/         # Shared utilities, dependencies and exceptions
└── main.py        # Application entry point
```

The separation of API routes by user role allows administrator, instructor, and student functionality to be maintained independently.

## Core Functionality

The system implements three user roles:

- **Administrator**
- **Instructor**
- **Student**

Access to application functionality is controlled using role-based access control (RBAC).

### Administrator

The administrator manages the entities required for operating the examination system:

- users;
- student groups;
- academic subjects.

Administrators can create, edit, and delete these entities.

User creation is intentionally restricted to administrators. This reflects the intended university-oriented deployment model, where access to the system is controlled rather than allowing arbitrary user registration.

### Instructor

Instructors are responsible for examination management and assessment.

They can:

- create and edit examinations;
- manage examination questions;
- associate examinations with subjects and student groups;
- filter examinations;
- review students' submitted answers;
- assign grades where manual assessment is required;
- view examination results.

### Student

Students can:

- view examinations available to them;
- filter available examinations;
- take examinations;
- submit answers;
- receive automatically calculated results;
- view their examination grades.

## Examination Model

The system currently supports two question types:

- **Single-choice questions** — evaluated automatically by comparing the submitted answer with the correct answer.
- **Open-ended questions** — submitted for instructor review and grading.

This combination allows the system to demonstrate both automated assessment and instructor-controlled evaluation.

## Authentication and Authorization

Authentication is implemented using **JSON Web Tokens (JWT)**.

The authorization model is based on **Role-Based Access Control (RBAC)**. API endpoints and application functionality are restricted according to the authenticated user's role.

Passwords are stored using password hashing rather than plain-text storage.

The security layer is separated from the application routes and contains dedicated authentication, configuration, and RBAC modules.

## Data Model

The application uses a relational data model implemented with SQLAlchemy ORM.

The main entities include:

- Users
- Student Groups
- Subjects
- Examinations
- Tasks / Questions
- Answers
- Student Answers
- Marks

The database schema uses foreign keys and ORM relationships to represent associations between these entities.

### Database Diagram

> **TODO:** Add an ER diagram of the database schema here.

```text
[Database ER Diagram]

<!-- Replace this section with the exported dbdiagram.io diagram -->
```

## API

The backend exposes a REST API through FastAPI.

API endpoints are organized according to their scope and user role:

```text
/api
├── /admin
├── /common
├── /student
└── /teacher
```

Common resources are separated from role-specific operations, while administrative and examination-related operations are protected by the corresponding authorization rules.

FastAPI also provides automatic API documentation, which can be used to inspect and interact with the available endpoints during development.

## Technology Selection

Python and the associated frameworks and libraries were selected primarily to enable rapid development within the limited timeframe of the coursework.

FastAPI was chosen as the backend framework because of its modern asynchronous architecture, type-hint-based development model, built-in request validation integration, and automatic API documentation.

SQLAlchemy was used as the ORM layer to represent the relational database model through Python classes and relationships. Pydantic was used for request and response schemas and data validation.

SQLite was selected because of its minimal deployment requirements and suitability for a small-scale educational application. It does not require a separate database server and stores the database in a single file.

For a production-oriented deployment, SQLite could be replaced with a server-based relational database such as PostgreSQL.

## Project Structure

The project is divided into backend and frontend components:

```text
course_work_3/
├── backend/
│   ├── app/
│   │   ├── core/
│   │   ├── crud/
│   │   ├── database/
│   │   ├── models/
│   │   ├── routes/
│   │   ├── security/
│   │   └── utils/
│   └── requirements.txt
│
├── frontend/
│   ├── static/
│   │   └── css/
│   └── templates/
│       ├── admin/
│       ├── student/
│       └── teacher/
│
├── LICENSE
└── README.md
```

## Screenshots

### Authentication

> **TODO:** Add login page screenshot.

### Administrator Dashboard

> **TODO:** Add administrator dashboard screenshot.

### Examination Management

> **TODO:** Add instructor examination management screenshot.

### Examination

> **TODO:** Add student examination screenshot.

### Results

> **TODO:** Add examination results screenshot.

## Running the Application

Clone the repository and install the required dependencies:

```bash
git clone https://github.com/egogoboy/course_work_3
cd course_work_3/backend

python3 -m venv env
source env/bin/activate

pip install -r requirements.txt

cd app
python -m uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```

After starting the server, open:

```text
http://localhost:8000/login
```

## Demo Accounts

The following accounts are provided for testing purposes.

### Administrator

```text
Login: admin
Password: admin
```

### Instructor

```text
Login: teacher
Password: teacher
```

### Student

```text
Login: student-23
Password: student-23
```

> **Note:** These credentials are intended exclusively for local demonstration and development.

## Testing

Automated unit tests were not implemented as part of the original coursework.

The application was primarily validated through manual testing of the main user workflows and interactions between the frontend, REST API, and database.

Automated testing would be a natural improvement for a future version of the project.

## Limitations and Possible Improvements

The project was developed as an academic coursework assignment and is not intended to represent a production-ready examination platform.

Potential improvements include:

- migration from SQLite to PostgreSQL;
- introduction of database migrations using Alembic;
- automated unit and integration testing;
- improved frontend architecture;
- more comprehensive input validation;
- additional examination and question types;
- improved deployment configuration;
- more extensive security hardening;
- containerization and production deployment.

## Project Context

This project was developed as a second-year Software Engineering coursework assignment.

Its primary purpose was to gain practical experience with:

- web application development;
- REST API design;
- relational database modeling;
- ORM-based data access;
- authentication and authorization;
- role-based application design;
- client-server architecture.

While the project is an educational application, it provided practical experience in designing and implementing a multi-role information system from database model to user interface.
