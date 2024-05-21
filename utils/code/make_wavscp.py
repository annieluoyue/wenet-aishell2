# 指定原始 wav.scp 文件的路径
original_file_path = '/data/aishell2/test/wav.scp'

# 定义要添加的前缀路径
prefix_path = "/data/aishell2/test/"

# 处理文件中的每一行，确保编号和地址之间只有一个空格，并添加前缀路径
processed_lines = []
with open(original_file_path, 'r') as file:
    for line in file:
        parts = line.strip().split()  # 移除首尾空白并分割字符串
        if len(parts) == 2:  # 确保只有编号和地址两部分
            complete_path = prefix_path + parts[1]  # 在地址前添加前缀路径
            processed_line = f"{parts[0]} {complete_path}"  # 用单个空格连接编号和完整地址
            processed_lines.append(processed_line)

# 将处理后的内容写入新的 wav.scp 文件
new_file_path = '/data/wenet/examples/aishell/s1/utils/test/wav.scp'
with open(new_file_path, 'w') as new_file:
    for processed_line in processed_lines:
        new_file.write(processed_line + '\n')

print(f"新的 wav.scp 文件已生成于路径：{new_file_path}")

