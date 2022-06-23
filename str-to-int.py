import pandas as pd

df = pd.read_csv("oral_bioavailability-test.csv")
df.fillna(0, inplace=True)
df["value"] = pd.to_numeric(df['value'])

df['target_organism'] = pd.np.where(df.assay_description.str.contains("rat","Rat"), "rat",
                   pd.np.where(df.assay_description.str.contains("mouse","Mouse","mice","Mice"), "mouse",
		   pd.np.where(df.assay_description.str.contains("human","Human"), "human",
		   pd.np.where(df.assay_description.str.contains("monkey","Monkey"), "human",
                   pd.np.where(df.assay_description.str.contains("dog","Dog"), "dog")))

df.to_csv("oral-bioavailability-values-test.csv", index=False)
print("Complete")