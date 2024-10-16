# AD-PWM

## Objectif

Développer un programme en MicroPython pour ajuster le volume d'une mélodie jouée sur un buzzer, avec le contrôle du volume assuré par un potentiomètre.

## Liste de matériel

- Microcontrôleur compatible MicroPython (Raspberry Pi Pico)
- Module potentiomètre
- Buzzer
- Câbles

## Principe

### PWM

Le PWM (Pulse Width Modulation), ou modulation de largeur d'impulsion, est une technique utilisée pour contrôler la puissance envoyée à un dispositif électronique (comme un moteur, une LED ou un buzzer) en modulant la durée pendant laquelle un signal reste actif. <br> La fréquence du signal PWM détermine la rapidité avec laquelle il oscille entre haut et bas. Une fréquence plus élevée signifie que le cycle de commutation se répète plus souvent par seconde. <br> Le rapport cyclique représente la proportion de temps pendant laquelle le signal est en état haut par rapport à un cycle complet.

![alt text](image.png)

## Cablage

![alt text](AD_PWM.png)

## Diagramme de flux

```mermaid
flowchart TD
    A[Début du Programme] --> B[Initialiser le Buzzer PWM sur Pin 27]
    B --> C[Initialiser le Capteur ADC sur ADC 0]
    C --> D[Définir le volume initial à 1000]
    D --> F[Définir les Fonctions des Notes Musicales]
    F --> G[Définir la Séquence Musicale : Frère Jacques]
    G --> E[Démarrer le Thread pour le Contrôle du Volume]
    G --> H[Démarrer la Boucle Principale]
    
    subgraph Thread pincipale
    H --> I{En cours d'éxécution?}
    I --> |Oui| J[Jouer la Séquence Frère Jacques]
    J --> K[Attendre 2 Secondes]
    K --> I

    end

    subgraph Thread
    E --> M[Exécuter le Thread de Contrôle du Volume]
    M --> N{En cours d'éxécution?}
    N --> |Oui| O[Lire le Volume depuis le Capteur]
    O --> P[Mettre à Jour le Cycle de Service du Buzzer]
    P --> N
    
    end

    I --non --> Q
    N --> |Non| Q[Arrêter le programme]
    Q --> R[Éteindre le Buzzer]
    R --> S[Fin du Programme]



```
