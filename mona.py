import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import altair as alt

dataset = pd.read_csv("refined_insurance.csv")

dataset.head()


fig, (ax, ax1,ax2,ax3) = plt.subplot()
sns.barplot(
    x="BMI Category", 
    y="age", hue="smoker", 
    data=dataset, palette="Blues",ax=ax)

sns.boxplot(
    x="smoker", 
    y="age", data=dataset, palette="Blues",ax=ax1)

sns.boxplot(
    x="smoker", 
    y="bmi", 
    data=dataset, palette="Blues",ax=ax2)

sns.boxplot(
    x="smoker", 
    y="Total 2022 PPP expenses", 
    data=dataset, palette="Blues",ax=ax3)
