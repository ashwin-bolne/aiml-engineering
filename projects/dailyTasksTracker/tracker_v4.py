import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3
from datetime import datetime
import matplotlib.pyplot as plt

# =============================
# DATABASE
# =============================
conn = sqlite3.connect("tracker_v4.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS logs (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    date TEXT,
    day TEXT,

    dsa_topic TEXT,
    dsa_problems INTEGER,
    dsa_accuracy INTEGER,

    quant_questions INTEGER,

    energy INTEGER,
    focus INTEGER
)
""")
conn.commit()

# =============================
# SAVE FUNCTION
# =============================
def save_data():
    try:
        cursor.execute("""
        INSERT INTO logs (date, day, dsa_topic, dsa_problems, dsa_accuracy, quant_questions, energy, focus)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            date_entry.get(),
            day_entry.get(),
            dsa_topic.get(),
            int(dsa_problems.get() or 0),
            int(dsa_accuracy.get() or 0),
            int(quant_questions.get() or 0),
            int(energy.get() or 0),
            int(focus.get() or 0)
        ))

        conn.commit()
        messagebox.showinfo("Saved", "Entry saved successfully")

    except Exception as e:
        messagebox.showerror("Error", str(e))

# =============================
# VIEW ENTRIES
# =============================
def view_data():
    window = tk.Toplevel(root)
    window.title("Entries")
    window.geometry("600x400")

    tree = ttk.Treeview(window, columns=("Date", "DSA", "Quant", "Energy"), show="headings")
    tree.heading("Date", text="Date")
    tree.heading("DSA", text="DSA")
    tree.heading("Quant", text="Quant")
    tree.heading("Energy", text="Energy")

    tree.pack(fill="both", expand=True)

    cursor.execute("SELECT id, date, dsa_problems, quant_questions, energy FROM logs ORDER BY id DESC")
    for row in cursor.fetchall():
        tree.insert("", tk.END, iid=row[0], values=(row[1], row[2], row[3], row[4]))

# =============================
# DASHBOARD
# =============================
def show_dashboard():
    cursor.execute("SELECT date, dsa_problems, quant_questions, energy, focus FROM logs ORDER BY date")
    data = cursor.fetchall()

    if not data:
        messagebox.showwarning("No Data", "No entries found")
        return

    dates, dsa, quant, energy, focus, score = [], [], [], [], [], []

    for row in data:
        dates.append(row[0])
        d = int(row[1] or 0)
        q = int(row[2] or 0)
        e = int(row[3] or 0)
        f = int(row[4] or 0)

        dsa.append(d)
        quant.append(q)
        energy.append(e)
        focus.append(f)

        score.append((d*2) + q + (e*5) + (f*5))

    plt.figure()
    plt.plot(dates, dsa)
    plt.plot(dates, quant)
    plt.title("DSA vs Quant")

    plt.figure()
    plt.plot(dates, energy)
    plt.plot(dates, focus)
    plt.title("Energy vs Focus")

    plt.figure()
    plt.plot(dates, score)
    plt.title("Productivity Score")

    plt.show()

# =============================
# UI
# =============================
root = tk.Tk()
root.title("Elite Tracker V4")
root.geometry("700x500")

frame = ttk.Frame(root, padding=20)
frame.pack(fill="both", expand=True)

row = 0

def add(label):
    global row
    ttk.Label(frame, text=label).grid(row=row, column=0, sticky="w", pady=5)
    e = ttk.Entry(frame, width=30)
    e.grid(row=row, column=1)
    row += 1
    return e

date_entry = add("Date")
date_entry.insert(0, datetime.today().strftime("%Y-%m-%d"))

day_entry = add("Day")

ttk.Label(frame, text="--- AIML ---").grid(row=row, column=0, columnspan=2)
row += 1

dsa_topic = add("DSA Topic")
dsa_problems = add("Problems")
dsa_accuracy = add("Accuracy")

ttk.Label(frame, text="--- CAT ---").grid(row=row, column=0, columnspan=2)
row += 1

quant_questions = add("Quant Questions")

ttk.Label(frame, text="--- REVIEW ---").grid(row=row, column=0, columnspan=2)
row += 1

energy = add("Energy")
focus = add("Focus")

# BUTTONS
ttk.Button(frame, text="Save", command=save_data).grid(row=row, column=0, pady=10)
ttk.Button(frame, text="View", command=view_data).grid(row=row, column=1)
row += 1

ttk.Button(frame, text="Dashboard", command=show_dashboard).grid(row=row, column=0, columnspan=2)

root.mainloop()