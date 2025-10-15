from itertools import cycle

key = "./exclusive_key"


def xor(a: bytes, b: bytes):
    #   return bytes(i ^ j for i, j in zip(a, b))
    return bytes(i ^ j for i, j in zip(a, cycle(b)))


with open(key, "rb") as file:
    text = file.read()

# with open("t.txt", "rb") as fi:
#    flag = fi.read()
flag = b"247CTF{"

xor_text = xor(text, flag)


with open("xor_results3.txt", "wb") as f:
    f.write(xor_text)
