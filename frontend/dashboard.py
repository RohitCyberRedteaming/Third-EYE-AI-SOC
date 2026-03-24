import streamlit as st
import requests
st.set_page_config(page_title='Third EYE AI SOC', page_icon='', layout='wide')
st.markdown('<h1 style="color:#00d4ff;"> Third EYE  AI Driven SOC Platform</h1>', unsafe_allow_html=True)
with st.sidebar:
    st.markdown('##  SOC Login')
    username = st.text_input('Username')
    if st.button('Login'):
        try:
            res = requests.post('http://localhost:8000/login', json={'username': username})
            d = res.json()
            st.session_state['token'] = d.get('token')
            st.success('Logged in: ' + username + ' | Role: ' + str(d.get('role')))
        except Exception as e:
            st.error(str(e))
    try:
        requests.get('http://localhost:8000/', timeout=2)
        st.success(' Backend Online')
    except:
        st.error(' Backend Offline')
tab1, tab2 = st.tabs([' Dashboard', ' AI Query'])
with tab1:
    st.metric('Status', 'Running')
    try:
        data = requests.get('http://localhost:8000/analyze', timeout=3).json()
        st.dataframe(data) if data else st.info('No data - QRadar not connected')
    except:
        st.info('Backend se data nahi mila')
with tab2:
    if 'token' not in st.session_state:
        st.warning('Pehle login karo!')
    else:
        q = st.text_input('Query')
        if st.button('Send'):
            r = requests.post('http://localhost:8000/ai-secure', json={'token': st.session_state['token'], 'query': q})
            st.success(r.json().get('response', 'No response'))
