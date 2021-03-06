#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import PIL
import qrcode

from funs import local_ip
from funs import sanitize_id


def id_url(item_id):
    ins_char = sanitize_id(item_id)
    return "http://{}:5002/insert/{}".format(local_ip(), ins_char)


def gen_qr(data):
    qr = qrcode.QRCode( version=1
                      , error_correction=qrcode.constants.ERROR_CORRECT_L
                      , box_size=10  # scale image size
                      , border=2
                      )
    qr.add_data(data)
    qr.make(fit=True)

    return qr


def export_qr(qr, dim, fn):
    img = qr.make_image(fill_color="white", back_color="black")
    img = img.resize((dim, dim), PIL.Image.ANTIALIAS)
    img.save(fn)


def main():
    dim = 200
    fn = "qr.png"
    url = id_url(51)
    qr = gen_qr(url)
    export_qr(qr, dim, fn)


if __name__ == "__main__":
    main()
