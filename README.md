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

## <h2>📁 Project Structure</h，拉>
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
- 🛡️ <b>Détection de fraudes dans les transactions</b> (detection_fraud_model.pkl)
- ⏱️ <b>Détection des délais de résolution anormaux</b> (detection_resolution_disputes_modele.pkl)

### <h3>💬 Chatbot – Analyse des Avis Clients</h3>
- Implémentation d’un chatbot basé sur des modèles NLP pour analyser les avis clients et répondre aux questions des utilisateurs en temps réel.
- ![Image](https://github.com/user-attachments/assets/2f2a6868-ed90-4950-a05d-1318cc986268)
- 
