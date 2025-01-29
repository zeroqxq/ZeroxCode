#Main vars
import os
com = 0
vars_list = []
arg = 0
args = []
pr_temp = ""
total_arg = ""
input_text = ""


def printer(args):
   global total_arg
   try:
      for arg in args:
         if arg == '*last_input':
            total_arg += input_text + " "
         else:
            total_arg += arg + " "
      print(total_arg)
   except Exception as e:
      print(f"Error. Description: {e}")

print("ZeroxCode v.0.0.1_alpha for x64")
while True:
   try:
      com = input(">> ")
      if com == "" or com == " ":
         continue
      elif com.startswith("#") == True:
         continue
      elif com == "print":
         while arg != "":
            arg = input("argument>>")
            args.append(arg)
         printer(args)
      elif com == "input":
         input_text=""
         input_text = input("input>> ")
      elif com == "clear":
         os.system("cls")
         print("ZeroxCode v.0.0.1_alpha for x64")
      else:
         print("Error: incorrect name command")
   except Exception as e:
        print(f"Error. Description - {e}")

