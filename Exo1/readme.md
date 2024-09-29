# Exo 1

## Objectif

 Écrire un programme en MicroPython qui fait clignoter une LED à des vitesses variées, en fonction du nombre de fois où l'on appuie sur un bouton poussoir.

# Diagramme de séquence du contrôle de la LED

Acteurs principaux :
        - Utilisateur : Appuie sur le bouton poussoir pour changer la vitesse de clignotement.

        - Thread principal : Gère le clignotement de la LED selon l'état.

        - Thread secondaire : Surveille les appuis sur le bouton poussoir et met à jour l'état (state).

        - LED : Clignote à des vitesses différentes selon la valeur de l'état.

```mermaid
sequenceDiagram
    participant B as Utilisateur
    participant T as Thread secondaire
    participant L as LED
    participant M as Boucle Principale

    B->>T: Appuyer sur le bouton
    T->>T: Lire l'état du bouton
    T-->>T: Vérifier l'état précédent
    alt Si le bouton est pressé
        T->>T: Incrémenter l'état
        T->>T: Vérifier si l'état > 3
        T-->>T: Réinitialiser l'état à 1
    end
    T->>T: Attendre debounce_time
    T->>T: Mettre à jour l'état précédent
    T->>M: Notification de changement d'état

    M->>M: Appeler toggle_led(state)
    alt Si delay est défini
        M->>L: Basculer l'état de la LED
        M->>M: Attendre delay
    else
        M->>L: Éteindre la LED
    end

    M->>T: Boucle jusqu'à l'arrêt
```
