import streamlit as st
import pandas as pd
import numpy as np
import altair as alt
import time 
from datetime import date, timedelta
import string 


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

st.write("Custom Index")

df2 = pd.DataFrame({
    "date": [date(2025,1,25), date(2025,2,21), date(2025,11,25) ],
    "total": [12334, 4455465, 23344554]
})

df2.set_index("date", inplace=True)

config = {
    "_index": st.column_config.DateColumn("Month", format="MMM, YYYY"),
    "total": st.column_config.NumberColumn("Total {$}")
}

st.dataframe(df2, column_config=config)


st.write("Sales report")

@st.cache_data
def get_data():
    product_names= ["Widget " + letter for letter in string.ascii_uppercase]
    average_daily_sales = np.random.normal(1000, 300, len(product_names))
    products = dict(zip(product_names, average_daily_sales))
    data=pd.DataFrame({})
    sales_dates=np.arange(date(2023, 1,1), date(2025, 1,1), timedelta(days=1))
    for product, sales in products.items():
        data[product]=np.random.normal(sales, 300, len(sales_dates)).round(2)

    data.index=sales_dates
    data.index=data.index.date
    return data

@st.fragment
def show_daily_sales(data):
    time.sleep(1)
    selected_date = st.date_input(
        "Pick a date",
        value = date(2023,1,1),
        min_value=date(2023,1,1),
        max_value=date(2024,12,31),
        key="selected_date"
    )

    if "previous_date" not in st.session_state:
        st.session_state.previous_date = selected_date

    previous_date=st.session_state.previous_date
    st.session_state.previous_date=selected_date

    is_new_month = selected_date.replace(day=1) != previous_date.replace(day=1)
    if is_new_month:
        st.rerun()

    st.header(f"Best Sellers, {selected_date: %m/%d/%y}")
    top_ten = data.loc[selected_date].sort_values(ascending = False)[0:10]
    cols= st.columns([1,4])
    cols[0].dataframe(top_ten)
    cols[1].bar_chart(top_ten)


    st.header(f"Worst Sellers, {selected_date: %m/%d/%y}")
    bottom_ten = data.loc[selected_date].sort_values()[0:10]
    cols = st.columns([1, 4])
    cols[0].dataframe(bottom_ten)
    cols[1].bar_chart(bottom_ten)



def show_monthly_sales(data):
   time.sleep(1)
   selected_date = st.session_state.selected_date
   this_month = selected_date.replace(day=1)
   next_month = (selected_date.replace(day=28) + timedelta(days=4)).replace(day=1)

   st.header(f"Daily sales for all products, {this_month: %B %Y} ")
   monthly_sales = data[(data.index < next_month) & (data.index >=this_month)]
   st.write(monthly_sales)

   st.header(f"Total sales of all products, {this_month: %B %Y}")
   st.bar_chart(monthly_sales.sum())


data = get_data()
show_daily_sales(data)
show_monthly_sales(data)

   
    


