# Django Diaries - Learning Project

A comprehensive Django learning project covering various Django concepts including forms, models, templates, URL routing, database operations, and more.

> 📌 **Important Note**  
> Unlike typical Django projects, this repository intentionally contains the **entire virtual environment (`myenv/`)**, because the actual Django project folder (`myproject/`) exists *inside* the virtual environment.  
> This setup is kept as-is for learning and backup purposes.

---

## 📚 Learning Resources

- **GitHub Repository**: https://github.com/Raghavgupta2003/Django_Diaries.git  
- **YouTube Tutorial**: https://www.youtube.com/watch?v=6mv9VtMbRmM

---

## 🚀 Prerequisites

Before you begin, ensure the following are installed:

- **Python** (3.8 or higher)
- **pip** (Python package installer)
- **Git** (optional, for cloning)

---

## 📋 Step-by-Step Setup Guide

### Step 1: Clone or Download the Repository

```bash
git clone https://github.com/Raghavgupta2003/Django_Diaries.git
cd Django_Diaries
```

Or download the ZIP file and extract it.

---

## ⚠️ IMPORTANT: Project Inside Virtual Environment

Your structure looks like this:

```
Django_practice/
└── myenv/
     └── myproject/
```

The **Django project is located inside the virtual environment folder**.

For this project, no new venv is required — it is already included.

---

### Step 2: Activate the Included Virtual Environment

**On Windows (PowerShell):**
```powershell
.\myenv\Scripts\Activate.ps1
```

**On Windows (CMD):**
```cmd
myenv\Scripts\activate.bat
```

**On macOS/Linux:**
```bash
source myenv/bin/activate
```

Once activated, you should see `(myenv)` in the terminal.

---

### Step 3: Navigate to the Django Project Directory

Because the actual project is inside `myenv/myproject`, run:

**Windows:**
```bash
cd myenv\myproject
```

**macOS/Linux:**
```bash
cd myenv/myproject
```

---

### Step 4: Run Database Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

---

### Step 5: Create a Superuser (Optional)

```bash
python manage.py createsuperuser
```

---

### Step 6: Run the Development Server

```bash
python manage.py runserver
```

Server runs at:  
➡ http://127.0.0.1:8000/

---

## 📁 Project Structure

```
Django_practice/
├── myenv/                          # Virtual environment (intentionally included)
│   └── myproject/                  # Django project
│       ├── manage.py
│       ├── db.sqlite3
│       ├── images/
│       ├── myapp/
│       │   ├── migrations/
│       │   ├── templates/
│       │   ├── admin.py
│       │   ├── apps.py
│       │   ├── forms.py
│       │   ├── models.py
│       │   ├── urls.py
│       │   └── views.py
│       └── myproject/
│           ├── settings.py
│           ├── urls.py
│           ├── wsgi.py
│           └── asgi.py
└── README.md
```

---

## 🎯 Features Covered

### 1. Basic Views and URLs
- Dynamic routing
- Regex URLs
- Query parameters

### 2. Templates
- Rendering
- Inheritance
- Passing data

### 3. Forms
- HTML forms
- Django forms
- Validation
- File uploads
- Model forms

### 4. Models
- User signup
- Blog post model
- Employee model
- CRUD operations

### 5. Advanced Topics
- Cookies
- Sessions
- PRG pattern
- Error handling
- Image uploads

---

## 🔗 Key URLs

- `/hello/`
- `/home/`
- `/greet/<name>/`
- `/recipe/?food=<food_name>`
- `/calculator/?num1=&num2=&operation=`
- `/simpleform/`
- `/djangoform/`
- `/validation/`
- `/signup/`
- `/signup2/`
- `/blogpost/`
- `/blogposts/`
- `/set-cookie/`
- `/get-cookie/`
- `/set-session/`
- `/get-session/`
- `/admin/`

---

## 🛠️ Troubleshooting

### `ModuleNotFoundError: No module named 'django'`
✔ Make sure the included virtual environment is activated.

### `Port 8000 already in use`
```bash
python manage.py runserver 8001
```

### Migration issues
```bash
python manage.py makemigrations
python manage.py migrate
```

---

## 📝 Notes

- The virtual environment (`myenv/`) is intentionally included.
- Project uses SQLite (no setup required).
- Designed for Django learning and experimentation.

---

## 🤝 Contributing

Feel free to fork and experiment!

---

## 📄 License

This project is for educational purposes only.

---

**Happy Learning! 🎉**
