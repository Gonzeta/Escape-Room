# ============================================================
# ESCAPE ROOM - Mansilla-Medina-Quiroz Edition
# ============================================================

-Cifrado propio-
def cifrar(texto, clave):
    resultado = ""
    for c in texto:
        code = ord(c)
        if c == " ":
            resultado += " "
        elif 65 <= code <= 90:       # Mayúsculas
            resultado += chr(((code - 65 + clave) % 26) + 65)
        elif 97 <= code <= 122:      # Minúsculas
            resultado += chr(((code - 97 + clave) % 26) + 97)
        else:
            resultado += c
    return resultado

def descifrar(texto, clave):
    return cifrar(texto, -clave)


-Intro
def intro():
    print("""
=====================================================
              E S C A P E   R O O M
=====================================================
Despertás en una casa abandonada. La luz entra apenas
por las grietas. Frente a vos hay:

- Un CUADRO colgado en la pared (algo raro tiene…)
- Una REJILLA rota a la derecha
- Una PUERTA cerrada
- Una CAJA FUERTE en el suelo
- Una COMPUTADORA vieja

Tu misión:
   Resolver 5 pruebas y escapar.

""")

-Var // juego
inventario = {
    "linterna": False,
    "llave_rejilla": False,
    "codigo_cuadro": False,    # palabra "puerta" descifrada
    "llave_caja": False
}

puerta_cerrada = True
caja_abierta = False
cuadro_resuelto = False
puerta_abierta = False

--ASCII
def ascii_puerta():
    print("""
    +-----------+
    |   _____   |
    |  |     |  |
    |  |  O  |  |
    |  |_____|  |
    |           |
    +-----------+
    """)

def ascii_cuadro():
    print("""
      _____________
     |  *  .  *   |
     |   . CUADRO |
     | .     *    |
     |   *   .    |
     |____________|

    (Hay algo oculto entre los puntos...)
    """)

-Prueba 1 // Cuadro
def examinar_cuadro():
    global cuadro_resuelto

    if cuadro_resuelto:
        print("\nYa descubriste el mensaje oculto del cuadro.")
        return

    ascii_cuadro()

    print("""
Observás el cuadro detenidamente.
Entre los puntos, aparece un texto cifrado:

         "sxhuwd"

Es tu PRIMER DESAFÍO.
Debés DESCIFRAR la palabra usando el sistema de cifrado.

Pista (oculta): la clave es la cantidad de letras de "sol" → 3
""")

    intento = input("Ingresá la palabra descifrada: ").strip().lower()

    if intento == "puerta":
        print("\n✔ Correcto. La palabra oculta era 'puerta'.")
        inventario["codigo_cuadro"] = True
        cuadro_resuelto = True
    else:
        print("\n✘ Esa no es la palabra correcta. Volvé a intentar luego.")


-Prueba 2 // Rejilla
def examinar_rejilla():
    if inventario["llave_rejilla"]:
        print("\nYa encontraste la llave en la rejilla.")
        return

    print("""
Te agachás y mirás la rejilla rota.
Entre los hierros doblados, algo brilla…
""")

    print("""
   [ .   .  * .  ]
   [   *   .   . ]
   [ .   LLAVE   ]

Encontrás una LLAVE pequeña.
""")

    inventario["llave_rejilla"] = True


Prueba 3 // Caja
def abrir_caja():
    global caja_abierta

    if caja_abierta:
        print("\nLa caja fuerte ya está abierta.")
        return

    if not inventario["llave_rejilla"]:
        print("\nNecesitás una llave para abrir la caja fuerte.")
        return

    print("""
Usás la llave de la rejilla para abrir la caja fuerte…
Dentro encontrás OTRA llave más robusta.

¡Clave obtenida para la puerta final!
""")

    inventario["llave_caja"] = True
    caja_abierta = True


-Prueba 4 // Computadora
def usar_computadora():
    if not inventario["codigo_cuadro"]:
        print("\nLa computadora te pide una palabra clave… pero aún no la sabés.")
        return

    print("""
Encendés la computadora vieja. Parpadea.

Pide la palabra clave descubierta en el cuadro.
""")

    ingreso = input("Ingresá la palabra: ").strip().lower()

    if ingreso == "puerta":
        print("\n✔ La computadora te muestra un número: 4826.")
        print("Este es el código numérico de la puerta final.")
        inventario["codigo_puerta"] = True
    else:
        print("\n✘ Incorrecto. Recordá lo que viste en el cuadro.")

-Prueba 5 // Puerta
def intentar_abrir_puerta():
    if not inventario.get("codigo_puerta"):
        print("\nLa puerta tiene un panel numérico… Necesitás un código.")
        ascii_puerta()
        return

    ascii_puerta()
    codigo = input("Ingresá el código numérico para abrir la puerta: ")

    if codigo == "4826":
        print("\n✔ La puerta se abre con un chirrido eterno...")
        print("   ESCAPASTE de la casa abandonada.")
        global puerta_abierta
        puerta_abierta = True
    else:
        print("\n✘ Código incorrecto.")


-Menu
def menu():
    print("""
¿Qué querés hacer?

1. Examinar el CUADRO  (cifrado + pista oculta)
2. Revisar la REJILLA  (observación)
3. Abrir la CAJA FUERTE (requiere llave)
4. Usar la COMPUTADORA  (requiere descifrado)
5. Intentar abrir la PUERTA (puzzle final)
6. Ver inventario
7. Salir
""")

-Inventario
def ver_inventario():
    print("\nInventario actual:")
    for item, estado in inventario.items():
        print(f"- {item}: {'✔' if estado else '✘'}")


--Loop de l juego
def juego():
    intro()
    while not puerta_abierta:
        menu()
        op = input("Elegí una opción: ")

        if op == "1":
            examinar_cuadro()
        elif op == "2":
            examinar_rejilla()
        elif op == "3":
            abrir_caja()
        elif op == "4":
            usar_computadora()
        elif op == "5":
            intentar_abrir_puerta()
        elif op == "6":
            ver_inventario()
        elif op == "7":
            print("\nSaliendo del juego…")
            return
        else:
            print("\nOpción inválida.")

    print("\nGracias por jugar, escapista.")
    print("Fin del Escape Room.")


# Ejecutar
juego()
