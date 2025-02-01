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
def comiler(f):
   file_opened = open(path , "r")
   file_read = file_opened.read().split("\n")
   for line in file_read:
            if line.startswith("#"):
                continue
            elif line.strip(" ") == "":
                continue
            else:
               line_list = line.split(";", maxsplit = 1 )
               if len(line_list) < 2:
                  print("Incorrect command format")
               func = line_list[0]
               args = line_list[1]
               args = args.strip()
               args = line_list[1].split("/")
               for arg in args:
                  arg = arg.strip()
               arg = "n"
               func = func.strip()
               
               if func == "print":
                  printer(args)
               if func == "setvar":
                  setvar(args[0] , args[1], args[2])
                  
               #print("Error: Incorrect name command")
def setvar(name , type , value):
   try:
      if name != "" or name.startswith(" "): 
         if type == "int":
            value = int(value)
            vars.update({name : value})
         elif type == "str" :
            value = str(value)
            vars.update({name : value})
         elif type == "float":
            value = float(value)
            vars.update({name : value})
         else:
            print("Incorrect variable type")
      else:
         print("A variable cannot start with a space or contain spaces, nor can the variable name be empty.")
   except Exception as e:
      print(f'Error. Main process: setvar. Description: {e}')
def inputer(text , svar = "last_input"):
   global input_text , save_var
   if text != "" or text != " ":
      if save_var in vars:
         vars.update({svar : text})
      else:
         vars.update({svar : text})
def delvar(delit):
   try:
      vars.pop(delit)
   except:
      print("Error. Variable not found")
def printer(args: list):
   try:
      global total_arg , arg , narg
      for arg in args:
         if arg.startswith("%") == True:
            narg = arg[1:]
            if narg in vars:
               total_arg += str(vars[narg]) + " "
            elif narg == "vars_list":
               for keys in vars.keys():
                  print(keys , end=" ")
                  print("" , end="\n")
            elif narg == "vars_items":
               for key,value in vars.items():
                  print(key , " : " , value, end=" ; ")
                  print("" , end="\n")
         else:
            total_arg += arg + " "
      print(total_arg)
      total_arg = ""
   except Exception as e:
      print(f"Error. Main process: print. Description: {e}")
   
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
         save_var = input("Save_var. If not required - enter>>")
         inputer(input_text, save_var)
      elif com == "max_var":
         try:
            var1name = input("var1_name>>")
            var2name = input("var2_name>>")
            if (var1name in vars and var2name in vars):
               temp1v = vars[var1name]
               temp2v = vars[var2name]
               if isinstance(temp1v , int) and isinstance(temp2v , int):
                  maxvar = max(temp2v, temp1v)
                  if maxvar in vars.values():
                        if maxvar == temp1v:
                           print("Max variable: ", var1name , "Value: " , maxvar)
                        elif maxvar == temp2v: 
                           print("Max variable: ", var2name , "Value: " , maxvar)
                  temp1v = ""
                  temp2v = ""
               else:
                  print("Error. The variable type is not an int type")
                  temp1v = ""
                  temp2v = ""
            else:
               print("These variables do not exist")
         except Exception as e:
            print(f"Error. Procces: max_var. Description: {e}")
      elif com == "min_var":
         try:
            var1name = input("var1_name>>")
            var2name = input("var2_name>>")
            if (var1name in vars and var2name in vars):
               temp1v = vars[var1name]
               temp2v = vars[var2name]
               if isinstance(temp1v , int) and isinstance(temp2v , int):
                  maxvar = min(temp2v, temp1v)
                  if maxvar in vars.values():
                        if maxvar == temp1v:
                           print("Min variable: ", var1name , "Value: " , maxvar)
                        elif maxvar == temp2v: 
                           print("Min variable: ", var2name , "Value: " , maxvar)
                  temp1v = ""
                  temp2v = ""
               else:
                  print("Error. The variable type is not an int type")
                  temp1v = ""
                  temp2v = ""
            else:
               print("These variables do not exist")
         except Exception as e:
            print(f"Error. Procces: max_var. Description: {e}")
      elif com == "clear":
         os.system("cls")
         print("ZeroxCode v.0.0.1_alpha for x64")
      elif com == "exit":
         raise SystemExit(0)
      elif com == "math_var":
         try:
            var1 = input("Var1_name>>")
            sym = input("symbol>>")
            var2 = input("Var2_name>>")
            if (var1 in vars) and (var2 in vars):
               var1d = vars[var1]
               var2d = vars[var2]
               ev = var1 + sym + var2
               print(eval(ev))
            else:
               print("Invalid variable name")
         except Exception as e:
            print(f"Error. Process: math_vars. Description {e}")
      elif com == "open":
         path = input("path (replace \\ to \\\\)>> ")
         comiler(path)

      else:
         print("Error: Incorrect name command")
   except SystemExit:
      raise SystemExit(0)
   except Exception as e:
        print(f"Error. Description - {e}")

