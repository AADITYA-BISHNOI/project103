import plotly.figure_factory as ff
import pandas as pd

df = pd.read_csv("data1.csv")

fig = ff.create_distplot([df["cases"].tolist()], ["cases"], show_hist=False)

fig.show()