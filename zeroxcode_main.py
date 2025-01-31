#Main vars
import os
com = 0
vars_list = []
arg = 0
args = []
pr_temp = ""
total_arg = ""
input_text = ""
vars = []

def setvar(name, type , value):
   try:
      if type == "int":
            value = int(value)
            vars.append(name)
            vars.append(value)
      elif type == "str":
         if isinstance(value, str) == True:
            value = str(value)
            vars.append(name)
            vars.append(value)
      elif type == "bool":
         if isinstance(value, bool) == True:
            value = bool(value)
            vars.append(name)
            vars.append(value)
   except:
      print('Error. Process: setavar')

def delvar(delit):
   index = vars.index(delit)
   vars.remove(delit)
   vars.pop(index+1)
   print(vars)
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

os.system("cls")
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
      elif com == "setvar": 
         var_name = input("var_name>>")
         var_type = input("var_type>>")
         var_value = input("var_value>>")
         setvar(var_name, var_type, var_value)
         print(vars)
      elif com == "delvar":
         namedel = input("name_var>>")
         delvar(namedel)
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

