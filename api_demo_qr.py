#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import PIL
import qrcode

from api_demo_funs import sanitize_id

# pure functions
def id_url(item_id):
    ins_char = sanitize_id(item_id)
    return "http://192.168.1.52:5002/insert/{}".format(ins_char)

def gen_qr(data):
    qr = qrcode.QRCode( version         =1
                      , error_correction=qrcode.constants.ERROR_CORRECT_L
                      , box_size        =10  # scale image size
                      , border          =2
                      )
    qr.add_data(data)
    qr.make(fit=True)
    return qr

# side-effects
def export_qr(qr, dim, fn):
    img = qr.make_image(fill_color="black", back_color="white")
    img = img.resize((dim, dim), PIL.Image.ANTIALIAS)
    img.save(fn)

def main():
    dim = 200
    fn  = "api_demo.png"
    url = id_url(51)
    qr  = gen_qr(url)
    export_qr(qr, dim, fn)

if __name__ == "__main__":
    main()
