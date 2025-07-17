#write a python program to print the content of a directory using os module
import os
directory_path ='/'
content = os.listdir(directory_path)

for item in content:
    print(item)