import streamlit as st
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
st.title('Santé mentale chez les étudiants')
df = pd.read_csv('Student _Mental_health.csv', sep = ',')
st.markdown("Aperçu de la base de données")
st.write(df.head())

# les métriques
col1, col2 = st.columns(2)
moyenne = df["Age"].mean()
col2.metric(label = "Moyenne d'âge", value = moyenne)
col1.metric(label = "Nombre de personnes interrogées", value = df.shape[0])
# graphiques généraux
repartition_sexe = df['Choose your gender'].value_counts().reset_index()
repartition_sexe.columns = ['Genre', 'Effectif']

repartition_etu = df['What is your course?'].value_counts().reset_index()
repartition_etu.columns = ["Niveau d'étude", "Effectif"]


col1, col2 = st.columns(2)
with col1:
    st.markdown("### Répartition par genre")
    fig, ax = plt.subplots()
    ax.pie(repartition_sexe['Effectif'], labels=repartition_sexe['Genre'], autopct='%1.1f%%', startangle=90)
    ax.axis('equal')  # Assure que le pie chart est un cercle.
    st.pyplot(fig)
with col2:
    etude = px.bar(repartition_etu, x = "Niveau d'étude", y = "Effectif")
    st.plotly_chart(etude)
