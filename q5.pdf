import pandas as pd

df = pd.read_csv("data/student_performance.csv")

print(df.head())
print("Rows, Cols:", df.shape)
print("Columns:", list(df.columns))
print("Missing values:\n", df.isnull().sum())

print("Average final score:", df["Final_Score"].mean())

top = df.loc[df["Final_Score"].idxmax()]
print("Top student:\n", top)

df["Improvement"] = df["Final_Score"] - df["Previous_Score"]

high_att = df[df["Attendance"] >= 80]
print("High attendance students:\n", high_att)

df_sorted = df.sort_values("Final_Score", ascending=False)
print(df_sorted)

df_sorted.to_csv("data/processed_student_performance.csv", index=False)
