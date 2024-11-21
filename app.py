import streamlit as st
from views.home import homepage
from views.simulator import simulator_page

st.set_page_config(layout="wide")

pages = st.navigation([
  homepage,
  simulator_page
])

pages.run()
