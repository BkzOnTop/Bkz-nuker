from pystyle import Colors, Colorate, Center
from datetime import datetime

class DeveloperInfo:
    def __init__(self):
        self.banner = r"""
  ███████╗██████╗ ███████╗██████╗ ███████╗███╗   ██╗████████╗
  ██╔════╝██╔══██╗██╔════╝██╔══██╗██╔════╝████╗  ██║╚══██╔══╝
  ███████╗██████╔╝█████╗  ██████╔╝█████╗  ██╔██╗ ██║   ██║
  ╚════██║██╔══██╗██╔══╝  ██╔══██╗██╔══╝  ██║╚██╗██║   ██║
  ███████║██║  ██║███████╗██║  ██║███████╗██║ ╚████║   ██║
  ╚══════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═══╝   ╚═╝
        """

    def show_info(self):
        print(Colorate.Horizontal(Colors.red_to_white, Center.XCenter(self.banner)))
        print(Colorate.Horizontal(Colors.red_to_white, Center.XCenter(f"""
───────────────────────────────────────────────
 Developer  : FPERCENT
 Group      : FSOCIETY
 Role       : Python Developer / Designer
 Active Since: {14.07.().2024 - 1} - {26.10().2025}
 Motto       : "Control the Code. Control the System."
───────────────────────────────────────────────
        """)))

if __name__ == "__main__":
    DeveloperInfo().show_info()
