from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class SunscreenPage:
    def __init__(self, driver):
        self.driver = driver
        self.product_cards = (By.XPATH, "//div[contains(@class,'text-center col-4')]")
        self.add_button_xpath = "//p[contains(text(), '{}')]/following-sibling::button[contains(text(), 'Add')]"
        self.cart_button = (By.XPATH, '//button[@onclick="goToCart()"]')

    def get_products(self):
        """Retrieve all products with names and prices."""
        products = []
        cards = WebDriverWait(self.driver, 10).until(
            EC.presence_of_all_elements_located(self.product_cards)
        )
        for card in cards:
            name = card.find_element(By.TAG_NAME, "p").text
            price_text = card.find_element(
                By.XPATH, ".//p[contains(text(), 'Price')]"
            ).text
            price = int(price_text.split()[-1])  # Extract price from "Price: Rs. X"
            products.append({"name": name, "price": price})
        return products

    def select_cheapest_products(self):
        """Select the cheapest SPF-30 and SPF-50 products and add to cart."""
        products = self.get_products()
        spf30_products = [p for p in products if "spf-30" in p["name"].lower()]
        spf50_products = [p for p in products if "spf-50" in p["name"].lower()]

        assert spf30_products, "No SPF-30 products found"
        assert spf50_products, "No SPF-50 products found"

        cheapest_spf30 = min(spf30_products, key=lambda x: x["price"])
        cheapest_spf50 = min(spf50_products, key=lambda x: x["price"])

        # Add products to cart
        self.driver.find_element(
            By.XPATH, self.add_button_xpath.format(cheapest_spf30["name"])
        ).click()
        self.driver.find_element(
            By.XPATH, self.add_button_xpath.format(cheapest_spf50["name"])
        ).click()

        return cheapest_spf30, cheapest_spf50

    def go_to_cart(self):
        """Navigate to cart page."""
        import time

        time.sleep(
            3
        )  # Wait longer for cart button to become available after adding products

        # Try multiple selectors for the cart button
        cart_selectors = [
            (By.XPATH, '//button[@onclick="goToCart()"]'),
            (By.XPATH, '//button[contains(text(), "Cart")]'),
            (
                By.XPATH,
                '//button[contains(@class, "btn") and contains(text(), "Cart")]',
            ),
            (By.CSS_SELECTOR, 'button[onclick="goToCart()"]'),
        ]

        cart_btn = None
        for selector in cart_selectors:
            try:
                cart_btn = WebDriverWait(self.driver, 5).until(
                    EC.element_to_be_clickable(selector)
                )
                break
            except:
                continue

        if cart_btn:
            cart_btn.click()
            # Wait for navigation to complete
            WebDriverWait(self.driver, 10).until(
                lambda driver: "cart" in driver.current_url
            )
        else:
            raise Exception("Could not find cart button")
