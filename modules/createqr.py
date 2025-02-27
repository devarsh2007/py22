# https://pypi.org/ - python packages


import qrcode

# Generate QR Code with simple data
img = qrcode.make("www.youtube.com")  # content of QR

# Save the generated QR code as an image
img.save("myqr.png")

# Show the QR code
img.show()
