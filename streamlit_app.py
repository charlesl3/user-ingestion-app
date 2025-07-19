import streamlit as st
from db_utils import create_table, insert_user, count_users, insert_manual_user, get_all_users


# Ensure the table exists every time the app runs
create_table()

st.title("👤 User Ingestion App")
st.markdown("Insert users into the database and view the total count.")

#to run, typoe this: streamlit run streamlit_app.py

# insert user feature
st.subheader("➕ Insert a New User")
name = st.text_input("Enter name")
age = st.number_input("Enter age", min_value=0, max_value=120, step=1)

if st.button("Insert User"):
    if name:
        insert_manual_user(name, age)
        st.success(f"✅ Inserted user: {name} ({age})")
    else:
        st.warning("⚠️ Please enter a name.")


# count user feature
st.subheader("📊 Show Total Users")

if st.button("Count Users"):
    total = count_users()
    st.info(f"📌 Total users in the database: {total}")

# View user feature
st.subheader("📋 View All Users")

if st.button("Show All Users"):
    users = get_all_users()
    if users:
        st.table(users)
    else:
        st.info("No users found.")