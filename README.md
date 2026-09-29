# ⏰ Alarm Clock

A simple Python-based alarm clock application with a graphical user interface built using **Tkinter**. The application allows users to enter a specific time and plays an alarm sound when the specified time is reached.

This project is a beginner-friendly Python project that demonstrates GUI development, user input, time handling, and audio playback.

## 📌 Features

- ⏰ Set an alarm using **hour, minute, and second**
- 🖥️ Simple graphical user interface built with **Tkinter**
- 🕐 Supports **24-hour time format**
- 🔊 Plays a custom alarm sound when the specified time is reached
- 📅 Displays the current date and time in the terminal
- 🐍 Built entirely with Python

## 🛠️ Technologies Used

- **Python**
- **Tkinter** – Graphical User Interface
- **playsound** – Audio playback
- **datetime** – Date and time handling
- **time** – Time delays and monitoring

## 📂 Project Structure

```text
AlarmClock/
│
├── main.py          # Main application
├── .gitignore       # Git ignored files
└── .idea/           # IDE configuration files
```

## 🚀 Getting Started

### Prerequisites

Make sure you have **Python 3.x** installed on your computer.

You can verify your Python installation with:

```bash
python --version
```

### 1. Clone the Repository

```bash
git clone https://github.com/thejoecodes/AlarmClock.git
```

Navigate into the project directory:

```bash
cd AlarmClock
```

### 2. Install Dependencies

Install the `playsound` package:

```bash
pip install playsound
```

> **Note:** Tkinter is included with most standard Python installations. On some Linux distributions, it may need to be installed separately.

### 3. Add an Alarm Sound

The application uses an audio file when the alarm is triggered.

In `main.py`, locate:

```python
playsound("path/sound.mp3")
```

Replace the path with the location of your preferred alarm sound:

```python
playsound("sounds/alarm.mp3")
```

For example, your project could contain:

```text
AlarmClock/
│
├── main.py
├── sounds/
│   └── alarm.mp3
└── README.md
```

### 4. Run the Application

Start the alarm clock with:

```bash
python main.py
```

A graphical window will open where you can enter the desired alarm time.

## 🕐 How to Use

1. Launch the application.
2. Enter the desired **hour**.
3. Enter the desired **minute**.
4. Enter the desired **second**.
5. Click **Set Alarm**.
6. The application monitors the current time.
7. When the current time matches the specified time, the alarm sound is played.

### Example

To set an alarm for **7:30:00 AM**, enter:

```text
Hour:   07
Minute: 30
Second: 00
```

The application uses the 24-hour time format, so **7:30 PM** should be entered as:

```text
19:30:00
```

## 🧠 What I Learned

This project provided hands-on practice with several Python concepts:

- Importing and using external libraries
- Working with Python's `datetime` module
- Creating graphical interfaces with Tkinter
- Using `StringVar` for GUI input
- Creating buttons and input fields
- Working with functions
- Using loops to continuously check the time
- Playing audio files from a Python application
- Organizing a small Python project

## 🔮 Future Improvements

Some potential improvements for future versions include:

- [ ] Add input validation for hours, minutes, and seconds
- [ ] Allow users to select an alarm sound from the GUI
- [ ] Add a **Stop Alarm** button
- [ ] Support multiple alarms
- [ ] Add a digital clock displaying the current time
- [ ] Improve the GUI design
- [ ] Add a snooze feature
- [ ] Allow users to cancel or reset an alarm
- [ ] Package the application as a standalone executable
- [ ] Add automated tests

## ⚠️ Current Limitations

This is a simple learning project and currently has some limitations:

- The alarm time must be entered manually.
- The application expects a valid alarm sound path.
- The alarm runs until the specified time is reached.
- The current implementation uses a continuous loop to check the time.
- Input validation and error handling can be improved.

## 🎯 Project Purpose

The goal of this project is to practice Python fundamentals by building a small, functional desktop application.

Rather than being a production-ready alarm application, it serves as a practical exercise in combining **Python programming, GUI development, time-based logic, and audio playback**.

## 👨‍💻 Author

**thejoecodes**

GitHub: [https://github.com/thejoecodes](https://github.com/thejoecodes)

## 📄 License

This project is available for educational and personal use. Add a specific open-source license to the repository if you intend to distribute or modify the project under defined licensing terms.
