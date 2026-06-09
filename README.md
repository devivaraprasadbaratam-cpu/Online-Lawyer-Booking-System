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

### Home Page

![Home Page](screenshots/home_page.png)

### Client Lawyers

![Client Lawyers](screenshots/client_lawyers.png)

### Client Bookings

![Client Bookings](screenshots/client_bookings.png)

### Lawyer Dashboard

![Lawyer Dashboard](screenshots/lawyer_dashboard.png)

### View Bookings

![View Bookings](screenshots/view_booking.png)

### Manage Files

![Manage Files](screenshots/manage_files.png)

### Feedback Page

![Feedback Page](screenshots/feedback.png)

### Admin Dashboard

![Admin Dashboard](screenshots/admin_dashboard.png)

---

## Installation

### Clone Repository

```bash
git clone https://github.com/devivaraprasadbaratam-cpu/Online-Lawyer-Booking-System.git
```

### Navigate to Project Folder

```bash
cd Online-Lawyer-Booking-System
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run Migrations

```bash
python manage.py migrate
```

### Start Server

```bash
python manage.py runserver
```

---

## Project Modules

### Admin
Manages lawyers, clients, and notifications.

### Lawyer
Handles bookings, services, file uploads, and client communication.

### Client
Books lawyers, downloads files, submits feedback, and raises queries.

---

## Author

**Devi Vara Prasad Baratam**

GitHub Profile:

https://github.com/devivaraprasadbaratam-cpu