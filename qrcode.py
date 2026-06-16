import qrcode

data = input("Masukkan link atau teks untuk QR Code: ")

qr = qrcode.make(data)
qr.save("qrcode.png")

print("QRCode berhasil dibuat dan disimpan sebagai qrcode.png")