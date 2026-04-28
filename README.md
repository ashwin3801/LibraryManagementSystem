# Library Management System


A full-stack web application built with **Flask** and **MySQL** to efficiently manage library operations — including book inventory, user registrations, and admin controls — with a clean and responsive frontend.

![Library Management System](https://github.com/shreyansh378/library-management-system/blob/master/ss/ss2.JPG?raw=true)

---

## 🚀 Features

- **Admin & User Authentication** — Separate login flows for administrators and members
- **Book Management** — Add, edit, view, and delete books from the inventory
- **User Management** — Register new members and manage existing ones
- **Book Search** — Search and browse available books
- **Book Issue & Return** — Track borrowing and returning transactions
- **Responsive Frontend** — Updated UI built with Bootstrap and custom CSS

---

## 🛠️ Tech Stack

| Layer      | Technology                     |
|------------|-------------------------------|
| Backend    | Python 3, Flask                |
| Frontend   | HTML5, Jinja2, Bootstrap, CSS  |
| Database   | MySQL                          |
| ORM/DB Layer | Custom DAO (Data Access Objects) |

---

## 📦 Installation



### 1. Create a Virtual Environment 

```bash
python -m venv venv
source venv/bin/activate        # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Set Environment Variables

```bash
export FLASK_APP=app.py
export FLASK_ENV=development
```

## ▶️ Run the Application

```bash
flask run
```

The application will be available at: **http://127.0.0.1:5000**

---

## Screenshots

| Page | Preview |
|------|---------|
| Home / Welcome | ![Home](ss/s1.png) |
| Dashboard | ![Dashboard](ss/ss2.JPG) |


