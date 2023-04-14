# Documentation-Interface

# Matériel nécessaire
- [ ] Caméra (intégré à un ordinateur portable ou une webcam)
- [ ] ArduinoMEGA 2560

# Installation des logiciels recommandés
- [ ] PyCharm
 ```
 https://www.jetbrains.com/pycharm/download/#section=windows
 ```
- [ ] QtDesigner
 ```
 https://build-system.fman.io/qt-designer-download
 ```

# Consolidation des versions et des dépendances
Ce projet fonctionne avec Python 3.7 ou 3.10, mais il est bon de noter que les dépendances décrites ci-dessous s'appliquent à un environnement python 3.10.

## Installation des librairies et interpréteur
Pour commencer, installez python sur votre machine.
Ensuite, dans PyCharm, vous allez ajouter les librairies nécessaires à votre interpréteur en vous fiant aux étapes suivantes:

1. À partir de l'onglet "File" sélectionner "Settings"
![image](https://user-images.githubusercontent.com/78489554/231928591-a2edf1bb-d9a8-4217-9c32-915a99832dc9.png)
2. Sous "Projet", sélectionner "Python Interpreter"
![image](https://user-images.githubusercontent.com/78489554/231928687-0256b4aa-de0a-4f44-8e68-8581bc0e26aa.png)
3. Choisir la version de python sur laquelle vous souhaitez installer vos librairies
![image](https://user-images.githubusercontent.com/78489554/232065544-888e7708-50fd-4de8-8ea1-8e20b2ef9fbf.png) 
4. En appuyant sur le bouton +, choissisez les librairies selon les requis énumérés ci-dessous et cliquez sur "Install Package"
![image](https://user-images.githubusercontent.com/78489554/231928832-087234c2-b583-47e6-889c-7f370e3d3fc6.png)

## Liste des librairies à installer
- [ ] opencv-contrib-python == 4.3.0
- [ ] scikit-learn == 0.11
- [ ] tensorflow == 2.2.0
- [ ] numpy == 1.18.3
- [ ] matplotlib == 3.1.0
- [ ] scipy == 1.4.1
- [ ] PyQt5 == 5.15.9

S'il y a des erreurs de compilation, fiez-vous aux messages d'erreurs de la console et intallez les librairies qu'il vous manque!

# Comment démarrer l'interface
Explication du fichier InterfaceJeux.py

# Comment fonctionne la reconnaissance visuelle
Explication du fichier algoRPC.py

# Comment fonctionne l'algorithme de jeux
Explication du fichier RPCmarkov.py

# Comment fonctionne la communication
Explication du fichier CommWorker.py
