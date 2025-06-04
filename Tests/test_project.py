from Pages.home_page import HomePage

def test_temperature_logic(driver):
    home = HomePage(driver)
    home.load()

    temp = home.get_temperature()
    print(f"Température actuelle : {temp}°C")

    if temp < 19:
        print("Condition : température < 19°C → Bouton 'moisturizers' attendu")
        assert home.is_moisturizer_button_visible(), "Le bouton moisturizers devrait apparaître"
    elif temp > 34:
        print("Condition : température > 34°C → Bouton 'sunscreens' attendu")
        assert home.is_sunscreen_button_visible(), "Le bouton sunscreens devrait apparaître"
    else:
        print("Température entre 19°C et 34°C : aucun bouton n'est requis.")
