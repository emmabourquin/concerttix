import tkinter as tk
from tkinter import messagebox
import webbrowser
import threading
import time
from datetime import datetime

def open_ticket_site(url, sale_time_str):
    try:
        # Split to remove the day name (e.g., "(FRI)")
        date_part, time_part = sale_time_str.strip().split(")")
        date_str, _ = date_part.split("(")  # date_str = "2025/06/06 "
        date_str = date_str.strip()
        time_str = time_part.strip()
        # Combine date and time with space
        datetime_str = f"{date_str} {time_str}"
        sale_time = datetime.strptime(datetime_str, "%Y/%m/%d %H:%M")
    except Exception as e:
        messagebox.showerror("Error", f"Invalid time format.\n\nError: {e}")
        return

    messagebox.showinfo("Scheduled", f"Waiting for {sale_time} to open {url}")
    while True:
        now = datetime.now()
        if now >= sale_time:
            webbrowser.open(url)
            messagebox.showinfo("Go!", "The ticket site has been opened. Secure your seat now!")
            break
        time.sleep(0.5)

def start_thread():
    url = url_entry.get()
    sale_time = time_entry.get()
    if not url or not sale_time:
        messagebox.showerror("Error", "Please enter both URL and sale time.")
        return
    threading.Thread(target=open_ticket_site, args=(url, sale_time)).start()

# Build the GUI
root = tk.Tk()
root.title("Concert Ticket Helper")

tk.Label(root, text="Concert Ticket URL:").pack(pady=5)
url_entry = tk.Entry(root, width=50)
url_entry.pack()

tk.Label(root, text="Sale Start Time (YYYY/MM/DD (DAY) HH:MM):").pack(pady=5)
tk.Label(root, text="Example: 2025/06/06 (FRI) 11:00").pack()
time_entry = tk.Entry(root, width=30)
time_entry.pack()

start_button = tk.Button(root, text="Schedule Ticket Opening", command=start_thread)
start_button.pack(pady=20)

tk.Label(root, text="⚠ Make sure you're logged in beforehand!\n⚠ This tool does not bypass site protections.").pack()

root.mainloop()
