# Bitácora 3 - State + Factory

Nombre: Armando José Salgado Rosa

## Defectos encontrados

En la clase `Order` el estado se cambia de manera arbitraria dentro de cada método. Esto provoca rigidez, pues al querer alterar las propiedades de transición de un estado es necesario revisar todos los métodos implementados.

```python
# order.py, línea 8
if self.status != "draft":
    return False
self.status = "open"
```
```python
# order.py, línea 15
if self.status not in {"draft", "open"}:
    return False
self.status = "paid"
```
```python
# order.py, línea 22
if self.status != "paid":
    return False
self.status = "packed"
```
```python
# order.py, línea 29
if self.status != "packed":
    return False
self.status = "shipped"
```
```python
# order.py, línea 36
if self.status == "shipped":
    return False
self.status = "cancelled"
```
Agregado a lo anterior se corre el riesgo de caer en viscocidad, pues agregar otro método que genere cambios de estado con condicionales parece sencillo y más eficiente que generar otras clases. Sin embargo, como se mencionó antes, eso lleva a un código más acoplado y frágil. Un fallo en una transición y todo el sistema de ordenes deja de funcionar.

Se violan principios de OCP ya que agregar un nuevo estado podría requerir modificaciones a varios métodos al mismo tiempo para mantener la consistencia.

***

## Patrón escogido para la refactorización

Se eligió usar State ya que permitirá manejar los estados de manera más desacoplada. Asimismo, se empleó Factory para separar la lógica de selección del tipo de estado a generar. Ya no es necesario alterar la clase `Order` para agregar estados o cambiar su comportamiento.

Se generó una clase abstracta para estados y una clase factory. Se crearon 6 clases hijas, cada una con sus propias reglas de transición.

Para añadir un nuevo estado ahora solo es necesario crear una clase que implemente la clase abstracta OrderState, y luego modificar OrderStateFactory para incluirla. Esto resulta más eficiente y desacoplado. Si bien, aún se toca la clase factory, es una operación aceptable.

Se crearon las siguientes clases:
- `OrderState`: Interfaz que define el comportamiento de los estados
- `OrderStateFactory`: Decide cuál estado se genera y ejecuta transiciones
- `DraftStatus`
- `OpenStatus`
- `PackedStatus`
- `PaidStatus`
- `ShippedStatus`
- `CancelledStatus`

Se respetan SRP ya que las responsabilidades de order se limitaron a gestionar los métodos de transición. La transición se relegó a OrderState y la validez de cada transición a su propia clase hija.

Cabe aclarar que esto es una adaptación del método State más Factory.

***

## Patrones descartados

No se tomó en consideración strategy porque los métodos ya separan la lógica particular de cada operación. Template no se utilizó ya que no hay procesos estructurados que tengan leves variaciones que necesiten clases propias. Descartamos command, ya que existe un formato de auditoría y no es un requisito tener que revertir operaciones. Observer tampoco es necesario ya que al manejarse estados internos, no se afecta de momento otras clases externas que dependan de los cambios de estado. Singleton no es necesario de momento, aunque a futuro podría recomendarse para `self.events` para mantener una sola instancia de eventos.

***