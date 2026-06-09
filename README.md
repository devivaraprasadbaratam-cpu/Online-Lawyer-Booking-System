# Online Lawyer Booking System

## Overview

The Online Lawyer Booking System is a web-based application developed using Django and MySQL. The system provides an online platform where clients can search lawyers, book appointments, access legal services, upload and download documents, submit queries, and provide feedback. Lawyers can manage bookings, services, files, and client communication. Administrators can manage the overall system.

---

## Features

### Admin Module
- Admin Login
- View Clients
- View Lawyers
- Add Notifications
- View Notifications

### Lawyer Module
- Lawyer Registration & Login
- Manage Profile
- View Client Bookings
- Approve / Reject Bookings
- Add Legal Services
- Upload Case Files
- Reply to Queries
- View Feedback

### Client Module
- Client Registration & Login
- Search Lawyers
- Book Lawyers
- Book Services
- Download Files
- Submit Queries
- Provide Feedback
- View Notifications

---

## Technologies Used

- Python
- Django
- MySQL
- HTML
- CSS
- Bootstrap
- JavaScript
- PyCharm

---

## Database Tables

- client
- lawyer
- book_lawyer
- services
- add_feedback
- add_queries
- notifications
- manage

---

## System Architecture

Client Browser
↓
Django Application
↓
MySQL Database

---

## Screenshots

Screenshots are available in the screenshots folder.

---

## Installation

1. Clone the repository

git clone https://github.com/devivaraprasadbaratam-cpu/Online-Lawyer-Booking-System.git

2. Navigate to project folder

cd Online-Lawyer-Booking-System

3. Install dependencies

pip install -r requirements.txt

4. Configure MySQL database

5. Run migrations

python manage.py migrate

6. Start server

python manage.py runserver

---

## Author

Devi Vara Prasad Baratam

GitHub:
https://github.com/devivaraprasadbaratam-cpu