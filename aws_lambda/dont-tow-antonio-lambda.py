import json
import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import logging

# Set up logging
logger = logging.getLogger()
logger.setLevel(logging.INFO)

def get_chrome_options():
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument('--window-size=1280x1696')
    chrome_options.add_argument('--single-process')
    chrome_options.add_argument('--disable-dev-shm-usage')
    chrome_options.binary_location = '/opt/chrome/chrome'
    return chrome_options

def lambda_handler(event, context):
    try:
        # Initialize the driver with Chrome options
        options = get_chrome_options()
        driver = webdriver.Chrome(
            executable_path="/opt/chromedriver",
            options=options
        )
        wait = WebDriverWait(driver, 10)
        
        # Navigate to the page
        driver.get("https://app.apartmentpermits.com/guest")
        
        # Find and interact with dropdown
        dropdown = wait.until(EC.presence_of_element_located((By.ID, "pv_id_1")))
        dropdown.click()
        
        # Find and interact with search bar
        search_bar = wait.until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, "input.p-dropdown-filter.p-inputtext")))
        search_bar.click()
        search_bar.send_keys("pecancreek")
        
        # Select first option
        first_option = wait.until(EC.presence_of_element_located(
            (By.XPATH, "//ul[@id='pv_id_1_list']/li[1]")))
        first_option.click()
        
        # Fill in Unit Number
        unit_number_input = wait.until(EC.presence_of_element_located(
            (By.XPATH, "//label[contains(text(), 'Unit Number')]/following-sibling::input")))
        unit_number_input.send_keys("203")
        
        # Fill in Phone PIN
        phone_pin_input = wait.until(EC.presence_of_element_located(
            (By.XPATH, "//label[contains(text(), 'Last 4 of Resident Phone or Guest PIN')]/following-sibling::input")))
        phone_pin_input.send_keys("2275")
        
        # Click Sign In
        sign_in_button = wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//button[@aria-label='Sign In']")))
        sign_in_button.click()
        
        # Fill in Year
        year_input = wait.until(EC.presence_of_element_located(
            (By.XPATH, "//label[contains(text(), 'Year')]/following-sibling::input")))
        year_input.send_keys("2012")
        
        # Handle Make/Model dropdown
        make_model_dropdown = wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//label[contains(text(), 'Make / Model')]/following-sibling::div")))
        make_model_dropdown.click()
        
        make_model_search = wait.until(EC.presence_of_element_located(
            (By.XPATH, "//input[@class='p-dropdown-filter p-inputtext p-component']")))
        make_model_search.send_keys("honda")
        
        first_make_option = wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//li[@role='option']")))
        first_make_option.click()
        
        # Handle Color dropdown
        color_dropdown = wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//label[contains(text(), 'Select a Color')]/following-sibling::div")))
        color_dropdown.click()
        
        color_search = wait.until(EC.presence_of_element_located(
            (By.XPATH, "//input[@class='p-dropdown-filter p-inputtext p-component']")))
        color_search.send_keys("grey")
        
        first_color_option = wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//li[@role='option']")))
        first_color_option.click()
        
        # Fill in License Plate
        license_plate_input = wait.until(EC.presence_of_element_located(
            (By.XPATH, "//label[contains(text(), 'License Plate')]/following-sibling::input")))
        license_plate_input.send_keys("tvl0161")
        
        # Click first Confirm button
        confirm_button = wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//button[span[contains(text(), 'Confirm')]]")))
        confirm_button.click()
        
        # Click second Confirm button
        confirm_button = wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//button[span[contains(text(), 'Confirm')]]")))
        confirm_button.click()
        
        # Confirm license plate
        confirm_license_input = wait.until(EC.presence_of_element_located(
            (By.XPATH, "//label[contains(text(), 'Confirm license plate')]/following-sibling::input")))
        confirm_license_input.send_keys("tvl0161")
        
        # Click Save button
        save_button = wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//button[span[contains(text(), 'Save')]]")))
        save_button.click()
        
        # Check for success/failure
        try:
            success_message = wait.until(EC.presence_of_element_located(
                (By.CLASS_NAME, "p-toast-message-success")))
            status = "Success"
        except:
            try:
                failure_message = wait.until(EC.presence_of_element_located(
                    (By.CLASS_NAME, "p-toast-message-error")))
                status = "Failed"
            except:
                status = "Unknown status"
        
        driver.quit()
        
        return {
            'statusCode': 200,
            'body': json.dumps({
                'message': 'Parking permit renewal process completed',
                'status': status
            })
        }
        
    except Exception as e:
        logger.error(f"Error: {str(e)}")
        if 'driver' in locals():
            driver.quit()
        return {
            'statusCode': 500,
            'body': json.dumps({
                'message': 'Error during parking permit renewal',
                'error': str(e)
            })
        }