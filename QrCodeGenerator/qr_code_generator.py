import qrcode 

#simple use
img = qrcode.make("Hello World")
img.save("myQrImage.png")

#using qrcode class allow more control
myQr = qrcode.QRCode(
    #from 1 to 40, determine the size of the Qr code
    version=1,
    #error correcton levels : L, M, Q, H
    error_correction = qrcode.constants.ERROR_CORRECT_L,
    #the size of each box
    box_size = 20,
    #size of border
    border = 4,
)
#add data to the Qr code
myQr.add_data("I am using a qrcode class")
#generate the qr code
myQr.make(fit=True)
#returns the image of the qr code
img = myQr.make_image()
#save it
img.save("QRClass_img.png")