from time import sleep
import random
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

# URL of the website to be accessed
website = "https://twstypes.typingclub.com/sportal/"

# Create a new instance of a Chrome WebDriver
driver = webdriver.Chrome()

# Navigate to the specified website
driver.get(website)
sleep(5)  # Wait for 5 seconds to allow the page to load
og_window = driver.current_window_handle
# Find and click the login button
login = driver.find_element(By.CSS_SELECTOR, "button.btn.btn-integration")
login.click()

# Switch to the new window that opens after clicking login
new_window = driver.window_handles[-1]
driver.switch_to.window(new_window)
sleep(2)  # Wait for 2 seconds for the new window to be ready

# Enter the username in the login field
login = driver.find_element(By.CLASS_NAME, "whsOnd.zHQkBf")
login.send_keys("tmartin29@wilberforceschool.org")
sleep(2)  # Wait for 2 seconds after entering the username

# Find and click the next button in the login process
button = driver.find_element(By.CSS_SELECTOR,
                             "button.VfPpkd-LgbsSe.VfPpkd-LgbsSe-OWXEXe-k8QpJ.VfPpkd-LgbsSe-OWXEXe-dgl2Hf.nCP5yc.AjY5Oe.DuMIQc.LQeN7.BqKGqe.Jskylb.TrZEUc.lw1w4b")
button.click()

# Wait for the next page to load
sleep(4)

# Enter the password in the password field
login = driver.find_element(By.CLASS_NAME, "whsOnd.zHQkBf")
login.send_keys("showpassword")

# Find and click the final login button
button = driver.find_element(By.CSS_SELECTOR,
                             "button.VfPpkd-LgbsSe.VfPpkd-LgbsSe-OWXEXe-k8QpJ.VfPpkd-LgbsSe-OWXEXe-dgl2Hf.nCP5yc.AjY5Oe.DuMIQc.LQeN7.BqKGqe.Jskylb.TrZEUc.lw1w4b")
button.click()

# Sleep
sleep(6)

## DO THE REST OF THE STUFF
# Switch to next window
driver.switch_to.window(og_window)

# Click start
start_button = driver.find_element(By.CLASS_NAME, "btn.btn-primary.lp-card-btn")
start_button.click()
sleep(3)

# Start next lesson
next_lesson = driver.find_elements(By.CLASS_NAME, "box-container.is_unlocked")
next_lesson[-1].click()
sleep(4)


# Typing
def typescreen():
    letters = driver.find_elements(By.CLASS_NAME, "token_unit._clr")
    print(len(letters))
    action = ActionChains(driver)
    todo = ""
    for letter in letters:
        todo += letter.text

    for char in todo:
        if random.randint(0, 15):
            action.send_keys(char).perform()
        else:
            action.send_keys("A")
        sleep(random.uniform(0, .4))


while True:
    for i in range(5):
        typescreen()
    sleep(5)
    action = ActionChains(driver)
    action.send_keys(Keys.ENTER).perform()
    sleep(3)

