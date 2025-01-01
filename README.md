# QR Code Generator and URL Shortener

This is a simple Streamlit web application that allows users to generate QR codes and shorten URLs. It combines the functionality of a QR code generator and a URL shortener, making it easy to share and distribute information.

## Features

1. **QR Code Generator**
   - Generate QR codes for any text or URL input.
   - Download the generated QR code as a PNG image.

2. **URL Shortener**
   - Shorten URLs using the TinyURL service.
   - Display and provide a clickable link to the shortened URL.

## Requirements

To run this application, ensure you have the following installed:

- Python 3.7+
- Required Python packages (listed below)

## Installation

1. Clone the repository or copy the code.

```bash
# Clone the repository
git clone <repository-url>

# Navigate to the project directory
cd <project-directory>
```

2. Install the required Python packages.

```bash
pip install streamlit qrcode pillow pyshorteners
```

## Usage

1. Run the Streamlit application.

```bash
streamlit run app.py
```

2. Open the provided URL in your web browser (usually `http://localhost:8501`).

3. Use the app:
   - Enter text or a URL in the "QR Code Generator" section to create a QR code.
   - Enter a URL in the "URL Shortener" section to shorten it.

## Application Workflow

1. **QR Code Generator**:
   - Enter the text or URL to generate a QR code.
   - Click "Generate QR Code" to display the QR code.
   - Optionally, download the QR code as a PNG file.

2. **URL Shortener**:
   - Enter the URL to shorten.
   - Click "Shorten URL" to display the shortened link.

## Dependencies

The following Python libraries are used in this project:

- `streamlit`: For building the web interface.
- `qrcode`: For generating QR codes.
- `pillow`: For image manipulation.
- `pyshorteners`: For shortening URLs.

Install them using the `pip install` command provided in the installation section.

## License

This project is open-source and available under the [MIT License](LICENSE).

## Acknowledgements

- [Streamlit Documentation](https://docs.streamlit.io/)
- [qrcode Library](https://pypi.org/project/qrcode/)
- [Pillow Documentation](https://pillow.readthedocs.io/)
- [pyshorteners Documentation](https://pypi.org/project/pyshorteners/)
