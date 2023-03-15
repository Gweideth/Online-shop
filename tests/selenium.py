import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get(url="http://127.0.0.1:8000/admin")


def element_is_clickable():
    # Tests to make sure all subpages open correctly

    # Login to admin panel
    driver.find_element("xpath", '//*[@id="id_username"]').send_keys("admin")
    driver.find_element("xpath", '//*[@id="id_password"]').send_keys("admin")
    time.sleep(1)
    driver.find_element("xpath", '/html/body/div/div[2]/div/div[1]/div/form/div[3]/input').click()

    # Return to website
    time.sleep(1)
    driver.find_element("xpath", '/html/body/div/div[1]/div[2]/a[1]').click()
    # Move to About_us
    time.sleep(1)
    driver.find_element("xpath", '/html/body/div[1]/ul/li[2]/a').click()
    # Move to News
    time.sleep(1)
    driver.find_element("xpath", '/html/body/div[4]/div[1]/h2/a').click()
    # Move to News Detail by clicking on title
    time.sleep(1)
    driver.find_element("xpath", '/html/body/div[1]/ul/li[1]/a').click()
    # Move to shop
    time.sleep(1)
    driver.find_element("xpath", '/html/body/div[1]/ul/li[3]/a').click()
    # Check some categories
    time.sleep(1)
    driver.find_element("xpath", '/html/body/div[4]/div[1]/ul/li[2]/a').click()
    time.sleep(1)
    driver.find_element("xpath", '/html/body/div[4]/div[1]/ul/li[4]/a').click()
    # Click on product
    time.sleep(1)
    driver.find_element("xpath", '/html/body/div[4]/div[2]/div/div[1]/a[2]').click()
    # Add to cart
    time.sleep(1)
    driver.find_element("xpath", '/html/body/div[4]/div/div/form/input[3]').click()
    # Continue shopping
    time.sleep(1)
    driver.find_element("xpath", '/html/body/div[4]/p/a[1]').click()
    # Return to cart
    time.sleep(1)
    driver.find_element("xpath", '/html/body/div[2]/div/a').click()
    # Ordering
    time.sleep(1)
    driver.find_element("xpath", '/html/body/div[4]/p/a[2]').click()
    time.sleep(2)

def add_new_elements():
    # Test to see if the addition of an item is going well

    # Login to admin panel
    driver.get(url="http://127.0.0.1:8000/admin")
    # Move to News Panel
    time.sleep(1)
    driver.find_element("xpath", '/html/body/div/div[2]/div/div[1]/div[1]/div[2]/table/tbody/tr[2]/th/a').click()
    # Add new News
    time.sleep(1)
    driver.find_element("xpath", '/html/body/div/div[3]/div/div[1]/div/ul/li/a').click()
    # Edit News
    time.sleep(1)
    driver.find_element("xpath", '//*[@id="id_title"]').send_keys("Test0000001")
    driver.find_element("xpath", '//*[@id="id_author"]').click()
    driver.find_element("xpath",
                        '/html/body/div[1]/div[3]/div/div[1]/div/form/div/fieldset/div[4]/div/div/select/option[2]').click()
    driver.find_element("xpath", '//*[@id="id_body"]').send_keys("Test001 Test001 Test001")
    driver.find_element("xpath", '//*[@id="id_status"]').click()
    driver.find_element("xpath",
                        '/html/body/div[1]/div[3]/div/div[1]/div/form/div/fieldset/div[6]/div/select/option[2]').click()
    driver.find_element("xpath", '/html/body/div[1]/div[3]/div/div[1]/div/form/div/div/input[1]').click()
    driver.find_element("xpath", '/html/body/div/div[1]/div[2]/a[1]').click()
    time.sleep(1)
    driver.find_element("xpath", '/html/body/div[1]/ul/li[2]/a').click()
    time.sleep(2)
    # Check if all is OK
    driver.find_element("xpath", '/html/body/div[4]/div[1]/h2/a').click()
    time.sleep(3)

    #Deleting News
    driver.get(url="http://127.0.0.1:8000/admin")
    time.sleep(3)
    driver.find_element("xpath", '/html/body/div/div[2]/div/div[1]/div[1]/div[2]/table/tbody/tr[2]/th/a').click()
    driver.find_element("xpath",
                        '/html/body/div/div[3]/div/div[1]/div/div/div[1]/form/div[2]/table/thead/tr/th[4]/div[2]/a').click()
    driver.find_element("xpath",
                        '//html/body/div/div[3]/div/div[1]/div/div/div[1]/form/div[2]/table/tbody/tr[1]/th/a').click()
    driver.find_element("xpath", '/html/body/div[1]/div[3]/div/div[1]/div/form/div/div/p/a').click()
    driver.find_element("xpath", '/html/body/div/div[3]/div/div[1]/form/div/input[2]').click()
    time.sleep(5)


element_is_clickable()
add_new_elements()
