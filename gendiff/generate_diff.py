from gendiff.file_parser import parse_file


def build_diff(data1, data2):
    keys = sorted(set(data1.keys()) | set(data2.keys()))
    diff = []
    for key in keys:
        if key not in data2:

            diff.append({
                'key': key,
                'type': 'removed',
                'value': data1[key]
            })
        elif key not in data1:
            diff.append({
                'key': key,
                'type': 'added',
                'value': data2[key]
            })
        elif isinstance(data1[key], dict) and isinstance(data2[key], dict):
            children = build_diff(data1[key], data2[key])
            diff.append({
                'key': key,
                'type': 'nested',
                'children': children
            })
        elif data1[key] == data2[key]:
            diff.append({
                'key': key,
                'type': 'unchanged',
                'value': data1[key]
            })
        else:
            diff.append({
                'key': key,
                'type': 'changed',
                'old_value': data1[key],
                'new_value': data2[key]
            })
    return diff


def generate_diff(file_path1, file_path2, format_name='stylish'):
    data1 = parse_file(file_path1) or {}
    data2 = parse_file(file_path2) or {}
    diff_tree = build_diff(data1, data2)
    if format_name == 'stylish':
        from gendiff.formatters.stylish import format_stylish
        return format_stylish(diff_tree)
    elif format_name == 'plain':

        from gendiff.formatters.plain import format_plain
        return format_plain(diff_tree)
    elif format_name == 'json':

        from gendiff.formatters.json import format_json
        return format_json(diff_tree)
    raise ValueError(f"Unknown format: {format_name}")
