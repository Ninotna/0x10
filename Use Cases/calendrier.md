%% Diagramme de cas d'utilisation pour l'agenda
graph TD
Utilisateur((Utilisateur enseignant ou élève)) -->|Se connecter| Connexion[Connexion]
Connexion -->|<<include>>| Agenda[Agenda]

    Agenda -->|<<include>>| Consulter[Consulter les evenements d un mois]
    Agenda -->|<<include>>| AjouterPerso[Ajouter un evenement personnel]
    Agenda -->|<<include>>| Supprimer[Supprimer un evenement]
    Agenda -->|<<include>>| AjouterEleve[Ajouter un evenement pour un eleve]

    Eleve((Eleve)) --> Consulter
    Enseignant((Enseignant)) --> AjouterPerso
    Enseignant --> AjouterEleve
    Enseignant --> Consulter
