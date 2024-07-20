
# mailto:<email_address>?subject=<subject>&body=<body>



import qrcode
email_address = "simons4ful@gmail.com"
subject = "Hello How are you"
body ="Hello there is all good with you ? Please let me know "

email_add = f"mailto:{email_address}?subject={subject}&body={body}"
img = qrcode.make(email_add)



print(type(img))  # qrcode.image.pil.PilImage
img.save("email_sender.png")