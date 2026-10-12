import streamlit as st

st.title('Streamlit website test')

name = st.text_input('輸入姓名')

if st.button('送出'):
    st.write('你好，', name)