from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

profileDir = r'C:\Users\Administrator\AppData\Roaming\Mozilla\Firefox\Profiles\jn7h4mc2.default-release'
options = webdriver.FirefoxOptions()
profile = webdriver.FirefoxProfile(profileDir)
profile.set_preference("javascript.enabled", True)
options.profile = profile

driver = webdriver.Firefox(options=options)
driver.get("https://cp.kuaishou.com/article/publish/video")


button = WebDriverWait(driver, 150).until(EC.element_to_be_clickable(
    (By.CSS_SELECTOR, "button[class='SOCr7n1uoqI-']")))

file_input = driver.find_element(By.CSS_SELECTOR, "input[type*='file']")
print('file_input', file_input)

video_path = r"E:\Github\transport\videos\audio.mp4"
file_input.send_keys(video_path)


# driver.quit()
