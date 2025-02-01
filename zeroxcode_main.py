#Main vars
import os
com = 0
vars = {}
arg = 0
args = []
narg = ""
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
   try:
      global total_arg , arg , narg
      for arg in args:
         if arg.startswith("%") == True:
            narg = arg[1:]
            if narg in vars:
               total_arg += str(vars[narg]) + " "
            elif narg == "last_input":
               total_arg += input_text + " "
            elif narg == "vars_list":
               for keys in vars.keys():
                  print(keys , end=" ")
                  print("" , sep="\n")
         else:
            total_arg += str(arg) + " "
      print(total_arg)
      total_arg = ""
   except:
      print("Error. Main process: print")
   
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
         args = []
         arg = "h"
         while arg != "":
            arg = input("argument>>")
            args.append(arg)
         printer(args)
      elif com == "setvar": 
         var_name = input("var_name>>")
         var_type = input("var_type>>")
         var_value = input("var_value>>")
         setvar(var_name, var_type, var_value)
      elif com == "delvar":
         namedel = input("name_var>>")
         delvar(namedel)
      elif com == "input":
         input_text= ""
         input_text = input("input>> ")
      elif com == "max_var":
         var1name = input("var1_name>>")
         var2name = input("var2_name>>")
         if (var1name in vars and var2name in vars):
            temp1v = vars[var1name]
            temp2v = vars[var2name]
            if isinstance(temp1v , int) and isinstance(temp2v , int):
               maxvar = max(temp2v, temp1v)
               if maxvar in vars.values():
                     pass
               
               temp1v = ""
               temp2v = ""
            else:
               print("Error. The variable type is not an int type")
               temp1v = ""
               temp2v = ""
         else:
            print("These variables do not exist")

      elif com == "clear":
         os.system("cls")
         print("ZeroxCode v.0.0.1_alpha for x64")
      else:
         print("Error: incorrect name command")
   except Exception as e:
        print(f"Error. Description - {e}")

