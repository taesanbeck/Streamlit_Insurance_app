import pandas as pd
import numpy as np
# import matplotlib.pyplot as plt
# import seaborn as sns
import altair as alt

dataset = pd.read_csv("refined_insurance.csv")

# dataset.head()


d_bar = alt.Chart(dataset).mark_bar().encode(
    x=alt.X('BMI Category:O',sort=['<25','26 - 35','36+']),
    y='age:Q',
    color= alt.Color("smoker:N", type="nominal",scale=alt.Scale(range=['#800000', ' #63ba97']),legend=alt.Legend(columns=2)),
    column=alt.Colsumn('Age Category:N',header=alt.Header(titleFontSize=20,titleColor='White',labelColor='White',labelFontSize=25)),
    tooltip=alt.Tooltip('smoker:N', title='smoker:N'),
).interactive().properties(width=200,height=300).configure_axis(
    grid=False, labelFontSize=20, titleFontSize = 20
).configure_legend(labelFontSize = 15,titleFontSize=15).configure_view(
    strokeWidth=0
)

















# fig, (ax, ax1,ax2,ax3) = plt.subplot()
# sns.barplot(
#     x="BMI Category", 
#     y="age", hue="smoker", 
#     data=dataset, palette="Blues",ax=ax)

# sns.boxplot(
#     x="smoker", 
#     y="age", data=dataset, palette="Blues",ax=ax1)

# sns.boxplot(
#     x="smoker", 
#     y="bmi", 
#     data=dataset, palette="Blues",ax=ax2)

# sns.boxplot(
#     x="smoker", 
#     y="Total 2022 PPP expenses", 
#     data=dataset, palette="Blues",ax=ax3)
