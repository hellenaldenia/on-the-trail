import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


st.title("Distribusi Eksponensial")


rate = st.slider("Pilih nilai lambda (rate):", min_value=0.1, step=0.1, value=1.0)

samples = np.random.exponential(scale=1/rate, size=1000)


fig, ax = plt.subplots()
ax.hist(samples, bins=30, density=True)
ax.set_xlabel("Nilai")
ax.set_ylabel("Frekuensi")
ax.set_title("Histogram Distribusi Eksponensial")

st.pyplot(fig)


st.subheader("Deskripsi Distribusi Eksponensial")
st.write(f"Nilai rata-rata (mean): {np.mean(samples):.2f}")
st.write(f"Nilai variansi: {np.var(samples):.2f}")