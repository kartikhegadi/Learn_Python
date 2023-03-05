import time,sys
indent = 0 # how many spaces to indent.
indent_increase=True # Whether the indenting is increased or not
try:
    while True:  #the main program loop;
        print(''*indent,end='')
        print('*********')
        time.sleep(0.1)

        if indent_increase:   #increase the number of spaces
            indent=indent+1
            if indent==20:#change direction
                indent_increase=False
        else:#decreasing the number of spaces
            indent=indent-1
            if indent ==0:# change direction
                indent_increase=True
except KeyboardInterrupt:
    sys.exit()
