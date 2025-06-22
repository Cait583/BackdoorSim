# BackdoorSim

BackdoorSim is an educational cybersecurity simulation tool written in Python. It mimics a realistic scenario where a user investigates a suspicious backdoor infection via a command-line interface.

This project is intended solely for learning and practice. No actual malicious actions are performed — all behaviors are simulated locally.

What It Does:

- Simulates a live system alert for an unauthorized remote access attempt

- Presents a secure analysis shell with a realistic command interface for investigation

- Supports commands like:

- netstat (view active connections)

- whoami (view current user)

- ps (list running processes)

- ls (list directory files)

- cat (view contents of certain log files)

- analyze (simulate malware analysis)

- trace (simulate network traceroute)

- hint (get help during investigation)

- help (list available commands)

- exit (exit shell and show summary)

Simulates typing effects and colored terminal output for immersive experience

Tracks investigation progress and provides tailored hints

Summarizes user actions upon exiting the shell

⚠️ Legal Disclaimer
This tool is strictly for educational and training purposes. Do NOT use it on any systems or networks without explicit permission. The author is not responsible for misuse.

How to Run
Clone this repository

Run the Python script:
python backdoorsim.py
