import pandas as pd
import numpy as np
import streamlit as st
import altair as alt


df = pd.read_csv('refined_insurance.csv')


## Kmeans
from sklearn.cluster import KMeans

km = KMeans(n_clusters=3, random_state=1)
new = df._get_numeric_data().dropna(axis=1)
km.fit(new)
predict=km.predict(new)

df['CLUSTERS'] = pd.Series(predict, index=df.index)



###CLusters Smoker and none Smoker SMOKER CHART#####
cluster_age = alt.Chart(df).mark_circle(size=60).encode(
    x='age',
    y='Total 2022 PPP expenses',
    color='CLUSTERS',
    tooltip=['age', 'bmi', 'region', 'smoker','Benefit from Proposed Price Yes/No','proposed_price','CLUSTERS']
).properties(width=500,height=500).interactive()

#### Cluster by those who Benifit from the Pricing BENIFIT CHART ###
cluster_bmi = alt.Chart(df).mark_circle(size=60).encode(
    x='bmi',
    y='Total 2022 PPP expenses',
    color='CLUSTERS',
    tooltip=['age', 'bmi', 'region', 'smoker','Benefit from Proposed Price Yes/No','proposed_price','CLUSTERS']
).properties(width=500,height=500).interactive()

cluster1 = cluster_age | cluster_bmi

###CLusters Smoker and none Smoker SMOKER CHART#####
smoker_cluster2 = alt.Chart(df).mark_circle(size=60).encode(
    x='age',
    y='Total 2022 PPP expenses',
    color= alt.Color("smoker", type="nominal",
    scale=alt.Scale(range=['#012bbf', '#00b10e']),
    legend=alt.Legend(title="Smoker",orient="top",
    direction='horizontal',titleAnchor='middle')),
    tooltip=['age', 'bmi', 'region', 'smoker','Benefit from Proposed Price Yes/No','proposed_price','CLUSTERS']
).properties(width=500,height=500).interactive()

#### Cluster by those who Benifit from the Pricing BENIFIT CHART ###
benifit_cluster2 = alt.Chart(df).mark_circle(size=60).encode(
    x='age',
    y='Total 2022 PPP expenses',
    color= alt.Color("Benefit from Proposed Price Yes/No",
     type="nominal",
     scale=alt.Scale(range=['#ac1008', '#00b10e']),
     legend=alt.Legend(title="Benefit",orient="top",
    direction='horizontal',titleAnchor='middle')),
    tooltip=['age', 'bmi', 'region', 'smoker','Benefit from Proposed Price Yes/No','proposed_price','CLUSTERS']
).properties(width=500,height=500).interactive()

