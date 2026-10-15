import os
import sys

print("Python 版本:", sys.version)
print("Python 可执行文件:", sys.executable)
print("sys.prefix:", sys.prefix)
print("sys.base_prefix:", sys.base_prefix)

venv_path = os.environ.get("VIRTUAL_ENV")
if venv_path:
    print("虚拟环境路径:", venv_path)
elif sys.prefix != sys.base_prefix:
    print("虚拟环境路径:", sys.prefix)
else:
    print("虚拟环境路径: 未检测到虚拟环境（当前使用系统/全局 Python）")
