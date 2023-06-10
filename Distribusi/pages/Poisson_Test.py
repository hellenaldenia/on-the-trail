import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


st.title("Distribusi Poisson")


rate = st.slider("Pilih nilai lambda (rate):", min_value=0.1, max_value=10.0, step=0.1, value=1.0)


sample_size = st.slider("Pilih jumlah sampel:", min_value=100, max_value=10000, step=100, value=1000)


samples = np.random.poisson(lam=rate, size=sample_size)


fig, ax = plt.subplots()
ax.hist(samples, bins=max(10, int(np.sqrt(sample_size))), density=True)
ax.set_xlabel("Nilai")
ax.set_ylabel("Frekuensi")
ax.set_title("Histogram Distribusi Poisson")


st.pyplot(fig)


st.subheader("Deskripsi Distribusi Poisson")
st.write(f"Nilai rata-rata (mean): {np.mean(samples):.2f}")
st.write(f"Nilai variansi: {np.var(samples):.2f}")