import time
import keyboard
from pyautogui import *
import win32gui


print("Starting in 3...")
time.sleep(1)
print("Starting in 2...")
time.sleep(1)
print("Starting in 1...")
time.sleep(1)

def get_pixel_colour(i_x, i_y): #110 fps
	i_desktop_window_id = win32gui.GetDesktopWindow()
	i_desktop_window_dc = win32gui.GetWindowDC(i_desktop_window_id)
	long_colour = win32gui.GetPixel(i_desktop_window_dc, i_x, i_y)
	i_colour = int(long_colour)
	win32gui.ReleaseDC(i_desktop_window_id,i_desktop_window_dc)
	return (i_colour & 0xff), ((i_colour >> 8) & 0xff), ((i_colour >> 16) & 0xff)
fps = []
l = True
l,r = True, False
#while True:
    #print(get_pixel_colour(861, 800)[0])
while not keyboard.is_pressed("q"):
    tic = time.time()
    if l:
        if get_pixel_colour(861, 662)[0] < 20:
            l,r = True,False
        else:
            l,r = False,True
    if r:
        if get_pixel_colour(1060, 656)[0] < 20:
            l,r = False,True                
        else:
            l,r = True,False

    if l: keyboard.press_and_release("a")
    if r: keyboard.press_and_release("d")
    try:
        fps.append(1 / (time.time() - tic))
    except:
        pass
    time.sleep(0.119)

# while not keyboard.is_pressed("q"): # média de 68 fps, calculado 3x
#     tic = time.time()
#     if get_pixel_colour(861, 662)[0] < 20 and l:
#         keyboard.press_and_release("a")
#     else:
#         l = False
#         if get_pixel_colour(1060, 656)[0] < 20:
#             keyboard.press_and_release("d")
#         else:
#             l = True
#     #print(f"FPS {1 / (time.time() - tic):0.0f}")
#     try:
#         fps.append(1 / (time.time() - tic))
#     except:
#         pass
#     time.sleep(0.119)

print(f"FPS=>{sum(fps) / len(fps):0.0f}")













#59, 56, 79
#while True:
# fps = []
# t = time.time()
# while not keyboard.is_pressed("q"):
#     get_pixel_colour(861, 662)
#     print(f"FPS: {(1 / (time.time() - t)):0.0f}")
#     try:
#         fps.append(int((1 / (time.time() - t))))
#     except:
#         pass
#     t = time.time()

# print(f"Média => {(sum(fps) / len(fps)):0.0f}")

        # if l:
        #     if pyautogui.locateOnScreen("log.png", region=(650, 580, 220, 120), grayscale=True, confidence=0.4) != None:
        #         #print("Tem tronco esquerda")
        #         keyboard.press_and_release("d")
        #         #l, r = False, True
        #         l = False
        #         r = True
        #         #input("PAROU")
        #     else:
        #         #print("Nao tem tronco esquerda")
        #         keyboard.press_and_release("a")

        # if r:
        #     if pyautogui.locateOnScreen("log2.png", region=(1060, 570, 230, 130), grayscale=True, confidence=0.4) != None:
        #         #print("Tem tronco direita")
        #         keyboard.press_and_release("a")
        #         #l, r = True, False
        #         l = True
        #         r = False
        #     else:
        #         keyboard.press_and_release("d")
        #         #print("Nao tem tronco direita")
        # if l:
        #     keyboard.press_and_release("a")
        # if r:
        #     keyboard.press_and_release("d")

        # time.sleep(0.5)