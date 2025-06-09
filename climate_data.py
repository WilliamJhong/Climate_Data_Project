import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd


def load_climate_data(filepath):

    # Do you need to load all the columns? 
    columns = [
        "NAME", 
        "DATE", 
        "DailyAverageDryBulbTemperature",
        "DailyMaximumDryBulbTemperature", 
        "DailyMinimumDryBulbTemperature",
        "DailyPrecipitation",
        "Average_Daily_Snow_Fall",
        "DailyAverageWindSpeed",
    ]


    rawdata = pd.read_csv(filepath, parse_dates=["DATE"], usecols=columns)
    # Do the rest of the data cleaning here. I don't want to download your large dataset.

    return rawdata


