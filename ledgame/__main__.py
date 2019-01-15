try:
    from sense_hat import SenseHat
    sense = SenseHat()
except ImportError:
    from notpi import NotPi
    sense = NotPi(scale=64)


w = [0xFF, 0xFF, 0xFF]
b = [0x0, 0x0, 0x0]

pixels = [
    w, w, w, w, w, w, w, w,
    w, w, w, b, b, w, w, w,
    w, w, w, b, b, b, b, b,
    w, w, b, b, b, b, b, b,
    w, b, b, b, b, b, b, b,
    b, b, b, b, b, b, b, b,
    w, w, w, w, w, w, w, w,
    w, w, b, b, b, b, b, b
]

i = 0
sense.set_pixels(pixels)

while True:
    sense.update()
    if i % 500 == 0:
        sense.flip_v()
        i = 0
    i += 1
