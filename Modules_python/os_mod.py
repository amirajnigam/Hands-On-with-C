import os

os.chdir("D:\\Spring2020\\EE 281\\HW\\HW1")  # use to change the directory

print(os.getcwd())   # shows the path of current directory

os.mkdir("D:\\Spring2020\\EE 281\\HW\\HW1\\Hail_Hitler")  # make directory

os.rmdir("D:\\Spring2020\\EE 281\\HW\\HW1\\Hail_Hitler")  #remove the directory

os.remove("D:\\coding\\practice_code\\OS mod\\fake.py")   #remove the file  

print(os.path.join("D:\\coding\\practice_code\\OS mod\\sparta","D:\\coding\\practice_code\\OS mod\\sys_mod.py"))

# dir OS mod is join with sys_mpod.py


print(os.path.split("D:\\coding\\practice_code\\OS mod\\sys_mod.py")) #it will split it into 2 parts i.e. dir and python file sys_mod.py

print(os.path.exists("D:\\coding\\practice_code\\OS mod\\sys_mod.py")) #it will tell whether that path exist or not 










































































