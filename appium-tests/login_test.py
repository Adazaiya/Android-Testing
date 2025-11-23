from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def run_test():
    print("\n" + "="*60)
    print("APPIUM LOGIN TEST")
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
        print("Connected successfully!")
        time.sleep(3)

        print("\n[2] Finding username field...")

        text_fields = driver.find_elements(AppiumBy.CLASS_NAME, "android.widget.EditText")
        if len(text_fields) >= 2:
            username_field = text_fields[0]  # username
            password_field = text_fields[1]  # password
            print("Found text fields")
        else:
            raise Exception("Could not find text fields")

        print("\n[3] Clicking and typing username: 'uzma'")
        username_field.click()
        time.sleep(0.5)
        username_field.send_keys("uzma")
        print("Username entered")
        time.sleep(1)

        print("\n[4] Clicking and typing password: 'uzma123'")
        password_field.click()
        time.sleep(0.5)
        password_field.send_keys("uzma123")
        print("Password entered")
        time.sleep(1)

        print("\n[5] Finding login button...")
        login_button = driver.find_element(
            AppiumBy.XPATH, "//*[@text='Login']"
        )
        print("Login button found")

        print("\n[6] Clicking login button...")
        login_button.click()
        print("Button clicked")
        time.sleep(2)

        print("\n[7] Verifying welcome message...")
        welcome_msg = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(
                (AppiumBy.XPATH, "//*[contains(@text, 'Welcome')]")
            )
        )

        message = welcome_msg.text
        print(f"Welcome message found: '{message}'")

        if "Welcome" in message and "uzma" in message:
            print("\n" + "="*60)
            print("TEST PASSED! LOGIN SUCCESSFUL!")
            print("="*60)
        else:
            print(f"\nUnexpected message: {message}")

        time.sleep(3)

    except Exception as e:
        print(f"\nTEST FAILED: {str(e)}")
        import traceback
        traceback.print_exc()

    finally:
        print("\n[8] Closing session...")
        try:
            driver.quit()
        except:
            pass
        print("Test completed\n")

if __name__ == "__main__":
    run_test()