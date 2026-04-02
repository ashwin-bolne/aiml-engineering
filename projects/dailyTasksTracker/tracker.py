import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3
from datetime import datetime

# =============================
# DATABASE SETUP
# =============================
conn = sqlite3.connect("tracker.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS logs (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    date TEXT,
    day TEXT,
    aiml TEXT,
    cat TEXT,
    hsd TEXT,
    review TEXT
)
""")
conn.commit()

# =============================
# SAVE FUNCTION
# =============================
def save_data():
    data = (
        date_entry.get(),
        day_entry.get(),
        aiml_text.get("1.0", tk.END),
        cat_text.get("1.0", tk.END),
        hsd_text.get("1.0", tk.END),
        review_text.get("1.0", tk.END),
    )

    cursor.execute("""
    INSERT INTO logs (date, day, aiml, cat, hsd, review)
    VALUES (?, ?, ?, ?, ?, ?)
    """, data)

    conn.commit()
    messagebox.showinfo("Saved", "Entry saved successfully")

# =============================
# VIEW DATA
# =============================
def view_data():
    window = tk.Toplevel(root)
    window.title("Past Entries")

    tree = ttk.Treeview(window, columns=("Date", "Day"), show="headings")
    tree.heading("Date", text="Date")
    tree.heading("Day", text="Day")

    tree.pack(fill="both", expand=True)

    cursor.execute("SELECT id, date, day FROM logs ORDER BY id DESC")
    rows = cursor.fetchall()

    for row in rows:
        tree.insert("", tk.END, values=(row[1], row[2]))

# =============================
# UI
# =============================
root = tk.Tk()
root.title("Elite Execution Tracker v2")
root.geometry("900x700")

style = ttk.Style()
style.theme_use("clam")

# HEADER
header = ttk.Label(root, text="Elite Execution Tracker", font=("Arial", 18, "bold"))
header.pack(pady=10)

# TOP FIELDS
top_frame = ttk.Frame(root)
top_frame.pack(pady=5)

ttk.Label(top_frame, text="Date").grid(row=0, column=0, padx=10)
date_entry = ttk.Entry(top_frame)
date_entry.insert(0, datetime.today().strftime("%Y-%m-%d"))
date_entry.grid(row=0, column=1)

ttk.Label(top_frame, text="Day").grid(row=0, column=2, padx=10)
day_entry = ttk.Entry(top_frame)
day_entry.grid(row=0, column=3)

# TABS
notebook = ttk.Notebook(root)
notebook.pack(expand=True, fill="both")

# AIML TAB
aiml_tab = ttk.Frame(notebook)
notebook.add(aiml_tab, text="AIML")

aiml_text = tk.Text(aiml_tab, wrap="word")
aiml_text.pack(expand=True, fill="both")

# CAT TAB
cat_tab = ttk.Frame(notebook)
notebook.add(cat_tab, text="CAT")

cat_text = tk.Text(cat_tab, wrap="word")
cat_text.pack(expand=True, fill="both")

# HSD TAB
hsd_tab = ttk.Frame(notebook)
notebook.add(hsd_tab, text="HSD")

hsd_text = tk.Text(hsd_tab, wrap="word")
hsd_text.pack(expand=True, fill="both")

# REVIEW TAB
review_tab = ttk.Frame(notebook)
notebook.add(review_tab, text="Review")

review_text = tk.Text(review_tab, wrap="word")
review_text.pack(expand=True, fill="both")

# BUTTONS
btn_frame = ttk.Frame(root)
btn_frame.pack(pady=10)

ttk.Button(btn_frame, text="Save Entry", command=save_data).grid(row=0, column=0, padx=10)
ttk.Button(btn_frame, text="View Past Entries", command=view_data).grid(row=0, column=1, padx=10)

root.mainloop()