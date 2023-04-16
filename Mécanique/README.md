# Documentation-Mécanique

## Fichiers ['CAD'](./CAD/)
Les fichiers suivants contiennent les CAD nécessaires à la ['fabrication'](##Fabrication%20des%20composantes) des composantes mécaniques du projet.

- [ ]  [`Doigts`](./CAD/Doigts/), [`Paume`](./CAD/Paume%20et%20poignet//), [`Poignet`](./CAD/Paume%20et%20poignet//) <br>
- [ ]  [`Ligaments`](./CAD/Ligaments/) <br>
- [ ]  [`Support moteur`](./CAD/Moteurs%20support%20et%20poulies/), [`Poulies moteurs`](./CAD/Moteurs%20support%20et%20poulies/) <br>
- [ ]  [`Support arbre`](./CAD/M%C3%A9canisme%20redirection%20fils/), [`Poulies arbre`](./CAD/M%C3%A9canisme%20redirection%20fils/), [`Support supérieur`](./CAD/M%C3%A9canisme%20redirection%20fils/) <br>
- [ ]  [`Base`](./CAD/Plaque%20montage/) <br>

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


## Fabrication des composantes
![avant bras v1](https://user-images.githubusercontent.com/92990215/232235138-21b190a2-598d-4fa9-a9e3-5926b624a40c.png)


La fabrication des composantes du projet nécessite l'accès à **une découpeuse laser**, **une imprimante 3D** et d'un **fer à souder**. 
Les étapes suivantes permmettent de fabriquer l'ensemble des composantes mécaniques du projets selon les étapes suivantes:

1. Impression des doigts du dossier [`Doigts`](./CAD/Doigts/) en PLA à l'aide d'une imprimante 3D (Infill minimum 80%).

2. Impression de la paume et de son support de type poignet dans le dossier [`Paume et poignet`](./CAD/Paume%20et%20poignet//) (Infill minimum 40%).

3. Impression des [`poulies de servo moteurs`](./CAD/Moteurs%20support%20et%20poulies/)  ( **x5** ), du [`support à moteurs`](./CAD/Moteurs%20support%20et%20poulies/), des [`poulies inserés sur les paliers à billes`](./CAD/M%C3%A9canisme%20redirection%20fils/) ( **x12** ) et des [`supports à arbre types 1 et 2`](./CAD/M%C3%A9canisme%20redirection%20fils/) ( **x4 chaque** ).

4. Découpe du [`support supérieur de la main`](./CAD/M%C3%A9canisme%20redirection%20fils/) en acrylique à l'aide d'une découpeuse laser.

4. Découpe des [`ligaments`](./CAD/Ligaments/) en nylon des différents doigts ( **2 par doigts** ) à l'aide de la découpeuse laser.

5. Découpe des [`ligaments`](./CAD/Ligaments/) en mica des différents doigts ( **3 par doigts** ) à l'aide de ciseaux.

6. Découpe des fils de pêche ≈ 60cm ( **x10** ).

7. Découpe de la [`base`](./CAD/Plaque%20montage/) en acrylique du support de la main à l'aide d'une découpeuse laser. 


## Assemblage mécanique
Pour l'assemblage des pièces mécaniques, se fier aux [`assemblages complets`](./CAD/Assemblages%20complets/) fournis ainsi qu'aux [`dessins`](./Dessins/), [images](https://github.com/frankgigeur/manUS-ludum/tree/main/Images) fournies et explications ultérieures.

![Dessin assemblage](https://github.com/frankgigeur/manUS-ludum/blob/main/M%C3%A9canique/Dessins/PNG/Dessin_assemblage.png)

![Dessin paume](https://github.com/frankgigeur/manUS-ludum/blob/main/M%C3%A9canique/Dessins/PNG/Dessin_paume.png)

![Dessin redirection fils](https://github.com/frankgigeur/manUS-ludum/blob/main/M%C3%A9canique/Dessins/PNG/Dessin_support_main.png)

### **Montage des doigts**
Pour le montage des doigts, il est nécesaire d'insérer les ligamants aux points d'insertion anatomique selon la figure suivante:
![exemple ligament](https://user-images.githubusercontent.com/92990215/232253651-91426f68-5720-48be-8098-8d6ce0e7ebe7.png)

Pour se faire, faire fondre les vis m1.2 aux points cibles et visser par la suite celles-ci avec les ligaments de mica et de nylon. La figure suivante présente le nom des ligaments à utiliser selon la jonction entre les ossements.

![nom ligaments](https://user-images.githubusercontent.com/92990215/232256772-1324709a-076f-477b-a915-4e05d39316b6.png)

La jonction MCPP est une superposition de ligaments de mica et de nylon, tandis que la jonction PPMP est seulement un ligament de nylon. Aussi, à noter que cette figure présente le montage de l'index, mais la même procédure s'applique pour tous les autres doigts. <br> <br>

Finalement, les poulies et les tendons peuvent être installés. Les aggraphes peuvent donc être pliées et coupées pour ensuite être insérées dans le doigt à l'aide d'un fer à souder. La figure suivante présente le positionnement des poulies.

![poulies](https://user-images.githubusercontent.com/92990215/232255831-4517c4ba-6d15-48b9-bab0-9319c1467285.png)

Le point rouge représente le point de fixation des tendons, soit des fils de pêche, et les points bleus représentent le positionnement des aggraphes à papier. <br> <br>
Ce processus se répete finalement sur la partie arrière des ossements. Il est à noter que le positionnement exact de ces éléments peut varier légèrement sans affecter les performances des doigts.

### Montage des doigts sur la paume
Une fois les doigts assemblés, il faut les placer sur la paume. Pour se faire, on glisse la goupille (dowel pin) dans le trou situé sur la phalange proximale du doigt de manière à ce que celle-ci dépasse également de chaque côté.

![dowel insert](https://github.com/frankgigeur/manUS-ludum/blob/main/M%C3%A9canique/Dessins/PNG/dowel_pin_insert.png)

Ensuite, on force le doigt avec la goupille dans chacune des positions de la paume pour les doigts correspondants. Une grande force pourrait être nécessaire.

![finger insert](https://github.com/frankgigeur/manUS-ludum/blob/main/M%C3%A9canique/Dessins/PNG/doigt_insertion.png)

### Montage des poulies sur la paume

Se fier à l'image suivante pour le montage des poulies de redirection des fils (agrafes à papier) sur la paume ainsi que le point de départ du fil de pêche:

![image](https://user-images.githubusercontent.com/73840473/232348058-5f65f2a4-4764-4f30-8342-b98ba0fd3554.png)


### Redirection des fils

Une fois la main assemblée et les poulies installées, il faut rediriger le fil de pêche vers les servos moteur. La figure suivante montre la redirection du fil pour le petit doigt. Les flèches rouges sont associés au fil du devant et les flèches bleues au fil du derrière. 
![image](https://user-images.githubusercontent.com/73840473/232348680-d7bfa03f-604b-4c3f-80bd-d12d4c30d56b.png)
![image](https://user-images.githubusercontent.com/73840473/232348693-baa05e3e-5d6a-425b-8686-4c460450115f.png)

Il est à noté que la redirection des fils de chaque doigt suit le même modèle que celui du petit doigt. Il suffit alors de reproduire pour chaque doigt.
