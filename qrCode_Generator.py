import qrcode
import os

def generate_qr_code(data, filename):
    
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)

    
    qr_img = qr.make_image(fill_color="black", back_color="white")

    
    desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")

    # Save QR code image as JPG on desktop
    file_path = os.path.join(desktop_path, filename)
    qr_img.save(file_path)

if __name__ == "__main__":
    
    data = input("Enter data to encode in QR code: ")
    filename = input("Enter filename: ") + ".jpg"
    generate_qr_code(data, filename)
    print(f"QR code saved as {filename} on the desktop.")
