import os
import subprocess
from datetime import datetime

# 源文件夹路径
src_folder = r'D:\.git\objects'   #这里是你的git文件夹的路径，.git文件夹是隐藏的，所以要在文件夹的地址栏中输入
# 目标文件夹路径
dst_folder = r'D:\git恢复文件'#这里是你要找回的保存的文件夹路径
# 目标日期
target_date = datetime(2023, 4, 7)

for root, dirs, files in os.walk(src_folder):
    for file_name in files:
        file_path = os.path.join(root, file_name)
        # 取出修改日期在目标日期之后的文件
        if os.path.splitext(file_path)[1] == '' and os.path.getmtime(file_path) >= target_date.timestamp():
            # 构造命令
            cmd = ['git', 'cat-file', '-p', (os.path.basename(root)+file_name)]
            # 执行命令
            output = subprocess.check_output(cmd, cwd=src_folder)
            # 保存到文件
            with open(os.path.join(dst_folder, '恢复结果', file_name+".txt"), 'wb') as f:
                f.write(output)
