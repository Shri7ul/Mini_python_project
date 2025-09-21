# QR Code Generator

A simple Python script to generate QR codes from any text or URL.  
The generated QR code will be saved as an image file (e.g., `.png`) and can also be previewed directly.

---

## Features
- Generate QR code from text or URL  
- Save QR code as an image file  
- Preview QR code after generation  

---

## Installation

Make sure you have Python installed (3.7 or above recommended).

Install required dependencies:

```bash
pip install qrcode[pil]
```

Or install separately:
```bash
pip install qrcode
```
```bash
pip install pillow
```

You will be prompted to enter:

1.The data you want to encode (e.g., a URL or text)

2.The filename where the QR code will be saved (e.g., qrcode.png)
 Enter the data to encode in the QR code: https://www.example.com
Enter the filename to save the QR code (e.g., 'qrcode.png'): my_qr.png

Example:
Enter the data to encode in the QR code: https://www.example.com
Enter the filename to save the QR code (e.g., 'qrcode.png'): my_qr.png

