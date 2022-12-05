import pandas as pd
import numpy as np
import altair as alt

df = pd.read_csv("./refined_insurance.csv")







































### AGE
bar_age = alt.Chart(df).mark_bar(color='lightblue').encode(
    x= 'age:Q',
    y= 'count():Q',
    tooltip= alt.Tooltip(['region:N','bmi:N','smoker:N','BMI Category:N','Total 2022 PPP expenses','proposed_price','age:N']),
).properties(width = 400).interactive()

box_age_region = alt.Chart(df).mark_boxplot().encode(
    x='region:O',
    y='age:Q',
).properties(width = 400).interactive()

### BMI
bar_bmi = alt.Chart(df).mark_bar(color='lightblue').encode(
    x= 'bmi:Q',
    y= 'count():Q',
    tooltip= alt.Tooltip(['region:N','bmi:N','smoker:N','BMI Category:N','Total 2022 PPP expenses','proposed_price','age:N']),
).properties(width = 400).interactive()

box_bmi_region = alt.Chart(df).mark_boxplot().encode(
    x='region:O',
    y='bmi:Q',
).properties(width = 400).interactive()

### Smoker
bar_smoker = alt.Chart(df).mark_bar(color='lightblue').encode(
    x= 'smoker:N',
    y= 'count():Q',
    tooltip= alt.Tooltip(['smoker:N']),
).properties(width = 400).interactive()


box_PPP_exp = alt.Chart(df).mark_boxplot().encode(
    x='region:N',
    y='Total 2022 PPP expenses:Q',
).properties(width = 400).interactive()

bar_age 
box_age_region
bar_bmi 
box_bmi_region
bar_smoker 
box_PPP_exp