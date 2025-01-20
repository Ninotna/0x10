%% Diagramme de cas d'utilisation avec sous-groupes
flowchart TB
%% Acteurs
Etudiant((Étudiant))
Enseignant((Enseignant))
Utilisateur((Utilisateur))
%% Sous-groupe - Créer un compte
subgraph CreationCompte [Créer un compte]
CreerCompte[Créer un compte]
CreerCompte -->|<<inclut>>| DefinirMDP[Définir un mot de passe]
CreerCompte -->|<<inclut>>| EmailValide[Adresse e-mail valide]
CreerCompte -->|<<étend>>| MessageValidation[Message de validation]
CreerCompte -->|<<inclut>>| VerifierIdentite[Vérifier l'identité]
end

%% Sous-groupe - Connexion
subgraph ConnexionSection [Connexion]
Connexion[Connexion]
Connexion -->|<<inclut>>| VerifierMDP[Vérifier le mot de passe]
Connexion -->|<<inclut>>| VerifierIdentite
Connexion -->|<<étend>>| AfficherErreur[Afficher une erreur]
end

%% Sous-groupe - Mot de passe oublié
subgraph MotDePasseOublie [Mot de passe oublié]
MdpOublie[Mot de passe oublié]
MdpOublie -->|<<étend>>| ReinitialiserMDP[Réinitialiser le mot de passe]
end

%% Liens des acteurs
Utilisateur --> CreerCompte
Utilisateur --> Connexion
Utilisateur --> MdpOublie
Etudiant --> Utilisateur
Enseignant --> Utilisateur
