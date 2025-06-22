# BackdoorSim

My BackdoorSim is a purely educational tool built in Python that simulates a simple command-based backdoor.

This project does not perform any real malicious actions. All functionality is local and intended for simulation and learning only.

---

## What It Does:

- Simulates a basic command listener (simulated "reverse shell")
- Accepts and executes simple local commands like:
  - `whoami`
  - `list_dir`
  - `get_time`
  - `exit`
- Logs all interactions to a local file
- Lets defenders (Blue Team) practice detecting or investigating backdoor behavior

---
## ⚠️ LEGAL DISCLAIMER

This tool is for **educational purposes only**. Do not use it on any system or network you do not own or have explicit permission to test. The creator is not responsible for any misuse of this code.

---

## How to Run:

1. Clone the repo
2. Run the Python file:
   ```bash
   python backdoorsim.py
