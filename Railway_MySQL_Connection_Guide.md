# Railway MySQL Connection Guide

This guide documents how to connect your Streamlit app to a MySQL database hosted on [Railway](https://railway.app/), especially when deploying your app to Streamlit Cloud.

---

## 🚫 Localhost Will Not Work

**Important:** If your connection code uses `host='localhost'` or `host='127.0.0.1'`, it will **not work** in production (e.g. on Streamlit Cloud) because the database is not hosted on the same server as your app. You must use the public TCP proxy endpoint provided by Railway.

---

## ✅ How to Connect Streamlit to Railway MySQL

### 1. Get Railway Connection Details
Go to your Railway project and note the following values from the **Variables** and **Settings > Networking** tabs:

- `MYSQLHOST` (e.g. `yamanote.proxy.rlwy.net`)
- `MYSQLPORT` (typically `21921`)
- `MYSQLUSER`
- `MYSQLPASSWORD`
- `MYSQLDATABASE`

You will use these in your `st.secrets` configuration.

---

### 2. Define Secrets in `.streamlit/secrets.toml`
If running locally, create a `.streamlit/secrets.toml` file like:

```toml
[mysql]
host = "yamanote.proxy.rlwy.net"
port = 21921
user = "root"
password = "YOUR_PASSWORD"
database = "railway"
```

If using **Streamlit Cloud**, define these keys under `st.secrets` in the web interface.

---

### 3. Use This Connection Code

```python
import mysql.connector
import streamlit as st

def get_connection():
    return mysql.connector.connect(
        host=st.secrets["mysql"]["host"],
        port=int(st.secrets["mysql"].get("port", 3306)),
        user=st.secrets["mysql"]["user"],
        password=st.secrets["mysql"]["password"],
        database=st.secrets["mysql"]["database"]
    )
```

---

## 🔒 Why We Use `st.secrets`
Streamlit Cloud redacts logs and protects secrets automatically. Hardcoding passwords or IPs will expose them. Always store credentials in `st.secrets`.

---

## ✅ Success
Once the proxy endpoint (`.proxy.rlwy.net`) is used and the secrets are set correctly, the connection should succeed from Streamlit Cloud.

---

## ❌ Gotchas
- You **must not** use `mysql.internal` unless your app is also hosted inside Railway.
- Ports like `3306` only work **within Railway’s private network** — use the **proxy port** (e.g. `21921`) externally.

---

Happy building! 🚀
