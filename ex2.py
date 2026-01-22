import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv(r"C:\Users\Ramya.R\Downloads\archive (2).zip")
print(df.head())
print(df.info())
print((df == 0).sum())
plt.hist(df["Glucose"], bins=20)
plt.title("Glucose Distribution")
plt.show()
plt.boxplot(df["Age"])
plt.title("Age Distribution")
plt.show()
