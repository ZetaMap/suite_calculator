"""Ce programme permet de calculer la raison et u_0 d'une suite, arithmétique ou géométrique, à partir de 2 points donnés, 
puis vous affiche le résultat proprement avec le calcul effectuer par la machine, pour vous aider.

Le programme vous proposera ensuite,  si vous le voulez, de calculer des points spécifiques dans cette suite, 
et/ou si vous voulez en faire la somme des termes.
"""

def center(s, width, char=' '):
  n = width - len(s)
  if n <= 0: return s
  half = n//2
  if n%2 and width%2: half += 1
  return char*half + s + char*(n-half)

###########################################

a = input("1- Suite arthmétique \n2- Suite géométrique \n|-> ")
while a != '1' and a != '2': a = input("|-> ")
u, isnan, text = [[],[],["Départ :","Arrivé :"]], False, """
Entrées :
Départ : u_{} = {}
Arrivé : u_{} = {}
--------------------
Calcul :{}
    {}
{} = {} = {}
    {}
--------------------
Résultat :
u_n+1 = u_n{}
  u_0 = {}
{}La suite est {}."""
for i in range(2):
  u[i].append(int(eval(input("{} u_".format(u[2][i])))))
  u[i].append(eval(input("{} u_{} = ".format(u[2][i], u[i][0]))))

if u[0][0] > u[1][0]: u = [u[1], u[0]]
else: u = [u[0], u[1]]


if a == '1':
  uu = u.copy()
  if uu[0][1] < uu[1][1]: uu.reverse()
  try: pas = (u[0][1]-u[1][1])/(u[0][0]-u[1][0])
  except ZeroDivisionError: 
    pas = float("nan")
    isnan = True
  u0, r, x, y = uu[0][1]-uu[0][0]*pas, str(round(pas, 5)), round(uu[0][1], 5), round(uu[1][1], 5)
  if u0 == int(u0): u0 = int(u0)
  up, down = str(x)+'-'+('('+str(y)+')' if uu[1][1] < 0 else str(y)), str(uu[0][0])+'-'+('('+str(uu[1][0])+')' if uu[1][0] < 0 else str(uu[1][0]))
  b = max(len(up), len(down))

  print(text.format(
    u[0][0], x,
    u[1][0], y,
    '',
    center(up, b),
    'r', '-'*b, r,
    center(down, b),
    r if pas < 0 else '+'+r,
    round(u0, 5),
    '\n',"nan" if isnan else "constante" if pas == 0 else "décroissante" if pas < 0 else "croissante"
  ))
  del uu, r, x, y, up, down, b 

else:
  try: pas = (u[1][1]/u[0][1])**(1/(u[1][0]-u[0][0]))
  except ZeroDivisionError: 
    pas = float("nan")
    isnan = True  
  u0, r, d, x, y = u[0][1]/pas**u[0][0], str(round(pas, 5)), str(u[1][0]-u[0][0]), round(u[0][1], 5), round(u[1][1], 5)
  if u0 == int(u0): u0 = int(u0)
  b, e = max(len(str(x)), len(str(y))), len(d)

  print(text.format(
    u[0][0], x,
    u[1][0], y,
    "\n    "+' '*(e+2)+'_'*(b+1),
    ' '*(e+1)+'|'+center(str(y), b),
    'q', d+" |"+'-'*b, r,
    ' '*e+"\\|"+center(str(x), b),
    '*'+('('+r+')' if pas < 0 else r),
    round(u0, 5),
    '', "nan" if isnan else "nulle" if pas == 0 else "constante" if pas == 1 else "décroissante" if pas < 0 else "croissante"
  ))
  del d, x, y, b, e

if not isnan:
  if input("Calculer des termes ? [o/n]: ") == 'o':
    print("> N'écrivez rien pour quitter.\n")
    t = input("u_")
    while t != '': 
      try: print("u_"+t+" =", round(u0+pas*int(t) if a == "1" else u0*pas**int(t), 5))
      except OverflowError: print("u_"+t+" = inf")
      t = input("u_")

  if input("Calculer la somme des termes ? \n[o/n]: ") == 'o':
    print("> N'écrivez rien pour calculer \nla somme à partir des valeurs \nde la suite.\n")
    s, text = [["Début :", "Fin :"]], """
    Entrées :
Début : u_{} = {}
Fin : u_{} = {}
--------------------
Calcul :
    {}
S = {}
    {}
  = {}
--------------------
Résultat :
      {}
S_n = {} 
      {}
    = {}"""
    try: 
      for i in range(2): 
        t = int(eval(input("{} u_".format(s[0][i]))))
        tt = u0+pas*t if a == '1' else u0*pas**t
        if tt == int(tt): tt = int(tt)
        s.append([t, tt])
    except (ValueError, SyntaxError): s += [u[0], u[1]]
    del u, t, tt, isnan
    s.pop(0)
    if s[0][0] > s[1][0]: s.reverse()


    x, y, d = round(s[0][1], 5), round(s[1][1], 5), s[1][0]-s[0][0]
    if a == '1':
      up, m, down = str(x)+'+'+('('+str(y)+')' if s[1][1] < 0 else str(y)), '('+str(d)+"+1)x", None
      b, bb, c = len(up), len(m), round((d+1)*((s[0][1]+s[1][1])/2), 5)
      
      print(text.format(
        s[0][0], x,
        s[1][0], y,
        ' '*bb+up,
        m+'-'*b,
        ' '*bb+center(str(2), b),
        c,
        "      u_i+u_n",
        "(n+1)x-------", 
        "         2",
        c
      ))

    else:
      up, m, down = "1-{}^({}+1)".format('('+r+')' if pas < 0 else r, d), str(round(u0, 5))+'x', "1-"+('('+r+')' if pas < 0 else r)
      b, bb, c = max(len(up), len(down)), len(m), round(u0*((1-pas**(d+1))/(1-pas)), 5)

      print(text.format(
        s[0][0], x,
        s[1][0], y,
        ' '*bb+up,
        m+'-'*b,
       ' '*bb+center(down, b),
       c,
       "    1-q^(n+1)",
       "u_0x---------",
       "       1-q",
       c
      ))

    del x, y, d, up, m, down, b, bb, c, s, u0, pas, text
else: input()
