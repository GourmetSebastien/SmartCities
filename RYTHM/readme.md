# RYTHM

## Objectif

Ce projet a pour but de créer un script MicroPython capable de contrôler une LED RGB connectée à un Raspberry Pi Pico W, en modifiant sa couleur en synchronisation avec la musique.

## Liste de matériel

- Raspberry Pi Pico W
- Module microphone
- Module LED RGB
- Fils de connexion

## Cablage

![alt text](image.png)

## Diagramme de flux

```mermaid
flowchart TD
    A[Début] --> B[Initialiser les variables]
    B --> C[Définir les couleurs]
    C --> D[Initialiser WS2812 et capteur de son]
    D --> E[Démarrer le thread de capteur]
    E --> F{En cours d'exécution ?}
    
    F -- Oui --> G[Lire le bruit du capteur]
    G --> H[Calculer la moyenne du bruit]
    H --> I[Imprimer la moyenne]
    I --> F
    
    F -- Non --> J[Arrêter le programme]
    
    subgraph Thread de Capteur
        F1{En cours d'exécution ?}
        F1 -- Oui --> K[Lire le bruit du capteur]
        K --> L[Calculer la moyenne]
        L --> I1[Imprimer la moyenne]
        I1 --> F1
        F1 -- Non --> J
    end

    F --> F1

    subgraph Boucle Principale
        F2{Moyenne > Ancienne + Seuil ?}
        F2 -- Oui --> M[Choisir une couleur aléatoire]
        M --> N[Mettre à jour la LED]
        N --> O[Afficher les pixels LED]
        O --> P[Mettre à jour l'ancienne moyenne]
        P --> F2
        
        F2 -- Non --> Q[Attendre 0.5 secondes]
        Q --> F2
    end

    F --> F2
```
