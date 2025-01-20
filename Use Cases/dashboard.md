%% Cas d'utilisation pour le Dashboard avec noms courts
flowchart TB
%% Acteurs
Etudiant((Étudiant))
Enseignant((Enseignant))
Utilisateur((Utilisateur))

    %% Dashboard principal
    Utilisateur -->|Profil| Profil[Configurer profil]
    Profil -->|<<extend>>| VoirInfo[Voir info]
    Profil -->|<<extend>>| Reglages[Paramètres]

    Utilisateur -->|Calendrier| Calendrier[Voir calendrier]
    Calendrier -->|<<include>>| Evenements[Événements]

    Utilisateur -->|Tâches| Taches[Voir tâches]
    Taches -->|<<include>>| Resume[Résumé]
    Taches -->|<<include>>| NotifTaches[Notif. tâches]

    Utilisateur -->|Messages| Messages[Voir messages]
    Messages -->|<<include>>| NotifMsg[Notif. msg]
    Messages -->|<<include>>| EnvoyerMsg[Envoyer msg]

    Utilisateur -->|Contact| Contact[Formulaire contact]
    Contact -->|<<extend>>| AllerForm[Aller au formulaire]

    Utilisateur -->|Logout| Logout[Déconnexion]

    %% Liens des acteurs
    Etudiant --> Utilisateur
    Enseignant --> Utilisateur
