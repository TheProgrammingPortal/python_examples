
import qrcode
qr = qrcode.make('TheProgrammingPortal')
qr.save('qr.png')
print('QR code is generated.')