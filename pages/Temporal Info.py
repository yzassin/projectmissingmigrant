
import altair as alt
import streamlit as st
import pandas as pd

# Load the migration data from migrants.csv
migration_df = pd.read_csv('Migrants.csv')

# Display a header
st.header("Migration Route Analysis :thermometer: :chart_with_upwards_trend:")

# Let's assume the columns in migrants.csv are 'route_name', 'number_of_migrants', 'origin', 'destination', 'year'
selected_columns = ['Number of Females', 'Number of Males', 'Number of Children']
total_migrants = migration_df[selected_columns].sum().sum()

# Filter by migration route
selected_route = st.selectbox("Select Migration Route", migration_df['Migration route'].unique())

filtered_data = migration_df[migration_df['Migration route'] == selected_route]

# Display a line chart based on the selected migration route
chart = (
    alt.Chart(
        filtered_data,
        title=f"Migration Route: {selected_route} Over Years",
    )
    .mark_line(point=True)
    .encode(
        x=alt.X("year:O", title="Year"),  # 'O' means ordinal for discrete years
        y=alt.Y(f"sum({', '.join(selected_columns)})", title="Number of Migrants"),
        color="Country of Origin",
        tooltip=["Incident year", "Country of Origin", "Location of death"],
    )
)

# Display the Altair chart using Streamlit
st.altair_chart(chart, use_container_width=True)
