%% Cas d'utilisation pour la gestion des tâches (version normale)
flowchart TB
%% Acteurs
Etudiant((Étudiant))
Enseignant((Enseignant))
Utilisateur((Utilisateur))

    %% Gestion des tâches
    Utilisateur -->|Créer une tâche pour lui-même| CreerPourSoi[Créer pour soi]
    Enseignant -->|Créer une tâche pour un étudiant| CreerPourAutre[Créer pour étudiant]
    Utilisateur -->|Consulter la liste des tâches| ConsulterListe[Consulter tâches]
    Utilisateur -->|Modifier une tâche existante| Modifier[Modifier tâche]
    Modifier -->|<<include>>| MettreAJourStatut[Mettre à jour le statut]
    Utilisateur -->|Supprimer une tâche| Supprimer[Supprimer tâche]

    %% Liens des acteurs
    Etudiant --> Utilisateur
    Enseignant --> Utilisateur
