#! python3
"""[9] Nos robaron la cartera - 10 Puntos:
Se recibirá una contraseña y se ha de determinar si cumple las normas"""
from re import search

contraseña = input()
reglasIncumplidas = []
if len(contraseña) < 8:
    reglasIncumplidas.append("Rule 1")
if not search("[0-9]", contraseña):
    reglasIncumplidas.append("Rule 2")
if not search("[a-z]", contraseña):
    reglasIncumplidas.append("Rule 3")
if not search("[A-Z]", contraseña):
    reglasIncumplidas.append("Rule 4")
if not search("[%, &, @]", contraseña):
    reglasIncumplidas.append("Rule 5")

if reglasIncumplidas:
    print("PASSWORD ERROR! %s" % ", ".join(reglasIncumplidas))
else:
    print("PASSWORD OK!")
