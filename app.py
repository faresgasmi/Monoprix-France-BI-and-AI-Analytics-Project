import streamlit as st
import base64
import joblib
import numpy as np
import pandas as pd
from datetime import datetime, timedelta
import plotly.graph_objects as go
import torch
from sentence_transformers import SentenceTransformer, util
from transformers import BertTokenizer, BertForSequenceClassification

# Chargement des modèles et du scaler
kmeans = joblib.load('kmeans_model.pkl')
scaler = joblib.load('scaler.pkl')
regression_model = joblib.load('equity_model.pkl')
scaler_regression = joblib.load('scaler_regression.pkl')
rf_model = joblib.load('random_forest_model.pkl')
scaler_rf = joblib.load('scalerRandom.pkl')
fraud_model = joblib.load('isolation_forest_model.pkl')
dispute_model = joblib.load('newRetard.pkl')  # Updated to correct model

# Chargement des modèles pour le chatbot
@st.cache_resource
def load_models():
    model_similarity = SentenceTransformer('paraphrase-multilingual-MiniLM-L12-v2')
    tokenizer_sentiment = BertTokenizer.from_pretrained('nlptown/bert-base-multilingual-uncased-sentiment')
    model_sentiment = BertForSequenceClassification.from_pretrained('nlptown/bert-base-multilingual-uncased-sentiment')
    return model_similarity, tokenizer_sentiment, model_sentiment

model_similarity, tokenizer_sentiment, model_sentiment = load_models()

# Fonction d’analyse de sentiment
def analyse_sentiment(texte):
    inputs = tokenizer_sentiment(texte, return_tensors="pt", truncation=True, padding=True, max_length=512)
    with torch.no_grad():
        outputs = model_sentiment(**inputs)
        logits = outputs.logits
        sentiment = torch.argmax(logits, dim=-1).item()
    sentiments = ["très négatif", "négatif", "neutre", "positif", "très positif"]
    return sentiments[sentiment]

# Fonction de réponse chatbot
def repondre_utilisateur(question, avis, avis_embeddings):
    question_embedding = model_similarity.encode(question, convert_to_tensor=True)
    similarites = util.pytorch_cos_sim(question_embedding, avis_embeddings)
    index_meilleur_avis = similarites.argmax()
    meilleur_avis = avis[index_meilleur_avis]
    sentiment_meilleur_avis = analyse_sentiment(meilleur_avis)
    return meilleur_avis, sentiment_meilleur_avis

# CSS global pour toutes les pages (sans image de fond)
st.markdown("""
    <style>
        .header { font-size: 40px; color: #1E90FF; font-weight: bold; text-align: center; }
        .subheader { font-size: 30px; color: #20B2AA; font-weight: bold; }
        .section-title { font-size: 24px; color: #D2691E; }
        .model-info { font-size: 16px; color: #4B0082; }
        .result { font-size: 20px; color: #228B22; font-weight: bold; }
    </style>
""", unsafe_allow_html=True)

# Lire et encoder l'image locale
def set_background(image_file):
    with open(image_file, "rb") as f:
        encoded = base64.b64encode(f.read()).decode()
    return f"data:image/jpg;base64,{encoded}"

# Page principale
def main_page():
    # Appliquer l'image de fond uniquement pour la page principale
    background_image = set_background("new.jpg")

    st.markdown(f"""
        <style>
            .stApp {{
                background-image: url("{background_image}");
                background-size: cover;
                background-position: center;
                background-repeat: no-repeat;
                background-attachment: fixed;
            }}

            .card {{
                background-color: rgba(255, 255, 255, 0.95);
                padding: 20px 30px;
                border-radius: 15px;
                margin: 20px auto;
                width: fit-content;
                text-align: center;
                box-shadow: 0 6px 16px rgba(0, 0, 0, 0.2);
            }}

            .page-title {{
                font-size: 28px;
                font-weight: bold;
                color: #1E90FF;
                margin: 0;
            }}

            .main-button {{
                display: inline-block;
                padding: 15px 30px;
                font-size: 18px;
                font-weight: bold;
                color: #1E90FF;
                background-color: rgba(255, 255, 255, 0.9);
                border: 2px solid #1E90FF;
                border-radius: 10px;
                text-decoration: none;
                text-align: center;
                transition: all 0.3s ease;
                box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
            }}

            .main-button:hover {{
                background-color: #20B2AA;
                color: #FFFFFF;
                border-color: #20B2AA;
                transform: translateY(-2px);
                box-shadow: 0 6px 12px rgba(0, 0, 0, 0.3);
            }}
        </style>
    """, unsafe_allow_html=True)

    # Titre dans une carte séparée
    st.markdown('<div class="card"><div class="page-title">Application complète : IA + Dashboard Power BI</div></div>', unsafe_allow_html=True)

    # Deux colonnes pour les boutons, chacun dans une carte
    col1, col2 = st.columns([1, 1])

    with col1:
        st.markdown('<div class="card"><a href="?page=models" class="main-button">Accéder aux Modèles IA</a></div>', unsafe_allow_html=True)

    with col2:
        st.markdown('<div class="card"><a href="?page=dashboard" class="main-button">Voir le Dashboard Power BI</a></div>', unsafe_allow_html=True)

# Page des modèles
def models_page():
    # Sidebar
    st.sidebar.title("Modèles")
    selected_model = st.sidebar.radio(
        "Sélectionnez un modèle",
        (
            "🔍 Segmentation des clients avec KMeans",
            "📊 Prédiction de l'Equity",
            "📈 Prédiction du Budget avec ARIMA",
            "🌲 Prédiction de la Classe avec Random Forest",
            "🤖 Chatbot Monoprix - Avis Clients",
            "🕵️ Détection de Fraude - Transactions",
            "⏰ Détection du Délai de Résolution de la Dispute"
        ),
        key="model_selector"
    )

    # Chargement des données d'avis pour le chatbot
    @st.cache_data
    def load_data():
        df = pd.read_csv('avis_monoprix.csv', encoding='cp1252', sep=';')
        avis = df["Content"].dropna().tolist()
        embeddings = model_similarity.encode(avis, convert_to_tensor=True)
        return avis, embeddings

    avis, avis_embeddings = load_data()

    # Chatbot
    if selected_model == "🤖 Chatbot Monoprix - Avis Clients":
        st.markdown('<p class="header">Chatbot Monoprix - Avis Clients</p>', unsafe_allow_html=True)
        st.markdown('<p class="model-info">Posez une question sur Monoprix et obtenez une réponse basée sur les avis clients.</p>', unsafe_allow_html=True)
        question = st.text_input("Pose une question sur Monoprix :", key="chatbot_question")
        if question:
            with st.spinner("Réflexion en cours..."):
                avis_reponse, sentiment_reponse = repondre_utilisateur(question, avis, avis_embeddings)
            st.markdown("### 💬 Réponse du chatbot :")
            st.success(avis_reponse)
            st.markdown("### 😊 Analyse de sentiment :")
            st.info(f"Sentiment : **{sentiment_reponse}**")

    # KMeans
    elif selected_model == "🔍 Segmentation des clients avec KMeans":
        st.markdown('<p class="header">Segmentation des clients avec KMeans</p>', unsafe_allow_html=True)
        amount = st.number_input("Montant (Amount)", min_value=0.0, key="kmeans_amount")
        total_price = st.number_input("Prix Total (Total Price)", min_value=0.0, key="kmeans_total_price")
        if st.button("Prédire le cluster", key="kmeans_predict"):
            data = np.array([[amount, total_price]])
            data_scaled = scaler.transform(data)
            cluster = kmeans.predict(data_scaled)
            st.markdown(f'<p class="result">Le client appartient au cluster : {cluster[0]}</p>', unsafe_allow_html=True)

    # Régression Equity
    elif selected_model == "📊 Prédiction de l'Equity":
        st.markdown('<p class="header">Prédiction de l\'Equity</p>', unsafe_allow_html=True)
        total_assets = st.number_input("Total des actifs (Total Assets)", min_value=0.0, key="equity_assets")
        budget = st.number_input("Budget", min_value=0.0, key="equity_budget")
        if st.button("Prédire l'Equity", key="equity_predict"):
            data_regression = np.array([[total_assets, budget]])
            data_scaled_regression = scaler_regression.transform(data_regression)
            equity_prediction = regression_model.predict(data_scaled_regression)
            st.markdown(f'<p class="result">L\'Equity prédit est : {equity_prediction[0]:.2f}</p>', unsafe_allow_html=True)

    # ARIMA
    elif selected_model == "📈 Prédiction du Budget avec ARIMA":
        st.markdown('<p class="header">Prédiction du Budget avec ARIMA</p>', unsafe_allow_html=True)
        try:
            df_budget = pd.read_csv("data.csv", skiprows=[1], parse_dates=["StatementDate"])
            df_budget = df_budget.sort_values("StatementDate")
            df_budget.set_index("StatementDate", inplace=True)
            df_budget["Budget"] = df_budget["Budget"].str.replace(",", ".").astype(float)
        except Exception as e:
            st.error("❌ Erreur chargement série : " + str(e))
            df_budget = None

        try:
            arima_model = joblib.load("arima_model.pkl")
        except Exception as e:
            st.error("❌ Erreur chargement modèle ARIMA : " + str(e))
            arima_model = None

        if df_budget is not None and arima_model is not None:
            n_periods = st.slider("Nombre de mois à prédire :", 1, 24, 6, key="arima_periods")
            forecast = arima_model.forecast(steps=n_periods)
            last_date = df_budget.index[-1]
            future_dates = [last_date + timedelta(days=30 * i) for i in range(1, n_periods + 1)]
            df_forecast = pd.DataFrame({"Date": future_dates, "Prévision Budget": forecast}).set_index("Date")

            fig = go.Figure()
            fig.add_trace(go.Scatter(x=df_budget.index, y=df_budget['Budget'], mode='lines', name='Historique'))
            fig.add_trace(go.Scatter(x=df_forecast.index, y=df_forecast['Prévision Budget'], mode='lines+markers', name='Prévision'))
            fig.update_layout(title="📊 Prédiction du Budget", xaxis_title="Date", yaxis_title="Budget", template="plotly_white")
            st.plotly_chart(fig)
            st.markdown('<p class="section-title">📅 Prévisions détaillées :</p>', unsafe_allow_html=True)
            st.dataframe(df_forecast.style.format({"Prévision Budget": "{:.2f}"}))
            st.markdown(f'<p class="result">✅ Prévision pour les {n_periods} mois à venir terminée.</p>', unsafe_allow_html=True)

    # Random Forest
    elif selected_model == "🌲 Prédiction de la Classe avec Random Forest":
        st.markdown('<p class="header">Prédiction de la Classe avec Random Forest</p>', unsafe_allow_html=True)
        amount_paid = st.number_input("Montant payé (Amount Paid)", min_value=0.0, key="rf_amount_paid")
        total_sales = st.number_input("Total des ventes (Total Sales)", min_value=0.0, key="rf_total_sales")
        if st.button("Prédire la classe", key="rf_predict"):
            data_rf = np.array([[amount_paid, total_sales]])
            data_scaled_rf = scaler_rf.transform(data_rf)
            class_prediction = rf_model.predict(data_scaled_rf)
            st.markdown(f'<p class="result">Classe prédite : {class_prediction[0]}</p>', unsafe_allow_html=True)

    # Détection de fraude
    elif selected_model == "🕵️ Détection de Fraude - Transactions":
        st.markdown('<p class="header">🕵️ Détection de Fraude dans les Transactions Fournisseur</p>', unsafe_allow_html=True)
        uploaded_file = st.file_uploader("📤 Téléverser un fichier CSV de transactions Monoprix :", type=["csv"], key="fraud_upload")
        if uploaded_file is not None:
            df = pd.read_csv(uploaded_file, encoding='cp1252', sep=';')

            st.markdown('<p class="section-title">Aperçu des données :</p>', unsafe_allow_html=True)
            st.dataframe(df.head())

            # Colonnes utilisées à l'entraînement
            features = ['SupplierFk', 'ProduitFk', 'Delai_Paiement', 'Delai_Dispute',
                        'AmountDue', 'AmountPaid', 'BalanceDue', 'TotalDiscountUsed',
                        'TotalSales', 'DiscountOffered']

            # Vérification des colonnes manquantes et ajout de colonnes manquantes avec valeur par défaut
            for col in features:
                if col not in df.columns:
                    df[col] = 0
                    st.warning(f"Colonne ajoutée avec valeur par défaut : {col}")

            # Nettoyage des colonnes
            for col in features:
                df[col] = df[col].astype(str).str.replace(',', '.').str.replace(' ', '')
                df[col] = pd.to_numeric(df[col], errors='coerce').fillna(0)

            try:
                data = df[features]
                anomalies = fraud_model.predict(data)
                df["Fraude"] = ["❌ Fraude" if x == -1 else "✅ OK" for x in anomalies]

                st.markdown('<p class="section-title">Résultats de la détection :</p>', unsafe_allow_html=True)
                st.dataframe(df)
                st.markdown(f'<p class="result">✅ Détection terminée.</p>', unsafe_allow_html=True)

            except Exception as e:
                st.error(f"❌ Erreur lors de la détection : {e}")

    # Détection du délai de résolution de la dispute
    elif selected_model == "⏰ Détection du Délai de Résolution de la Dispute":
        st.markdown('<p class="header">⏰ Détection du Délai de Résolution de la Dispute</p>', unsafe_allow_html=True)
        st.markdown('<p class="model-info">Prédisez si un retard dans la résolution de la dispute est détecté ou non.</p>', unsafe_allow_html=True)

        # Debug: Afficher le nombre de caractéristiques attendues
        st.write(f"Nombre de caractéristiques attendues par le modèle : {dispute_model.n_features_in_}")
        if hasattr(dispute_model, 'feature_names_in_'):
            st.write(f"Noms des caractéristiques : {dispute_model.feature_names_in_}")

        # Entrées utilisateur pour les 5 features
        amount_due = st.number_input("Montant dû (AmountDue)", min_value=0.0, value=0.0, key="dispute_amount_due")
        amount_paid = st.number_input("Montant payé (AmountPaid)", min_value=0.0, value=0.0, key="dispute_amount_paid")
        balance_due = st.number_input("Solde dû (BalanceDue)", min_value=0.0, value=0.0, key="dispute_balance_due")
        total_discount_used = st.number_input("Total des remises utilisées (TotalDiscountUsed)", min_value=0.0, value=0.0, key="dispute_total_discount_used")
        total_sales = st.number_input("Total des ventes (TotalSales)", min_value=0.0, value=0.0, key="dispute_total_sales")

        if st.button("Vérifier si un retard est détecté", key="dispute_predict"):
            with st.spinner("Analyse en cours..."):
                # Créer une nouvelle ligne pour tester
                nouvelle_transaction = pd.DataFrame({
                    'AmountDue': [amount_due],
                    'AmountPaid': [amount_paid],
                    'BalanceDue': [balance_due],
                    'TotalDiscountUsed': [total_discount_used],
                    'TotalSales': [total_sales]
                })

                try:
                    # Prédire le retard avec le modèle
                    prediction = dispute_model.predict(nouvelle_transaction)[0]
                    result = "❌ Retard détecté dans la résolution de la dispute !" if prediction == 1 else "✅ Pas de retard détecté dans la résolution de la dispute."

                    # Afficher les résultats
                    st.markdown("### Résultat de la détection :")
                    st.markdown(f'<p class="result">{result}</p>', unsafe_allow_html=True)
                    st.markdown("#### Détails de la transaction :")
                    st.markdown(f"💰 **Montant dû** : {amount_due:.2f}")
                    st.markdown(f"💸 **Montant payé** : {amount_paid:.2f}")
                    st.markdown(f"⚖️ **Solde dû** : {balance_due:.2f}")
                    st.markdown(f"🎁 **Total des remises utilisées** : {total_discount_used:.2f}")
                    st.markdown(f"📈 **Total des ventes** : {total_sales:.2f}")
                except ValueError as e:
                    st.error(f"❌ Erreur lors de la prédiction : {e}")
                    st.warning("Il semble que le modèle 'newRetard.pkl' attende des caractéristiques différentes (par exemple, 2 caractéristiques comme SupplierFk et DelaiPaiement). Veuillez vérifier que le modèle est entraîné sur les 5 caractéristiques suivantes : AmountDue, AmountPaid, BalanceDue, TotalDiscountUsed, TotalSales. Sinon, mettez à jour les entrées pour correspondre aux caractéristiques attendues.")

# Page du dashboard
def dashboard_page():
    st.markdown('<p class="header">Visualisation Dashboard Power BI</p>', unsafe_allow_html=True)
    dashboard_url = "https://app.powerbi.com/reportEmbed?reportId=f0b3c283-b7aa-4715-9167-9aa1b2350ab4&autoAuth=true&ctid=604f1a96-cbe8-43f8-abbf-f8eaf5d85730"
    st.components.v1.iframe(dashboard_url, height=600, width=1000)

# Navigation
query_params = st.query_params
page = query_params.get("page", "main")

if page == "main":
    main_page()
elif page == "models":
    models_page()
elif page == "dashboard":
    dashboard_page()