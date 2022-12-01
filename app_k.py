# Bar Graph
import altair as alt
import pandas as pd

# import K_Chart
# import os

# os.chdir('./Data')
source = pd.read_csv('./refined_insurance.csv')
source2 = pd.read_csv('./refined_insurance_2.csv')

Benefit_by_age = alt.Chart(source2).mark_bar().encode(
    x=alt.X('type:N',sort = ['Current','Forward','Proposed'], axis=alt.Axis(title=None, labels=False)),
    y='Cost:Q',
    color= alt.Color("type:N",scale=alt.Scale(scheme='tableau20'),legend=alt.Legend(title="Cost Type",orient="top",
         direction='horizontal',
         titleAnchor='middle')),
    column=alt.Column('Age Category:N',header=alt.Header(titleFontSize=20,titleColor='White',labelColor='White',labelFontSize=25)),
    tooltip= alt.Tooltip('Cost:Q',format = ",.0f"),
).transform_fold(
    as_=['type','Cost'],
    fold=['Current','Forward','Proposed']
).properties(width=200,height=300).configure_axis(
    grid=False, labelFontSize=20, titleFontSize = 20
).configure_legend(labelFontSize = 15,titleFontSize=15)

input_dropdown = alt.binding_select(options=[True,False], name='Smoker')
selection = alt.selection_single(fields=['smoker'], bind=input_dropdown)

ben_age_bmi = alt.Chart(source).mark_bar().encode(
    x=alt.X('BMI Category:N',sort=['<25','26 - 35','36+']),
    y='mean(benefit/cost from proposed pricing):Q',
    color= alt.Color("Benefit from Proposed Price Yes/No:N", type="nominal",scale=alt.Scale(range=['#800000', ' #63ba97']),legend=None),
    column=alt.Column('Age Category:N',header=alt.Header(titleFontSize=20,titleColor='White',labelColor='White',labelFontSize=25))
).interactive().add_selection(
    selection
).transform_filter(
    selection
).properties(width=200,height=300).configure_axis(
    grid=False, labelFontSize=20, titleFontSize = 20
).configure_legend(labelFontSize = 15,titleFontSize=15).configure_view(
    strokeWidth=0
)

