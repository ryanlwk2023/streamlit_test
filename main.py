import streamlit as st
import pandas as pd
st.write("### Good morning!")

a=329*3
a

[ 12, 13, 14]

st.image("./PictureC.jpg", width=200)

df=pd.DataFrame({"stud_num":["01","02","03"],
              "class":["classA","classA", "classB"],
              "result":[92, 67,70]
})
st.dataframe(df)
st.divider()
st.table(df)