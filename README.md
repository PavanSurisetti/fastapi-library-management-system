# 📚 Library Management System API (FastAPI + PostgreSQL)

### A fast, scalable REST API for managing books, members, and borrowing operations using FastAPI and PostgreSQL.

---

## 🚀 Live Demo

🔗 **Live API:** [Library Management System API](https://fastapi-library-management-system-06wi.onrender.com?utm_source=chatgpt.com)

📄 **API Docs (Swagger UI):**
[API Documentation](https://fastapi-library-management-system-06wi.onrender.com/docs?utm_source=chatgpt.com)

> ⚠️ Hosted on Render free tier — first request may be slow due to cold starts.

---

## 🛠 Tech Stack

* **Backend Framework:** FastAPI
* **Database:** PostgreSQL
* **ORM:** SQLAlchemy
* **Server:** Uvicorn
* **Validation:** Pydantic
* **Deployment:** Render

---

## 💡 Features

* 📖 Add, view, and manage books
* 👤 Register and manage members
* 🔄 Borrow and return books system
* 📊 Track available copies in real-time
* 🧾 Borrow history per member
* ⚡ Fully RESTful API design
* 📄 Interactive Swagger documentation

---

## 📂 Project Structure

```
fastapi-library-management-system/
├── main.py              # API endpoints & business logic
├── models.py            # Database models (Book, Member, Borrow)
├── database.py         # DB connection & session setup
├── requirements.txt    # Dependencies
├── .env                # Environment variables
└── .gitignore          # Ignored files
```

---

## ⚙️ Database Models

### 📘 Book

* id
* title
* author
* total_copies
* available_copies

### 👤 Member

* id
* name
* email (unique)

### 🔄 Borrow

* id
* member_id (FK)
* book_id (FK)
* borrow_date
* return_date

---

## 🚀 Installation & Local Setup

### 1️⃣ Clone the repository

```bash
git clone https://github.com/PavanSurisetti/fastapi-library-management-system
```

### 2️⃣ Navigate to project

```bash
cd fastapi-library-management-system
```

### 3️⃣ Create virtual environment

```bash
python -m venv venv
```

**Activate:**

* Windows:

```bash
venv\Scripts\activate
```

* Mac/Linux:

```bash
source venv/bin/activate
```

### 4️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

### 5️⃣ Configure environment variables

Create `.env` file:

```env
DATABASE_URL=your_postgresql_connection_string
```

### 6️⃣ Run the server

```bash
uvicorn main:app --reload
```

### 7️⃣ Open API docs

```
http://127.0.0.1:8000/docs
```

---

## 🔗 API Endpoints

| Method | Endpoint              | Description           |
| ------ | --------------------- | --------------------- |
| GET    | `/`                   | Welcome message       |
| POST   | `/book`               | Add a new book        |
| GET    | `/Books`              | Get all books         |
| GET    | `/books/available`    | Get available books   |
| POST   | `/register`           | Register member       |
| GET    | `/memeber`            | Get all members       |
| POST   | `/borrow`             | Borrow a book         |
| POST   | `/return`             | Return a book         |
| GET    | `/borrowhistory/{id}` | Member borrow history |

---

## 🧠 How It Works

1. User sends request via API
2. FastAPI validates input using Pydantic
3. SQLAlchemy interacts with PostgreSQL
4. Business logic updates book/membership data
5. JSON response is returned

---

## 🚀 Deployment

* Hosted on **Render**
* Connected to **Neon PostgreSQL**
* Environment variables managed securely
* Auto-deploy from GitHub

---

## 🔮 Future Improvements

* JWT Authentication 🔐
* Role-based access (Admin/User)
* Book reservation system
* Pagination & filtering
* Docker containerization

---

## 📫 Contact

* GitHub: [PavanSurisetti](https://github.com/PavanSurisetti)
* LinkedIn: [Pavan Surisetti LinkedIn](https://www.linkedin.com/in/pavan-surisetti-b3281228b/)

---

## 📄 License

This project is licensed under the **MIT License**.

