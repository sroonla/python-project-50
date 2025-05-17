def to_str(value, depth=0):
    """
    Преобразует произвольное значение в строку:
     - dict: рекурсивно форматирует со сдвигом depth
     - bool, None: всегда маленькими буквами (true/false/null)
     - остальное: str(value)
    """
    if isinstance(value, dict):
        indent = '    ' * (depth + 1)
        lines = []
        for k, v in value.items():
            lines.append(f"{indent}    {k}: {to_str(v, depth + 1)}")
        inner = "\n".join(lines)
        return f"{{\n{inner}\n{'    ' * depth}}}"
    if isinstance(value, bool):
        return 'true' if value else 'false'
    if value is None:
        return 'null'
    return str(value)


def format_stylish(diff_tree, _=None, depth=0):
    """
    Форматирует дерево diff_tree в формат "stylish".
    Второй аргумент (_), legacy stringify, не используется.
    """
    indent = '    ' * depth
    lines = []

    for node in diff_tree:
        key = node['key']
        t = node['type']
        if t == 'nested':
            children = format_stylish(node['children'], None, depth + 1)
            lines.append(f"{indent}    {key}: {children}")
        elif t == 'removed':
            val = to_str(node['value'], depth)
            lines.append(f"{indent}  - {key}: {val}")
        elif t == 'added':
            val = to_str(node['value'], depth)
            lines.append(f"{indent}  + {key}: {val}")
        elif t == 'changed':
            old = to_str(node['old_value'], depth)
            new = to_str(node['new_value'], depth)
            lines.append(f"{indent}  - {key}: {old}")
            lines.append(f"{indent}  + {key}: {new}")
        else:  # 'unchanged'
            val = to_str(node['value'], depth)
            lines.append(f"{indent}    {key}: {val}")

    body = "\n".join(lines)
    return f"{{\n{body}\n{indent}}}"
