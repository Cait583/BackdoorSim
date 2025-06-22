import time  # This imports the time module to add delays into the program creating realistic typing effects and timed alerts
import threading  # This threading helps run parts of the program one at a time to simulate background tasks running
import random  # Generates random choices or numbers simulating the attacker moves or system responses

class COLORS: # I am creating a toolbox named COLORS to hold special codes that tells your computer to change the color of the text in the terminal
  RED = '\033[91m' # Makes the text red using ANSI escape codes
  YELLOW = '\033[93m' # ANSI escape code for yellow text
  GREEN = '\033[92m' # ANSI escape code for green text
  END = '\033[0m' # This tells it to stop coloring and go back to the normal text color

# All these newly created functions will take the message that will show to the user and add a special color to it. It will then print the message
def print_alert(text):
    print(Colors.RED + text + Colors.END)

def print_warning(text):
    print(Colors.YELLOW + text + Colors.END)

def print_success(text):
    print(Colors.GREEN + text + Colors.END)

def print_slow(text,
               delay=0.03):  # Creates a function print_slow to print the text one character at a time with a delay of 0.03 seconds
    for char in text:  # Starts a for loop to go through each character in the text
        print(char, end='', flush=True)  # Prints the characters without a newline, making it appear immediately
        time.sleep(delay)  # This controls the typing speed
    print()  # Moves the cursor to the next line after the message stops


def simulate_alert():  # Creates a new function to start the simulated threat alert to warn the user of the attack
    print_alert(
        "🔴 ALERT: Unauthorized remote access attempt detected!")  # Tells the user that their system has just detected unauthorized remote access attempt
    time.sleep(
        1)  # This pauses the alert for 1 second for the user to have time to see it and think of their next steps
    print_slow(
        "SYSTEM NOTICE: Potential backdoor behavior identified on this device.")  # A second message appears to the user telling them another warning about the suspicious behavior
    time.sleep(1.5)  # This adds another pause for the user
    print_slow(
        "📍 LOCATION: Unknown remote shell connected from IP: 185.220.101.1")  # Here it prints slowly on the screen for the user giving a fake but realistic looking IP address
    time.sleep(1)  # This pauses each line to simulate a live log
    print_slow("Timestamp: " + time.strftime(
        "%Y-%m-%d %H:%M:%S"))  # Prints another message to the user showing a timestamp of the current date and time from the system
    time.sleep(1.2)  # Another pause for this line
    print_warning(
        "⚠️ ACTION REQUIRED: Investigate the potential threat immediately.")  # Informs the user they need to investigate immediately
    time.sleep(1)  # Pauses the line
    print_success(
        "Launching secure analysis shell...")  # Sets up the next part for the user to interact with a fake CLI, this appears to the user before this
    time.sleep(2)  # Pauses the line again for 2 seconds to simulate the shell now loading


def investigation_shell():  # Creates another new function to begin simulating the shell for investigating the threat
    print_success(
        "\n You are now in the secure analysis shell.")  # Informs the user that they are now in the secure analysis shell on a newline
    print_slow("Type a command to begin your investigation.")  # lets the user know they can now type a command
    print_warning(
        "Available commands: netstat, whoami, ps, ls, exit (Please type one at a time)")  # Gives the user the available commands to use
    print_warning(
        "Type 'help' at any time to see the list of available commands.")  # Gives the user information to get assistance on what commands are allowed if they forget
    print()  # Adds a blank line for readability

    attacker_ip = random.choice(["185.220.101.1", "103.21.244.1",
                                 "45.33.32.156"])  # This will pick a random IP address out of those listed to simulate that each time this is run the backdoor could be coming from a different source
    scenario_stage = 1  # Creates a variable called scenario_stage to 1 which tracks what phrase of investigation the user is currently in
    user_choice = []  # Creates an empty list so that each time the user enters a command it will be stored here along with the scenario stage
    hints_used = 0  # Creates a counter called hints_used to track each time the user types the command hint to get help with the situation

    while True:  # Starts the command loop
        cmd = input(
            "shell> ").strip().lower()  # This takes the users input and removes the extra spaces and puts it into lowercase

        if cmd == "help":  # Show the available commands to the user when they type 'help'
            print("Available commands: netstat, whoami, ps, ls, exit, help, hint")
            print("Please type your next command.")
            continue

        elif cmd == "hint":  # Added hint command handling
            hints_used += 1  # This adds 1 to the number of hints the user has asked for
            print(
                f"HINT: {get_hint(scenario_stage)}")  # Gives a hint message to the user based on the current step in the investigation
            print("Please type your next command.")
            continue

        elif cmd == "netstat":  # Starts an if loop to check is the user has typed netstat as their first command
            print(
                "[*] Active Connections:")  # Simulates the output of the netstat command for the user to show active network connections
            print(
                "Proto  Local Address          Foreign Address        State")  # Header line to show simulating the real netstat status
            print("TCP    192.168.1.5:443        93.184.216.34:51515     ESTABLISHED")  # Fake TCP connection
            print("TCP    192.168.1.5:22         203.0.113.76:40212      TIME_WAIT")  # Another fake TCP connection
            print("UDP    0.0.0.0:68             *:*                    LISTENING\n")  # UDP listening
            user_choice.append((scenario_stage,
                                cmd))  # This logs each command the user types as well as the current investigation stage they are at
            scenario_stage = 2  # Progress the scenario stage after netstat
            print("Please type your next command.")
            continue

        elif cmd == "whoami":  # If the user types 'whoami' it will simulate showing the current user
            print("user382")  # Fake username showing the compromised user
            user_choice.append((scenario_stage, cmd))
            scenario_stage = 5  # Progress the scenario stage after whoami
            print("Please type your next command.")
            continue

        elif cmd == "ps":  # If the user types ps it will show a fake list of running processes
            print(" PID   USER     COMMAND")
            print("  101  root     sshd")
            print("  382  user382  python3")
            print("  567  user382  chrome")
            print("  789  root     nginx\n")
            user_choice.append((scenario_stage, cmd))
            scenario_stage = 3  # Progress the scenario stage after ps
            print("Please type your next command.")
            continue

        elif cmd == "ls":  # If the user types ls this gives a listing of the files in the current directory
            print("Documents  Downloads  secret_notes.txt  malware_sample.exe  script.py\n")
            user_choice.append((scenario_stage, cmd))
            scenario_stage = 4  # Progress the scenario stage after ls
            print("Please type your next command.")
            continue

        elif cmd == "exit":  # If the user types 'exit' it will print a message and then go back to waiting for the next command
            print_slow("Exiting the secure shell")
            print_summary(
                user_choice)  # If the user types exit it will not just exit but print the summary of the investigation done
            break  # Exits the while loop to leave the shell

        else:
            print_alert("Unknown command. Type 'help' to see available commands.")
            print("Please type your next command.")


def get_hint(stage):  # Creates a new function that take one parameter 'stage'
    hints = {  # Makes a dictionary to map each stage to a specific hint message given
        1: "Try checking active network connections with 'netstat' to find suspicious activity.",
        2: "Look at the running processes with 'ps' to identify unfamiliar programs.",
        3: "List files in the current directory using 'ls' to find suspicious files.",
        4: "Use 'whoami' to confirm the current user privileges.",
        5: "Try 'exit' if you think the investigation is done or to quit the shell."
    }
    return hints.get(stage,
                     "No hints available for this step.")  # Returns the hint for the given stage if it exists if not it returns 'No hints available for this step'


def print_summary(user_choice):  # Creates a new function for showing the summary at the end for the user to look over
    print("\n--- Investigation Summary ---")
    stages_done = set(stage for stage, cmd in
                      user_choice)  # Creates a set of unique investigation stages the user has done by taking away the stage from each (stage, cmd) pair in the user_choice list

    if 1 in stages_done:
        print_success("You checked network connections with 'netstat'. Good start.")
    if 2 in stages_done:
        print("You inspected running processes with 'ps'. Useful info found.")
    if 3 in stages_done:
        print("You listed directory files with 'ls'. Found suspicious files.")
    if 4 in stages_done:
        print("You confirmed user privileges with 'whoami'.")
    if 5 in stages_done:
        print("You ended the investigation properly with 'exit'.")

    if not stages_done:  # Informs the user if they have not done the stages correctly
        print("You didn't perform any investigation commands.")
    print("--- End of Summary ---\n")


if __name__ == "__main__":
    alert_thread = threading.Thread(target=simulate_alert)
    alert_thread.start()
    alert_thread.join()  # Wait for the alert to finish before starting shell
    investigation_shell()
