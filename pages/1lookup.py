import json
import streamlit as st
from customs.custom import css
#사이드바 제거
st.markdown(css, unsafe_allow_html=True)

#실시간 알람 불러오기
with open('C:\\Users\\USER\\ve_1\\alarmCapture\\db\\info_.json','r',encoding="UTF-8") as f:
    DF = json.load(f)
mid = st.text_input("MID조회(입력 후 Enter)")
look = [i for i in range(len(DF)) if DF[i]['mid']==mid]

if mid:
    if look != []:
        st.markdown(':blue[**정보**]')
        st.write(DF[look[0]]['info'])
        st.markdown(':blue[**담당자**]')
        st.write(DF[look[0]]['char'])
    else:
        st.write('존재하지 않는 MID입니다.')