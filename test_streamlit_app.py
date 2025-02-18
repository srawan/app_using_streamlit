import streamlit as st
import pandas as pd
import numpy as np
import altair as alt
import time

st.write("Hello, *World !* :sunglasses: ")
st.write(1234)
st.write(
pd.DataFrame (
    {
        "First column": [1,2,3,4],
        "Second column":[10, 20, 30, 40]
    }
)
)

st.write("Draw a chart")

df = pd.DataFrame(np.random.randn(200, 3), columns=["a", "b", "c"])
c = (
    alt.Chart(df)
    .mark_circle()
    .encode(x="a", y ="b", size="c", color="c", tooltip=["a", "b", "c"])
)
st.write(c)

st.write("Code for strean test")

text = """
    Lorem ipsum dolor sit amet, **consectetur adipiscing** elit, sed do eiusmod tempor
    incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis
    nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.
    """
def stream_data():
    for word in text.split(" "):
        yield word + " "
        time.sleep(0.02)

    yield pd.DataFrame(
        np.random.randn(5,9),
        columns=["a", "b", "c", "d", "e", "f", "g", "i", "j"]
    )

    for word in text.split(" "):
        yield word + " "
        time.sleep(0.02)


if st.button("Stream Data"):
    st.write_stream(stream_data())

'''
# this is first title

This is some _markdown_
'''
df = pd.DataFrame({"Column1": ["1","2", "3"]})
df

x=10
'x', x 

df = pd.DataFrame(np.random.randn(50, 20), columns=("col %d" % i for i in range(20)))

st.dataframe(df)


st.dataframe(df.style.highlight_max(axis=0))


st.write("Column configuration")

df1 = pd.DataFrame(
    {
        "name":["Roadmap", "Extras", "Issues"],
        "url": ["http://roadmap.streamlit.com", "http://extras.streamlit.com", "http://issue.streamlit.com"],
        "starts": [np.random.randint(0, 1000) for _ in range(3)],
        "views_history":[[np.random.randint(0, 5000) for _ in range(30)] for _ in range(3)]
    }
)

st.dataframe(
    df1,
    column_config={
        "name": "App Name",
        "stars": st.column_config.NumberColumn(
            "GitHub Stars",
            help="Numbers of stars in github",
            format="% ⭐ "
        ),
        "url": st.column_config.LinkColumn("App URL"),
        "view_history": st.column_config.LineChartColumn(
            "Views (Past 30 days)", y_min=0, y_max=5000
        ),
    },
    hide_index=True
)