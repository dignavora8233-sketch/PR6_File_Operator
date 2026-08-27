print("=============================================")
print("              File Operator                  ")
print("=============================================")

from datetime import datetime


class JournalManager:

    def __init__(self):
        self.filename = "journal.txt"

#-----------------Add Entry----------------#

    def add_entry(self):
        try:
            entry = input("Enter your journal entry: ")

            if entry.strip() == "":
                print("Entry cannot be empty.")
                return

            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            with open(self.filename, "a") as file:
                file.write(f"[{timestamp}]\n")
                file.write(entry + "\n")

            print("Entry added successfully!")

        except PermissionError:
            print("Error: Permission denied.")

#-----------------View Entry-----------------#            

    def view_entries(self):
        try:
            with open(self.filename, "r") as file:
                data = file.read()

            print("\nYour Journal Entries:")
            print("-" * 40)
            print(data)

        except FileNotFoundError:
            print("No journal entries found.")

#----------------Search Entry------------------#

    def search_entry(self):
        keyword = input("Enter a keyword or date to search: ").lower()

        try:
            with open(self.filename, "r") as file:
                data = file.read()

            entries = data.strip().split("\n\n")
            found = False

            for entry in entries:
                if keyword in entry.lower():
                    print("\n", entry)
                    found = True

            if not found:
                print("No matching entry found.")

        except FileNotFoundError:
            print("No journal entries found.")

#------------------Delete Entry---------------------#

    def delete_entries(self):
        try:
            with open(self.filename, "w") as file:
                file.write("")

            print("All journal entries have been deleted.")

        except PermissionError:
            print("Error: Permission denied.")
            
#--------------------Main Menu----------------------#

    def menu(self):
        while True:
            print("\nWelcome to Personal Journal Manager!")
            print("\nPlease select an option:")
            print("1. Add a New Entry")
            print("2. View All Entries")
            print("3. Search for an Entry")
            print("4. Delete All Entries")
            print("5. Exit")

            choice = input("\nEnter your choice: ")

            if choice == "1":
                self.add_entry()

            elif choice == "2":
                self.view_entries()

            elif choice == "3":
                self.search_entry()

            elif choice == "4":
                self.delete_entries()

            elif choice == "5":
                print("Thank you for using Personal Journal Manager.")
                print("Goodbye!")
                break

            else:
                print("Invalid option.")


journal = JournalManager()
journal.menu()
