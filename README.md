# UserAuth
## 🔐 Building a Secure and Scalable Authentication System with FastAPI & SQLAlchemy! 💻  

Here’s a quick overview of what it does:  

### 1️⃣ User Registration Endpoint  
Collects user details like name, email, and password.  
Validates uniqueness of the email in the database.  
Hashes passwords securely before storing them.  

### 2️⃣ Login Endpoint  
Validates email and password against database records.  
Generates a secure JWT access token upon successful login.  

### 3️⃣ MySQL Database Integration
Powered by SQLAlchemy for easy-to-manage models and queries.  


### Key Technologies:  
🔹 FastAPI – Fast, modern, and highly efficient Python framework.  
🔹 SQLAlchemy – Database ORM for seamless interaction with MySQL.  
🔹 Passlib & JWT – Ensuring secure user authentication.  
