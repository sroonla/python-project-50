def to_string(value):
    if isinstance(value, dict):
        return '[complex value]'
    if isinstance(value, bool):
        return 'true' if value else 'false'
    if value is None:
        return 'null'
    if isinstance(value, str):
        return f"'{value}'"
    return str(value)


def format_plain(diff, path=''):
    lines = []
    for node in diff:
        key = node['key']

        current_path = f"{path}.{key}" if path else key
        node_type = node['type']
        if node_type == 'nested':
            nested_result = format_plain(node['children'], current_path)
            if nested_result:
                lines.append(nested_result)
        elif node_type == 'added':
            value = to_string(node['value'])
            lines.append(
                f"Property '{current_path}' was added with value: {value}"
            )
        elif node_type == 'removed':
            lines.append(f"Property '{current_path}' was removed")
        elif node_type == 'changed':
            old_value = to_string(node['old_value'])
            new_value = to_string(node['new_value'])
            lines.append(
                f"Property '{current_path}' was updated. "
                f"From {old_value} to {new_value}"
            )
    return '\n'.join(lines)
