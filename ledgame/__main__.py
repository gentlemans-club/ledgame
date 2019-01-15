try:
    from sense_hat import SenseHat
    sense = SenseHat()
except ImportError:
    from notpi import NotPi
    sense = NotPi(scale=100)


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

while True:
    sense.set_pixels(pixels)
