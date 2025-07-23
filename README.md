# Flask Inventory Management System

A simple and educational **Inventory Management System** built using **Flask**, **MongoDB**, and **Vanilla JavaScript**. This project is ideal for beginners who want to explore full-stack development using Python on the backend and Bootstrap-powered frontend.

---

## 🚀 Features

* 🛒 Load **sample products** from a JSON file
* ➕ Add new products to the database
* 🔄 Update and delete existing products
* ✅ Apply batch quantity reductions (simulate checkout)
* 📦 View current inventory in a clean UI

---

## 🛠️ Tech Stack

* **Backend:** Flask, Flask-PyMongo, Python
* **Database:** MongoDB (Local or Cloud via MongoDB Atlas)
* **Frontend:** HTML, CSS (Bootstrap), JavaScript (Vanilla)

---

## 📁 Project Structure

```
flask_inventory/
│
├── app.py                  # Main Flask app
├── samples.json            # Sample products (used for testing checkout)
├── .env                    # Environment variables (e.g., MongoDB URI)
│
├── templates/
│   └── dashboard.html      # Main HTML dashboard (Jinja2 template)
│
├── static/
│   ├── style.css           # Optional: Custom styles
│   └── script.js           # Frontend logic (fetch, update, render)
```

---

## ⚙️ Setup Instructions

### 1. Clone the Repo

```bash
git clone https://github.com/obaidah3/flask-inventory.git
cd flask-inventory
```

### 2. Set up the Virtual Environment

```bash
python -m venv venv
# On Windows:
venv\Scripts\activate
# On Mac/Linux:
source venv/bin/activate
```

### 3. Install Requirements

```bash
pip install -r requirements.txt
```

### 4. Add your `.env` file

Create a file named `.env` in the root directory:

```
MONGO_URI=mongodb://localhost:27017/inventory_db
```

Or use your MongoDB Atlas connection string.

### 5. Run the App

```bash
python app.py
```

Open your browser at [http://127.0.0.1:5000](http://127.0.0.1:5000)

---

## 📸 Screenshots

<img width="1893" height="676" alt="Image" src="https://github.com/user-attachments/assets/3097892c-fff3-4baf-bf8f-95fa9f7efacb" />

<img width="1920" height="1080" alt="Image" src="https://github.com/user-attachments/assets/609b208c-ba5a-41c3-803c-141a070be369" />

<img width="1920" height="1080" alt="Image" src="https://github.com/user-attachments/assets/109b05f1-711b-45ae-bd70-fc9a8a6dfb54" />

<img width="1621" height="267" alt="Image" src="https://github.com/user-attachments/assets/33a86cf7-833a-4ee2-95ea-62c37dfd28d6" />

<img width="1920" height="1080" alt="Image" src="https://github.com/user-attachments/assets/a3dd9922-2e5a-4e95-9fde-f7857769bc16" />

<img width="1128" height="624" alt="Image" src="https://github.com/user-attachments/assets/3fe858ef-b3b0-423e-9b82-ca9a4754c224" />

---

## ✍️ Author

**Obaidah Essam**
CSIT & Embedded Systems Student | Automotive & IoT Enthusiast

---

## 📜 License

This project is open source and available under the [MIT License](LICENSE).

---

