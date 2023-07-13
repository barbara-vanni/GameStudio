from main import *
from settings import *
import time
import numpy as np
from numba import njit

#---------------------------------------------
#  Floorcasting BETA
#---------------------------------------------
class Floorcasting(window):
    def __init__(self, width=0, height=0, title=""):
        super().__init__(width,height,title)
        self.angle = 0

        self.horizon_gap = 5

        self.texture = pg.image.load("image/sol.png.web").convert()
        self.texture_bitmap = self.texture.tobytes()

        self.ouverture = 60*np.pi/180
        self.background = pg.image.load("image/sol.png.web")
        self.resizeBackgroundImage()

        self.xt0 = self.yt0 = 0.0
        self.angle = 0
        self.z = self.texture.height/2

    def keyProc(self, event):
        super().keyProc(event)
        if event.keysym == "Left":
            self.angle -= np.pi/180
        elif event.keysym == "Right":
            self.angle += np.pi/180
        elif event.keysym == "Up":
            self.z += 2
        elif event.keysym == "Down":
            self.z -= 2

    def resizeBackgroundImage(self):
        w = self.buffer.width*2*np.pi/self.ouverture
        h = self.buffer.height/2+self.horizon_gap
        self.bg_resized = self.background.resize((int(w), int(h)))

    def onResize(self, event):
        super().onResize(event)
        self.resizeBackgroundImage()

    def draw(self, imagedraw, w,h):
        # imagedraw.rectangle((0,0,w,h),fill="black")

        global t0
        t = time.perf_counter()

        if self.bg_resized:
            f_angle = w / self.ouverture
            x = -(self.angle % (2*np.pi)) * f_angle
            self.buffer.paste(self.bg_resized, (int(x),0))
            if x+self.bg_resized.width < w:
                self.buffer.paste(self.bg_resized, (int(x+self.bg_resized.width),0))
            if x > 0:
                self.buffer.paste(self.bg_resized, (int(x-self.bg_resized.width),0))

        bmparray = bytearray(self.buffer.tobytes())

        c = np.cos(self.angle)
        s = np.sin(self.angle)

        mapFloorTexture(bmparray, w, h,
                    h/2+self.horizon_gap, self.z,
                    self.texture_bitmap, self.texture.width, self.texture.height,
                    self.xt0, self.yt0, c, s, s, -c)

        self.buffer.frombytes(bytes(bmparray))

        print(1/(time.perf_counter()-t),"FPS", 1/(t-t0), "FPS_total")
        t0 = t

        # self.angle = self.angle - np.pi/180
        # self.xt0 += self.texture.width/20

@njit
def mapFloorTexture(bmparray, w, h, yhorz, z, texture, wtex, htex, ox, oy, a11, a12, a21, a22 ):
    scaleX = w
    scaleY = scaleX
    XC = int(w / 2)
    YC = int(h / 2)

    for line in range(int(yhorz), h-1):
        x, y = invertCoords(0, line, z, XC, YC, scaleX, scaleY)
        xtex, ytex = matMulXY(x-ox,y-oy, a11, a12, a21, a22)
        x, y = invertCoords(w-1, line, z, XC, YC, scaleX, scaleY)
        xtex2, ytex2 = matMulXY(x-ox,y-oy, a11, a12, a21, a22)
        xd = (xtex2-xtex)/w
        yd = (ytex2-ytex)/h
        #  light : 0 to 255
        light = int(128*(0.5+1.5*((line-yhorz)/(h-yhorz))))
        mapTextureHLine(bmparray,w,line,texture,wtex,htex,xtex,ytex,xd,yd,light)

@njit
def invertCoords(X,Y,z,XC,YC,scaleX,scaleY):
    y = z * scaleY/(Y-YC)
    x = y * (X-XC)/scaleX
    return (x, y)

@njit
def matMulXY( x, y, a11, a12, a21, a22 ):
    return (x*a11+y*a21, x*a12+y*a22)

@njit
def mapTextureHLine(bmparray, w, y, texture, wtex, htex, ox, oy, xdx, xdy, light):
    i = (y*w)*3
    xtex1 = ox; ytex1 = oy
    for x in range(0, w):
        X = int(xtex1) % wtex
        Y = int(ytex1) % htex
        if X < 0: X = X + wtex
        if Y < 0: Y = Y + htex
        itex = (Y * wtex + X) * 3
        bmparray[i] = texture[itex]*light//256
        bmparray[i+1] = texture[itex+1]*light//256
        bmparray[i+2] = texture[itex+2]*light//256
        i = i + 3
        xtex1 = xtex1 + xdx
        ytex1 = ytex1 + xdy


t0 = time.perf_counter()

window = Floorcasting(width=640, height=480)
window.loop()