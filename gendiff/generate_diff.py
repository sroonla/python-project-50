import os
from gendiff.file_parser import parse_file
from gendiff.formatters.stylish import format_stylish

def build_diff(data1, data2):
    """
    Строит дерево различий между двумя словарями без искусственной группировки.
    """
    keys = sorted(set(data1.keys()) | set(data2.keys()))
    diff = []
    
    for key in keys:
        # Ключ удален
        if key not in data2:
            diff.append({
                'key': key,
                'type': 'removed',
                'value': data1[key]
            })
            
        # Ключ добавлен
        elif key not in data1:
            diff.append({
                'key': key,
                'type': 'added',
                'value': data2[key]
            })
            
        # Оба значения - словари (рекурсивное сравнение)
        elif isinstance(data1[key], dict) and isinstance(data2[key], dict):
            children = build_diff(data1[key], data2[key])
            diff.append({
                'key': key,
                'type': 'nested',
                'children': children
            })
            
        # Значения разные
        elif data1[key] != data2[key]:
            diff.append({
                'key': key,
                'type': 'changed',
                'old_value': data1[key],
                'new_value': data2[key]
            })
            
        # Значения одинаковые
        else:
            diff.append({
                'key': key,
                'type': 'unchanged',
                'value': data1[key]
            })
    
    return diff

def generate_diff(file_path1, file_path2, format_name='stylish'):
    """
    Генерирует различия между двумя файлами
    """
    data1 = parse_file(file_path1) or {}
    data2 = parse_file(file_path2) or {}

        # Отладочная печать
    print("Data from file1:", data1)
    print("Data from file2:", data2)

    diff_tree = build_diff(data1, data2)
    
        # Печать diff-дерева
    print("Diff tree:", diff_tree)
    
    if format_name == 'stylish':
        result = format_stylish(diff_tree)
        print("Formatted result:", result)
        return result
    
    raise ValueError(f"Unknown format: {format_name}")