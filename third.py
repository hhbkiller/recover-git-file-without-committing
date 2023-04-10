import os
import shutil

# 读取路径
result_path = r"D:\git恢复文件"  #接上个文件，如果你需要在找回的文件中搜索特定的关键字并保存在特定格式
# 存放符合条件的文件的目录
new_path = r"D:\git恢复文件重命名"

if not os.path.exists(new_path):
    os.makedirs(new_path)

for file in os.listdir(result_path):
    if file.endswith(".txt"):
        file_path = os.path.join(result_path, file)
        with open(file_path, "r", encoding="utf-8") as f:
            try:
                content = f.read()
            except UnicodeDecodeError:
                continue  # 如果打开失败，继续下一个文件
            class_name = ""
            # 判断文件内容是否包含类名
            if "class " in content:
                index = content.index("class ") + 6
                while content[index].isalnum() or content[index] == "_":
                    class_name += content[index]
                    index += 1
                # 如果类名非空，说明文件内容中包含类名
                if class_name != "":
                    new_file_path = os.path.join(new_path, class_name + ".txt")
                    shutil.copy(file_path, new_file_path)
