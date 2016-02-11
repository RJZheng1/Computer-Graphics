def makeImage():
    f = open('pic.ppm', 'w')
    xres = 600
    yres = 600
    maxRGB = 255
    r = 2
    g = 3
    b = 5
    f.write("P3 " + str(xres) + " " + str(yres) + " " + str(maxRGB) + " ")
    for x in xrange(xres):
        for y in xrange(yres):
            f.write(str(r) + " " + str(g) + " " + str(b) + " ")
            r = (r * 2) % maxRGB
            g = (g * 3) % maxRGB
            b = (b * 5) % maxRGB
    f.close()

makeImage()
