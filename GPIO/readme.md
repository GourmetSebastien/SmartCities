# GPIO

## Objectif

Écrire un programme en MicroPython qui fait clignoter une LED à des vitesses variées, en fonction du nombre de fois où l'on appuie sur un bouton poussoir.

## Liste de matériel

- Raspberry Pi Pico
- LED
- Bouton poussoir
- Cable

## Principe

### Bouton poussoir

Le bouton poussoir est un interrupteur temporaire (il n'agit que s'il est pressé). Il peut avoir deux états : 0 (relâché) ou 1 (appuyé).

Un phénomène de rebond peut apparaître lors de l'utilisation de ceux-ci. Ce phénomène se manifeste lorsqu'un bouton est pressé ou relâché, les contacts mécaniques ne se connectent ou ne se déconnectent pas immédiatement. Ces rebonds peuvent être interprétés comme une nouvelle pression par le programme. Afin de résoudre ce problème, il est possible d'ajouter un délai de quelques millisecondes du côté logiciel.

## Câblage

![alt text](SchemaExo1.png)

## Diagramme de séquence du contrôle de la LED

**Acteurs principaux** :

- **Utilisateur** : Appuie sur le bouton poussoir pour changer la vitesse de clignotement.
- **Thread principal** : Gère le clignotement de la LED selon l'état.
- **Thread secondaire** : Surveille les appuis sur le bouton poussoir et met à jour l'état (`state`).
- **LED** : Clignote à des vitesses différentes selon la valeur de l'état.

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

## Diagramme de flux

```mermaid
flowchart TD
    A[Début du programme] --> B[Initialisation des Pins]
    B --> C[Thread de surveillance du bouton démarré]
    C --> D[Thread boucle: Lire état du bouton]
    D --> E{Bouton appuyé ?}
    E -->|Non| F[Attendre 0.01s]
    F --> D
    E -->|Oui| G[Vérifier état précédent]
    G --> H[Incrémenter l'état]
    H --> I{L'état est > 3 ?}
    I -->|Oui| J[Réinitialiser l'état à 1]
    I -->|Non| K[Attendre debounce_time]
    J --> K
    K --> L[Retour à la boucle principale]
    
    L --> M{Appeler toggle_led}
    M -->|State == 1| N[Clignotement rapide de la LED]
    M -->|State == 2| O[Clignotement lent de la LED]
    M -->|State > 2| P[LED éteinte]
    N --> Q[Boucle jusqu'à l'arrêt]
    O --> Q
    P --> Q
    Q --> R[Fin du programme]
```
