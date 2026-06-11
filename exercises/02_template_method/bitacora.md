# Bitácora 2 - Template Method

Nombre: Armando José Salgado Rosa

## Defectos encontrados

La función `build_report` en `reports.py` muestra signos de fragilidad y rigidez. En una misma función están coexistiendo formas distintas de generar un reporte. Esto provoca que si la lógica de un reporte falla, el otro también lo hará. Se vuelve complicado agregar un nuevo reporte, porque se debe asegurar que no hayan fallos en el resto de integraciones.

```python
# reports.py, línea 5
    if report_type == "sales":
        total = 0.0
        for row in rows:
            lines.append(f"{row['name']}: ${row['amount']:.2f}")
            total += float(row["amount"])
        lines.append(f"Total: ${total:.2f}")
        lines.append(f"Count: {len(rows)}")
        return "\n".join(lines)

    if report_type == "inventory":
        total_units = 0
        low_stock = 0
        for row in rows:
            lines.append(f"{row['sku']} | {row['name']} | {row['units']} units")
            total_units += int(row["units"])
            if int(row["units"]) <= 5:
                low_stock += 1
        lines.append(f"Total units: {total_units}")
        lines.append(f"Low stock: {low_stock}")
        return "\n".join(lines)
```

Al momento de implementar un nuevo reporte o alterar uno previo, es necesario hacer cambios a la función. Esto viola OCP y SRP. La función `build_report` no debería alterarse para eso, pues su responsabilidad es orquestar. A futuro, una clase abierta puede ocasionar comportamientos inesperados tras ser actualizada.

Por otra parte, existen pasos repetidos para cada tipo de reporte. Ambos tienen el mismo comienzo y operan con el mismo final. Esto va en contra del principio DRY.

```python
#reports.py, línea 2
    title = title or f"{report_type.title()} Report"
    lines = [title, "=" * len(title)]
```

```python
# reports.py, línea 12, 24 y 27
    return "\n".join(lines)
```

## Patrón escogido para la refactorización

Se implementó Template Method. Había pasos repetidos que podían integrarse en una sola clase abstracta. Se creó la clase `Report` que orquesta la impresión del reporte, haciendo uso de los pasos repetidos y dejando abstraidos aquellos particulares que varían para cada tipo. En esta ocasión, se implementaron tres clases hijas `InventoryReport`, `SalesReport` y `UnsupportedReport`.

Por otro lado, la función `build_report()` ahora se encarga de gestionar cuál reporte generar. Esta clase tendrá que alterarse cada vez que se agregué un nuevo tipo, no obstante, es más eficiente que antes; ya que la responsabilidad de orquestar el reporte se encapsuló en la clase abstracta. Por ende, no se arriesga romper comportamientos al hacer una actualización. Asimismo, el proceso de añadir el nuevo reporte es más desacoplado, ya que requiere una clase nueva independiente del resto, que implemente la clase abstracta.

## Patrones descartados

No se tomó en cuenta strategy, ya que si bien, cierta lógica varía, había muchos pasos repetidos. En búsqueda de mantener DRY, se optó por un template. No se aplicó factory ya que la única responsabilidad de la función `build_report` es gestionar la misma tarea que haría un factory (decidir cuál instancia de reporte generar). Los patrones command y observer no eran adecuados, ya que no estamos resolviendo acciones que necesiten auditarse o disparar otros eventos. Finalmente, no hay estados que requiran ser manejados ni clases que se optimicen mediante un singleton.