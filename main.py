import time 
import os
from colorama import Fore, Style
import subprocess 


def logo(text):
 logo_menu = """
    ███╗   ███╗███████╗  ███╗   ██╗██╗   ██╗
    ████╗ ████║██╔════╝████╗  ██║██║   ██║
    ██╔████╔██║█████╗  ██╔██╗ ██║██║   ██║
    ██║╚██╔╝██║██╔══╝  ██║╚██╗██║██║   ██║
    ██║ ╚═╝ ██║███████╗██║ ╚████║╚██████╔╝
    ╚═╝     ╚═╝╚══════╝╚═╝  ╚═══╝ ╚═════╝ 
                                          
 """;

 logo_player = """
    ██████╗ ██╗      █████╗ ██╗   ██╗███████╗██████╗ 
    ██╔══██╗██║     ██╔══██╗╚██╗ ██╔╝██╔════╝██╔══██╗
    ██████╔╝██║     ███████║ ╚████╔╝ █████╗  ██████╔╝
    ██╔═══╝ ██║     ██╔══██║  ╚██╔╝  ██╔══╝  ██╔══██╗
    ██║     ███████╗██║  ██║   ██║   ███████╗██║  ██║
    ╚═╝     ╚══════╝╚═╝  ╚═╝   ╚═╝   ╚══════╝╚═╝  ╚═╝
                                                     
""";
 if (text == "menu"):
  os.system("clear");
  print(Fore.RED + logo_menu);
 if(text == "player"):
  os.system("clear");
  print(Fore.GREEN + logo_player);
  
def exit_logo():
  print(Fore.RED+"[0]"+Fore.WHITE+" : Exit Player");

def funcs():
 print(Fore.GREEN+"[1]"+Fore.WHITE+" : Player::setSpeed(float)");
 print(Fore.GREEN+"[2]"+Fore.WHITE+" : LocalPlayer::setSneaking(bool)")
 print(Fore.GREEN+"[3]"+Fore.WHITE+" : LocalPlayer::setSprinting(bool)");
 print(Fore.GREEN+"[4]"+Fore.WHITE+" : LocalPlayer::setLeavingLevel(bool)");
 print(Fore.GREEN+"[5]"+Fore.WHITE+" : LocalPlayer::setPortalEffectTime(float)");

def author():
 print(Fore.RED+"\n           Author : "+Fore.BLUE+"Squate_Dev");
 print(Fore.RED+"Version"+Fore.WHITE+" : 0.0.3");
 
def menu(): 
 logo("menu");
 print(Fore.GREEN+"┓");
 print("┣"+Fore.RED+"[1]"+Fore.WHITE+" Player::")
 print(Fore.GREEN+"┣"+Fore.RED+"[2]"+Fore.WHITE+" MinecraftGame::")
 print(Fore.GREEN+"┣"+Fore.RED+"[3]"+Fore.WHITE+" LevelRenderer::")
 print(Fore.GREEN+"┛")
 text_input = input(Fore.YELLOW+" Введите Число : "+Fore.WHITE)
 if "1" in text_input.lower():
  os.system("clear");
  time.sleep(2);
  logo("player");
  exit_logo();
  funcs();
  author();
  text_1_input = input(Fore.BLUE+"Введите Число : ");
  if "0" in text_1_input.lower():
   os.system("clear");
   os.system("exit");
   time.sleep(0.2);
   menu();
  if "1" in text_1_input.lower():
   os.system("clear");
   
menu();
