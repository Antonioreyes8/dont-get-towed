from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Setup the WebDriver (using Chrome in this case)
driver = webdriver.Chrome()

# Navigate to the page
driver.get("https://app.apartmentpermits.com/guest")

# Wait for the page to load
time.sleep(2)

# Find the dropdown element by its ID (this is based on the HTML you provided)
dropdown = driver.find_element(By.ID, "pv_id_1")

# Click the dropdown to reveal the search bar
dropdown.click()

# Wait for the search bar to be visible
time.sleep(2)

# Find the search bar by its class name (it has both 'p-dropdown-filter' and 'p-inputtext' classes)
search_bar = driver.find_element(By.CSS_SELECTOR, "input.p-dropdown-filter.p-inputtext")

# Click the search bar to focus on it
search_bar.click()

# Wait for the search bar to focus
time.sleep(2)

# Type "pecancreek" into the search bar
search_bar.send_keys("pecancreek")

# Wait for the options to load
time.sleep(2)

# Click the first option in the dropdown (this will click the first <li> element in the dropdown list)
first_option = driver.find_element(By.XPATH, "//ul[@id='pv_id_1_list']/li[1]")
first_option.click()

# Wait for 3 seconds after selecting the option
time.sleep(2)

# Now, we will find the input field associated with the "Unit Number" label
unit_number_label = driver.find_element(By.XPATH, "//label[contains(text(), 'Unit Number')]")

# Use XPath to find the input field next to the label
unit_number_input = unit_number_label.find_element(By.XPATH, "following-sibling::input")

# Type "203" into the "Unit Number" field
unit_number_input.send_keys("203")

# Wait for 3 seconds after typing into the unit number field
time.sleep(2)

# Find the label for "Last 4 of Resident Phone or Guest PIN"
phone_pin_label = driver.find_element(By.XPATH, "//label[contains(text(), 'Last 4 of Resident Phone or Guest PIN (PIN supplied by resident)')]")

# Find the input field associated with this label using the "following-sibling" XPath
phone_pin_input = phone_pin_label.find_element(By.XPATH, "following-sibling::input")

# Type "2275" into the "Last 4 of Resident Phone or Guest PIN" field
phone_pin_input.send_keys("2275")

# Wait for 3 seconds after typing into the phone PIN field
time.sleep(2)

# Find the "Sign In" button and click it
sign_in_button = driver.find_element(By.XPATH, "//button[@aria-label='Sign In']")

# Click the "Sign In" button
sign_in_button.click()

# Wait for the page to process the sign-in
time.sleep(2)

# Find the label for "Year"
year_label = driver.find_element(By.XPATH, "//label[contains(text(), 'Year')]")

# Find the input field associated with this label using the "following-sibling" XPath
year_input = year_label.find_element(By.XPATH, "following-sibling::input")

# Type "2012" into the "Year" field
year_input.send_keys("2012")

# Wait for 3 seconds after typing into the year field
time.sleep(2)

# Find the label for "Make / Model"
make_model_label = driver.find_element(By.XPATH, "//label[contains(text(), 'Make / Model')]")

# Find the dropdown associated with this label
make_model_dropdown = make_model_label.find_element(By.XPATH, "following-sibling::div")

# Click to open the dropdown
make_model_dropdown.click()
time.sleep(1)  # Allow the dropdown to open

# Find the search input inside the dropdown and type "honda"
make_model_search = driver.find_element(By.XPATH, "//input[@class='p-dropdown-filter p-inputtext p-component']")
make_model_search.send_keys("honda")
time.sleep(1)  # Allow options to appear

# Select the first option from the dropdown
first_option = driver.find_element(By.XPATH, "//li[@role='option']")
first_option.click()

time.sleep(2)

# Find the label for "Select a Color"
color_label = driver.find_element(By.XPATH, "//label[contains(text(), 'Select a Color')]")

# Find the dropdown associated with this label
color_dropdown = color_label.find_element(By.XPATH, "following-sibling::div")

# Click to open the dropdown
color_dropdown.click()
time.sleep(1)  # Allow the dropdown to open

# Find the search input inside the dropdown and type "grey"
color_search = driver.find_element(By.XPATH, "//input[@class='p-dropdown-filter p-inputtext p-component']")
color_search.send_keys("grey")
time.sleep(1)  # Allow options to appear

# Select the first option from the dropdown
first_option = driver.find_element(By.XPATH, "//li[@role='option']")
first_option.click()

time.sleep(2)

# Find the input field labeled "License Plate" and type "tvl0161"
license_plate_input = driver.find_element(By.XPATH, "//label[contains(text(), 'License Plate')]/following-sibling::input")
license_plate_input.send_keys("tvl0161")

time.sleep(2)

# Find and click the button labeled "Confirm"
confirm_button = driver.find_element(By.XPATH, "//button[span[contains(text(), 'Confirm')]]")
confirm_button.click()

time.sleep(2)

# Find and click the button labeled "Confirm"
confirm_button = driver.find_element(By.XPATH, "//button[span[contains(text(), 'Confirm')]]")
confirm_button.click()

time.sleep(2)

# Find the input field labeled "License Plate" and type "tvl0161"
license_plate_input = driver.find_element(By.XPATH, "//label[contains(text(), 'Confirm license plate')]/following-sibling::input")
license_plate_input.send_keys("tvl0161")

time.sleep(2)

# Find and click the button labeled "Save"
save_button = driver.find_element(By.XPATH, "//button[span[contains(text(), 'Save')]]")
save_button.click()

time.sleep(2)

# Check for success message
try:
    success_message = driver.find_element(By.CLASS_NAME, "p-toast-message-success")
    print("Success")
except:
    try:
        # Check for failure message
        failure_message = driver.find_element(By.CLASS_NAME, "p-toast-message-error")
        print("Failed")
    except:
        print("Unknown status")


# Close the browser
driver.quit()
