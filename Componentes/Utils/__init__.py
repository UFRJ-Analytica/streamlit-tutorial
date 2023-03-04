import pandas as pd

def get_bike_data():
    """Retorna os dados de bicicleta"""

    data = pd.read_parquet("Data/citibike2019_sample.parquet", engine="fastparquet").rename(
        columns={
            'starttime': "Start Time", 
            'stoptime': "Stop Time", 
            'start station id': "Start Station ID", 
            'start station name': "Start Station Name",
            'start station latitude': "Start Station Latitude", 
            'start station longitude': "Start Station Longitude", 
            'end station id': "End Station ID",
            'end station name': "End Station Name", 
            'end station latitude': "End Station Latitude", 
            'end station longitude': "End Station Longitude",
            'bikeid': "Bike ID", 
            'usertype': "User Type", 
            'birth year': "Birth Year", 
            'gender': "Gender",
            'tripduration': "Trip Duration"
        }
    )

    data["Start Time"] = pd.to_datetime(data["Start Time"])
    data["Stop Time"] = pd.to_datetime(data["Stop Time"])

    return data