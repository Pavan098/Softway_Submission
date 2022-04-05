
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# launch new browser
chrome_option = webdriver.ChromeOptions()
chrome_option.add_argument('--Guest')
driver = webdriver.Chrome(executable_path="F:\\chromedriver\\chromedriver.exe")
driver.implicitly_wait(10)

# Open URL
driver.get("https://www.flipkart.com/")
driver.maximize_window()
print(driver.title)

# Search for the product you like(Any phones)
driver.find_element(By.XPATH, "/html/body/div[2]/div/div/button").click()
driver.implicitly_wait(20)
driver.find_element(By.CLASS_NAME, "_3704LK").send_keys("redmi phones")
driver.find_element(By.XPATH, "//button[@type='submit']").click()

# Click on the first Item from the list
driver.implicitly_wait(20)
driver.find_element(By.XPATH, "//*[@id='container']/div/div[3]/div[1]/div[2]/div[2]/div/div/div/a/div[2]/div[1]/div[1]").click()

# print the price of the item
driver.implicitly_wait(50)

driver.switch_to.window(driver.window_handles[1])

firstprice = driver.find_element(By.XPATH, "//*[@id='container']/div/div[3]/div[1]/div[2]/div[3]/div/div[4]/div[1]/div/div[1]").text

print(firstprice)
url = driver.current_url

# Add to cart in guest mode
driver = webdriver.Chrome(executable_path="F:\\chromedriver\\chromedriver.exe", options=chrome_option)

driver.get(url)

driver.find_element(By.XPATH, "//button[@class = '_2KpZ6l _2U9uOA _3v1-ww']").click()
driver.implicitly_wait(30)

# Verify it Redirects to Cart Page
driver.find_element(By.CLASS_NAME, "_3g_HeN").text.__contains__("My Cart")

# Increase the quantity by 1
driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")

element = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='+']")))

driver.find_element(By.XPATH, "//button[normalize-space()='+']").click()

# Print the price after addition of quantity
element = WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.XPATH, "//input[@value='2']")))
secondprice = driver.find_element(By.XPATH, "//*[@id='container']/div/div[2]/div/div/div[1]/div/div[2]/div/div[1]/div[1]/span[1]").text
print(secondprice)

# close the browser
driver.quit()