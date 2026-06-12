# Bitácora 4 - Command

Nombre: Armando José Salgado Rosa

## Defectos encontrados

En la clase `Editor` se están implementando acciones que deberían ser reversibles. Asimismo, los comandos se encuentran definidos dentro de la clase, lo que provoca fragilidad ante cambios. Si uno es modificado, el resto puede terminar afectado. La rigidez se muestra a su vez, porque implementar un nuevo comando conlleva analizar el impacto que tendrá en el resto de la clase.

```python
# editor.py, línea 8
self.history.append(self.text)
self.text = f"{self.text}{value}"
```
```python
# editor.py, línea 13
self.history.append(self.text)
count = int(value or 0)
self.text = self.text[:-count] if count else self.text
```
```python
# editor.py, línea 19
self.history.append(self.text)
old, new = value
self.text = self.text.replace(old, new, 1)
```
```python
# editor.py, línea 25
if self.history:
    self.text = self.history.pop()
```

Se detecta también una violación al principio DRY porque se repite la siguiente línea de código: 

```python
# editor.py, líneas 10, 16, 22, 27 y 29
return self.text
```

Finalmente, se observa un falla en OCP y SRP porque la clase editor debe ser modificada ya sea para alterar la lógica de los comandos o para agregar uno nuevo. Asimismo, comparte la responsabilidad de clasificar que comando utilizar e implementar los cambios.
***

## Patrón escogido para la refactorización

Se decidió adaptar el patrón Command y Factory para mejorar el desacoplamiento que presentaba la clase editor. Primero, se implementó la interfaz `Command` que se encarga de definir la abstracción del objeto que puede ejecutar una acción. Luego, se desarrolló la clase `CommandFactory` que se encarga de instanciar los comandos especificos dependiendo de la acción deseada. Después, se programó una clase `Invoker` que tiene la responsabilidad de llamar a los diferentes comandos. Finalmente se implementaron las siguientes clases hijas de `Command`:

- `InsertCommand`
- `DeleteCommand`
- `ReplaceCommand`
- `UndoCommand`

Se respetan SRP ya que las responsabilidades de `Editor` se limitaron a gestionar el llamado de execute. La lógica de decisión se paso al Factory, el detalle de los efectos secundario se almacena en cada clase comando y la lógica de ejecución del comando se encapsula en el invoker.

Esto permite además respetar OCP. Ya que editor no tiene porque ser modificado. La clase `CommandFactory` queda abierta, pues cada vez que se agregue un nuevo comando se deberá incorporar al match. No obstante, es un costo menor manejable en comparación al estado original. Como se mencionó, un nuevo comando puede agregarse extendiendo `Command`, sin necesidad de alterar el editor o invoker.

Se eliminó la repetición de la línea de código, por lo que se respeta DRY.

***

## Patrones descartados

Strategy no se implementó en esta ocasión pues había ciertos elementos y responsabilidades compartidas que se resolvieron a través de un invoker. Con strategy se hubiese distribuido el código legacy en clases robustas que repetirían lógica y mantendrían el acoplamiento. Estas al ser "acciones" que se convirtieron en "clases" convenía más manejarlas como comandos. Template method no era conveniente, pues cada comando ejecuta una acción totalmente distinta. State tampoco era adecuado ya que no hay un estado interno que lo requiera. Observer es menos apropiado que command, ya que el único efecto secundario que se activa de momento es el historial. No hay necesidad de que otra clase escuche el evento. Un singleton sería util para el historial y no se descarta que deba implementarse en un futuro, sin embargo, de momento el único que accede al historial es editor, por lo que se considera prescindible.

***