import qrcode
import os

def generate_qr_code(data, filename):
    # script er folder er absolute path ber kora
    script_dir = os.path.dirname(os.path.abspath(__file__))
    filepath = os.path.join(script_dir, filename)

    qr_code = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr_code.add_data(data)
    qr_code.make(fit=True)

    img = qr_code.make_image(fill_color="black", back_color="white")
    img.save(filepath)
    img.show()

    print(f"QR code saved at: {filepath}")

if __name__ == "__main__":
    data = input("Enter the data to encode in the QR code: ")
    filename = input("Enter the filename (e.g., 'qrcode.png'): ")
    generate_qr_code(data, filename)
