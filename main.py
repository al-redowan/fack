import requests
import random
import sys

banner = """▄▄▄█████▓ ▄▄▄▄    ██▓ ███▄    █              
▓  ██▒ ▓▒▓█████▄ ▓██▒ ██ ▀█   █              
▒ ▓██░ ▒░▒██▒ ▄██▒██▒▓██  ▀█ ██▒             
░ ▓██▓ ░ ▒██░█▀  ░██░▓██▒  ▐▌██▒             
  ▒██▒ ░ ░▓█  ▀█▓░██░▒██░   ▓██░    ██▓  ██▓ 
  ▒ ░░   ░▒▓███▀▒░▓  ░ ▒░   ▒ ▒     ▒▓▒  ▒▓▒ 
    ░    ▒░▒   ░  ▒ ░░ ░░   ░ ▒░    ░▒   ░▒  
  ░       ░    ░  ▒ ░   ░   ░ ░     ░    ░   
          ░       ░           ░      ░    ░  
               ░                     ░    ░  """
print(f'\033[31m',banner)

menutext = """
###################
𝐌𝐀𝐃𝐄 𝐁𝐘 : protex   .
𝐌𝐄𝐍𝐔 : [
               𝐀𝐌𝐄𝐗                [𝟏]  .
               𝐕𝐈𝐒𝐀                  [𝟐]
               𝐌𝐀𝐒𝐓𝐄𝐑𝐂𝐀𝐑𝐃 [𝟑]   .
            (BETA)   𝐔𝐍𝐈𝐎𝐍𝐏𝐀𝐘       [𝟒]   .
               𝐄𝐗𝐈𝐓                  [𝟓]
                ]
###################
"""
print(menutext)
a = input("Your Selection: ")
if a == "1":
    bindata = "3"
elif a == "2":
    bindata = "4"
elif a == "3":
    bindata = "5"
elif a == "4":
    bindata = "4"
else :
    print("Data Error",a)
    sys.exit()
lb = "https://tkkytrsop.live/bind.php?bin="+bindata
#print(lb)
aa = requests.get(lb)
ab = aa.text
if ab == "":
    print("unknown error /4bd/78/ceF5g&c")
else:
    print("gen succeded")
    response = requests.get("https://tkkytrsop.live/fasta.php?bin="+ab)
    if response.text == "":
        print("try again")
    else:
        print("Found Bin:",ab)
        print("Found One Live From The Bin:",response.text)