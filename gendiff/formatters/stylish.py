def to_str(value, depth):
    """
    Рекурсивно преобразует значение в строку с правильными отступами
    """
    if isinstance(value, dict):
        indent = '    ' * (depth + 1)
        lines = []
        for key, val in value.items():
            lines.append(f"{indent}{key}: {to_str(val, depth + 1)}")
        return "{\n" + "\n".join(lines) + "\n" + '    ' * depth + "}"
    
    if isinstance(value, bool):
        return 'true' if value else 'false'
    
    if value is None:
        return 'null'
    
    return str(value)

def format_stylish(diff_tree, depth=0):
    """
    Форматирует дерево различий в стильный вывод с правильными отступами
    """
    indent = '    ' * depth
    lines = []
    
    for node in diff_tree:
        key = node['key']
        node_type = node['type']
        new_indent = indent + '    '

        if node_type == 'nested':
            children = format_stylish(node['children'], depth + 1)
            # Для вложенных узлов используем специальное форматирование
            lines.append(f"{new_indent}{key}: {children}")
        
        elif node_type == 'removed':
            value = to_str(node['value'], depth + 1)
            lines.append(f"{indent}  - {key}: {value}")
        
        elif node_type == 'added':
            value = to_str(node['value'], depth + 1)
            lines.append(f"{indent}  + {key}: {value}")
        
        elif node_type == 'changed':
            old_value = to_str(node['old_value'], depth + 1)
            new_value = to_str(node['new_value'], depth + 1)
            lines.append(f"{indent}  - {key}: {old_value}")
            lines.append(f"{indent}  + {key}: {new_value}")
        
        else:  # unchanged
            value = to_str(node['value'], depth + 1)
            lines.append(f"{indent}    {key}: {value}")

    # Формируем результат с учетом уровня вложенности
    if depth == 0:
        result = "{\n" + "\n".join(lines) + "\n}"
    else:
        result = "{\n" + "\n".join(lines) + "\n" + indent + "}"

    return result