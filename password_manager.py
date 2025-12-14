import json 

def save_passwords(passwords):
    with open("data.json", "w") as file:
        
        json.dump(passwords, file)

def main():
    passwords = [] 

    while True:
        print("\n--- Password Manager ---")
        print("1. Add a new password")
        print("2. View all passwords")
        print("3. Exit")
        
        choice = input("Enter your choice (1, 2, or 3): ")
        
        if choice == '1':
            website = input("Enter the website name: ")
            password = input(f"Enter the password for {website}: ")
            
            entry = {"website": website, "password": password}
            passwords.append(entry)
            
            
            save_passwords(passwords)
            print(f"Successfully saved password for {website} to data.json!")

        elif choice == '2':
            
            print("\n--- Your Saved Passwords ---")
            if not passwords:
                print("No passwords saved yet.")
            else:
                for item in passwords:
                    print(f"Website: {item['website']} | Password: {item['password']}")
        
        elif choice == '3':
            print("Goodbye!")
            break

if __name__ == "__main__":
    main()