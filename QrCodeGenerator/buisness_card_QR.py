#create a qr code for a virtual buisness card
import qrcode

def create_virtual_card(name, phone, email, filename, organisation=" ", title=" "):
    vcard = f"""BEGIN:VCARD
VERSION:4.0
FN:{name}
N:{name.split(' ')[1]};{name.split(' ')[0]};;;
ORG:{organisation}
TITLE:{title}
TEL;TYPE=WORK,VOICE:{phone}
EMAIL;TYPE=PREF,INTERNET:{email}
END:VCARD"""
    
    # Create QR

    qr = qrcode.QRCode(
        version = 1,
        error_correction = qrcode.constants.ERROR_CORRECT_L,
        box_size = 10,
        border = 4,
        )

    qr.add_data(vcard)
    qr.make(fit=True)
    img = qr.make_image()
    img.save(filename)


if __name__=="__main__":
    print("please enter your buisness card info : ")
    name = input("name : ")
    phone = input("phone : ")
    email = input("email : ")
    organistion = input("organisation : ")
    title = input("title : ")
    file_name = input("save logo under file name ? :")
    
    create_virtual_card(name=name, email=email, phone=phone,title=title, organisation =organistion, filename=file_name)