from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from colorama import Fore
from pystyle import Center, Colors, Colorate
import os
import time


program = True
ProxyCount = 0

def proxy_checker():
    global ProxyCount
    ProxyCount += 1
    print(Colorate.Vertical(Colors.cyan_to_blue, Center.XCenter(f"Viewer {ProxyCount} Sent")))
    time.sleep(1)



def start():
    os.system(f"title Kichi779 Twitch Vod/Clip Bot .gg/AFV9m8UXuT / kichi779shop.mysellix.io")

    print(Colorate.Vertical(Colors.blue_to_white, Center.XCenter("""
           
                 ▄█   ▄█▄  ▄█    ▄████████    ▄█    █▄     ▄█  
                ███ ▄███▀ ███   ███    ███   ███    ███   ███  
                ███▐██▀   ███▌  ███    █▀    ███    ███   ███▌ 
               ▄█████▀    ███▌  ███         ▄███▄▄▄▄███▄▄ ███▌ 
              ▀▀█████▄    ███▌  ███        ▀▀███▀▀▀▀███▀  ███▌ 
                ███▐██▄   ███   ███    █▄    ███    ███   ███  
                ███ ▀███▄ ███   ███    ███   ███    ███   ███  
                ███   ▀█▀ █▀    ████████▀    ███    █▀    █▀   
                ▀                                             
    Edit the code, but please don't remove my name. do not make the sale.
                    Discord discord.gg/fesaScZqpn       
                    Github  https://github.com/kichi779   
                    Shop  kichi779shop.mysellix.io     
                       
                      
                      """)))



    chrome_path = 'C:\Program Files\Google\Chrome\Application\chrome.exe'
    driver_path = 'chromedriver.exe'

    vodclip = input(Colorate.Vertical(Colors.green_to_blue, Center.XCenter ("Enter vod or clip: ")))
    print()
    twitch_clip_id = input(Colorate.Vertical(Colors.green_to_blue, Center.XCenter ("Enter your Vod/Clip id: ")))
    print()
    twitch_user_name = input(Colorate.Vertical(Colors.green_to_blue, Center.XCenter("Enter your username: ")))
    print()

    proxy_count = int(input(Colorate.Vertical(Colors.cyan_to_blue, Center.XCenter ("How many Clip/Vod Views do you want to open?: "))))


    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--disable-logging')
    chrome_options.add_argument('--log-level=3')
    chrome_options.add_argument('--disable-extensions')
    chrome_options.add_argument("--mute-audio")
    chrome_options.add_argument("--hardware-acceleration-enabled")
    chrome_options.add_argument('--disable-dev-shm-usage')
    chrome_options.binary_location = chrome_path
    driver = webdriver.Chrome(executable_path=driver_path, options=chrome_options)

    driver.get('https://www.blockaway.net')

    text_box = driver.find_element(By.ID, 'url')


    text_box.send_keys(f'www.twitch.tv/{twitch_user_name}/{vodclip}/{twitch_clip_id}')


    text_box.send_keys(Keys.RETURN)

    time.sleep(15)
    proxy_checker()
    for i in range(proxy_count):
        driver.execute_script("window.open('https://www.blockaway.net/')")
        driver.switch_to.window(driver.window_handles[-1])
        text_box = driver.find_element(By.ID, 'url')
        text_box.send_keys(f'www.twitch.tv/{twitch_user_name}/{vodclip}/{twitch_clip_id}')
        text_box.send_keys(Keys.RETURN)
        proxy_checker()
        time.sleep(30)

    print(Colorate.Vertical(Colors.blue_to_cyan, Center.XCenter("---------------------------------------------------")))
    print(Colorate.Horizontal(Colors.red_to_blue, Center.XCenter("Viewers have all been sent.")))
    print(Colorate.Horizontal(Colors.red_to_blue, Center.XCenter("Press enter to continue.")))
    print(Colorate.Vertical(Colors.blue_to_cyan, Center.XCenter("---------------------------------------------------")))
    QUIT = input(Colorate.Vertical(Colors.cyan_to_blue, Center.XCenter("Type Quit to close program: ")))
    print(Colorate.Vertical(Colors.blue_to_cyan, Center.XCenter("---------------------------------------------------")))
    if QUIT == "Quit":
        program = False
    else:
        print(Colorate.Diagonal(Colors.red, Center.XCenter("...")))
while program:
    start() 
    
    
    # ==========================================
# Copyright 2023 Kichi779

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
# ==========================================
