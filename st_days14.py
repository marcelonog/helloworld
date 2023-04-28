#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 27 20:45:08 2023

@author: marcelo
"""

import streamlit as st
import pandas as pd
import pandas_profiling
from streamlit_pandas_profiling import st_profile_report

st.header('`streamlit_pandas_profiling`')

df = pd.read_csv('https://raw.githubusercontent.com/dataprofessor/data/master/penguins_cleaned.csv')

pr = df.profile_report()
st_profile_report(pr)