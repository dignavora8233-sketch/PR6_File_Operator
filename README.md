# 📔 Personal Journal Manager

A simple **Python File Handling project** that allows users to create, view, search, and delete personal journal entries.

## 🚀 Features

* ✍️ Add a new journal entry
* 📖 View all journal entries
* 🔍 Search entries using a keyword or date
* 🗑️ Delete all journal entries
* 🕒 Automatically stores date and time with each entry
* 📁 Uses a text file (`journal.txt`) for data storage
* ⚠️ Handles common file-related errors

## 🛠️ Technologies Used

* **Python**
* **File Handling**
* **OOP (Object-Oriented Programming)**
* **datetime module**
* **Exception Handling**

## 📂 Project Structure

```text
Personal-Journal-Manager/
│
├── journal.py
├── journal.txt
└── README.md
```

## ▶️ How to Run

### 1. Install Python

Make sure Python is installed on your computer.

### 2. Save the Code

Save the Python program as:

```text
journal.py
```

### 3. Run the Program

Open the terminal in the project folder and run:

```bash
python journal.py
```

## 📋 Menu Options

When the program starts, the following menu is displayed:

```text
Welcome to Personal Journal Manager!
Please select an option:
1. Add a New Entry
2. View All Entries
3. Search for an Entry
4. Delete All Entries
5. Exit
```

### 1️⃣ Add a New Entry

Enter your journal entry when prompted.

The program automatically stores the current date and time.

Example:

```text
Enter your journal entry: Today I learned Python File Handling.
Entry added successfully!
```

### 2️⃣ View All Entries

Displays all saved journal entries from `journal.txt`.

Example:

```text
Your Journal Entries:
----------------------------------------
[2026-08-27 10:30:15]
Today I learned Python File Handling.
```

### 3️⃣ Search for an Entry

You can search for an entry using a **keyword or date**.

Example:

```text
Enter a keyword or date to search: python
```

The program displays matching entries.

### 4️⃣ Delete All Entries

Deletes all saved journal entries from the file.

```text
All journal entries have been deleted.
```

### 5️⃣ Exit

Closes the program.

```text
Thank you for using Personal Journal Manager.
Goodbye!
```

## 🧠 Concepts Used

### Object-Oriented Programming

The project uses a `JournalManager` class to organize all journal-related operations.

### File Handling

The program uses:

* `a` mode → Add new entries
* `r` mode → Read entries
* `w` mode → Delete all entries

### Date & Time

The `datetime` module is used to automatically record the date and time of each journal entry.

### Exception Handling

The program handles errors such as:

* `FileNotFoundError`
* `PermissionError`

## 📄 Data Storage

All journal entries are stored in:

```text
journal.txt
```

The file is created automatically when the first entry is added.

## 🎯 Project Objective

The main objective of this project is to practice **Python File Handling, OOP, datetime, and exception handling** by creating a simple real-world journal management application.

## 👩‍💻 Author

**Digna Vora**

### ⭐ If you like this project, feel free to explore and improve it!

## 🔗 Connect Me:

* 💼 **LinkedIn:www.linkedin.com/in/digna-vora-b135a3416

* 📧 **Email:**dignavora8233@gmail.com

Feel free to connect with me and explore my projects! 🚀
