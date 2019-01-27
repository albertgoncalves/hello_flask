#!/usr/bin/env python3


def sanitize_id(item_id):
    sanitize = check_type(item_id, int)

    if sanitize is not None:
        ins_char = sanitize
    else:
        ins_char = str("null")

    return ins_char


def check_type(input_val, output_type):
    try:
        return output_type(input_val)
    except (ValueError, TypeError):
        return None


def local_ip():
    with open("ip", "r") as f:
        local_ip = f.read().replace("\n", "")

    return local_ip
