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
        np.random.randn(5,10),
        columns=["a", "b", "c", "d", "e", "f", "g", "i", "j"]
    )

    for word in text.split(" "):
        yield word + " "
        time.sleep(0.02)


if st.button("Stream Data"):
    st.write_stream(stream_data())


