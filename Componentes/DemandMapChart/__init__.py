import streamlit as st
import pydeck as pdk

class DemandMapChart:

    def __init__(self):
        pass

    def render(self, filtered_bike_data):
        st.markdown("## Análise Gráfica das Estações")
        st.markdown("O Gráfico de Hexágonos agrupa instâncias na mesma localização para construir a altura dos pilares. Quanto mais alto mais demanda.")

        stations = filtered_bike_data[["Start Station Latitude", "Start Station Longitude"]]
        stations.columns = ["lat", "lon"]

        st.pydeck_chart(
            pdk.Deck(
                map_style=None,
                initial_view_state=pdk.ViewState(
                    latitude=stations.lat.mean(),
                    longitude=stations.lon.mean(),
                    zoom=11,
                    pitch=50,
                ),
                layers=[
                    pdk.Layer(
                        'HexagonLayer',
                        data=stations,
                        get_position='[lon, lat]',
                        radius=200,
                        elevation_scale=4,
                        elevation_range=[0, 1000],
                        pickable=True,
                        extruded=True,
                    )
                ],
            )
        )
