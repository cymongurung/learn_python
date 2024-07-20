import qrcode
img = qrcode.make('suman gurung')
type(img)  # qrcode.image.pil.PilImage
img.save("cymon.png")

# WIFI:T:{wifi_type};S:{wifi_ssid};P:{wifi_password};;


