import asyncio
import aiohttp
import os
import random
import time
from pystyle import Colors, Colorate, Center

class UltimateRoleSpammer:
    def __init__(self):
        self.banner = r"""
  ________  ________  ___       _______      
|\   __  \|\   __  \|\  \     |\  ___ \     
\ \  \|\  \ \  \|\  \ \  \    \ \   __/|    
 \ \   _  _\ \  \\\  \ \  \    \ \  \_|/__  
  \ \  \\  \\ \  \\\  \ \  \____\ \  \_|\ \ 
   \ \__\\ _\\ \_______\ \_______\ \_______\
    \|__|\|__|\|_______|\|_______|\|_______|
                                            
                                            
                                                               
        """
        self.token = ""
        self.guild_id = ""
        self.role_name_prefix = "FSOCIETY" 
        self.role_count = 50
        self.delay = 0.5
        self.session = None
        self.colors = [0xff0000, 0x00ff00, 0x0000ff, 0xffff00, 0xff00ff, 0x00ffff,
                       0xffa500, 0x800080, 0x008000, 0x4682b4, 0xff69b4] 

    def clear(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def display_menu(self):
        self.clear()
        print(Colorate.Horizontal(Colors.purple_to_blue, Center.XCenter(self.banner)))
        print("\n")
        print(Colorate.Horizontal(Colors.purple_to_blue, Center.XCenter("Role spammer by FPERCENT")))
        print("\n")

    async def create_roles(self):
        headers = {
            "Authorization": f"Bot {self.token}",
            "Content-Type": "application/json"
        }

        for i in range(self.role_count):
           
            random_suffix = ''.join(random.choices('abcdefghijklmnopqrstuvwxyz0123456789', k=5))
            role_name = f"{self.role_name_prefix}-{random_suffix}"
            payload = {
                "name": role_name,
                "color": random.choice(self.colors),
                "hoist": True,
                "mentionable": True,
                "permissions": "0"
            }
            try:
                async with self.session.post(
                    f"https://discord.com/api/v9/guilds/{self.guild_id}/roles",
                    headers=headers,
                    json=payload
                ) as resp:
                    if resp.status == 200:
                        role = await resp.json()
                        print(Colorate.Horizontal(Colors.purple_to_blue,
                            Center.XCenter(f"[+] Role created: {role['name']} [+]")))
                        await asyncio.sleep(self.delay)
                    else:
                        error_data = await resp.text()
                        print(Colorate.Horizontal(Colors.purple_to_blue,
                            Center.XCenter(f"[!] Error creating role (Status {resp.status}): {error_data} [!]")))
                        await asyncio.sleep(5) 
            except Exception as e:
                print(Colorate.Horizontal(Colors.purple_to_blue,
                    Center.XCenter(f"[!] Unexpected error: {str(e)} [!]")))
                await asyncio.sleep(5)

    async def run(self):
        self.session = aiohttp.ClientSession()
        print(Colorate.Horizontal(Colors.purple_to_blue,
            Center.XCenter("\n[!] ROLE CHAOS UNLEASHED! [!]\n"))) 
        await self.create_roles()
        await self.session.close()
        print(Colorate.Horizontal(Colors.purple_to_blue,
            Center.XCenter("\n[+] SERVER FLOODED WITH ROLES! [+]"))) 

    def get_inputs(self):
        self.display_menu()
        self.token = input(Colorate.Horizontal(Colors.purple_to_blue,
            Center.XCenter(" Bot Token: "))).strip()

        self.display_menu()
        self.guild_id = input(Colorate.Horizontal(Colors.purple_to_blue,
            Center.XCenter(" Server ID: "))).strip()

        self.display_menu()
        self.role_name_prefix = input(Colorate.Horizontal(Colors.purple_to_blue,
            Center.XCenter(" Role Prefix (Default: FSOCIETY): "))).strip() or "FSOCIETY" 

        self.display_menu()
        self.role_count = int(input(Colorate.Horizontal(Colors.purple_to_blue,
            Center.XCenter(" Role Count (Default: 50): ")) or "50"))

        self.display_menu()
        self.delay = float(input(Colorate.Horizontal(Colors.purple_to_blue,
            Center.XCenter(" Delay Between Roles (Default: 0.5): ")) or "0.5"))

        self.display_menu()
        print(Colorate.Horizontal(Colors.purple_to_blue,
            Center.XCenter(" WARNING: THIS WILL FLOOD THE SERVER WITH ROLES")))
        time.sleep(2)

        confirm = input(Colorate.Horizontal(Colors.purple_to_blue,
            Center.XCenter("\nStart Attack? (y/n): "))).lower()

        if confirm == 'y':
            asyncio.run(self.run())
        else:
            print(Colorate.Horizontal(Colors.purple_to_blue,
                Center.XCenter("\n[!] OPERATION CANCELLED [!]\n")))

if __name__ == "__main__":
    spammer = UltimateRoleSpammer()
    spammer.get_inputs()
    input(Colorate.Horizontal(Colors.purple_to_blue,
        Center.XCenter("\nPress ENTER to exit...")))