def merge_files(file1_path, file2_path, output_file_path):
    with open(file1_path, 'r', encoding='utf-8') as file1:
        file1_content = file1.read()

    with open(file2_path, 'r', encoding='utf-8') as file2:
        file2_content = file2.read()

    with open(output_file_path, 'w', encoding='utf-8') as output_file:
        output_file.write(file1_content)
        output_file.write(file2_content)

    print(f"合并后的文件已保存到：{output_file_path}")

# 指定文件路径
wav_scp_path1 = '/data/experiment/wenet/examples/aishell/s1/utils/train/data.list'
wav_scp_path2 = '/data/wenet/examples/aishell/s1/utils/faster-whisper-aishell2/data.list'
output_wav_scp_path = '/data/wenet/examples/aishell/s1/utils/aishell1_whisperaishell2/data.list'

# 调用函数合并文件
merge_files(wav_scp_path1, wav_scp_path2, output_wav_scp_path)


