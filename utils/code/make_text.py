# 指定原始 text 文件的路径
original_file_path = '/data/aishell2/test/trans.txt'

# 处理文件中的每一行，确保编号和文本之间只有一个空格
processed_lines = []
with open(original_file_path, 'r', encoding='utf-8') as file:
    for line in file:
        parts = line.strip().split()  # 移除首尾空白并以空格分割字符串
        if len(parts) >= 2:  # 确保有编号和至少一个文本部分
            processed_line = f"{parts[0]} {' '.join(parts[1:])}"  # 使用单个空格连接编号和文本
            processed_lines.append(processed_line)

# 将处理后的内容写入新的 text 文件
new_file_path = '/data/wenet/examples/aishell/s1/utils/test/text.txt'
with open(new_file_path, 'w', encoding='utf-8') as new_file:
    for processed_line in processed_lines:
        new_file.write(processed_line + '\n')

print(f"新的 text 文件已生成于路径：{new_file_path}")

