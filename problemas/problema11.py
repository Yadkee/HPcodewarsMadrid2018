#! python3
"""[11] Seguridad en las cuentas - 17 Puntos:
Se recibirán usuario y contraseña en dos líneas y se ha de devolver
 el nombre junto con el hash de la contraseña."""


def hash(contraseña):
    valor = 2166136261
    for cadaByte in contraseña:
        valor *= 16777619
        valor ^= ord(cadaByte)
    return valor

usuario = input()
contraseña = input()
print("%s:%s" % (usuario, hex(hash(contraseña))[-8:]))
