import pandas as pd
import numpy as np
import altair as alt

df = pd.read_csv("./refined_insurance.csv")


################################################################### Khalid's STUFF #########################################
### histograms by age 

age_hist = alt.Chart(df).mark_bar().encode(
    x='age:Q',
    y='count():Q'
).properties(width=400,height=300).configure_axis(
    grid=False, labelFontSize=20, titleFontSize = 20
).configure_legend(labelFontSize = 15,titleFontSize=15)

### histograms by bmi

BMI_hist = alt.Chart(df).mark_bar().encode(
    x='bmi:Q',
    y='count():Q'
).properties(width=400,height=300).configure_axis(
    grid=False, labelFontSize=20, titleFontSize = 20
).configure_legend(labelFontSize = 15,titleFontSize=15)

### boxplot by age category

age_box = alt.Chart(df).mark_boxplot(extent='min-max').encode(
    x='Age Category',
    y='Total 2022 PPP expenses:Q',
    tooltip=alt.Tooltip('Total 2022 PPP expenses', format='.2f')
).interactive().properties(width=400,height=300).configure_axis(
    grid=False, labelFontSize=20, titleFontSize = 20
).configure_legend(labelFontSize = 15,titleFontSize=15)

### boxplot by bmi category

bmi_box = alt.Chart(df).mark_boxplot(extent='min-max').encode(
    x='BMI Category',
    y='Total 2022 PPP expenses:Q',
    tooltip=alt.Tooltip('Total 2022 PPP expenses', format='.2f')
).interactive().properties(width=400,height=300).configure_axis(
    grid=False, labelFontSize=20, titleFontSize = 20
).configure_legend(labelFontSize = 15,titleFontSize=15)


### bar graph
age_bar = alt.Chart(df).mark_bar().encode(
    x='age:Q',
    y='Total 2022 PPP expenses:Q',
    tooltip = alt.Tooltip('Total 2022 PPP expenses:Q', format='.2f')
)

rule = alt.Chart(df).mark_rule(color='red').encode(
    y=alt.Y('Forward PPP expenses:Q',axis=alt.Axis(title=None))
)

(age_bar + rule).properties(width=500,height=300).configure_axis(
    grid=False, labelFontSize=20, titleFontSize = 20
).configure_legend(labelFontSize = 15,titleFontSize=15)
############################################################# Khalid's STUFF ##################

### AGE ################################### BECK'S STUFF #####################################
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

# ### Smoker
# bar_smoker = alt.Chart(df).mark_bar(color='lightblue').encode(
#     x= 'smoker:N',
#     y= 'count():Q',
#     tooltip= alt.Tooltip(['smoker:N']),
# ).properties(width = 400).interactive()


box_PPP_exp = alt.Chart(df).mark_boxplot().encode(
    x='region:N',
    y='Total 2022 PPP expenses:Q',
).properties(width = 400).interactive()
################################################# BECK's STUFF #############################################################3

### BECK's CHARTS
#bar_age 
#box_age_region

#bar_bmi 
#box_bmi_region

#bar_smoker 
 # Kahlid's is better I needed pairs of 2
b#ox_PPP_exp

### Khalid's CHART's
age_hist
BMI_hist

age_box
bmi_box

age_bar