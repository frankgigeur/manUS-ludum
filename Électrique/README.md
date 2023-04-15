# Documentation ManUS Ludum - Électrique

## Liste des matériaux et composantes
### **Électrique**
- [ ] &nbsp;Arduino Mega 2560  [(Arduino)](https://ca.robotshop.com/fr/products/hitec-hs-422-servo-motor) <br>
- [ ] &nbsp;Module PCA9685 [(Adafruit)](https://learn.adafruit.com/16-channel-pwm-servo-driver?view=all) <br>
- [ ] &nbsp;Connecteurs mâle-femelle type "jumper" (**x4**) <br>
- [ ] &nbsp;Alimentation 12V <br>
- [ ] &nbsp;Câble USB type A/B <br>

## Assemblage électrique
L'assemblage électrique du projet se résume aux étapes suivantes en se basant sur le schéma électrique suivant : ![Schema electrique](https://github.com/frankgigeur/manUS-ludum/blob/main/%C3%89lectrique/Schema_electrique.png)


1. Connecter les fils 5V, GND, SDA, SCL de l'Arduino au module PCA9685 selon le schéma ci-haut à l'aide des connecteurs mâle-femelle.

2. Connecter les fils des servomoteurs au module PCA9685 selon le schéma électrique en s'assurant de les placer dans le bon sens (bien regarder que le fil noir du servomoteur soit connecté au GND du module).

3. Connecter le convertisseur 12V à 5V au module PCA9685 toujours selon le schéma électrique.

4. Connecter l'alimentation 12V au Arduino et au convertisseur 12V à 5V.

5. Connecter le câble USB type A/B au Arduino ainsi qu'à l'ordinateur.
