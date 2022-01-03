


import time
animation = "|/-\\"
idx = 0
while 1:
    print(animation[idx % len(animation)], end="\r")
    idx += 1
    time.sleep(0.1)
    raise Exception("asd")
