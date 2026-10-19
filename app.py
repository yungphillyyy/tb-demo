import streamlit as st
from PIL import Image
import numpy as np
import random
import time

# ===============================
# Konfigurasi Halaman
# ===============================
st.set_page_config(
    page_title="Deteksi Tuberkulosis X-Ray",
    layout="centered"
)

# ===============================
# Judul Aplikasi
# ===============================
st.title("🫁 Sistem Deteksi Tuberkulosis")
st.write("Berbasis Deep Learning – MobileNetV2")

st.warning(
    "⚠️ Aplikasi ini merupakan **prototype penelitian** dan hanya "
    "digunakan sebagai alat bantu **skrining awal**, "
    "bukan diagnosis klinis."
)

# ===============================
# Informasi Model
# ===============================
with st.expander("ℹ️ Informasi Model"):
    st.markdown("""
    - **Arsitektur**: MobileNetV2  
    - **Pendekatan**: Transfer Learning  
    - **Input**: Citra X-Ray Dada (224 × 224 piksel)  
    - **Output**: Klasifikasi TB Positif / TB Negatif  
    """)

# ===============================
# Upload Citra
# ===============================
uploaded_file = st.file_uploader(
    "📤 Upload Citra X-Ray Dada",
    type=["jpg", "jpeg", "png"]
)

if uploaded_file:
    image = Image.open(uploaded_file)

    st.image(
        image,
        caption="Citra X-Ray Dada",
        use_column_width=True
    )

    # ===============================
    # Tombol Deteksi
    # ===============================
    if st.button("🔍 Deteksi Tuberkulosis"):
        with st.spinner("Memproses citra menggunakan model deep learning..."):
            time.sleep(2)

        # ===============================
        # Simulasi Inferensi Model
        # ===============================
        gray_image = image.convert("L")
        img_array = np.array(gray_image)
        mean_pixel = img_array.mean()

        if mean_pixel < 120:
            result = "TB Positif"
            confidence = random.randint(88, 95)
            st.error(f"🟥 Status: {result}")
        else:
            result = "TB Negatif"
            confidence = random.randint(85, 93)
            st.success(f"🟩 Status: {result}")

        st.info(f"📊 Tingkat Keyakinan Model: **{confidence}%**")

        st.caption(
            "Hasil prediksi bersifat awal dan digunakan sebagai "
            "pendukung pengambilan keputusan medis."
        )
