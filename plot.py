

from plotly.plotly import iplot
import plotly.graph_objs as go

import pandas as pd
import math


df=pd.read_csv("plot.csv",converters={"Topic_Id":int,"GlobalTopic_Frequency":float})
print(df)

trace0 = go.Scatter(
    x=df['Topic_Id'],
    y=df['GlobalTopic_Frequency'],
    mode='markers',
    marker=dict(
        size=[40, 60, 80, 100],
    )
)

data = [trace0]
iplot(data, filename='bubblechart-size')