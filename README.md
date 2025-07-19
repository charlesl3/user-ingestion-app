# User Ingestion App 🚀

A lightweight, production-ready data ingestion pipeline built with **Python**, **MySQL (Railway)**, and **Streamlit**. The app allows users to submit information via a simple web interface and stores it in a cloud-hosted MySQL database using Railway.

## 🔧 Features

- Streamlit-based web app for user input
- Cloud MySQL database integration (Railway)
- Modular database utility functions
- Easy to deploy and extend
- Docker- and cloud-friendly architecture

---

## 📁 Project Structure

```
├── Railway_MySQL_Connection_Guide.md   # Step-by-step guide for setting up Railway + MySQL
├── db_utils.py                         # Functions for connecting to and interacting with the MySQL DB
├── main.py                             # Entrypoint for CLI-style interactions or testing
├── requirements.txt                    # Dependencies
├── streamlit_app.py                    # Streamlit frontend app
```

---

## 🚀 Getting Started

### 0. Run the App (feel free to stop reading after doing this step -- just play around!)

[👉 Live Demo on Streamlit](https://user-ingestion-app.streamlit.app/)

### 1. Clone the Repo

```bash
git clone https://github.com/charlesl3/user-ingestion-app.git
cd user-ingestion-app
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Set Environment Variables

Create a `.env` file or export the following:

```bash
export DB_HOST=<your-host>
export DB_USER=<your-username>
export DB_PASSWORD=<your-password>
export DB_NAME=<your-database-name>
```

Or follow the instructions in [`Railway_MySQL_Connection_Guide.md`](./Railway_MySQL_Connection_Guide.md)

---

### 4. Run the Streamlit App

```bash
streamlit run streamlit_app.py
```

---

## 🛠️ Usage

Users can:

- Submit their info via form fields on the web app
- Store user data securely in the cloud
- View logs or confirm inserts via console output or logs

---

## ✅ Deployment Tips

- You can easily Dockerize the app for deployment
- Database credentials should be stored as environment variables
- You can host the Streamlit app on [Streamlit Cloud](https://streamlit.io/cloud) or any cloud VM

---

## 📌 Future Extensions

- Authentication for user submissions
- User dashboard for data analytics
- Admin backend to view/export submissions

---

## 📄 License

MIT License (add `LICENSE` file if needed)

---

## 👤 Author

**charlesl3** — [GitHub Profile](https://github.com/charlesl3)
