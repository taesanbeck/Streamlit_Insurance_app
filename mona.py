import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

dataset = pd.read_csv("refined_insurance.csv")

dataset.head()

age_smoker_bar = sns.barplot(x="BMI Category", y="age", hue="smoker", data=dataset, palette="Blues")


smoker_age_box = sns.boxplot(x="smoker", y="age", data=dataset, palette="Blues")


smoker_bmi_box = sns.boxplot(x="smoker", y="bmi", data=dataset, palette="Blues")


smoker_expense_box = sns.boxplot(x="smoker", y="Total 2022 PPP expenses", data=dataset, palette="Blues")
