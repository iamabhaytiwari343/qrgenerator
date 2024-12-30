import streamlit as st
import qrcode
from io import BytesIO
from PIL import Image

# App Title
st.title("QR Code Generator")

# User Input
st.subheader("Enter text or URL to generate a QR Code")
user_input = st.text_area("Input", placeholder="Type here...")

# Generate QR Code
if st.button("Generate QR Code"):
    if user_input:
        # Create QR Code
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_H,
            box_size=10,
            border=4,
        )
        qr.add_data(user_input)
        qr.make(fit=True)
        img = qr.make_image(fill_color="black", back_color="white")

        # Display QR Code
        st.image(img, caption="Generated QR Code", use_column_width=True)

        # Download QR Code
        buffer = BytesIO()
        img.save(buffer, format="PNG")
        buffer.seek(0)
        st.download_button(
            label="Download QR Code",
            data=buffer,
            file_name="qr_code.png",
            mime="image/png",
        )
    else:
        st.error("Please enter some text or a URL to generate a QR code.")
