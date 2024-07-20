import qrcode
phone = "0562898172"
message = "Hello How are you"
wifi_password ="7D0E24DF"
sms = f"SMSTO : {phone}:{message}"
img = qrcode.make(sms)



print(type(img))  # qrcode.image.pil.PilImage
img.save("sms.png")