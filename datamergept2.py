import pandas as pd

# Load the massive list CSV file
massive_list = pd.read_csv("ICRAlist.csv")

# Keep only the columns of interest
narrowed_list = massive_list[["Document Title", "Authors", "Publication Year", "PDF Link", "Abstract"]]

# Add a new column "Implementation?" with values "YES" or "NO" based on the presence of "github" in the abstract
narrowed_list["Implementation?"] = narrowed_list["Abstract"].str.contains("github", case=False, na=False).replace({True: "YES", False: "NO"})

# Save the simplified list to a new CSV file
narrowed_list.to_csv("output2.csv", index=False)