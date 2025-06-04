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

Lancer la commande suivante dans le terminal à la racine du projet :

```bash
python -m pytest -s Tests/test_project.py
```

Le navigateur Chrome s'ouvrira automatiquement.

Le test affichera la température lue et vérifiera la présence du bouton adéquat.

La fenêtre du navigateur se fermera automatiquement à la fin du test.


## Les membres du projet
*Feth-Eddine Zineb*
*Aoun Houssam*
*Malek Jihane*
*Lakssir Mohamed*