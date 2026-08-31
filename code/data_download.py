import pandas as pd
import geopandas as gpd

#TAZEEN - SA2 district (external) dataset
#digital boundary download
sa2_2021 = pd.read_excel("data/external/SA2_2021_AUST.xlsx")

#filter for just Victorian districts
vic_sa2_21 = sa2_2021[sa2_2021["STATE_NAME_2021"] == "Victoria"].copy()
sa2districts_21 = vic_sa2_21["SA2_NAME_2021"].unique()
print("2021 Victorian SA2s:")
print(sa2districts_21)