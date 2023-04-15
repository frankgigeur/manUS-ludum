# Documentation-Mécanique

## Fichiers ['CAD'](./CAD/)
Les fichiers suivants contiennent les CAD nécessaires à la ['fabrication'](##Fabrication%20des%20composantes) des composantes mécaniques du projet.

- [ ]  [`Doigts`](./CAD/Doigts/), [`Paume`](./CAD/Paume%20et%20poignet//), [`Poignet`](./CAD/Paume%20et%20poignet//) <br>
- [ ]  [`Ligaments`](./CAD/Doigts//) <br>
- [ ]  [`Support moteur`](./CAD/Moteurs%20support%20et%20poulies/), [`Poulies moteurs`](./CAD/Moteurs%20support%20et%20poulies/) <br>
- [ ]  [`Support arbre`](./CAD/M%C3%A9canisme%20redirection%20fils/), [`Poulies arbre`](./CAD/M%C3%A9canisme%20redirection%20fils/), [`Support supérieur`](./CAD/M%C3%A9canisme%20redirection%20fils/) <br>
- [ ]  [`Base`](./CAD/Plaque%20montage/) <br>



## Fabrication des composantes
![avant bras v1](https://user-images.githubusercontent.com/92990215/232235138-21b190a2-598d-4fa9-a9e3-5926b624a40c.png)


La fabrication des composantes du projet nécessite l'accès à **une découpeuse laser**, **une imprimante 3D** et d'un **fer à souder**. 
Les étapes suivantes permmettent de fabriquer l'ensemble des composantes mécaniques du projets selon les étapes suivantes:

1. Impression des doigts du dossier [`Doigts`](./CAD/Doigts/) en PLA à l'aide d'une imprimante 3D.

2. Impression de la paume et de son support de type poignet dans le dossier [`Paume et poignet`](./CAD/Paume%20et%20poignet//).

3. Impression des [`poulies de servo moteurs`](./CAD/Moteurs%20support%20et%20poulies/)  ( **x5** ), du [`support à moteurs`](./CAD/Moteurs%20support%20et%20poulies/), des [`poulies inserés sur les paliers à billes`](./CAD/M%C3%A9canisme%20redirection%20fils/) ( **x12** ) et des [`supports à arbre types 1 et 2`](./CAD/M%C3%A9canisme%20redirection%20fils/) ( **x4 chaque** ).

4. Découpe du [`support supérieur de la main`](./CAD/M%C3%A9canisme%20redirection%20fils/) en acrylique à l'aide d'une découpeuse laser.

4. Découpe des [`ligaments`](./CAD/Ligaments/) en nylon des différents doigts ( **2 par doigts** ) à l'aide de la découpeuse laser.

5. Découpe des [`ligaments`](./CAD/Ligaments/) en mica des différents doigts ( **3 par doigts** ) à l'aide de ciseaux.

6. Découpe des fils de pêche ≈ 60cm ( **x10** ).

7. Découpe de la [`base`](./CAD/Plaque%20montage/) en acrylique du support de la main à l'aide d'une découpeuse laser. 

## Liste des matériaux et composantes
- [ ] &nbsp;Vis autoperçantes M1.2 x 3mm <br>
- [ ] &nbsp;Vis M3 x 20mm <br>
- [ ] &nbsp;Vis M3 x 45mm <br>
- [ ] &nbsp;Vis M5 x 10mm <br>
- [ ] &nbsp;Vis M5 x 50mm <br>
- [ ] &nbsp;12 x 12 x 1/8 po. Acrylique <br>
- [ ] &nbsp;Feuille de nylon cordura 1000D [(Club Tissu)](https://www.clubtissus.com/fr/nylon-cordura-1000d-noir?fbclid=IwAR1-LkjzjMgMWKu80fnkrolP66I-jkD7ACOhfdXqo_PhgQrl8uaRKlY1G78) <br>
- [ ] &nbsp;Mica plastique transparent 20 ga (Club Tissu) <br>
- [ ] &nbsp;Aggraphe à papier <br>
- [ ] &nbsp;Arbre de métal 5mm x 100mm [(Amazon)](https://www.amazon.ca/dp/B01B27MJC6?psc=1&ref=ppx_yo2ov_dt_b_product_details&fbclid=IwAR362ei__UgU11dEIUVBtTV-3JzH9szivByOdhoxnguKB56Yidi5-6fRLzg) <br>
- [ ] &nbsp;Bearing à billes 5mm x 11mm x 4mm [(Amazon)](https://www.amazon.ca/dp/B07GBTWLCZ?ref=ppx_yo2ov_dt_b_product_details&th=1&fbclid=IwAR22SOt6oHsRRFlgVRrsB5KiavJjqLkp366aq2QIwt-hIwIwVPaSqANGHF4) <br>
- [ ] &nbsp;Fil de pêche 80 lbs <br>
- [ ] &nbsp;Goupille (dowel pin) 1/8 x 0.5 po. <br> 
- [ ] &nbsp;Servomoteur HS-422 Hitec [(Robotshop)](https://ca.robotshop.com/fr/products/hitec-hs-422-servo-motor) <br>

## Assemblage mécanique
Pour l'assemblage des pièces mécaniques, se fier aux [`assemblages complets`](./CAD/Assemblages%20complets/) fournis ainsi qu'aux [`dessins`](./Dessins/) et explications ultérieures.

### **Montage des doigts**
Pour le montage des doigts, il est nécesaire d'insérer les ligamants aux points d'insertion anatomique selon la figure suivante:
![exemple ligament](https://user-images.githubusercontent.com/92990215/232253651-91426f68-5720-48be-8098-8d6ce0e7ebe7.png)

Pour se faire, faire fondre les vis m1.2 aux points cibles et visser par la suite celles-ci avec les ligaments de mica et de nylon. La figure suivante présente le nom des ligaments à utiliser selon la jonction entre les ossements.

![montage doigt index](https://user-images.githubusercontent.com/92990215/232254743-88300a97-06f6-4cc5-a2d7-a04028a713ea.png)

La jonction MCPP est une superposition de ligaments de mica et de nylon, tandis que la jonction PPMP est seulement un ligament de nylon. Aussi, à noter que cette figure présente le montage de l'index, mais la même procédure s'applique pour tous les autres doigts. <br> <br>

Finalement, les poulies et les tendons peuvent être installés. Les aggraphes peuvent donc être pliées et coupées pour ensuite être insérées dans le doigt à l'aide d'un fer à souder. La figure suivante présente le positionnement des poulies.

![poulies](https://user-images.githubusercontent.com/92990215/232255831-4517c4ba-6d15-48b9-bab0-9319c1467285.png)

Le point rouge représente le point de fixation des tendons, soit des fils de pêche, et les points bleus représentent le positionnement des aggraphes à papier. <br> <br>
Ce processus se répete finalement sur la partie arrière des ossements. Il est à noter que le positionnement exact de ces éléments peut varier légèrement sans affecter les performances des doigts.
