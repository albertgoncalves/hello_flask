#!/usr/bin/env python3

# pure functions
def sanitize_id(item_id):
    sanitize = check_type(item_id, int, 0)

    if sanitize is not None:
        ins_char = sanitize
    else:
        ins_char = str('null')

    return ins_char

# ...pure?
def check_type(input_val, output_type, default_val):
    try:
        val = output_type(input_val)
    except (ValueError, TypeError):
        val = None
    return val
