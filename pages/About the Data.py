import pandas as pd
import streamlit as st
import plotly.express as px

st.set_page_config(
        page_title="Data",
        page_icon="📈",
    )
st.title('Missing Migrant Data')
st.subheader('The data includes some of the important informations such as:')
st.markdown('''
**1. Demographic information about the missing migrants** – Gender, Country of origin.\n
**2. Temporal information on when was the incident occured** – By year and month\n
**3. Geospatial information on where was the incident occured** - The migration route taken, coordinates of the incident location.\n

- The dataset can be obtain [here](https://www.kaggle.com/datasets/nelgiriyewithana/global-missing-migrants-dataset)
''')

st.divider()

def load_data():
    df = pd.read_csv('migrants.csv')
    return df
df = load_data()

def plot_missing_migrant_features(features):
    feature = st.selectbox('**Choose Feature**', tuple(features))
    
    if feature == 'Gender':
        # Create separate columns for each gender
        df['Females'] = df['Number of Females'].fillna(0)
        df['Males'] = df['Number of Males'].fillna(0)
        df['Children'] = df['Number of Children'].fillna(0)

        # Create a new DataFrame for gender counts
        gender_counts = df[['Females', 'Males', 'Children']].sum()
        
            # Create a bar chart using Plotly Express
        fig = px.bar(gender_counts, x=gender_counts.index, y=gender_counts.values, labels={'y': 'Count'}, title='Gender Counts')
    else:
        # Plot the selected feature
        fig = px.bar(df, x=feature, title=f'{feature} Counts')
    
    st.plotly_chart(fig)

st.subheader('Missing Migrant Features')
migrant_features = [
    'Region of Origin', 'Region of Incident',
    'Cause of Death', 'Migration route', 'Gender'
]

plot_missing_migrant_features(migrant_features)
