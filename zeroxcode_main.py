#Main vars
import os
com = 0
vars = {}
arg = 0
args = []
pr_temp = ""
total_arg = ""
input_text = ""
def setvar(name , type , value):
   try:
      if type == "int":
         value = int(value)
         vars.update({name : value})
      elif type == "str" :
         value = str(value)
         vars.update({name : value})
      elif type == "float":
         value = float(value)
         vars.update({name : value})
   except:
      print('Error. Main process: setvar')

def delvar(delit):
   try:
      vars.pop(delit)
   except:
      print("Error. Variable not found")

def printer(args):
   global total_arg
   try:
      for arg in args:
         if arg == '&last_input':
            total_arg += input_text + " "
         else:
            total_arg += arg + " "
      print(total_arg)
   except:
      print("Error. Main process: print ")

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
      elif com == "vars_list":
         for keys in vars.keys():
            print(keys , end=" ")
         print("" , sep="\n")
      elif com == "delvar":
         namedel = input("name_var>>")
         delvar(namedel)
      elif com == "input":
         input_text= ""
         input_text = input("input>> ")
      elif com == "clear":
         os.system("cls")
         print("ZeroxCode v.0.0.1_alpha for x64")
      else:
         print("Error: incorrect name command")
   except Exception as e:
        print(f"Error. Description - {e}")

