import streamlit as st
import matplotlib.pyplot as plt

from Componentes import Sidebar, DemandMapChart, DistributionAnalysis
from Componentes.Utils import get_bike_data

st.set_page_config(page_title="Streamlit", page_icon="💡", layout="wide")

def main():
    try:
        bike_data = get_bike_data()
    except Exception as e:
        st.warning("This dashboards depends on downloading data from a Drive, refer to the README.md file.")
        return
    
    sidebar = Sidebar(st.sidebar)
    sidebar.render(bike_data)
    filtered_bike_data = sidebar.get_filtered_data()

    st.markdown("# Análise de Bike Compartilhada NYC")

    st.markdown("## Organização da Base de Dados")
    st.dataframe(filtered_bike_data.head(30))

    distribution_analysis = DistributionAnalysis()
    distribution_analysis.render(filtered_bike_data)
        
    demand_map_chart = DemandMapChart()
    demand_map_chart.render(filtered_bike_data)


if __name__ == '__main__':
    main()