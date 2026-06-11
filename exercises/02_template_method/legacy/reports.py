def build_report(report_type, rows, title=None):
    title = title or f"{report_type.title()} Report"
    lines = [title, "=" * len(title)]

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

    lines.append("Unsupported report")
    return "\n".join(lines)
