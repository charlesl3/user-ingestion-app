# main.py

from db_utils import create_table, insert_user, count_users

"""
main.py

A simple interactive data pipeline that:
- Creates a user table in MySQL
- Inserts fake user data (name, age)
- Tracks and reports the total number of users

This pipeline is modular, CLI-driven, and ideal for learning SQL + Python data ingestion.
"""

def main():
    # Always make sure the table exists
    create_table()

    while True:
        print("\n🎛️ User Ingest Pipeline Menu")
        print("1. Insert one user")
        print("2. Count total users")
        print("3. Insert multiple users")
        print("4. Exit")

        choice = input("\nSelect an option (1–4): ").strip()

        if choice == "1":
            name, age = insert_user()
            print(f"✅ Inserted: {name} ({age})")

        elif choice == "2":
            total = count_users()
            print(f"📊 Total users: {total}")

        elif choice == "3":
            try:
                n = int(input("How many users to insert? "))
                for _ in range(n):
                    name, age = insert_user()
                    print(f"✅ Inserted: {name} ({age})")
                print(f"🎉 Done inserting {n} users.")
            except ValueError:
                print("❌ Invalid number.")

        elif choice == "4":
            print("👋 Exiting pipeline.")
            break

        else:
            print("❌ Invalid choice. Try 1–4.")

        input("\nPress Enter to continue...")

if __name__ == "__main__":
    main()