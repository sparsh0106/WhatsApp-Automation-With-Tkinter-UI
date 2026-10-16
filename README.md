# 💬 WhatsApp Message Scheduler & Automation (Tkinter GUI)

A desktop GUI application built with **Python**, **Tkinter**, and **PyWhatKit** that schedules and sends automated WhatsApp messages at a user-specified time (24-hour format) via WhatsApp Web.

---

## 📂 Repository Structure

- `project.py`: Tkinter GUI interface and `pywhatkit.sendwhatmsg` scheduler integration.
- `README.md`: Project documentation and setup guide.

---

## ✨ Features

- **Graphical Scheduling Interface**: Enter the recipient's phone number (with country code), message body, target hour (24-hour format), and minute in a clean Tkinter window.
- **Automated Browser Dispatch**: Uses `pywhatkit.sendwhatmsg()` to open WhatsApp Web in your default browser and deliver the message automatically at the scheduled time.

---

## 🚀 Getting Started

### Prerequisites
- Ensure you are signed into **WhatsApp Web** on your default web browser.
- Install `pywhatkit`:
  ```bash
  pip install pywhatkit
  ```

### Run the Application
```bash
git clone https://github.com/sparsh0106/WhatsApp-Automation-With-Tkinter-UI.git
cd WhatsApp-Automation-With-Tkinter-UI
python project.py
```

---

## 👤 Author

**Sparsh Agarwal** — [GitHub](https://github.com/sparsh0106)
