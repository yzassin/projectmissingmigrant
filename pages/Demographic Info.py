import altair as alt
import streamlit as st
import pandas as pd

st.set_page_config(
        page_title="Demographic",
        page_icon="👨‍👩‍👦",
    )
df = pd.read_csv('migrants.csv')

st.subheader("Demographic Analysis over the year")
selected_columns = ['Number of Females', 'Number of Males', 'Number of Children']
grouped_df = df.groupby('Incident year')[selected_columns].sum().reset_index()

# Melt the DataFrame to have a 'variable' column for demographics
melted_df = pd.melt(grouped_df, id_vars='Incident year', value_vars=selected_columns, var_name='Demographic', value_name='Count')

# Plotting with Altair
chart = (
    alt.Chart(
        melted_df,
        title="",
    )
    .mark_line(point=True)
    .encode(
        x=alt.X("Incident year:O", title="Incident Year"),
        y=alt.Y("Count", title="Count"),
        color="Demographic",
        tooltip=["Incident year", "Count", "Demographic"],
    )
)
# Display the Altair chart using Streamlit
st.altair_chart(chart, use_container_width=True)

#-------------------------------------------------
st.divider()
st.subheader("Popular Migration route by Migrant's Origin")

selected_columns = ['Number of Females', 'Number of Males', 'Number of Children']
total_migrants = df[selected_columns].sum().sum()

# Filter by migration route
selected_route = st.selectbox("Select Migration Route", df['Migration route'].unique())
filtered_data = df[df['Migration route'] == selected_route]

# Filter out certain values in "Country of Origin"
excluded_countries = ['Unknown']
filtered_data = filtered_data[~filtered_data['Region of Origin'].isin(excluded_countries)]

excluded_route = ['nan']
filtered_data = filtered_data[~filtered_data['Migration route'].isin(excluded_route)]
# Display a line chart based on the selected migration route
chart = (
    alt.Chart(
        filtered_data,
        title=f"Migration Route: {selected_route} Over Years",
    )
    .mark_line(point=True)
    .encode(
        x=alt.X("Incident year", title="Year"),  # 'O' means ordinal for discrete years
        color=alt.Color("Region of Origin:N", title="Region of Origin"),
        y=alt.Y(selected_columns[0], title="Number of Migrants"),  # Using the first selected column initially

        tooltip=["Incident year", "Region of Origin", "Number of Migrants"],
    )
)
# Display the Altair chart using Streamlit
st.altair_chart(chart, use_container_width=True)
