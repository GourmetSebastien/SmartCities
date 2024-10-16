# LCD

## Objectif

Développer un programme en MicroPython pour contrôler un thermostat multi-états.

## Liste de matériel

- Microcontrôleur compatible MicroPython (Raspberry Pi Pico)
- Module capteur température/humidité
- Module LED
- Module potentiomètre
- Module écran LCD
- Module Buzzer
- Câbles

## Principe

### LCD

Un LCD (Liquid Crystal Display) est un écran qui utilise des cristaux liquides pour afficher des informations visuelles, telles que du texte, des chiffres ou des images.<br> Les critaux liquides ont la capacité de changer leur orientation lorsqu'un courant électrique leur est appliqué.<br>Derrière les cristaux liquides, il y a une source de lumière (rétroéclairage), qui émet de la lumière à travers les cristaux. En modifiant l'orientation des cristaux liquides avec un courant électrique, il est possible de contrôler la quantité de lumière qui passe à travers chaque pixel de l'écran.

### I2C

L'I2C (Inter-Integrated Circuit) est un protocole de communication série qui permet aux microcontrôleurs et autres composants électroniques de communiquer entre eux.<br>Le protocole I2C fonctionne selon un modèle maître-esclave :

- Maître : Le dispositif qui initie et contrôle la communication. Le microcontrôleur joue souvent le rôle de maître.
- Esclaves : Les dispositifs qui reçoivent les commandes du maître.

<br>L'I2C utilise deux lignes pour la communication :

- SDA (Serial Data Line) : C'est la ligne de données, utilisée pour transmettre les données entre les dispositifs.
- SCL (Serial Clock Line) : C'est la ligne d'horloge, qui synchronise les transmissions de données entre les dispositifs.

## Cablage

![alt text](image.png)

## Diagramme de flux

```mermaid
flowchart TD
    A[Début du Programme] --> B[Initialiser I2C pour LCD]
    B --> C[Initialiser le capteur DHT11]
    C --> D[Initialiser Buzzer et LED PWM]
    D --> E[Initialiser Potentiomètre ADC]
    E --> F[Définir Variables et Fonction ConversionTemp]

    F --> G[Début de la Boucle Principale]
    G --> H[Lire la valeur du Potentiomètre]
    H --> I[Convertir la valeur en Température de Consigne]

    I --> J[Lire la Température Actuelle du capteur DHT11]
    J --> K{Température Actuelle > Température de Consigne ?}
    
    K --> |Oui| L[Activer la LED PWM à 100%]
    L --> M{Température Actuelle > Température de Consigne + 3 ?}
    M --> |Oui| N[Activer le Buzzer et Afficher ALARM sur LCD]
    N --> O[Mise à jour de la Température de Consigne]
    O --> M
    M --> |Non| P[Désactiver le Buzzer]
    P --> Q[Désactiver la LED]
    K --> |Non| Q

    Q --> R[Effacer l'écran LCD]
    R --> S[Afficher Température de Consigne sur LCD]
    S --> T[Afficher Température Actuelle sur LCD]
    T --> U[Attendre 1 Seconde]
    U --> G

```
