# 🕵️ Motion Detection with Email Alerts

This project is a **Python-based motion detection system** that uses OpenCV to detect movement from a webcam and automatically sends an email alert with a captured frame when new motion is detected.

---

## ✨ Features
- 🎥 Real-time motion detection using your webcam.
- 🖼️ Saves snapshots of detected motion as images.
- 📧 Sends an email alert with an attached image whenever new motion is detected.
- 🧹 Automatically cleans up saved images after sending an email.
- ⚡ Uses multithreading for smooth operation (video capture and email sending don’t block each other).

---

## 🛠️ Technologies Used
- [Python 3](https://www.python.org/)
- [OpenCV](https://opencv.org/) – image processing and motion detection
- [PIL (Pillow)](https://pillow.readthedocs.io/) – image handling
- [smtplib](https://docs.python.org/3/library/smtplib.html) – sending emails
- [dotenv](https://pypi.org/project/python-dotenv/) – managing secrets and API keys
- [Threading](https://docs.python.org/3/library/threading.html) – background tasks
