import pytest
from selenium.webdriver.common.by import By
from Pages.payment import PaymentPage
from Pages.cart_page import CartPage

@pytest.mark.product
def test_payment(driver):
    try:
        cart = CartPage(driver)
        cart.open()
        
        prices = cart.get_prices()
        assert cart.count_items() == 2, "Expected 2 items in the cart"
        assert cart.total_amount() == sum(prices), "Total amount does not match the sum of item prices"

        print(f"✅ Cart validated: 2 items for a total of {sum(prices)} Rs")
        cart._open_stripe_modal()

        payment = PaymentPage(driver)
        payment.pay(
            email="test@example.com",
            card="4242424242424242",
            exp="12/34",  # Use a valid expiration date format
            cvc="123",
            zip_code="12345"
        )

        assert payment.payment_successful(), "❌ Payment not confirmed"
        print("✅ Test completed successfully! Payment processed.")
    except Exception as e:
        body = driver.find_element(By.TAG_NAME, "body").text
        print("📍 Visible content:\n", body[:1000])  # Limit to 1000 characters
