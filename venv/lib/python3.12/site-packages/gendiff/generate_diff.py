import json


def read_json(filepath):
    with open(filepath, 'r') as file:
        return json.load(file)


def generate_diff(file_path1, file_path2):
    data1 = read_json(file_path1)
    data2 = read_json(file_path2)

    all_keys = sorted(set(data1) | set(data2))
    lines = []

    for key in all_keys:
        if key in data1 and key not in data2:
            lines.append(f"  - {key}: {data1[key]}")
        elif key not in data1 and key in data2:
            lines.append(f"  + {key}: {data2[key]}")
        elif data1[key] != data2[key]:
            lines.append(f"  - {key}: {data1[key]}")
            lines.append(f"  + {key}: {data2[key]}")
        else:
            lines.append(f"    {key}: {data1[key]}")

    result = "{\n" + "\n".join(lines) + "\n}"
    return result
