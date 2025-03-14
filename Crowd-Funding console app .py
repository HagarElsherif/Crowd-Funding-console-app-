import re

users = []
projects = []

def is_valid_email(email):
    return re.match(r"^[\w\.-]+@[\w\.-]+\.\w+$", email)

def is_valid_phone(phone):
    return re.match(r"^(\+20|0)1[0-9]{9}$", phone)

def register():
    print("\n--- Register ---")
    first_name = input("First name: ")
    last_name = input("Last name: ")
    email = input("Email: ")
    while not is_valid_email(email):
        print("Invalid email format. Try again.")
        email = input("Email: ")
    password = input("Password: ")
    confirm_password = input("Confirm password: ")
    while password != confirm_password:
        print("Passwords do not match. Try again.")
        password = input("Password: ")
        confirm_password = input("Confirm password: ")
    phone = input("Mobile phone: ")
    while not is_valid_phone(phone):
        print("Invalid Egyptian phone number. Try again.")
        phone = input("Mobile phone: ")
    
    users.append({"first_name": first_name, "last_name": last_name, "email": email, "password": password, "phone": phone})
    print("Registration successful!")

def login():
    print("\n--- Login ---")
    email = input("Email: ")
    password = input("Password: ")
    for user in users:
        if user["email"] == email and user["password"] == password:
            print("Login successful!")
            return email
    print("Invalid email or password.")
    return None

def create_project(user_email):
    print("\n--- Create Project ---")
    title = input("Title: ")
    details = input("Details: ")
    target = input("Total target amount (EGP): ")
    start_date = input("Start date (YYYY-MM-DD): ")
    end_date = input("End date (YYYY-MM-DD): ")
    
    projects.append({"owner": user_email, "title": title, "details": details, "target": target, "start_date": start_date, "end_date": end_date})
    print("Project created successfully!")

def view_projects():
    print("\n--- All Projects ---")
    for p in projects:
        print(f"Title: {p['title']}, Target: {p['target']} EGP, Start: {p['start_date']}, End: {p['end_date']}")

def edit_project(user_email):
    print("\n--- Edit Project ---")
    title = input("Enter project title to edit: ")
    for project in projects:
        if project["owner"] == user_email and project["title"] == title:
            project["details"] = input("New details: ")
            project["target"] = input("New target amount (EGP): ")
            project["start_date"] = input("New start date (YYYY-MM-DD): ")
            project["end_date"] = input("New end date (YYYY-MM-DD): ")
            print("Project updated successfully!")
            return
    print("Project not found or not owned by you.")

def delete_project(user_email):
    print("\n--- Delete Project ---")
    title = input("Enter project title to delete: ")
    for project in projects:
        if project["owner"] == user_email and project["title"] == title:
            projects.remove(project)
            print("Project deleted successfully!")
            return
    print("Project not found or not owned by you.")

def search_project_by_date():
    print("\n--- Search Project by Date ---")
    search_date = input("Enter date (YYYY-MM-DD): ")
    found = False
    for project in projects:
        if project["start_date"] == search_date or project["end_date"] == search_date:
            print(f"Title: {project['title']}, Target: {project['target']} EGP, Start: {project['start_date']}, End: {project['end_date']}")
            found = True
    if not found:
        print("No projects found on this date.")

def main():
    while True:
        print("\nCrowd-Funding Console App")
        print("1. Register")
        print("2. Login")
        print("3. Exit")
        choice = input("Choose an option: ")
        
        if choice == "1":
            register()
        elif choice == "2":
            user_email = login()
            if user_email:
                while True:
                    print("\n1. Create Project")
                    print("2. View Projects")
                    print("3. Edit My Project")
                    print("4. Delete My Project")
                    print("5. Search Project by Date")
                    print("6. Logout")
                    option = input("Choose an option: ")
                    if option == "1":
                        create_project(user_email)
                    elif option == "2":
                        view_projects()
                    elif option == "3":
                        edit_project(user_email)
                    elif option == "4":
                        delete_project(user_email)
                    elif option == "5":
                        search_project_by_date()
                    elif option == "6":
                        break
        elif choice == "3":
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
