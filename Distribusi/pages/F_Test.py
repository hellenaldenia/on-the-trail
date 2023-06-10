import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import f


st.title("Distribusi F")

# Input parameter derajat kebebasan (dfn dan dfd)
dfn = st.slider("Pilih derajat kebebasan (dfn):", min_value=1, max_value=30, step=1, value=5)
dfd = st.slider("Pilih derajat kebebasan (dfd):", min_value=1, max_value=30, step=1, value=5)


samples = f.rvs(dfn, dfd, size=1000)


fig, ax = plt.subplots()
ax.hist(samples, bins=30, density=True)
ax.set_xlabel("Nilai")
ax.set_ylabel("Frekuensi")
ax.set_title("Histogram Distribusi F")


st.pyplot(fig)


st.subheader("Deskripsi Distribusi F")
st.write(f"Derajat kebebasan numerator (dfn): {dfn}")
st.write(f"Derajat kebebasan denominator (dfd): {dfd}")
st.write(f"Nilai rata-rata (mean): {np.mean(samples):.2f}")
st.write(f"Nilai variansi: {np.var(samples):.2f}")