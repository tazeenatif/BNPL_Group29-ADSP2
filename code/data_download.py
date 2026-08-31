import pandas as pd
import geopandas as gpd

#TAZEEN - SA2 district (external) dataset
#digital boundary download
sa2_2021 = pd.read_excel("data/external/SA2_2021_AUST.xlsx")

#filter for just Victorian districts
vic_sa2_21 = sa2_2021[sa2_2021["STATE_NAME_2021"] == "Victoria"].copy()
sa2districts_21 = vic_sa2_21["SA2_NAME_2021"].unique()

#list of victorian sa2 districts
print("2021 Victorian SA2 districts:")
print(f"There are {len(sa2districts_21)} registered Victorian SA2 districts from the 2021 ASGS ABS dataset.")
print(sa2districts_21)