# 🎟️ Concert Ticket Helper

A simple Python application to help you **secure concert tickets faster** by opening the ticket URL automatically exactly when tickets go on sale.
This is my first project using Python. It's certainly not perfect and there's no UI elements. This code is simply to help remind you of when concert tickets go on sale!

---

## 🚀 Features

- Schedule your ticket URL to open at the precise sale time.
- Supports convenient sale time format like `2025/06/06 (FRI) 11:00`.
- Simple and clean GUI using Tkinter.
- Alerts you when the ticket page opens.
- Lightweight and easy to use.

---

## 📅 Sale Time Format

Enter the sale time in the format: YYYY/MM/DD (DAY) 00:00


Example:  

The `(DAY)` part is for readability and will be ignored by the app when scheduling.

---

## 🛠️ How to Use

1. Run the Python script:
    ```bash
    python ticket_helper.py
    ```
2. Paste the concert ticket URL in the **Concert Ticket URL** field.
3. Enter the sale start time in the specified format.
4. Click **Schedule Ticket Opening**.
5. The app will wait and then open your browser at the exact time.
6. Godspeed lol (people are faster than a second omg). Try and secure your ticket quickly!

---

## 💡 Notes

- Make sure you are logged in to the ticketing site **before** the sale time.
- This tool does **not** automate purchasing or bypass any website protections.
- Use responsibly and follow ticket seller terms of service.

---

## 📦 Requirements

- Python 3.x
- Standard libraries: `tkinter`, `webbrowser`, `threading`, `datetime`
- No external dependencies required for basic functionality.

---

## 🔍 Code Overview

- GUI built with `tkinter`.
- Uses a separate thread to avoid freezing the interface while waiting.
- Parses the sale time string, ignoring the day abbreviation.
- Opens your default web browser when the sale time is reached.
- Uses pop-up message boxes for status updates and alerts.


---

## 🤝 Contributions

Feel free to fork this repository, open issues, or submit pull requests with improvements!

---

⭐ Thank you for checking out my project! Hope this tool helps you snag your favorite concert tickets! ⭐

