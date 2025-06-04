from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

class HomePage:
    """
    Classe représentant la page d'accueil du site Weather Shopper.
    Permet d'interagir avec les éléments clés de la page (température, boutons).
    """

    URL = "https://weathershopper.pythonanywhere.com"
    TEMP_LOCATOR = (By.ID, "temperature")
    MOISTURIZER_BTN = (By.XPATH, "//button[text()='Buy moisturizers']")
    SUNSCREEN_BTN = (By.XPATH, "//button[text()='Buy sunscreens']")

    def __init__(self, driver):
        """
        Initialise la page avec un objet WebDriver Selenium.
        """
        self.driver = driver

    def load(self) -> None:
        """
        Ouvre la page d'accueil dans le navigateur.
        """
        self.driver.get(self.URL)

    def get_temperature(self) -> int:
        """
        Récupère la température affichée sur la page.
        
        Returns:
            int: La température en degrés Celsius.

        Raises:
            ValueError: Si le texte de la température n'est pas dans le format attendu.
        """
        temp_text = self.driver.find_element(*self.TEMP_LOCATOR).text
        try:
            temp_value = int(temp_text.split()[0])
            return temp_value
        except (IndexError, ValueError) as e:
            raise ValueError(f"Impossible d'extraire la température depuis '{temp_text}'") from e

    def is_moisturizer_button_visible(self) -> bool:
        """
        Vérifie si le bouton 'Buy moisturizers' est visible.

        Returns:
            bool: True si visible, False sinon.
        """
        try:
            return self.driver.find_element(*self.MOISTURIZER_BTN).is_displayed()
        except NoSuchElementException:
            return False

    def is_sunscreen_button_visible(self) -> bool:
        """
        Vérifie si le bouton 'Buy sunscreens' est visible.

        Returns:
            bool: True si visible, False sinon.
        """
        try:
            return self.driver.find_element(*self.SUNSCREEN_BTN).is_displayed()
        except NoSuchElementException:
            return False
