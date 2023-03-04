import streamlit as st

class Sidebar:

    def __init__(self, streamlit_sidebar, ):
        self.sidebar = streamlit_sidebar
        self.filters = {}

    def render(self, bike_data):
        self.sidebar.markdown("# Filtros da Sidebar")
        self.sidebar.markdown("Nesta área podemos ter divesos filtros relacionados aos dados do dashboard.")

        filtered_bike_data = bike_data.copy()

        # Filtragem da Data
        min_datetime = filtered_bike_data["Start Time"].min()
        max_datetime = filtered_bike_data["Stop Time"].max()
        
        (self.filters["min_time"], self.filters["max_time"]) = self.sidebar.date_input("Intervalo da Ocorrência", (min_datetime, max_datetime), min_datetime, max_datetime)

        filtered_bike_data = filtered_bike_data[
            (filtered_bike_data["Start Time"].dt.date >= self.filters["min_time"]) &
            (filtered_bike_data["Start Time"].dt.date <= self.filters["max_time"]) &
            (filtered_bike_data["Stop Time"].dt.date >= self.filters["min_time"]) &
            (filtered_bike_data["Stop Time"].dt.date <= self.filters["max_time"])
        ]

        self.filtered_bike_data = filtered_bike_data
        return filtered_bike_data

    def get_filtered_data(self):
        return self.filtered_bike_data