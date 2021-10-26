from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import time
from teams import team

# Run the Bot headless Mode
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--mute-audio")
chrome_options.add_argument("--window-size=1920x3000")
# Get Website Link
 # Get the chrome driver path
chrome_driver_path = "C:\ChromeDriver\chromedriver.exe"
# initialize Chrome Driver




class splinterlands_login:
    def __init__(self, email_address, password):
        self.email_address = email_address
        self.password = password
        self.driver = webdriver.Chrome(chrome_options=chrome_options, executable_path=chrome_driver_path)
        self.driver.implicitly_wait(60)
        #self.driver.set_window_size(1920, 3000)
        self.load_splinterlands()
        self.login()
        self.mana = None




    def load_splinterlands(self):
        
        self.driver.get("https://splinterlands.com/")

    def send_inputs(self, path, input):

        element = self.driver.find_element_by_xpath(path)

        if input == "send_keys":
            element.send_keys(Keys.ENTER)

        if not element.is_displayed():
            print("Element Not Display Reloading Browser")

        else:
            print("Typing " + input)
            return element.send_keys(input)

    def login(self):

        # Find the login button click
        self.driver.find_element_by_id("play_now_btn").click()
        print("Play Button Click...")
        time.sleep(5)

        # Input Username / Email Address
        print("Typing username...")
        self.send_inputs('//*[@id="email"]', input=self.email_address)
        # Input Password
        print("Typing password...")
        self.send_inputs('//*[@id="password"]', input=self.password)
        # Send Enter Key
        self.send_inputs('//*[@id="login_dialog_v2"]/div/div/div[2]/div/div[2]/form[2]/div[3]/div/button',
                         "send_keys")

        # Check if there's any pop up
        time.sleep(10)
        modal_pop_up = self.driver.find_element_by_xpath('//*[@id="dialog_container"]/div/div/div/div[1]/button')
        if modal_pop_up.is_displayed():
            print("Modal Popup Found... Closing it now!")
            modal_pop_up.click()
            print("Bot is ready for a battle!")



    def battle(self):

        try:
            # Find the battle button
            print("finding the battle button")
            battle = self.driver.find_element_by_xpath('//*[@id="battle_category_btn"]')
            # If battle button is not displayed try finding it again
            print("battle button found...")
            battle.click()
            print("battle button click")
        except TimeoutError:
            print("Page Take Too long To Load Retrying....")

    def search_match(self):

        try:
            time.sleep(10)
            mana = self.driver.find_element_by_xpath('//*[@id="dialog_container"]/div/div/div/div[2]/div[2]/div/section/div/div[2]/div/div/div/div/div')
            print('mana displayed?:' + str(mana.is_displayed()))
            self.mana = int(mana.text)
            print('mana ' + mana.text)
            create_team = self.driver.find_element_by_xpath(
                '//*[@id="dialog_container"]/div/div/div/div[2]/div[3]/div[2]/button')
            print("create team button found...")
            create_team.click()
            print("create team button click")
        except TimeoutError:
            print("Page Take Too long To Load Retrying....")

    def create_team(self):
        composition = team(self.mana)
        for monster in composition:
            time.sleep(2)
            summoner = self.driver.find_element_by_css_selector(f"*[card_detail_id='{monster}']")
            summoner.click()
        
    def battle_start(self):
        battle = self.driver.find_element_by_xpath('//*[@id="page_container"]/div/div[1]/div/button')
        battle.click()
        print("Battle Begins")
        WebDriverWait(self.driver, 500).until(EC.presence_of_all_elements_located(('id', 'btnRumble')))
        time.sleep(5)
        print("Rumble Button Found...")
        btn_rumble = self.driver.find_element_by_xpath('//*[@id="btnRumble"]')
        btn_rumble.click()
        print("Battle Started Looking for skip button")
        time.sleep(10)
        skip = self.driver.find_element_by_xpath('//*[@id="btnSkip"]')
        skip.click()
        print("Skip Button Found, Skipping Match")
        time.sleep(10)
        self.driver.close()
        print("Closing Match")
        print("====================================")


















#//*[@id="dialog_container"]/div/div/div/div[2]/div[2]/div/section/div/div[2]/div/div/div/div/div

# Create team xpath
# skip to result xpath //*[@id="btnSkip"]
# close xpath after skipped //*[@id="dialog_container"]/div/div/div/div[2]/div[3]/div[3]/button
# https://splinterlands.com/?p=create_team2

# Earth
# 27
# 174
# 221

# //*[@id="page_container"]/div/div[1]/div/button
# //*[@id="btnRumble"]
# //*[@id="btnSkip"]
# //*[@id="dialog_container"]/div/div/div/div[2]/div[3]/div[3]/button
