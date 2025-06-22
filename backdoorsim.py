import time  # This imports the time module to add delays into the program creating realistic typing effects and timed alerts
import threading  # This threading helps run parts of the program one at a time to simulate background tasks running
import random  # Generates random choices or numbers simulating the attacker moves or system responses
import difflib  # This is used to find close matches for what the user types in their commands

class Colors: # I am creating a toolbox named COLORS to hold special codes that tells your computer to change the color of the text in the terminal
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
        "Available commands: netstat, whoami, ps, ls, cat, exit (Please type one at a time)")  # Gives the user the available commands to use
    print_warning(
        "Type 'help' at any time to see the list of available commands.")  # Gives the user information to get assistance on what commands are allowed if they forget
    print()  # Adds a blank line for readability

    attacker_ip = random.choice(["185.220.101.1", "103.21.244.1", "45.33.32.156"])  # This will pick a random IP address out of those listed to simulate that each time this is run the backdoor could be coming from a different source
    scenario_stage = 1  # Creates a variable called scenario_stage to 1 which tracks what phrase of investigation the user is currently in
    user_choice = []  # Creates an empty list so that each time the user enters a command it will be stored here along with the scenario stage
    hints_used = 0  # Creates a counter called hints_used to track each time the user types the command hint to get help with the situation

    while True:  # Starts the command loop
        cmd = input("shell> ").strip().lower()  # This takes the users input and removes the extra spaces and puts it into lowercase

        if cmd == "help":  # Show the available commands to the user when they type 'help'
            print("Available commands: netstat, whoami, ps, ls, exit, help, hint, trace, cat, analyze")
            print("Please type your next command.")
            continue

        elif cmd == "hint":  # Added hint command handling
            hints_used += 1  # This adds 1 to the number of hints the user has asked for

            next_stage = scenario_stage + 1 # This will calculate the next stage to give a hint for
            hint = get_hint(next_stage) # This gets the hint for the next stage

            if hint != "No hints available for this step.": # Starts a for loop with hint to only show if a hint exists
              print_warning(f"Next hint: {hint}") # This shows the user the next steps hint
            else:
              print_warning("No further hints available for this step") # Tells the user that there are no more hints available
              
            print("Please type your next command.")
            continue

        elif cmd == "netstat":  # Starts an if loop to check is the user has typed netstat as their first command
            print(
                "[*] Active Connections:")  # Simulates the output of the netstat command for the user to show active network connections
            print("Proto  Local Address          Foreign Address        State")  # Header line to show simulating the real netstat status
            print("TCP    192.168.1.5:443        93.184.216.34:51515     ESTABLISHED")  # Fake TCP connection
            print("TCP    192.168.1.5:22         203.0.113.76:40212      TIME_WAIT")  # Another fake TCP connection
            print("UDP    0.0.0.0:68             *:*                    LISTENING\n")  # UDP listening
            user_choice.append((scenario_stage, cmd))  # This logs each command the user types as well as the current investigation stage they are at
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
            print("Documents  Downloads  secret_notes.txt  malware_sample.exe  script.py  auth.log\n")
            user_choice.append((scenario_stage, cmd))
            scenario_stage = 4  # Progress the scenario stage after ls
            print("Please type your next command.")
            continue

        elif cmd.startswith("cat "): # If the user tries to read the file using the cat command
            filename = cmd.split(" ", 1)[1] # This splits what the user is saying into two parts at the first space, and it will save the second part as a filename for the user
            if filename == "auth.log": # Starts an if loop if the file name matches 'auth.log'
                print_slow("[auth.log]")
                print_slow("Jun 22 16:30:45 sshd[101]: Accepted password for user382 from 185.220.101.1 port 40212 ssh2")
                print_slow("Jun 22 16:31:10 sshd[101]: Received disconnect from 185.220.101.1 port 40212:11: Bye Bye")
                print_slow("Jun 22 16:31:12 sshd[101]: Disconnected from 185.220.101.1 port 40212")
            else:
                print_warning(f"Cannot open {filename}: Permission denied or file not found.") # Gives the user a warning if it does not match that filename
            print("Please type your next command.")
            continue

        elif cmd.startswith("analyze "): # If the user types 'analyze malware_sample.exe'
            filename = cmd.split(" ", 1)[1]
            if filename == "malware_sample.exe": # Checks that the filename is that name and sends messages to the user:
                print_slow("Analyzing malware_sample.exe...")
                time.sleep(2)
                print_slow("⚠️ Behavior detected: Opens reverse shell to 45.33.32.156")
                print_slow("⚠️ Modifies registry and disables antivirus.")
            else:
                print_warning(f"{filename} is not a recognized suspicious file.") # Gives the user a warning if the file is not recognized
            print("Please type your next command.")
            continue

        elif cmd.startswith("trace "):  # Simulates tracing an IP address for the user
            ip = cmd.split(" ", 1)[1]
            print_slow(f"Tracing route to {ip}...") # Simulates the tracing route to the IP for the user
            time.sleep(2)
            hops = [ # Simulates hops for the user to show on the screen
                "1   192.168.1.1",
                "2   10.23.0.1",
                "3   172.67.0.4",
                f"4   {ip} [Destination reached]"
            ]
            for hop in hops: # Goes through each hop one by one for the user
                print_slow(hop) # Prints each hop slowly to simulate real traceroute
                time.sleep(1) # Waits 1 second between each hop
            print_success("Trace complete.")
            print("Please type your next command.")
            continue

        elif cmd == "exit":  # If the user types 'exit' it will print a message and then go back to waiting for the next command
            print_slow("Exiting the secure shell")
            print_summary(
                user_choice)  # If the user types exit it will not just exit but print the summary of the investigation done
            break  # Exits the while loop to leave the shell

        else:
          print("Unknown command.")
          suggestion = difflib.get_close_matches(cmd, ["netstat", "whoami", "ps", "ls", "cat", "analyze", "hint", "help", "exit"], n=1) # ensures if the user is unsure of what to type next they get a suggestion
          if suggestion:
            print(f"Did you mean '{suggestion[0]}'?")
          else:
            print("Type 'help' to see the list of available commands.")


def get_hint(stage):  # Creates a new function that take one parameter 'stage'
    hints = {  # Makes a dictionary to map each stage to a specific hint message given
        1: "Try checking active network connections with 'netstat' to find suspicious activity.",
        2: "Look at the running processes with 'ps' to identify unfamiliar programs.",
        3: "List files in the current directory using 'ls' to find suspicious files.",
        4: "Use 'whoami' to confirm the current user privileges.",
        5: "Try 'exit' if you think the investigation is done or use 'cat auth.log' to see recent logs."
    }
    return hints.get(stage, "No hints available for this stage.")


def print_summary(choices):  # Creates a new function to print the summary of the investigation
    print_success("\nInvestigation Summary:")
    for stage, cmd in choices:  # Goes through each tuple in the choices list showing the stage and the command typed
        print(f"Stage {stage}: Command used - {cmd}")


def main():  # Main function to run the entire program
    simulate_alert()  # Starts the initial alert simulation
    investigation_shell()  # Enters the investigation shell


if __name__ == "__main__":  # Only run this if this file is executed directly (not imported as a module)
    main()
