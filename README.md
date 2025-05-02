# <h1>Monoprix France – BI & AI Analytics Project</h1>

## <h2>📝 Overview</h2>
Ce projet combine Business Intelligence (BI) et Intelligence Artificielle (IA) pour aider Monoprix France à :

- Mieux gérer les relations avec les fournisseurs
- Améliorer le suivi financier
- Comprendre les comportements clients
- Prendre des décisions basées sur les données

Le projet comprend :

- Un dashboard Power BI interactif
- Des modèles IA/ML (machine learning) pour la prédiction de budget, l’analyse NLP, etc.

## <h2>🚀 Key Features</h2>

### <h3>Staging Area for Data Integration</h3>
- Création d'une <i>staging area</i> centralisant les données provenant de multiples sources sur Monoprix France (financières, fournisseurs, clients, etc.).
- Harmonisation et nettoyage des données avant leur traitement pour garantir la qualité et la fiabilité de l'analyse.

### <h3>ETL Process to Build a Data Warehouse</h3>
- Mise en place d'un processus ETL (<i>Extract, Transform, Load</i>) pour nettoyer, transformer et charger les données dans une <i>data warehouse</i> structurée.
- Organisation des données sous forme de tables de faits et dimensions pour optimiser les requêtes et analyses.

### <h3>Machine Learning Models</h3>
- Développement de modèles <i>Machine Learning</i> pour des tâches de prédiction de l'équité et classification des clients selon les ventes totales et le montant payé.
- Implémentation de modèles NLP pour créer un <i>chatbot</i> capable de répondre aux questions des utilisateurs basées sur des données textuelles.
- Utilisation de modèles avancés comme les séries temporelles pour prédire des tendances financières et comportementales.

### <h3>Power BI Dashboard for Decision-Making</h3>
- Création d'un <i>dashboard Power BI</i> interactif pour visualiser les données de manière dynamique et comprendre les performances sur trois axes : <i>Finance Management</i>, <i>Supplier Management</i>, et <i>Customer Management</i>.
- Analyse des principaux KPI pour aider à la prise de décision au sein de Monoprix France.

### <h3>Deployment with Streamlit</h3>
- Déploiement des modèles et du tableau de bord via <i>Streamlit</i>, offrant une interface utilisateur interactive et conviviale.
- Création de pages dédiées pour les modèles de <i>Machine Learning</i> et le <i>Power BI Dashboard</i>, permettant aux utilisateurs d'interagir avec les résultats de manière fluide.

## <h2>🛠 Technologies Used</h2>
- <b>Power BI</b> pour la visualisation des données et la création des dashboards interactifs.
- <b>Machine Learning</b> (scikit-learn, TensorFlow, etc.) pour les modèles de prédiction et de classification.
- <b>Natural Language Processing (NLP)</b> pour la création du chatbot intelligent.
- <b>Azure SQL Database</b> pour le stockage structuré des données.
- <b>ETL Tools</b> (SQL, Python, etc.) pour le processus de transformation des données.
- <b>Streamlit</b> pour le déploiement de l’application et l'interface utilisateur.

## <h2>📊 Data Sources</h2>
- <b>Sources de données internes de Monoprix</b>: Données financières, fournisseurs, ventes, etc.
- <b>Processus de collecte des données</b>: Les données sont extraites, nettoyées et intégrées dans la <i>staging area</i> avant d’être transformées et chargées dans la <i>data warehouse</i>.

## <h2>📁 Project Structure</h2>
<pre>
├── Monoprix_image.jpg                       # Illustration utilisée dans le README ou l’app
├── app.py                                   # Application Streamlit (interface utilisateur)
├── avis_monoprix.csv                        # Données clients ou feedbacks
├── budget_data.csv                          # Données budgétaires utilisées pour les modèles
├── *.pkl (modèles ML & scalers)             # Modèles IA/ML pré-entraînés et objets de normalisation
├── README.md                                # Documentation du projet
</pre>

## <h2>📸 Screenshots</h2>

### <h3>🔍 Page de Déploiement – Modèles Machine Learning</h3>
Cette capture d’écran illustre la page principale de l’application Streamlit, dédiée au déploiement des modèles d’intelligence artificielle développés pour Monoprix France.

✅ <b>Modèles disponibles sur l’interface</b> :
- 🎯 <b>Prédiction de l’équité financière des clients</b> (equity_model.pkl)
- 👥 <b>Classification des clients selon leurs achats</b> (client_classe_model.pkl)
- 🧠 <b>Segmentation comportementale des clients</b> (segmentation_client_model.pkl)
- 📊 <b>Prédiction budgétaire avec des modèles de séries temporelles</b> (predection_budget_serie_temporaire.pkl)
- 🛡️ <b>Détection de fraudes dans Estamos transactions</b> (detection_fraud_model.pkl)
- ⏱️ <b>Détection des délais de résolution anormaux</b> (detection_resolution_disputes_modele.pkl)

### <h3>💬 Chatbot – Analyse des Avis Clients</h3>
- Implémentation d’un chatbot basé sur des modèles NLP pour analyser les avis clients et répondre aux questions des utilisateurs en temps réel.
- ![Image](https://github.com/user-attachments/assets/0a9a9260-01f9-4842-9fe4-8e25ec77aba2)

### <h3>📊 Power BI Dashboard</h3>

#### <h4>💼 Finance Management</h4>
- La capture d’écran montre un tableau de bord de gestion financière avec des indicateurs clés tels que :
  - <b>Ventes totales</b>: 35K €
  - <b>Bénéfices</b>: 20K €
  - <b>Capitaux propres</b>: 23,1M €
  - <b>Budget</b>: 6M €
- Visualisations incluant :
  - Un graphique des <b>top 10 des ventes par magasin</b>.
  - Un graphique des <b>tendances des ventes</b>.
- Utilisation de formules DAX pour des analyses comparatives, par exemple :
  - Comparaison des ventes totales avec l’année et le mois précédents, en utilisant les fonctions <b>PREVIOUSMONTH</b> et <b>SAMEPERIODLASTYEAR</b> pour calculer les variations.
  - ![Image](https://github.com/user-attachments/assets/e3af6be4-8c83-4f0a-b1ad-662699235da9)

#### <h4>🏭 Supplier Management</h4>
- La capture d’écran montre un tableau de bord "<i>Supplier Manager</i>" avec des indicateurs clés tels que :
  - <b>Nombre de litiges ouverts</b>: 12
  - <b>Total des achats</b>: 48,2K €
- Visualisations incluant :
  - Un graphique des <b>soldes impayés par fournisseur</b>.
  - Un graphique des <b>ventes totales par fournisseur</b>.
- Utilisation de formules DAX pour des analyses comparatives, par exemple :
  - Comparaison des soldes impayés avec l’année et le mois précédents, en utilisant les fonctions <b>PREVIOUSMONTH</b> et <b>SAMEPERIODLASTYEAR</b> pour calculer les variations.
  - ![Image](https://github.com/user-attachments/assets/dbc7df83-022b-4ce1-bd9c-f10ec9201994)

#### <h4>👥 Customer Management</h4>
- La capture d’écran présente un tableau de bord dédié à la gestion des clients, mettant en avant :

  **Indicateurs clés** :
  - <b>Nombre de clients actifs</b>: Non précisé (ex. : 250)
  - <b>Chiffre d’affaires total</b>: 35K € (affiché dans le graphique des revenus annuels)
  - <b>Nombre de transactions</b>: 175 (maximum en 2024)

  **Visualisations principales** :
  - <b>Classement des clients par ventes</b> :
    - Top 10 clients (ex. : Client 1372 avec 1 000 €, Client 492 avec 500 €).
  - <b>Comparaison annuelle</b> :
    - Revenus clients (de 0 à 35K €) vs. nombre de transactions (de 0 à 175), avec données pour 2020, 2022, 2024.
  - <b>Évaluation des auteurs/clients</b> :
    - Tableau de notes (Rating) et catégories (ex. : Excellent, Correct).

  **Analyse avancée (DAX)** :
  - Des formules comme <b>PREVIOUSMONTH</b> ou <b>SAMEPERIODLASTYEAR</b> pourraient être utilisées pour :
    - Comparer les ventes mensuelles ou annuelles avec les périodes précédentes.
    - Calculer des tendances (ex. : croissance des transactions entre 2020 et 2024).
    - ![Image](https://github.com/user-attachments/assets/f1c309e7-6e6c-4544-91bf-fd4c4cdc555f)
