import notpi

notpi = notpi.NotPi()

w = [255, 255, 255]
b = [0, 0, 0]

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
    notpi.set_pixels(pixels)
    notpi.update()
