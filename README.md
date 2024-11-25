# Library Management System (LMS)

## Description

Le **Library Management System (LMS)** est une application de gestion de bibliothèque développée en Python, utilisant PyQt5 et Qt Designer. Cette application permet de gérer efficacement les étudiants, les livres empruntés, ainsi que les transactions d'emprunt. Elle offre une interface intuitive et simple d'utilisation, permettant de gérer les livres, les étudiants et les emprunts en quelques clics.

## Fonctionnalités principales

- **Gestion des étudiants :**
  - Ajout, suppression et modification des informations des étudiants.
- **Gestion des livres :**

  - Ajout, suppression et modification des informations des livres dans la bibliothèque.

- **Gestion des emprunts :**
  - Enregistrement des emprunts de livres par les étudiants.
  - Suivi de la date d'emprunt et de retour des livres.
- **Base de données CSV :**
  - L'application utilise un fichier CSV comme base de données pour stocker les informations des étudiants, des livres et des emprunts. Le fichier CSV est automatiquement créé lors du premier lancement de l'application.

## Installation

### Version exécutable (Windows)

Une version prête à l'emploi de l'application est fournie sous forme de fichier exécutable **`LMS.exe`**. Il suffit de télécharger l'archive contenant ce fichier et de l'exécuter sur une machine Windows. Vous n'avez pas besoin d'installer Python ou les dépendances, tout est inclus dans l'exécutable.

### Code source

Le code source complet de l'application est inclus dans un dossier nommé `source_code`. Vous pouvez cloner le repository ou télécharger le dossier compressé contenant le code source pour personnaliser ou développer davantage l'application.

#### Pour utiliser le code source :

1. Clonez le repository ou téléchargez-le en utilisant le lien suivant :
   ```bash
   git clone https://github.com/kassemabbassi/Library-Management-System.git
   ```

### Utilisation

**Version .exe** : L'exécutable LMS.exe permet de lancer l'application sans installation supplémentaire. Lors du premier lancement, un fichier CSV est créé automatiquement si ce dernier n'existe pas déjà. Vous pouvez ensuite utiliser l'interface pour gérer les étudiants, les livres et les emprunts.
**Code source** : Si vous utilisez le code source, le fichier CSV sera également créé automatiquement lors de la première exécution de l'application. L'interface graphique permet de naviguer entre les différentes sections : gestion des étudiants, gestion des livres, gestion des emprunts.

## Technologies utilisées:

**Python**
**PyQt5**
**Qt Designer**
**CSV (pour la gestion de la base de données)**

## Contribuer

Les contributions sont les bienvenues ! Si vous souhaitez améliorer cette application, vous pouvez forker le projet, y apporter vos modifications, puis soumettre une pull request.
