from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class MoisturizerPage:
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
        """Select the cheapest Aloe and Almond products and add to cart."""
        products = self.get_products()
        aloe_products = [p for p in products if "aloe" in p["name"].lower()]
        almond_products = [p for p in products if "almond" in p["name"].lower()]

        assert aloe_products, "No Aloe products found"
        assert almond_products, "No Almond products found"

        cheapest_aloe = min(aloe_products, key=lambda x: x["price"])
        cheapest_almond = min(almond_products, key=lambda x: x["price"])

        # Add products to cart
        self.driver.find_element(
            By.XPATH, self.add_button_xpath.format(cheapest_aloe["name"])
        ).click()
        self.driver.find_element(
            By.XPATH, self.add_button_xpath.format(cheapest_almond["name"])
        ).click()

        return cheapest_aloe, cheapest_almond

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
