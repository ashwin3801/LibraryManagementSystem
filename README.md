# Library Management System


A full-stack web application built with **Flask** and **MySQL** to efficiently manage library operations — including book inventory, user registrations, and admin controls — with a clean and responsive frontend.

![Library Management System](https://github.com/shreyansh378/library-management-system/blob/master/ss/ss2.JPG?raw=true)

---

## 🚀 Features

- 🔐 **Admin & User Authentication** — Separate login flows for administrators and members
- 📖 **Book Management** — Add, edit, view, and delete books from the inventory
- 👥 **User Management** — Register new members and manage existing ones
- 🔍 **Book Search** — Search and browse available books
- 📋 **Book Issue & Return** — Track borrowing and returning transactions
- 🎨 **Responsive Frontend** — Updated UI built with Bootstrap and custom CSS

---

## 🛠️ Tech Stack

| Layer      | Technology                     |
|------------|-------------------------------|
| Backend    | Python 3, Flask                |
| Frontend   | HTML5, Jinja2, Bootstrap, CSS  |
| Database   | MySQL                          |
| ORM/DB Layer | Custom DAO (Data Access Objects) |

---

## 📁 Project Structure

```
library-management-system/
│
├── App/                    # Core application logic
│   ├── Actor.py
│   ├── Admin.py
│   ├── Books.py
│   └── User.py
│
├── Controllers/            # Business logic controllers
│   ├── AdminManager.py
│   ├── BookManager.py
│   └── UserManager.py
│
├── Models/                 # Database access layer (DAO)
│   ├── AdminDAO.py
│   ├── BookDAO.py
│   ├── UserDAO.py
│   └── DB.py
│
├── routes/                 # Flask route definitions
│   ├── admin.py
│   ├── book.py
│   └── user.py
│
├── templates/              # Jinja2 HTML templates
│   ├── admin/
│   │   ├── books/
│   │   └── home.html
│   ├── shared/
│   │   └── layout.html
│   ├── home.html
│   ├── signin.html
│   ├── signup.html
│   └── welcome.html
│
├── static/                 # Static assets
│   ├── style.css
│   ├── home.css
│   ├── bootstrap.min.css
│   └── images/
│
├── db/
│   └── lms.sql             # MySQL database schema
│
├── app.py                  # Flask app entry point
├── requirements.txt
└── README.md
```

---

## ⚙️ Prerequisites

Make sure you have the following installed on your system:

- [Python 3.x](https://www.python.org/downloads/)
- [MySQL Server](https://dev.mysql.com/downloads/mysql/)
- [pip](https://pip.pypa.io/en/stable/)
- Git

---

## 📦 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/shreyansh378/library-management-system.git
cd library-management-system
```

### 2. Create a Virtual Environment (Recommended)

```bash
python -m venv venv
source venv/bin/activate        # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🗄️ Database Setup

### 1. Start your MySQL server and log in:

```bash
mysql -u root -p
```

### 2. Create the database and import the schema:

```sql
CREATE DATABASE lms;
USE lms;
SOURCE db/lms.sql;
```

> 💡 Make sure to update your database credentials in the DB configuration file (`Models/DB.py`) before running the app.

---

## 🔧 Set Environment Variables

```bash
export FLASK_APP=app.py
export FLASK_ENV=development
```

On **Windows (Command Prompt)**:

```cmd
set FLASK_APP=app.py
set FLASK_ENV=development
```

On **Windows (PowerShell)**:

```powershell
$env:FLASK_APP = "app.py"
$env:FLASK_ENV = "development"
```

---

## ▶️ Run the Application

```bash
flask run
```

Or alternatively:

```bash
python -m flask run
```

The application will be available at: **http://127.0.0.1:5000**

---

## 🖼️ Screenshots

| Page | Preview |
|------|---------|
| Home / Welcome | ![Home](ss/s1.png) |
| Dashboard | ![Dashboard](ss/ss2.JPG) |

---

## 👤 Default Admin Credentials

> ⚠️ Change these credentials after your first login.

```
Username: admin
Password: admin
```

---

## 🤝 Contributing

Contributions are welcome! To contribute:

1. Fork the repository
2. Create a new branch: `git checkout -b feature/your-feature-name`
3. Make your changes and commit: `git commit -m "Add: your feature description"`
4. Push to your branch: `git push origin feature/your-feature-name`
5. Open a Pull Request

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

---

## 🙌 Acknowledgements

- [Flask Documentation](https://flask.palletsprojects.com/)
- [Bootstrap](https://getbootstrap.com/)
- [MySQL](https://www.mysql.com/)
