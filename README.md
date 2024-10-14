# Serveur éducatif avec FastAPI et Clean Architecture

Ce projet est un serveur simple, construit à des fins éducatives, en utilisant **FastAPI** et les principes de base de l'**architecture Clean**. Il permet de comprendre l'organisation d'un projet selon ces principes et propose deux fonctionnalités principales : 

1. **Un serveur de page HTML** avec un simple scroller.
2. **Une API pour définir un volume** via une requête HTTP.

## Fonctionnalités

- **Page HTML avec Scroller :**  
  Un point d'accès `/scroll` qui sert une page HTML contenant un simple scroller pour l'exploration.
  
- **Définition du Volume :**  
  Un second point d'accès `/volume` qui permet à l'utilisateur de définir un volume via une requête HTTP (POST), en envoyant des données JSON. Ce point retourne le volume défini.

## Lancement automatique au démarrage

Le projet est configuré pour se lancer automatiquement au démarrage de la Raspberry Pi. Lors de l'installation, un service systemd est créé pour exécuter le serveur à chaque redémarrage de l'appareil.

## Installation

1. Clonez ce dépôt :
   `git clone https://github.com/Alex-Helianthe/music_server.git`

2. Accédez au dossier du projet :
   `cd music_server`

3. Installez les dépendances via un environnement virtuel :
   `sudo make install`
   Appuyez sur `Y` pour valider l'installation quand demandé.

4. Lancez le serveur :
   `make run`

## Configuration Bluetooth (Relais)

Ce projet permet également d'utiliser l'appareil comme un relais Bluetooth, en ajoutant cette fonctionnalité via un script. Pour configurer et installer cette fonctionnalité, exécutez la commande suivante :

`make bluetooth`

Cette commande télécharge et installe un script depuis GitHub qui configure l'appareil pour agir en tant que relais audio via Bluetooth.

## Redémarrage du serveur

Pour redémarrer le serveur en cours d'exécution :

`make reboot`

## Désinstallation et nettoyage

Pour désinstaller l'environnement virtuel et nettoyer les fichiers temporaires générés par le projet (comme __pycache__, .pytest_cache, etc.), utilisez la commande suivante :

`sudo make uninstall`

## Points d'accès

- **GET /** : Renvoie une page HTML avec un scroller.
- **POST /volume** : Définit un volume en envoyant des données JSON, par exemple :
``{"volume": 10}``


## Technologies utilisées

- **FastAPI** : Framework rapide et efficace pour les APIs en Python.
- **Clean Architecture** : Principes de structuration logicielle pour maintenir la séparation des préoccupations.

---

# Educational Server with FastAPI and Clean Architecture

This project is a simple server built for educational purposes using **FastAPI** and the basics of **Clean Architecture**. It helps understand how to organize a project based on these principles, and offers two main features:

1. **A server serving an HTML page** with a simple scroller.
2. **An API to set a volume** through an HTTP request.

## Features

- **HTML Page with Scroller:**  
  An endpoint `/scroll` serves an HTML page with a simple scroller for navigation.
  
- **Set Volume:**  
  A second endpoint `/volume` allows the user to set a volume via an HTTP (POST) request, sending JSON data. This endpoint returns the defined volume.

## Automatic startup on boot

The project is configured to automatically start on Raspberry Pi boot. During installation (make install), a systemd service is created to run the server every time the device restarts.

## Installation

1. Clone this repository:
   `git clone https://github.com/Alex-Helianthe/music_server.git`

2. Navigate to the project directory:
   `cd music_server`

3. Install dependencies using a virtual environment:
   `sudo make install`
   Press `Y` to proceed with the installation when prompted.

4. Start the server:
   `make run`

## Bluetooth Configuration (Relay)

This project also allows the device to be used as a Bluetooth relay by adding this functionality via a script. To configure and install this feature, run the following command:

`make bluetooth`

This command downloads and installs a script from GitHub that configures the device to act as an audio relay via Bluetooth.

## Restarting the server

To restart the currently running server:

`make reboot`

## Uninstallation and cleaning

To uninstall the virtual environment and clean temporary files (such as __pycache__, .pytest_cache, etc.), use the following command:

`sudo make uninstall`

## Points d'accès

- **GET /** : Returns an HTML page with a scroller.
- **POST /volume** : Sets a volume by sending JSON data, for example :
``{"volume": 10}``

## Technologies Used

- **FastAPI**: Fast and efficient framework for building APIs in Python.
- **Clean Architecture**: Software structuring principles to maintain separation of concerns.
