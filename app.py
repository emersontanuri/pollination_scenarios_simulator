import streamlit as st
from views.home import homepage
from views.simulator import simulator_page
from views.releases import releases_page

st.set_page_config(layout="wide")

pages = st.navigation([
  homepage,
  simulator_page,
  releases_page
])

pages.run()
