"""The rgb() method is incomplete. Complete the method so that passing in RGB decimal values will result in a hexadecimal
representation being returned. The valid decimal values for RGB are 0 - 255. Any (r,g,b) argument values that fall out of
that range should be rounded to the closest valid value."""

def valid(number):
    return 0 if number < 0 else 255 if number > 255 else number
def to_hex(number):
    return hex(valid(number))[2:].upper() if number > 15 else '0' + hex(valid(number))[2:].upper()
def rgb(r, g, b):
    #your code here :)
    return to_hex(r) + to_hex(g) + to_hex(b)
