'''
shutil - helps in performing high level file operations
'''

import shutil
import os

# agar copy ki jagah copy2 use karey to exact copy banadega
shutil.copy("main.py","main2.py")

# copytree - purey folder ki copy banadega
#shutil.copytree(".tutorial", "mytutorial")

#shutil.move - helps in moving a file

shutil.rmtree("mytutorial")  # helps in removing a folder

os.remove("file.file")  # file remove karney ke liye os module ko heen use karna padega

