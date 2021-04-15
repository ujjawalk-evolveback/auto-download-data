from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# To login the url automatically and download the xlxs file
def do_login(driver: webdriver, start_date, end_date, property):
    # Getting Home Page
    driver.get("https://live.mycloudhospitality.com/Login/Common/Index.aspx")
    # Disabling Captcha
    driver.execute_script('$("#lblHiddenSuppressCaptchaValidation")[0].value = "Y"')
    # Login and Passsword {FILL IT BEFORE RUNNING}
    driver.find_element_by_name('txtUserNameEmailId').send_keys('*********')
    driver.find_element_by_name('txtPassword').send_keys('*********')
    #Click Login
    driver.find_element_by_name('btnLogin').click()
    wait_short = WebDriverWait(driver, 10)
    wait_long = WebDriverWait(driver, 400)
    # Select the Property based on argument passed
    element = wait_short.until(
        EC.element_to_be_clickable((By.ID, f"dgChangeProperty_btnOpenChangeProperty_{property}"))
    )
    element.click()
    element = wait_short.until(
        EC.element_to_be_clickable((By.ID, "imgCPMS"))
    )
    element.click()
    element = wait_short.until(
        EC.element_to_be_clickable((By.ID, "btnReportsWelcome"))
    )
    element.click()

    element = wait_short.until(
        EC.element_to_be_clickable((By.ID, "txtSearchReports"))
    )
    element.send_keys('Guest Transaction')

    element = wait_short.until(
        EC.element_to_be_clickable((By.ID, "btnSearchReports"))
    )
    element.click()
    wait_short.until(
        EC.invisibility_of_element((By.ID, "overlayProcess"))
    )
    element = wait_short.until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="dgReportsList"]/tbody/tr[3]/td[4]'))
    )
    element.click()
    wait_short.until(
        EC.element_to_be_clickable((By.ID, "cmbDatefrom"))
    )
    # Passing in start and end date based on parameters given
    driver.execute_script(f'$("#cmbDatefrom")[0].value = {start_date}')
    driver.execute_script(f'$("#cmbDateto")[0].value = {end_date}')

    element = wait_short.until(
        EC.element_to_be_clickable((By.ID, "btnOkReports"))
    )
    element.click()
    wait_short.until(
        EC.invisibility_of_element((By.ID, "overlayProcess"))
    )

    wait_long.until(
        EC.invisibility_of_element((By.ID, "overlayProcess"))
    )
    #End of Loop
    time.sleep(5)
    return