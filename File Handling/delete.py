import os
if os.path.exists("dhamu.txt"):
    os.remove("dhamu.txt")
else:
    print("The file doesnot exist")