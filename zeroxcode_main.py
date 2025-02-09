#Main vars
import os
from random import randint,random
com = 0
vars = {}
arg = 0
args = []
redcom = ""
narg = ""
pr_temp = ""
total_arg = ""
input_text = ""
bannedfunc = []
def compiler(f):
   if "compiler" in bannedfunc:
      raise Exception("Function banned")
   global redcom, npe , vars
   file_opened = open(f , "r")
   file_read = file_opened.read().split("\n")
   for line in file_read:
            
            if line.startswith("#"):
                continue
            elif line.strip() == "":
                continue
            else:
               line_list = line.split(";" , maxsplit=1)
               if len(line_list) < 2:
                  print("Incorrect command format")
               func = line_list[0].strip()
               args = line_list[1].split("/")
               l = args[0].strip()
               args[0] = l
               func = func.strip()
               if func == "print":
                  printer(args)
               elif func == "setvar":
                  setvar(args[0] , args[1], args[2])
               elif func == "delvar":
                  delvar(args[0])
               elif func == "input":
                  itext = input()
                  inputer(itext, args[0])
               elif func == 'math':
                  if len(args) == 3:
                     math(args[0], args[1], args[2])
                  elif len(args) == 4:
                     math(args[0], args[1], args[2], args[3])
               elif func == "tof":
                  if len(args) == 3:
                     tof(args[0], args[1], args[2])
                  elif len(args) == 4:
                     tof(args[0], args[1], args[2], args[3])
               elif func == "vars_clear":
                  vars.clear()
               elif func == "ban":
                  ban(args)
               elif func == "flrand":
                  if len(args) == 1:
                     flrandom(args[0])
                  else:
                     flrandom()
               elif func == "intrand":
                  intrand(args[0],args[1],args[2])
def ban(a : list):
   for el in a:
      bannedfunc.append(el)               
def setvar(name , type , value):
   if "setvar" in bannedfunc:
      raise Exception("Function banned")
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
   if "input" in bannedfunc:
      raise Exception("Function banned")
   if text != "" or text != " ":
      if svar in vars:
         vars.update({svar : text})
      else:
         vars.update({svar : text})
def delvar(delit):
   try:
      if "delvar" in bannedfunc:
         raise Exception("Function banned")
      vars.pop(delit)
   except:
      print("Error. Variable not found")
def printer(args: list):
   if "print" in bannedfunc:
      raise Exception("Function banned")
   try:
      global total_arg , arg , narg
      for arg in args:
         if arg.startswith("%") == True:
            narg = arg[1:]
            narg = str(narg)
            narg = narg.strip()
            if narg in vars:
               total_arg += str(vars[narg]) + " "
            elif narg == "vars_list":
               for keys in vars.keys():
                  print(keys , end=" ; ")
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
def math(n1 , s , n2 , sv="last_math"):
      if "math" in bannedfunc:
         raise Exception("Function banned")
   #try:
      if n1 in vars:
            nu1 = vars.get(n1)
            nu1 =str(nu1)
      else:
         nu1 = n1
         nu1 = str(nu1)
      if n2 in vars:
         nu2 = vars.get(n2)
         nu2 = str(nu2)
      else:
         nu2 = n2
         nu2 = str(nu2)
      
      ev = nu1 + s + nu2
      res = eval(ev)
      vars.update({sv:res})
   #except Exception as e:
      #print(f"Error[m01] math: Description - {e}")
def tof(nov1 , s , nov2, vret="last_tof"):
   if "tof" in bannedfunc:
      raise Exception("Function banned")
   ret = ""
   
   if nov1 in vars:
      v1 = vars.get(nov1)
      if isinstance(v1 , int) == False:
         raise TypeError("A variable containing a number must be entered")
   else:
      v1 = int(nov1)
   if nov2 in vars:
      v2 = vars.get(nov2)
      if isinstance(v2 , int) == False:
         raise TypeError("A variable containing a number must be entered")
   else:
      v2 = int(nov2)
   if s == "=":
      if v1 == v2:
         ret = True
      else:
         ret = False
   if s == ">":
      if v1>v2:
         ret = True
      else:
         ret = False
   if s == "<":
      if v1<v2:
         ret = True
      else:
         ret = False
   vars.update({vret : ret})
def flrandom(c = "last_flrand"):
   if "flrandom" in bannedfunc:
      raise Exception("Function banned")
   v = random()
   vars.update({c:v})
def intrand(sp,stp,vs = "last_intrand"):
   st = int(st)
   stp = int(stp)
   it = randint(sp,stp)
   vars.update({vs:it})
os.system("cls")
print("ZeroxCode v.0.0.3_alpha for x64")
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
                           print(f"Max variable: {var1name} Value: {maxvar} " )
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
         print("ZeroxCode v.0.0._alpha for x64")
      elif com == "vars_clear":
         vars.clear()
      elif com == "exit":
         raise SystemExit(0)
      elif com == "math":
         n1 = input("number1>>")
         symbm = input("symbol>>")
         n2 = input("number2>>")
      elif com == "open":
         path = input("path (replace \\ to \\\\)>> ")
         compiler(path)
      elif com == "tof":
         a1 = input("var1 or number1>>")
         csi = input("mark>>")
         a2 = input("var2 or number2>>")
         tof(a1,csi,a2)
      elif com == "ban":
         fb = "n"
         while fb != "":
            fb = input("func_name>>")
            bannedfunc.append(fb)
      elif com == "flrand":
         r1 = input("var_save. If not required - enter>>")
         flrandom(r1)
      elif com == "intrand":
         startp = input("start_point>>")
         stopp = input("stop_point>>")
         irvs = input("var_save. If not required - enter>>")
         intrand(startp,stopp)
      else:
         print("Error[n002]: Incorrect name command")
   except SystemExit:
      raise SystemExit(0)
   except Exception as e:
      print(f"Main error. Description - {e}")


