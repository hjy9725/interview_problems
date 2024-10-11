import os
import re

def replace_tex_with_dollars_in_md_files(directory):
    # 遍历目录及其子目录下的所有文件
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.md'):
                file_path = os.path.join(root, file)
                with open(file_path, 'r', encoding='utf-8') as md_file:
                    content = md_file.read()
                
                # 使用正则表达式替换 \[ \] 和 \( \) 为 $
                content = re.sub(r'\\\[', '$', content)
                content = re.sub(r'\\\]', '$', content)
                content = re.sub(r'\\\(', '$', content)
                content = re.sub(r'\\\)', '$', content)
                
                with open(file_path, 'w', encoding='utf-8') as md_file:
                    md_file.write(content)
                print(f'Processed file: {file_path}')

# 调用函数，传入你想要处理的目录路径
replace_tex_with_dollars_in_md_files('./')