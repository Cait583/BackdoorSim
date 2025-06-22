import time # This imports the time module to add delays into the program creating realistic typing effects and timed alets
import threading # This threading helps run parts of the program one at a time to simulate background tasks running
import random # Generates random choices or numbers simulating the attacker moves or system responses

def print_slow(text, delay=0.03): # Creates a function print_slow to print the text one character at a time with a delay of 0.03 seconds
  for char in text: # Starts a for loop to go through each character in the text
    print(char, end='', flush=True) # Prints the characters without a newline, making it appear immediately
    time.sleep(delay) # This controls the typing speed
  print() # Moves the cursor to the next line after the message stops

def simulate_alert(): # Creates a new function to start the simulated threat alert to warn the user of the attack
  print_slow("🔴 ALERT: Unauthorized remote access attempt detected!") # Tells the user that their system has just detected a unauthorized remote access attempt
  time.sleep(1) # This pauses the alert for 1 second for the user to have time to see it and think of their next steps
  print_slow("SYSTEM NOTICE: Potential backdoor behavior identified on this device.") # A second message appears to the user telling them another warning about the suspicious behavior
  time.sleep(1.5) # This adds another pause for the user
  print_slow("📍 LOCATION: Unknown remote shell connected from IP: 185.220.101.1") # Here it prints slowly on the screen for the user giving a fake but realistic looking IP address
  time.sleep(1) # This pauses each line to simulate a live log
  print_slow("Timestamp: " + time.strftime("%Y-%m-%d %H:%M:%S")) # Prints another message to the user showing a timestamp of the current date and time from the system
  time.sleep(1.2) # Another pause for this line
  print_slow("⚠️ ACTION REQUIRED: Investigate the potential threat immediately.") # Informs the user they need to investigate immediately
  time.sleep(1) # Pauses the line
  print_slow("Launching secure analysis shell...") # Sets up the next part for the user to interact with a fake CLI, this appears to the user before this
  time.sleep(2) # Pauses the line again for 2 seconds to simulate the shell now loading

def investigation_shell(): # Creates another new function to begin simulating the shell for investigating the threat
  print_slow("\n You are now in the secure analysis shell.") # Informs the user that they are now in the secure analysis shell on a newline
  print_slow("Type a command to begin your investigation.") # lets the user know they can now type a command
  print_slow("Available commands: netstat, whoami, ps, ls, exit (Please type one at a time)") # Gives the user the available commands to use
  print_slow("Type 'help' at any time to see the list of available commands.") # Gives the user information to get assistance on what commands are allowed if they forget
  print()  # Adds a blank line for readability

  while True: # Starts the command loop
    cmd = input("shell> ").strip().lower() # This takes the users input and removes the extra spaces and puts it into lowercase

    if cmd == "help": # Show the available commands to the user when they type 'help'
      print("Available commands: netstat, whoami, ps, ls, exit, help")
      print("Please type your next command.")
      continue

    elif cmd == "netstat": # Starts an if loop to check is the user has typed netstat as their first command
      print("[*] Active Connections:") # Simulates the output of the netstat command for the user to show active network connections
      print("Proto  Local Address          Foreign Address        State")  # Header line to show simulating the real netstat status
      print("TCP    192.168.1.5:443        93.184.216.34:51515     ESTABLISHED")  # Fake TCP connection
      print("TCP    192.168.1.5:22         203.0.113.76:40212      TIME_WAIT")  # Another fake TCP connection
      print("UDP    0.0.0.0:68             *:*                    LISTENING\n")  # UDP listening
      print("Please type your next command.")
      continue

    elif cmd == "whoami": # If the user types 'whoami' it will simulate showing the current user
      print("user382")  # Fake username showing the compromised user
      print("Please type your next command.")
      continue

    elif cmd == "ps": # If the user types ps it will show a fake list of running processes
      print(" PID   USER     COMMAND")
      print("  101  root     sshd")
      print("  382  user382  python3")
      print("  567  user382  chrome")
      print("  789  root     nginx\n")
      print("Please type your next command.")
      continue

    elif cmd == "ls": # If the user types ls this gives a listing of the files in the current directory
      print("Documents  Downloads  secret_notes.txt  malware_sample.exe  script.py\n")
      print("Please type your next command.")
      continue

    elif cmd == "exit": # If the user types 'exit' it will print a message and then go back to waiting for the next command
      print_slow("Exiting the secure shell. Stay safe!")
      break  # Exits the while loop to leave the shell

    else:
      print("Unknown command. Type 'help' to see available commands.")
      print("Please type your next command.")

if __name__ == "__main__":
  simulate_alert()
  investigation_shell()
