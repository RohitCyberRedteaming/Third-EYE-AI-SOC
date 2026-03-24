import streamlit as st
import requests

st.set_page_config(page_title="Third EYE AI SOC", page_icon="👁️", layout="wide")

st.markdown("""<style>
.title-block{background:linear-gradient(135deg,#1a1a2e,#16213e);padding:2rem;border-radius:12px;border-left:4px solid #00d4ff;margin-bottom:2rem;}
</style>""", unsafe_allow_html=True)

st.markdown("""<div class="title-block">
<h1 style="color:#00d4ff;margin:0;">👁️ Third EYE – AI Driven SOC Platform</h1>
<p style="color:#aaa;margin:0.5rem 0 0;">Security Operations Center · Real-time AI Threat Analysis</p>
</div>""", unsafe_allow_html=True)

with st.sidebar:
    st.markdown("## 🔐 SOC Login")
    username = st.text_input("Username", placeholder="admin / l2 / analyst")
    if st.button("Login", use_container_width=True):
        try:
            res = requests.post("http://localhost:8000/login", json={"username": username})
            data = res.json()
            st.session_state["token"] = data.get("token")
            st.session_state["role"] = data.get("role")
            st.success(f"✅ Logged in as {username}")
            st.info(f"🎭 Role: {data.get('role')}")
        except Exception as e:
            st.error(f"❌ Error: {e}")
    st.divider()
    st.markdown("### 📡 System Status")
    try:
        r = requests.get("http://localhost:8000/", timeout=2)
        if r.status_code == 200:
            st.success("🟢 Backend Online")
    except:
        st.error("🔴 Backend Offline")

tab1, tab2, tab3 = st.tabs(["📊 Dashboard", "🤖 AI Query", "🔍 Analyze"])

with tab1:
    col1, col2, col3 = st.columns(3)
    col1.metric("🚨 Total Alerts", "0")
    col2.metric("🔴 Critical", "0")
    col3.metric("🟢 Status", "Running")
    st.divider()
    st.markdown("### 🛡️ Recent Incidents")
    try:
        data = requests.get("http://localhost:8000/analyze", timeout=3).json()
        if isinstance(data, list) and len(data) > 0:
            st.dataframe(data)
        else:
            st.info("📭 No incidents. QRadar not connected — dummy mode.")
    except Exception as e:
        st.warning(f"⚠️ Could not fetch: {e}")

with tab2:
    st.markdown("### 🤖 Ask the AI SOC Engine")
    if "token" not in st.session_state:
        st.warning("⚠️ Please login from sidebar first!")
    else:
        query = st.text_input("Enter your query", placeholder="show critical alerts / block threat / status")
        if st.button("🚀 Send to AI", use_container_width=True):
            try:
                res = requests.post("http://localhost:8000/ai-secure", json={
                    "token": st.session_state["token"], "query": query})
                st.success(f"🤖 {res.json().get('response')}")
            except Exception as e:
                st.error(f"Error: {e}")

with tab3:
    st.markdown("### 🔍 Secure Threat Analysis")
    if "token" not in st.session_state:
        st.warning("⚠️ Please login from sidebar first!")
    else:
        if st.button("🔎 Run Analysis", use_container_width=True):
            try:
                res = requests.post("http://localhost:8000/analyze-secure", json={
                    "token": st.session_state["token"]})
                result = res.json()
                st.markdown(f"**User:** {result.get('user')} | **Role:** {result.get('role')}")
                data = result.get("data", [])
                if data:
                    st.dataframe(data)
                else:
                    st.info("No threats. QRadar not connected.")
            except Exception as e:
                st.error(f"Error: {e}")

st.divider()
st.markdown("<center><small style='color:#555'>👁️ Third EYE AI SOC · Built by Rohit</small></center>", unsafe_allow_html=True)