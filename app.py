import streamlit as st
import qrcode
from io import BytesIO
from PIL import Image
import pyshorteners


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

        # Convert to Image format compatible with Streamlit
        buffer = BytesIO()
        img.save(buffer, format="PNG")
        buffer.seek(0)
        qr_image = Image.open(buffer)

        # Display QR Code
        st.image(qr_image, caption="Generated QR Code", use_column_width=True)

        # Download QR Code
        st.download_button(
            label="Download QR Code",
            data=buffer,
            file_name="qr_code.png",
            mime="image/png",
        )
    else:
        st.error("Please enter some text or a URL to generate a QR code.")


# URL Shortener
st.subheader("URL Shortener")
url_to_shorten = st.text_input("Enter URL to shorten", placeholder="Paste URL here...")

if st.button("Shorten URL"):
    if url_to_shorten:
        try:
            shortener = pyshorteners.Shortener()
            shortened_url = shortener.tinyurl.short(url_to_shorten)
            st.success(f"Shortened URL: {shortened_url}")
            st.write(f"[Open Shortened URL]({shortened_url})")
        except Exception as e:
            st.error(f"Error shortening URL: {e}")
    else:
        st.error("Please enter a URL to shorten.")
