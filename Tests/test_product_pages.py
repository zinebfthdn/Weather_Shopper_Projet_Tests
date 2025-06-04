import pytest
import sys
import os

# Add the parent directory to Python path so we can import from pages
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from Pages.moisturizers_product import MoisturizerPage
from Pages.sunscreens_product import SunscreenPage


@pytest.mark.product
@pytest.mark.smoke
def test_moisturizer_page(driver):
    """Test moisturizer page functionality - select cheapest Aloe and Almond products."""
    driver.get("https://weathershopper.pythonanywhere.com/moisturizer")
    moisturizer_page = MoisturizerPage(driver)

    # Select cheapest Aloe and Almond products
    aloe_product, almond_product = moisturizer_page.select_cheapest_products()

    # Verify products were added (case-insensitive)
    assert "aloe" in aloe_product["name"].lower(), "Aloe product not selected"
    assert "almond" in almond_product["name"].lower(), "Almond product not selected"

    # Navigate to cart
    moisturizer_page.go_to_cart()

    # Verify cart page loaded
    assert "cart" in driver.current_url, "Failed to navigate to cart"


@pytest.mark.product
@pytest.mark.smoke
def test_sunscreen_page(driver):
    """Test sunscreen page functionality - select cheapest SPF-30 and SPF-50 products."""
    driver.get("https://weathershopper.pythonanywhere.com/sunscreen")
    sunscreen_page = SunscreenPage(driver)

    # Select cheapest SPF-30 and SPF-50 products
    spf30_product, spf50_product = sunscreen_page.select_cheapest_products()

    # Verify products were added
    assert "spf-30" in spf30_product["name"].lower(), "SPF-30 product not selected"
    assert "spf-50" in spf50_product["name"].lower(), "SPF-50 product not selected"

    # Navigate to cart
    sunscreen_page.go_to_cart()

    # Verify cart page loaded
    assert "cart" in driver.current_url, "Failed to navigate to cart"
