# <h1>Monoprix France – BI & AI Analytics Project</h1>

## <h2>📝 Overview</h2>
This project combines Business Intelligence (BI) and Artificial Intelligence (AI) to assist Monoprix France in:

- Improving supplier relationship management
- Enhancing financial tracking
- Understanding customer behaviors
- Making data-driven decisions

The project includes:

- An interactive Power BI dashboard
- AI/ML (machine learning) models for budget prediction, NLP analysis, and more

## <h2>🚀 Key Features</h2>

### <h3>Staging Area for Data Integration</h3>
- Creation of a <i>staging area</i> to centralize data from multiple sources at Monoprix France (financial, supplier, customer, etc.).
- Data harmonization and cleaning before processing to ensure quality and reliability of analysis.

### <h3>ETL Process to Build a Data Warehouse</h3>
- Implementation of an ETL (<i>Extract, Transform, Load</i>) process to clean, transform, and load data into a structured <i>data warehouse</i>.
- Data organized into fact and dimension tables to optimize queries and analyses.

### <h3>Machine Learning Models</h3>
- Development of <i>Machine Learning</i> models for tasks such as equity prediction and customer classification based on total sales and payments.
- Implementation of NLP models to create a <i>chatbot</i> capable of answering user questions based on textual data.
- Use of advanced models like time series for predicting financial and behavioral trends.

### <h3>Power BI Dashboard for Decision-Making</h3>
- Creation of an interactive <i>Power BI dashboard</i> to dynamically visualize data and understand performance across three axes: <i>Finance Management</i>, <i>Supplier Management</i>, and <i>Customer Management</i>.
- Analysis of key KPIs to support decision-making within Monoprix France.

### <h3>Deployment with Streamlit</h3>
- Deployment of models and the dashboard via <i>Streamlit</i>, providing an interactive and user-friendly interface.
- Dedicated pages for <i>Machine Learning</i> models and the <i>Power BI Dashboard</i>, enabling seamless user interaction with results.

## <h2>🛠 Technologies Used</h2>
- <b>Power BI</b> for data visualization and creation of interactive dashboards.
- <b>Machine Learning</b> (scikit-learn, TensorFlow, etc.) for prediction and classification models.
- <b>Natural Language Processing (NLP)</b> for the creation of an intelligent chatbot.
- <b>Azure SQL Database</b> for structured data storage.
- <b>ETL Tools</b> (SQL, Python, etc.) for the data transformation process.
- <b>Streamlit</b> for application deployment and user interface.

## <h2>📊 Data Sources</h2>
- <b>Internal Monoprix data sources</b>: Financial data, supplier data, sales, etc.
- <b>Data collection process</b>: Data is extracted, cleaned, and integrated into the <i>staging area</i> before being transformed and loaded into the <i>data warehouse</i>.

## <h2>📁 Project Structure</h2>
<pre>
├── Monoprix_image.jpg                       # Illustration used in the README or app
├── app.py                                   # Streamlit application (user interface)
├── avis_monoprix.csv                        # Customer data or feedback
├── budget_data.csv                          # Budget data used for models
├── *.pkl (ML models & scalers)              # Pre-trained AI/ML models and normalization objects
├── README.md                                # Project documentation
</pre>

## <h2>📸 Screenshots</h2>

### <h3>🔍 Deployment Page – Machine Learning Models</h3>
This screenshot illustrates the main page of the Streamlit application, dedicated to deploying the AI models developed for Monoprix France.

✅ <b>Models available on the interface</b> :
- 🎯 <b>Financial equity prediction for customers</b> (equity_model.pkl)
- 👥 <b>Customer classification based on purchases</b> (client_classe_model.pkl)
- 🧠 <b>Behavioral customer segmentation</b> (segmentation_client_model.pkl)
- 📊 <b>Budget forecasting with time series models</b> (predection_budget_serie_temporaire.pkl)
- 🛡️ <b>Fraud detection in transactions</b> (detection_fraud_model.pkl)
- ⏱️ <b>Detection of abnormal dispute resolution delays</b> (detection_resolution_disputes_modele.pkl)

### <h3>💬 Chatbot – Customer Review Analysis</h3>
- Implementation of a chatbot based on NLP models to analyze customer reviews and answer user questions in real-time.
- ![Image](https://github.com/user-attachments/assets/0a9a9260-01f9-4842-9fe4-8e25ec77aba2)

### <h3>📊 Power BI Dashboard</h3>

#### <h4>💼 Finance Management</h4>
- The screenshot shows a financial management dashboard with key metrics such as:
  - <b>Total sales</b>: 35K €
  - <b>Profits</b>: 20K €
  - <b>Equity</b>: 23.1M €
  - <b>Budget</b>: 6M €
- Visualizations include:
  - A chart of the <b>top 10 sales by store</b>.
  - A chart of <b>sales trends</b>.
- Use of DAX formulas for comparative analysis, for example:
  - Comparing total sales with the previous year and month using <b>PREVIOUSMONTH</b> and <b>SAMEPERIODLASTYEAR</b> functions to calculate variations.
  - ![Image](https://github.com/user-attachments/assets/e3af6be4-8c83-4f0a-b1ad-662699235da9)

#### <h4>🏭 Supplier Management</h4>
- The screenshot shows a "<i>Supplier Manager</i>" dashboard with key metrics such as:
  - <b>Open disputes</b>: 12
  - <b>Total purchases</b>: 48.2K €
- Visualizations include:
  - A chart of <b>outstanding balances by supplier</b>.
  - A chart of <b>total sales by supplier</b>.
- Use of DAX formulas for comparative analysis, for example:
  - Comparing outstanding balances with the previous year and month using <b>PREVIOUSMONTH</b> and <b>SAMEPERIODLASTYEAR</b> functions to calculate variations.
  - ![Image](https://github.com/user-attachments/assets/dbc7df83-022b-4ce1-bd9c-f10ec9201994)

#### <h4>👥 Customer Management</h4>
- The screenshot presents a dashboard dedicated to customer management, highlighting:

  **Key Metrics**:
  - <b>Number of active customers</b>: Not specified (e.g., 250)
  - <b>Total revenue</b>: 35K € (displayed in the annual revenue chart)
  - <b>Number of transactions</b>: 175 (maximum in 2024)

  **Main Visualizations**:
  - <b>Customer ranking by sales</b>:
    - Top 10 customers (e.g., Client 1372 with 1,000 €, Client 492 with 500 €).
  - <b>Annual comparison</b>:
    - Customer revenue (0 to 35K €) vs. number of transactions (0 to 175), with data for 2020, 2022, 2024.
  - <b>Customer/author evaluation</b>:
    - Rating table and categories (e.g., Excellent, Correct).

 
  - ![Image](https://github.com/user-attachments/assets/f1c309e7-6e6c-4544-91bf-fd4c4cdc555f)

## <h2>🛒 How This Helps Monoprix France</h2>
This analytics and AI platform has been designed to help Monoprix France make better, faster, and more data-driven decisions by offering:

- **360° Business Insights** through a comprehensive Power BI dashboard
- **Intelligent Predictions** with AI/ML models trained on internal datasets
- **Centralized & Clean Data** thanks to a staging area and data warehouse
- **Accessible Deployment** via a simple and interactive Streamlit interface

## <h2>🧠 Insights & Findings</h2>
- 📊 **Forecasts** of budget usage and equity predictions using time series models
- 🔍 **Customer classification and segmentation** based on behavior and sales
- 🤖 A **Chatbot NLP model** to automatically analyze client reviews
- 🛠️ **Detection** of fraud and dispute resolution delays through ML models

## <h2>📌 Why This Project?</h2>
This project provides a scalable BI & AI solution tailored for Monoprix France to:

- ✅ **Unify and transform data** from multiple sources using ETL pipelines
- ✅ **Analyze supplier efficiency** and delivery reliability
- ✅ **Personalize customer insights** to improve marketing and retention
- ✅ **Predict financial trends** and anomalies to enhance budget control

It also demonstrates my ability to:

- ✅ Build a robust **data pipeline** (Staging Area ➝ Data Warehouse ➝ Dashboard)
- ✅ Design and deploy **ML models** integrated into a real app
- ✅ Create **end-to-end business intelligence solutions** for enterprise use cases

## <h2>⚙️ Tech Stack</h2>
- **Programming & Modeling**: Python, Pandas, Scikit-learn
- **Data Engineering**: SQL, ETL pipelines, Data Warehouse modeling (Fact & Dimension tables)
- **Visualization**: Power BI
- **AI & NLP**: Machine Learning (Classification, Regression, Time Series), Chatbot (NLP)
- **Deployment**: Streamlit

## <h2>🌐 Connect with Me</h2>
If you found this project valuable or inspiring, feel free to reach out!

- 📧 **Email**: faresguesmi815@gmail.com
- 📩 **My LinkedIn Account**: <a href="https://www.linkedin.com/in/fares-guesmi-6aa849262/">Fares Guesmi</a>

## <h2>⭐ Give It a Star!</h2>
If you like this project, don't forget to star this repository! ⭐
