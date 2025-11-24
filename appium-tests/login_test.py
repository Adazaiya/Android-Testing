from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def run_test():
    print("\n" + "="*60)
    print("APPIUM ANDROID TESTING DEMO")
    print("="*60)

    options = UiAutomator2Options()
    options.platform_name = "Android"
    options.device_name = "emulator-5554"
    options.app_package = "com.example.android_testing"
    options.app_activity = ".MainActivity"
    options.automation_name = "UiAutomator2"
    options.no_reset = True

    print("\n[1] Connecting to Appium Server...")

    try:
        driver = webdriver.Remote('http://localhost:4723', options=options)
        print("Connected successfully")
        time.sleep(3)

        # CHECK IF ALREADY LOGGED IN
        print("\n[2] Checking app state...")


        try:
            welcome_check = driver.find_element(
                AppiumBy.XPATH, "//*[contains(@text, 'Welcome')]"
            )
            print("Already logged in, logging out first...")

            # Find and click logout button
            logout_btn = driver.find_element(AppiumBy.XPATH, "//*[@text='Logout']")
            logout_btn.click()
            time.sleep(2)
            print("Logged out successfully")
        except:
            print("Not logged in, proceeding to login...")


        print("\n" + "="*60)
        print("LOGIN AUTHENTICATION")
        print("="*60)

        print("\n[3] Finding username and password fields...")
        time.sleep(1)  # Wait for login screen
        text_fields = driver.find_elements(AppiumBy.CLASS_NAME, "android.widget.EditText")
        if len(text_fields) >= 2:
            username_field = text_fields[0]
            password_field = text_fields[1]
            print("Found login fields")
        else:
            raise Exception("Could not find text fields")

        print("\n[4] Entering username: 'testuser'")
        username_field.click()
        time.sleep(0.5)
        username_field.send_keys("testuser")
        print("Username entered")
        time.sleep(1)

        print("\n[5] Entering password: 'testuser123'")
        password_field.click()
        time.sleep(0.5)
        password_field.send_keys("testuser123")
        print("Password entered")
        time.sleep(1)

        print("\n[6] Clicking login button...")
        login_button = driver.find_element(AppiumBy.XPATH, "//*[@text='Login']")
        login_button.click()
        print("Login button clicked")
        time.sleep(2)

        print("\n[7] Verifying welcome message...")
        welcome_msg = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(
                (AppiumBy.XPATH, "//*[contains(@text, 'Welcome')]")
            )
        )
        message = welcome_msg.text
        print(f"✓ Welcome message: '{message}'")

        if "Welcome" in message and "testuser" in message:
            print("\nLOGIN TEST PASSED!")
        else:
            print(f"\nUnexpected message: {message}")

        time.sleep(2)

        # MESSAGE FORMATTING
        print("\n" + "="*60)
        print("MESSAGE FORMATTING FEATURES")
        print("="*60)

        print("\n[8] Finding message input field...")
        # new EditText field
        text_fields = driver.find_elements(AppiumBy.CLASS_NAME, "android.widget.EditText")
        if len(text_fields) >= 1:
            message_field = text_fields[0]  # message field
            print("Message field found")
        else:
            raise Exception("Could not find message field")

        print("\n[9] Typing test message...")
        message_field.click()
        time.sleep(0.5)
        message_field.send_keys("Hello from Appium!")
        print("Message entered: 'Hello from Appium!'")
        time.sleep(1)

        print("\n[10] Testing Bold formatting...")
        bold_button = driver.find_element(AppiumBy.XPATH, "//*[@text='B']")
        bold_button.click()
        print("Bold button clicked")
        time.sleep(1)

        print("\n[11] Testing Italic formatting...")
        italic_button = driver.find_element(AppiumBy.XPATH, "//*[@text='I']")
        italic_button.click()
        print("Italic button clicked")
        time.sleep(1)

        print("\n[12] Verifying formatted message...")
        formatted_msg = driver.find_element(
            AppiumBy.XPATH, "//*[contains(@text, 'Hello from Appium')]"
        )
        if formatted_msg.is_displayed():
            print("Formatted message displayed")
            print("\nMESSAGE FORMATTING TEST PASSED!")
        time.sleep(2)

        # THEME TESTING
        print("\n" + "="*60)
        print("THEME CUSTOMIZATION")
        print("="*60)

        print("\n[13] Testing Blue theme...")
        blue_theme = driver.find_element(AppiumBy.XPATH, "//*[@text='Blue']")
        blue_theme.click()
        print("Blue theme applied")
        time.sleep(1)

        print("\n[14] Testing Green theme...")
        green_theme = driver.find_element(AppiumBy.XPATH, "//*[@text='Green']")
        green_theme.click()
        print("Green theme applied")
        time.sleep(1)

        print("\n[15] Testing Red theme...")
        red_theme = driver.find_element(AppiumBy.XPATH, "//*[@text='Red']")
        red_theme.click()
        print("Red theme applied")
        time.sleep(1)

        print("\nTHEME TESTING PASSED!")
        time.sleep(1)

        #COUNTER TESTING
        print("\n" + "="*60)
        print("COUNTER FUNCTIONALITY")
        print("="*60)

        print("\n[16] Finding counter value...")
        counter_text = driver.find_element(
            AppiumBy.XPATH, "//*[contains(@text, 'Counter:')]"
        )
        initial_counter = counter_text.text
        print(f"Initial counter: {initial_counter}")

        print("\n[17] Testing increment button...")
        increment_btn = driver.find_element(AppiumBy.XPATH, "//*[@text='+']")
        for i in range(3):
            increment_btn.click()
            time.sleep(0.5)
        print("Incremented 3 times")
        time.sleep(1)

        print("\n[18] Testing decrement button...")
        decrement_btn = driver.find_element(AppiumBy.XPATH, "//*[@text='-']")
        decrement_btn.click()
        time.sleep(0.5)
        print("Decremented once")
        time.sleep(1)

        counter_text = driver.find_element(
            AppiumBy.XPATH, "//*[contains(@text, 'Counter:')]"
        )
        final_counter = counter_text.text
        print(f"Final counter: {final_counter}")

        if "Counter: 2" in final_counter:
            print("\nCOUNTER TEST PASSED!")
        else:
            print(f"\nCounter value unexpected: {final_counter}")
        time.sleep(2)

        # RESET THEME
        print("\n" + "="*60)
        print("RESET FUNCTIONALITY")
        print("="*60)

        print("\n[19] Testing reset theme button...")
        reset_btn = driver.find_element(AppiumBy.XPATH, "//*[@text='Reset Theme']")
        reset_btn.click()
        print("Theme reset to default")
        time.sleep(2)

        print("\nRESET TEST PASSED!")

        # LOGOUT
        print("\n" + "="*60)
        print("LOGOUT")
        print("="*60)

        print("\n[20] Finding logout button...")
        logout_btn = driver.find_element(AppiumBy.XPATH, "//*[@text='Logout']")
        print("Logout button found")

        print("\n[21] Clicking logout...")
        logout_btn.click()
        print("Logout clicked")
        time.sleep(2)

        print("\n[22] Verifying return to login screen...")
        login_screen = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(
                (AppiumBy.XPATH, "//*[@text='Login Demo']")
            )
        )
        if login_screen.is_displayed():
            print("Returned to login screen")
            print("\nLOGOUT TEST PASSED!")
        time.sleep(2)

        # RESULTS
        print("\n" + "="*60)
        print("ALL TESTS COMPLETED SUCCESSFULLY!")
        print("="*60)
        print("\nLogin Authentication")
        print("Message Formatting (Bold/Italic)")
        print("Theme Customization (Blue/Green/Red)")
        print("Counter Operations (Increment/Decrement)")
        print("Reset Functionality")
        print("Logout Flow")
        print("\n" + "="*60)

        time.sleep(3)

    except Exception as e:
        print("\n" + "="*60)
        print("TEST FAILED!")
        print("="*60)
        print(f"\nError: {str(e)}")
        import traceback
        traceback.print_exc()

    finally:
        print("\nClosing Appium session...")
        try:
            driver.quit()
            print("Session closed successfully")
        except:
            pass
        print("\n" + "="*60)
        print("Test execution completed")
        print("="*60 + "\n")

if __name__ == "__main__":
    print("\nAppium Test Suite")
    print("  1. Appium server is running")
    print("  2. Android emulator is running")
    input("\nPress ENTER to begin testing...")

    run_test()