import streamlit as st

st.title("標題")
st.write("write")
st.text("text")
st.markdown(
    """helloo
   * **niugga**

 * **粗體文字**
 * *斜體文字*
 ```python
 print("Hello, World!")
 ```
 * [連結](https://www.youtube.com)
 * ![圖片](https://via.placeholder.com/150)
 #標題１
 ##標題２
 ###標題３
 ###標題４
"""
)
