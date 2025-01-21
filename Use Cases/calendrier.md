graph TD
Utilisateur((Utilisateur enseignant ou élève)) -->|Se connecter| Connexion[Connexion]
Connexion -->|<>| Agenda[Agenda]

    Agenda -->|<<include>>| Consulter[Consulter les événements d'un mois]
    Agenda -->|<<include>>| AjouterPerso[Ajouter un événement personnel]
    Agenda -->|<<include>>| Supprimer[Supprimer un événement]
    Agenda -->|<<include>>| AjouterEleve[Ajouter un événement pour un élève]

    Eleve((Élève)) --> Consulter
    Enseignant((Enseignant)) --> AjouterPerso
    Enseignant --> AjouterEleve
    Enseignant --> Consulter
