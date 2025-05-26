import pandas as pd

data_path = "/workspaces/DSC478/DSC478 CODE/data/video_game_reviews.csv" 
df = pd.read_csv(data_path)

print("Data Preview:")
print(df.head())