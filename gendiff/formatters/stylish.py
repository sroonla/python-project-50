def to_str(value, depth):
    if isinstance(value, dict):
        indent = '    ' * (depth + 1)
        lines = []
        for k, v in value.items():
            lines.append(f"{indent}{k}: {to_str(v, depth + 1)}")
        inner = "\n".join(lines)
        return f"{{\n{inner}\n{'    ' * depth}}}"
    if isinstance(value, bool):
        return 'true' if value else 'false'
    if value is None:
        return 'null'
    return str(value)


def format_stylish(diff_tree, depth=0):
    indent = '    ' * depth
    lines = []

    for node in diff_tree:
        key = node['key']
        node_type = node['type']

        if node_type == 'nested':
            children = format_stylish(node['children'], depth + 1)
            lines.append(f"{indent}    {key}: {children}")
        elif node_type == 'removed':
            val = to_str(node['value'], depth + 1)
            lines.append(f"{indent}  - {key}: {val}")
        elif node_type == 'added':
            val = to_str(node['value'], depth + 1)
            lines.append(f"{indent}  + {key}: {val}")
        elif node_type == 'changed':
            old_val = to_str(node['old_value'], depth + 1)
            new_val = to_str(node['new_value'], depth + 1)
            lines.append(f"{indent}  - {key}: {old_val}")
            lines.append(f"{indent}  + {key}: {new_val}")
        else:
            val = to_str(node['value'], depth + 1)
            lines.append(f"{indent}    {key}: {val}")

    if depth == 0:
        result = "{\n" + "\n".join(lines) + "\n}"
    else:
        result = "{\n" + "\n".join(lines) + "\n" + indent + "}"

    return result
