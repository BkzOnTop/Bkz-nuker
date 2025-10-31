import os
import sys
import time
from pystyle import Colors, Colorate, Center
import subprocess

class DiscordTool:
    def __init__(self):
        self.banner = r"""
 ▄▄▄▄    ██ ▄█▀▒███████▒    ███▄    █  █    ██  ██ ▄█▀▓█████  ██▀███  
▓█████▄  ██▄█▒ ▒ ▒ ▒ ▄▀░    ██ ▀█   █  ██  ▓██▒ ██▄█▒ ▓█   ▀ ▓██ ▒ ██▒
▒██▒ ▄██▓███▄░ ░ ▒ ▄▀▒░    ▓██  ▀█ ██▒▓██  ▒██░▓███▄░ ▒███   ▓██ ░▄█ ▒
▒██░█▀  ▓██ █▄   ▄▀▒   ░   ▓██▒  ▐▌██▒▓▓█  ░██░▓██ █▄ ▒▓█  ▄ ▒██▀▀█▄  
░▓█  ▀█▓▒██▒ █▄▒███████▒   ▒██░   ▓██░▒▒█████▓ ▒██▒ █▄░▒████▒░██▓ ▒██▒
░▒▓███▀▒▒ ▒▒ ▓▒░▒▒ ▓░▒░▒   ░ ▒░   ▒ ▒ ░▒▓▒ ▒ ▒ ▒ ▒▒ ▓▒░░ ▒░ ░░ ▒▓ ░▒▓░
▒░▒   ░ ░ ░▒ ▒░░░▒ ▒ ░ ▒   ░ ░░   ░ ▒░░░▒░ ░ ░ ░ ░▒ ▒░ ░ ░  ░  ░▒ ░ ▒░
 ░    ░ ░ ░░ ░ ░ ░ ░ ░ ░      ░   ░ ░  ░░░ ░ ░ ░ ░░ ░    ░     ░░   ░ 
 ░      ░  ░     ░ ░                ░    ░     ░  ░      ░  ░   ░     
      ░        ░                                                      
                                by bkz.py

            """
        self.tokens = []
        self.file_mapping = {
            
            1: "tools/channel_spammer.py",
            2: "tools/role_spammer.py",
            3: "tools/delete_channels.py",
            4: "tools/delete_roles.py",
            5: "tools/ban_all_members.py",
            6: "tools/webhook_spammer.py",
            7: "tools/emoji_spammer.py",
            8: "tools/server_nuker.py",
            9: "tools/developer.py",
            
            11: "tools/voice_channel_spammer.py",
            12: "tools/join_server.py",
            13: "tools/leave_server.py",
            14: "tools/message_spammer.py",
            15: "tools/reaction_spammer.py",
            17: "tools/friend_request_spammer.py"
        }

    def clear(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def display_banner(self):
        self.clear()
        print(Colorate.Horizontal(Colors.purple_to_blue, Center.XCenter(self.banner)))
        print("\n")

    def handle_selection(self, option):
        filepath = self.file_mapping.get(option)
        if filepath:
            print(f"Executing: {filepath}")
            try:
                process = subprocess.Popen(['python', filepath], stdout=sys.stdout, stderr=sys.stderr)
                process.wait()
                print(f"{filepath} finished.")
                time.sleep(1)
            except FileNotFoundError:
                print(f"Error: {filepath} not found in the 'tools' folder!")
                time.sleep(1)
            except Exception as e:
                print(f"An error occurred while trying to execute {filepath}: {e}")
                time.sleep(1)
        else:
            print("Invalid option!")

    def nuker_menu(self):
        while True:
            self.display_banner()
            print(Colorate.Horizontal(Colors.blue_to_white, Center.XCenter("""
╔════════════════════════════════════════════╗
║         DISCORD NUKER HUD                  ║
╠════════════════════════════════════════════╣
║ 1. Channel Spammer                         ║
║ 2. Role Spammer                            ║
║ 3. Delete All Channels                     ║
║ 4. Delete All Roles                        ║
║ 5. Ban All Members                         ║
║ 6. Webhook Spammer                         ║
║ 7. Emoji Spammer                           ║
║ 8. Full Server Nuke                        ║
║ 9. developer bkz.py                        ║
║ N. Next Menu (Raider)                      ║
║ Q. Exit                                    ║
╚════════════════════════════════════════════╝
""")))
            choice = input("\n> ").lower()

            if choice == 'n':
                self.raider_menu()
                break
            elif choice == 'q':
                sys.exit()
            elif choice.isdigit() and 1 <= int(choice) <= 8:
                self.handle_selection(int(choice))
            else:
                print("Invalid option!")
                time.sleep(1)

    def raider_menu(self):
        while True:
            self.display_banner()
            print(Colorate.Horizontal(Colors.purple_to_blue, Center.XCenter("""
╔════════════════════════════════════════════╗
║               RAIDER MENU                  ║
╠════════════════════════════════════════════╣
║ 1. Add Tokens                              ║
║ 2. Token Checker                           ║
║ 3. Voice Channel Spammer                   ║
║                                            ║
║ !INFO ABOUT ME IM BKZ AND I LOVE           ║
║  SCIPTING MY MOTTO IS IF YOU DONT RULE THE ║
║  CODE YOU DONT RULE THE WORLD              ║
║                                            ║
║                                            ║
║                                            ║
║                                            ║
║                                            ║
║ B. Back to Nuker Menu                      ║
║ Q. Exit                                    ║
╚════════════════════════════════════════════╝
""")))
            choice = input("\n> ").lower()

            if choice == 'b':
                self.nuker_menu()
                break
            elif choice == 'q':
                sys.exit()
            elif choice == '1':
                self.add_tokens()
            elif choice == '2':
                self.check_tokens()
            elif choice.isdigit() and 3 <= int(choice) <= 9:
                self.handle_selection(int(choice) + 8)  
            else:
                print("Invalid option!")
                time.sleep(1)

    def add_tokens(self):
        self.display_banner()
        print(Colorate.Horizontal(Colors.purple_to_blue, Center.XCenter("ADD TOKENS")))
        print("\n")

        try:
            num_tokens = int(input("Enter number of tokens to add: "))
            print(f"\nEnter {num_tokens} tokens (one per line):")

            for i in range(num_tokens):
                token = input(f"Token {i+1}: ").strip()
                if token:
                    self.tokens.append(token)

            print(f"\nSuccessfully added {len(self.tokens)} tokens.")
            input("\nPress Enter to continue...")
        except ValueError:
            print("Please enter a valid number!")
            time.sleep(1)
            self.add_tokens()

    def check_tokens(self):
        self.display_banner()
        print(Colorate.Horizontal(Colors.red_to_white, Center.XCenter("CHECK TOKENS")))
        print("\n")

        if not self.tokens:
            print("No tokens to check! Please add tokens first.")
            input("\nPress Enter to continue...")
            return

        print(f"Checking {len(self.tokens)} tokens...\n")
        valid_tokens = []
        invalid_tokens = []

        for token in self.tokens:
            time.sleep(0.1)
            if len(token) > 50:  
                valid_tokens.append(token)
                print(f"[VALID] {token[:20]}...")
            else:
                invalid_tokens.append(token)
                print(f"[INVALID] {token}")

        print(f"\nResults: {len(valid_tokens)} valid, {len(invalid_tokens)} invalid")
        input("\nPress Enter to continue...")

    def start(self):
        self.nuker_menu()

if __name__ == "__main__":
    try:
        tool = DiscordTool()
        tool.start()
    except KeyboardInterrupt:
        print("\nExiting...")

        sys.exit()
