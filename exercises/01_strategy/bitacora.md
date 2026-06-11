# Bitacora 1 - Strategy

Nombre: Armando José Salgado Rosa

## Defectos encontrados

En el archivo `pricing.py` en la función `calculate_total()` se puede identificar una clara fragilidad a raíz de que se utiliza una estructura condicional que contiene dentro de sí todas las implementaciones de cálculo de precio. Si un error surge dentro de alguna estrategia, el resto también se verá afectado.

```python
# pricing.py, línea 6
        if category == "book":
            if customer_type == "student":
                price *= 0.85
            elif customer_type == "vip":
                price *= 0.80
        elif category == "food":
            if customer_type == "student":
                price *= 0.95
            elif customer_type == "vip":
                price *= 0.90
        elif category == "digital":
            if customer_type == "vip":
                price *= 0.75
        else:
            if customer_type == "student":
                price *= 0.97
            elif customer_type == "vip":
                price *= 0.92
```

Además, se está violando SRP, ya que la función pricing no solo orquesta sino que implementa directamente los algoritmos del cálculo de precio. Esta función debe modificarse si se quiere alterar un algoritmo específico o la orquestación general del precio final. También, se viola OCP; debido a que la función deberá seguir alterandose cada vez que se quiera agregar un nuevo tipo de descuento. Ya sea por la categoría de producto o por condiciones de la compra.

```python
# pricing.py, línea 25
    if len(items) >= 4:
        total *= 0.95
    if rush:
        total += 4.5
    if customer_type == "vip" and total > 100:
        total *= 0.97
```
***

## Patrón escogido para la refactorización

Se plantea utilizar strategy para separar la lógica de los precios dinámicos según categoria. Asimismo, se propone usar factory para mantener SRP y OCP. De esta forma se genera una clase CategoryFactory (la que llama pricing.py), una interfaz Category y 4 clases que implementan dicha interfaz:

- `Category`: Interfaz que tiene el método calcular_precio
- `CategoryFactory`: Encargado de decidir que estrategia implementar
- `BookCategory`
- `DigitalCategory`
- `FoodCategory`
- `DefaultCategory`

Además, se generó una clase `AdjustmentsApplier` que separá la lógica de los ajuste del total de `calculate_total()`. Esto para mantener SRP en esta misma. La nueva clase utiliza la interfaz `Adjustment` que permite mantener DIP. Se aplica strategy pues se generaron tres clases que encapsulan la lógica de cada ajuste. Un cambio en cualquier ajuste no afectará al resto. Asimismo, para agregar un nuevo ajuste solo se debe agregar una nueva clase que implemente la interfaz y agregar la condición en el constructor del applier. Esto permite que pricing ahora sea totalmente cerrada.

- `Adjustment`: Interfaz que define un contrato para aplicar cambios
- `AdjustmentApplier`: Clase que utiliza la interfaz y calcula el nuevo total, aplicando solo los ajustes necesarios
- `amountAdjustment`
- `rushAdjustment`
- `vipAdjustment`

Ahora, si se quiere agregar otro tipo de categoría, se genera una nueva clase y solo se modifica una línea del factory. La función `calculate_total()` ya no debe ser modificada por cada cambio en una estrategia especifica o para agregar un nuevo descuento. Un fallo en la estrategia de libros no afectará la ejecución de la estrategia de Comida.

***

## Patrones descartados

No se aplicó template porque no existe más de un proceso con pasos estandarizados. Las estrategias de precio y ajustes cambian del todo. No se manejan estados internos así que no se aplicó state. En el caso de command, no se aplicó ya que las acciones no necesitan transformarse en clases, lo más similar fue la clase AdjustmentsApplier, pero aún así, no convierte los cambios a aplicar en clases reversibles (podría implementarse más fácilmente en un futuro). No se aplicaron singletons ya que la función no requiere de una única instancia de clases, cada calculo debe ser independiente. Finalmente, se descartó usar observers pues es una única acción a realizar, no hay otras que requieran escuchar el evento "calculado" por ejemplo.