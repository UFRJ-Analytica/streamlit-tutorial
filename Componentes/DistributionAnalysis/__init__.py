

import streamlit as st
import matplotlib.pyplot as plt

class DistributionAnalysis:

    def __init__(self):
        pass

    def render(self, filtered_bike_data):
        st.markdown("## Análises de Distribuição dos Valores")
        col1, col2 = st.columns(2)

        with col1:
            fig, ax = plt.subplots()
            durations = filtered_bike_data["Trip Duration"]
            ax.hist(durations[durations < 1000])
            ax.set_title("Distribuicao de Duração das Corridas")
            st.pyplot(fig)

        with col2:
            fig, ax = plt.subplots()
            data_captura = 2019
            ages = data_captura - filtered_bike_data["Birth Year"]
            ax.hist(ages)
            ax.set_title("Distribuicao de Idades")
            st.pyplot(fig)