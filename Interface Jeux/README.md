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

S'il y a des erreurs de compilation, fiez-vous aux messages d'erreurs de la console et installez les librairies manquantes!

# Comment démarrer l'interface
Pour lancer et ou modifier l'interface, le fichier de code est InterfaceJeux.py .
Pour démarrer l'interface il suffit, dans PyCharm, d'appuyer sur le bouton "Run".
![image](https://user-images.githubusercontent.com/78489554/232337099-de01fa02-72ee-4455-853a-f669517a608c.png)

L'interface comprends des boutons de contrôle de la main, une rétroaction temps réel de la caméra, un décompte de jeux et des statistiques.
![image](https://user-images.githubusercontent.com/78489554/232337570-edd9e586-6d58-49ad-85db-1a51ec508308.png)

# Comment fonctionne la reconnaissance visuelle
Pour entraîner un nouveau modèle de reconnaissance visuelle, utilisez le fichier /ModeleVision/modelTraining.py .
Dans ce fichier, en vous fiant aux commentaires, vous serez en mesure de changer les différents paramètres du modèle
et d'entraîner votre propre modèle. Ensuite, dans le fichier algoRPC du dossier principal, vous n'aurez qu'à changer 
le nom du modèle à télécharger et à vous assurer que le dit modèle se trouve dans le dossier.
![image](https://user-images.githubusercontent.com/78489554/232338412-ab952e2f-910b-4119-87b0-f522b5ded0c7.png)

# Comment fonctionne l'algorithme décisionnel de jeux
De base, l'ordinateur jouera des coups aléatoires. Cependant, il est possible de le faire jouer avec un algorithme décisionnel
de type chaînes de Markov. Le code responsable des calculs statistiques derrrière les prédictions des chaînes est dans le fichier RPCmarkov.py

# Comment fonctionne la communication
La communication entre l'ordinateur et le microcontrôleur Arduino se fait par série avec le fichier CommWorker.py
Ce code produit une rétroaction à la console permettant à l'utilisateur de comprendre les commandes envoyées à la main.
![image](https://user-images.githubusercontent.com/78489554/232338623-5928d6ce-c606-4d40-a7b0-26c76b70a1f0.png)

