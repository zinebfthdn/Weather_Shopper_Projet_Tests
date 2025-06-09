import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class PaymentPage:
    STRIPE_IFRAME = (By.XPATH, "//iframe[contains(@name,'stripe_checkout_app')]")

    EMAIL_INPUT = (By.ID, "email")
    CARD_INPUT  = (By.ID, "card_number")
    EXP_INPUT   = (By.ID, "cc-exp")
    CVC_INPUT   = (By.ID, "cc-csc")
    ZIP_INPUT   = (By.ID, "billing-zip")
    SUBMIT_BTN  = (By.ID, "submitButton")

    SUCCESS_HDR = (By.XPATH, "//h2[contains(translate(text(), 'abcdefghijklmnopqrstuvwxyz', 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'), 'PAYMENT SUCCESS')]")

    def __init__(self, driver, timeout=20):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    def _switch_to_iframe(self):
        self.wait.until(EC.frame_to_be_available_and_switch_to_it(self.STRIPE_IFRAME))

    def _switch_to_default(self):
        self.driver.switch_to.default_content()

    def _type(self, locator, value):
        field = self.wait.until(EC.visibility_of_element_located(locator))
        field.clear()
        field.send_keys(value)

    def _click(self, locator):
        self.wait.until(EC.element_to_be_clickable(locator)).click()

    def pay(self, email, card, exp, cvc, zip_code):
        """Fill in all Stripe fields and click Pay."""
        self._switch_to_iframe()
        self._type(self.EMAIL_INPUT, email)
        time.sleep(0.5)
        self._type(self.CARD_INPUT, card)
        time.sleep(0.5)
        self._type(self.EXP_INPUT, exp)
        time.sleep(0.5)
        self._type(self.CVC_INPUT, cvc)
        time.sleep(0.5)
        self._type(self.ZIP_INPUT, zip_code)
        time.sleep(0.5)
        self._click(self.SUBMIT_BTN)
        self._switch_to_default()
        time.sleep(2)

    def payment_successful(self, timeout=20):
        """Check if a success message appears after payment."""
        try:
            self.wait.until(EC.visibility_of_element_located(self.SUCCESS_HDR))
            return True
        except TimeoutException:
            return False
