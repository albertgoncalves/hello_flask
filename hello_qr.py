#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import qrcode
import PIL

if __name__ == "__main__":
    dim  = 200
    data = {"Hello, ": "world!"}
    qr   = qrcode.QRCode( version         =1
                        , error_correction=qrcode.constants.ERROR_CORRECT_L
                        , box_size        =10  # scale image size
                        , border          =4
                        )
    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img = img.resize((dim, dim), PIL.Image.ANTIALIAS)
    img.save("hello_qr.png")
