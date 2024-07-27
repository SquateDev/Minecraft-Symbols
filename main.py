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
  time.sleep(0.3);
  print(Fore.RED+"[01]"+Fore.WHITE+" : Exit ALL");
  print(Fore.RED+"[0]"+Fore.WHITE+" : Exit Player");

def funcs():
 print(Fore.GREEN+"[1]"+Fore.WHITE+" : Player::setSpeed(float)");
 time.sleep(0.3);
 print(Fore.GREEN+"[2]"+Fore.WHITE+" : LocalPlayer::setSneaking(bool)")
 time.sleep(0.3);
 print(Fore.GREEN+"[3]"+Fore.WHITE+" : LocalPlayer::setSprinting(bool)");
 time.sleep(0.3);
 print(Fore.GREEN+"[4]"+Fore.WHITE+" : LocalPlayer::setLeavingLevel(bool)");
 time.sleep(0.3);
 print(Fore.GREEN+"[5]"+Fore.WHITE+" : LocalPlayer::setPortalEffectTime(float)");
 time.sleep(0.3);
 print(Fore.GREEN+"[6]"+Fore.WHITE+" : LocalPlayer::setPos(Vec3 const&)");
 time.sleep(0.3);
 print(Fore.GREEN+"[7]"+Fore.WHITE+" : Player::setPlayerGameType(GameType)");
 time.sleep(0.3);
 print(Fore.GREEN+"[8]"+Fore.WHITE+" : Player::isInCreativeMode()");
 time.sleep(0.3);
 print(Fore.GREEN+"[9]"+Fore.WHITE+" : Player::getSelectedItem()");
 time.sleep(0.3);
 print(Fore.GREEN+"[10]"+Fore.WHITE+" : LocalPlayer::setOffhandSlot(ItemInstance const&)");
 time.sleep(0.3);
 print(Fore.GREEN+"[11]"+Fore.WHITE+" : LocalPlayer::move(Vec3 const&)");
 
def author():
 time.sleep(0.4);
 print(Fore.RED+"\nAuthor : "+Fore.BLUE+"Squate_Dev");
 print(Fore.RED+"Version"+Fore.WHITE+" : 0.0.3");

def search(num):
 if(num == "1"):
  print(Fore.RED+"┣"+Fore.WHITE+"NAME : Player::setSpeed(float)");
  print(Fore.RED+"┣"+Fore.WHITE+"SYMBOL : _ZN6Player8setSpeedEf");
  print(Fore.RED+"┣"+Fore.WHITE+"ARGUMENT : float");
  print(Fore.RED+"┣"+Fore.WHITE+"CLASS : Player");
  print(Fore.RED+"┣"+Fore.WHITE+"NAME : setSpeed");  
 if(num == "2"):  
  print("Hack!");

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
  time.sleep(0.9);
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
  if "01" in text_1_input.lower():
   os.system("clear");
   os.system("exit");
   print(Fore.RED+"Exit!!!");
  if text_1_input.lower():
   os.system("clear");
   logo("player");
   search(text_1_input);
   
menu();
