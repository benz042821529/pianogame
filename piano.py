import autopy
import time
def findLDP():
    for i in range(30):
        screen = autopy.bitmap.capture_screen()
        LDP = autopy.bitmap.Bitmap.open("LDP.png")
        fistPOS = screen.find_bitmap(LDP)
        if fistPOS:
            print(fistPOS)
            return fistPOS
        else:
            print("cannot find game area "+ str(i+1) + "/30")

def multiclick():
    autopy.mouse.toggle(autopy.mouse.Button.LEFT,True)
    time.sleep(0.2)
    autopy.mouse.toggle(autopy.mouse.Button.LEFT,False)

def keyArea(fistPOS):
    screen = autopy.bitmap.capture_screen()
    print(fistPOS)
    fistArea = screen.find_color((53,159,198),0.05,((fistPOS[0]+50,fistPOS[1]+540),(450,80)))
    if not fistArea:
        fistArea = screen.find_color((0,0,0),0.05,((fistPOS[0]+50,fistPOS[1]+540),(540,80)))
    print(fistArea)
    if fistArea:
        autopy.mouse.move(fistArea[0],fistArea[1])
        # autopy.mouse.click()
        multiclick()
    

def start():
    fistPOS = findLDP()
    while True:
        keyArea(fistPOS)

start()
