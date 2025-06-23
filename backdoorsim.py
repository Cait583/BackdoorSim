import time  # This imports the time module to add delays into the program creating realistic typing effects and timed alerts
import threading  # This threading helps run parts of the program one at a time to simulate background tasks running
import random  # Generates random choices or numbers simulating the attacker moves or system responses
import difflib  # This is used to find close matches for what the user types in their commands


class Colors:  # I am creating a toolbox named COLORS to hold special codes that tells your computer to change the color of the text in the terminal
    RED = '\033[91m'  # Makes the text red using ANSI escape codes
    YELLOW = '\033[93m'  # ANSI escape code for yellow text
    GREEN = '\033[92m'  # ANSI escape code for green text
    END = '\033[0m'  # This tells it to stop coloring and go back to the normal text color


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
        "Available commands: netstat, whoami, ps, ls, cat, exit (Please type one at a time)")  # Gives the user the available commands to use
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
            print("Available commands: netstat, whoami, ps, ls, exit, help, hint, trace, cat, analyze")
            print("Please type your next command.")
            continue

        elif cmd == "hint":  # Added hint command handling
            hints_used += 1  # This adds 1 to the number of hints the user has asked for

            next_stage = scenario_stage + 1  # This will calculate the next stage to give a hint for
            hint = get_hint(next_stage)  # This gets the hint for the next stage

            if hint != "No hints available for this stage.":  # Starts a for loop with hint to only show if a hint exists
                print_warning(f"Next hint: {hint}")  # This shows the user the next steps hint
            else:
                print_warning(
                    "No further hints available for this step")  # Tells the user that there are no more hints available

            print("Please type your next command.")
            continue

        elif cmd == "netstat":  # Starts an if loop to check is the user has typed netstat as their first command
            scenario_stage = 2  # Progress the scenario stage after netstat
            user_choice.append((scenario_stage,
                                cmd))  # This logs each command the user types as well as the current investigation stage they are at
            print(
                "[*] Active Connections:")  # Simulates the output of the netstat command for the user to show active network connections
            print(
                "Proto  Local Address          Foreign Address        State")  # Header line to show simulating the real netstat status
            print("TCP    192.168.1.5:443        93.184.216.34:51515     ESTABLISHED")  # Fake TCP connection
            print("TCP    192.168.1.5:22         203.0.113.76:40212      TIME_WAIT")  # Another fake TCP connection
            print("UDP    0.0.0.0:68             *:*                    LISTENING\n")  # UDP listening
            print("Please type your next command.")
            continue

        elif cmd == "whoami":  # If the user types 'whoami' it will simulate showing the current user
            scenario_stage = 4  # Progress the scenario stage after whoami
            user_choice.append((scenario_stage, cmd))
            print("user382")  # Fake username showing the compromised user
            print("Please type your next command.")
            continue

        elif cmd == "ps":  # If the user types ps it will show a fake list of running processes
            scenario_stage = 5  # Progress the scenario stage after ps
            user_choice.append((scenario_stage, cmd))
            print(" PID   USER     COMMAND")
            print("  101  root     sshd")
            print("  382  user382  python3")
            print("  567  user382  chrome")
            print("  789  root     nginx\n")
            print("Please type your next command.")
            continue

        elif cmd == "ls":  # If the user types ls this gives a listing of the files in the current directory
            scenario_stage = 3  # Progress the scenario stage after ls
            user_choice.append((scenario_stage, cmd))
            print("Documents  Downloads  secret_notes.txt  malware_sample.exe  script.py  auth.log\n")
            print("Please type your next command.")
            continue

        elif cmd.startswith("cat"):  # If the user tries to read the file using the cat command
            parts = cmd.split(" ", 1)
            if len(parts) == 1 or not parts[1].strip():
                print_warning("Error: 'cat' requires a filename. Try 'cat auth.log'.")
                print("Please type your next command.")
                continue
            filename = parts[1].strip().lower()  # Normalize filename to lowercase for comparison
            if filename == "auth.log":  # Starts an if loop if the file name matches 'auth.log'
                print_slow("[auth.log]")
                print_slow(
                    "Jun 22 16:30:45 sshd[101]: Accepted password for user382 from 185.220.101.1 port 40212 ssh2")
                print_slow("Jun 22 16:31:10 sshd[101]: Received disconnect from 185.220.101.1 port 40212:11: Bye")
                print_slow("Jun 22 18:52:58 Backdoor connection attempt detected from 103.21.244.1")
            else:
                print_warning("File not found or permission denied.")
            print("Please type your next command.")
            continue

        elif cmd == "trace":  # Simulate tracing the attacker's IP address
            scenario_stage = 6
            user_choice.append((scenario_stage, cmd))
            print(f"Tracing attacker IP: {attacker_ip} ...")
            time.sleep(1)
            print("Trace complete. Location identified as Eastern Europe.")
            print("Please type your next command.")
            continue

        elif cmd == "analyze":  # Simulate analyzing logs for backdoor signatures
            scenario_stage = 7
            user_choice.append((scenario_stage, cmd))
            print("Analyzing system logs for backdoor signatures...")
            time.sleep(1)
            print(f"Backdoor activity confirmed from IP: {attacker_ip}")
            print("Please type your next command.")
            continue

        elif cmd == "exit":  # Allows the user to exit the shell
            print("Exiting secure analysis shell...\n")
            break

        else:
            # Try to suggest closest command if unknown
            commands = ["netstat", "whoami", "ps", "ls", "cat", "exit", "help", "hint", "trace", "analyze"]
            close_matches = difflib.get_close_matches(cmd, commands)
            if close_matches:
                print_warning(f"Unknown command '{cmd}'. Did you mean '{close_matches[0]}'?")
            else:
                print_warning(f"Unknown command '{cmd}'. Type 'help' to see the list of commands.")
            print("Please type your next command.")
            continue

    # After exiting the loop, print the investigation summary
    print("Investigation Summary:")
    for stage, command in user_choice:
        print(f"Stage {stage}: Command executed: {command}")
    print(f"\nYou used {hints_used} hint(s) during your investigation.")
    print("\nThank you for completing the simulated cyber threat investigation.")
    print("\nProcess finished with exit code 0")


def get_hint(stage):  # Creates a new function called get_hint that looks up what the next command should be based on the current stage
    hints = {  # Creates a dictionary that stores the hints for each stage
        2: "List directory contents with 'ls'.",
        3: "Check who you are logged in as using 'whoami'.",
        4: "List running processes with 'ps'.",
        5: "Trace the attacker IP with 'trace'.",
        6: "Analyze system logs using 'analyze'."
    }
    return hints.get(stage, "No hints available for this stage.")  # Returns the hint for the current stage, or a default message if none exists


def main():  # The main function starts here to run everything together when the program is launched
    simulate_alert()  # Calls the alert simulation first to show the warning messages
    investigation_shell()  # Calls the investigation shell where the user can type commands


if __name__ == "__main__":  # This means if this script is run directly, start the main function
    alert_thread = threading.Thread(target=simulate_alert)
    alert_thread.start()
    alert_thread.join()
    investigation_shell()
