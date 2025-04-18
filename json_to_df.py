import pandas as pd
import json


with open("actions_infosys.json", "r", encoding="utf-8") as f:
    data = json.load(f)

board_meetings_data = data["board_meetings"]["data"]
board_meetings_df = pd.DataFrame(board_meetings_data, columns=data["board_meetings"]["header"])

print(board_meetings_df.head())

print(board_meetings_df.columns)
board_meetings_df.to_csv("actions_infosys.csv", index=False)