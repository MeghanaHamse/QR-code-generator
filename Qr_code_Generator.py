import qrcode

def generate_qr_code(url, file_name):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(url)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img.save(file_name)
    img.show()

if __name__ == "__main__":
    url = "https://example.com"
    file_name = "example_qr_code.png"
    generate_qr_code(url, file_name)
    print(f"QR code generated for {url} and saved as {file_name}")
