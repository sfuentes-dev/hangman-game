# Optimizaciones realizadas

## Optimizaciones de codigo en eficiencia y velocidad:

- En la función `read_word`, la comprensión de la lista se utiliza directamente como argumento para random.choice en lugar de crear una lista intermedia. Los reemplazos de letras también se hacen en una sola línea usando el método replace.

- En la función `new_word`, las variables se asignan directamente en la definición de la función en lugar de pasarlas como argumentos. Esto elimina la necesidad de pasar y devolver dichas variables.

- En la función `comparar_letra`, la variable l se renombra a char para mayor claridad. El método items() se utiliza para iterar directamente sobre los pares clave-valor del diccionario.

- La lista de letras se inicializa utilizando la función chr para generar los alfabetos en lugar de codificarlos y se añade la letra Ñ de manera "manual" ya que no se incluye por defecto a traves de esta funcion.

- La variable `no_letter` se inicializa a 0 en lugar de establecerla explícitamente después de llamar a `new_word`.

- El manejo de excepciones por entrada inválida se simplifica capturando ValueError directamente y eliminando la letra de la lista de letras usando el método remove.

- En la función de `run` ahora llamada `hangman`, la función `new_word` se llama directamente sin necesidad de pasar las variables como argumentos.

- La condición `if fail == True` se simplifica a `if fail`, y la condición else se elimina ya que no es necesaria.

- La condición `"".join(discovered).replace(' ', '') == word` se utiliza en lugar de `''.join(descubierta).replace(' ','') == word` para eliminar los espacios antes de la comparación.

- Se elimina la sentencia continue después de llamar a `new_word` ya que el bucle continuará naturalmente sin ella.

## Optimizaciones en facilidad de lectura del codigo:

1. En la función `read_word`, los reemplazos de letras se realizan directamente dentro de la comprensión de la lista.

2. La función `compare_letter` ahora inicializa `Fail` a `True` y lo pone a False sólo cuando se encuentra una letra. Esto elimina la necesidad de una condición else.
3. La variable `no_letter` se inicializa a False en lugar de establecerla explícitamente después de llamar a la funcion `new_word`.
4. El formato f-string se utiliza para el prompt de entrada en consola tenga una mejor egibilidad.
5. Se elimina la sentencia continue después de llamar a la funcion `new_word` ya que el bucle continuará naturalmente sin ella.
6. La condición `''.join(descubierta).replace(' ', '') == word` se utiliza directamente sin asignarla a una variable.

## Optimizaciones para respetar el principio DRY:

En esta versión optimizada, he realizado los siguientes cambios:

1. Trasladé las imágenes del ahorcado a un diccionario para facilitar su recuperación en función del número de muertes.

2. Eliminadas las condiciones if-else innecesarias para la comprobación de letras mediante el uso de una lista de letras disponibles.
3. Simplificada la función refresh() para reducir la duplicación de código.
4. Eliminadas las llamadas redundantes a `os.system('cls')` y `os.system('clear')` utilizando saltos de línea apropiados en la salida.
5. Esta versión del código incluye una función play_again que pregunta al jugador si quiere jugar otra ronda. Si el jugador elige "S" para sí, el juego se reinicia. Si elige 'N' para no, el juego sale. Esto con el fin de simplificar la funcion `run` ahora llamada `hangman` y respetar el princpio de responsabilidad unica.
