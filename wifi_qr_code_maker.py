import qrcode
wifi_type = "WPA"
wifi_ssid = "X28-2.4G-4ED1A1"
wifi_password ="7D0E24DF"
wifi = f"WIFI:T:{wifi_type};S:{wifi_ssid};P:{wifi_password};;"
img = qrcode.make(wifi)
type(img)  # qrcode.image.pil.PilImage
img.save("cymon_wifi.png")