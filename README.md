# SCTS-Backend  
Backend for the Student College Tour System (SCTS)  

## Table of Contents  
- [Overview](#overview)  
- [Features](#features)  
- [Technology Stack](#technology-stack)  
- [Getting Started](#getting-started)  
  - [Prerequisites](#prerequisites)  
  - [Installation](#installation)  
  - [Configuration](#configuration)  
  - [Running the Application](#running-the-application)  
- [API Endpoints](#api-endpoints)  
- [Folder Structure](#folder-structure)  
- [Contributing](#contributing)  
- [License](#license)  
- [Contact](#contact)  

## Overview  
The SCTS-Backend project provides the server-side functionality for the “Student College Tour System”, allowing college students and organisers to manage industrial visits, schedule tours, track attendance, and generate reports.  
This backend is built with Python and the Django web framework, and exposes RESTful APIs for the front-end application.

## Features  
- User authentication (admin, college-organiser, student)  
- Tour scheduling: create, update, list industrial visits  
- Attendance tracking and reporting  
- Notifications to students/organisers  
- Admin dashboard for data management  
- Secure APIs with role-based access control  

## Technology Stack  
- Python (3.x)  
- Django (latest stable release)  
- Django REST Framework  
- SQLite (for development)  
- HTML & CSS for simple templates (if required)  
- Git for version control  

## Getting Started  

### Prerequisites  
- Python 3.8+ installed  
- pip (Python package installer)  
- Git (to clone this repository)  
- (Optional) Virtual environment tool such as `venv` or `virtualenv`  

### Installation  
```bash
# Clone the repository
git clone https://github.com/GouriBiswas/SCTS-Backend.git
cd SCTS-Backend

# (Recommended) Create a virtual environment
python -m venv venv
source venv/bin/activate     # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
