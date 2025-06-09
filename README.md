# Projet d'Automatisation des Tests Fonctionnels Web – Weather Shopper

## Contexte

Ce projet automatise le scénario principal (happy path) du site [Weather Shopper](https://weathershopper.pythonanywhere.com), une boutique en ligne qui propose des produits de soin selon la température ambiante.

---

## Objectif

Automatiser le parcours utilisateur suivant :

- Lire la température affichée sur la page d’accueil.
- Cliquer sur le bouton correspondant à la température :
  - **Moisturizers** si température < 19°C
  - **Sunscreens** si température > 34°C
  - Sinon, aucun bouton à cliquer.
- Vérifier que le bouton correct est visible selon la température.

---

<pre>
## Structure du projet ``` Weather_Shopper_Project_Tests/ │ ├── Pages/ # Objets des pages (Page Object Model) │ ├── home_page.py │ ├── cart_page.py │ ├── moisturizers_product.py │ └── sunscreens_product.py │ ├── Tests/ # Scénarios de tests automatisés │ └── test_project.py │ ├── Utils/ # Fonctions utilitaires │ └── utils_project.py │ ├── conftest.py # Fixtures Pytest (driver setup/teardown) ├── requirements.txt # Dépendances Python └── README.md # Documentation du projet ``` </pre>

---

## Prérequis

- **Python 3**
- **Selenium WebDriver**
- **Pytest**
- **Pytest-HTML** (pour les rapports de tests)
- **ChromeDriver**

---

## Installation

1. Cloner ou télécharger le projet.
2. Installer les dépendances Python avec
    **pip install -r requirements.txt**
3. Vérifier que `chromedriver` est accessible (variable PATH ou même dossier que les scripts).

---

## Exécution des tests

### Tests disponibles

Le projet contient maintenant plusieurs types de tests :

1. **Test de logique de température** : `Tests/test_project.py`
   - Vérifie que le bon bouton apparaît selon la température

2. **Tests des pages produits** : `Tests/test_product_pages.py`
   - Test de la page moisturizers (sélection des produits Aloe et Almond les moins chers)
   - Test de la page sunscreens (sélection des produits SPF-30 et SPF-50 les moins chers)

### Commandes de test

Lancer tous les tests :

```bash
python -m pytest -v
```

![Résultat de python -m pytest -v](assets/Screenshot/python-m-pytest-v.png)

Lancer un test spécifique :

```bash
python -m pytest Tests/test_project.py -v
python -m pytest Tests/test_product_pages.py -v
```

![Résultat de lancer un test spécifique](assets/Screenshot/Lancer-un-test-spécifique.png)

Lancer les tests avec génération de rapport HTML :

```bash
python -m pytest --html=reports/report.html --self-contained-html
```

Lancer uniquement les tests smoke :

```bash
python -m pytest -m smoke
```

![Résultat de lancer uniquement les tests smoke](assets/Screenshot/Lancer-uniquement-les-tests-smoke.png)

Lancer uniquement les tests de produits :

```bash
python -m pytest -m product
```

![Résultat de lancer uniquement les tests de produits](assets/Screenshot/Lancer-uniquement-les-tests-de-produits.png)

Le navigateur Chrome s'ouvrira automatiquement grâce à webdriver-manager.

Les tests afficheront les résultats dans le terminal et un rapport HTML sera généré dans le dossier `reports/`.

La fenêtre du navigateur se fermera automatiquement à la fin des tests.

## Les membres du projet

*Feth-Eddine Zineb*
*Aoun Houssam*
*Malek Jihane*
*Lakssir Mohamed*
