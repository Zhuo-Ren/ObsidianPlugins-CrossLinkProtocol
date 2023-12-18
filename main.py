import argparse
import os
import re
import subprocess
import urllib.parse
import traceback
import time


try:
    # argument parse and get protocol string
    parser1 = argparse.ArgumentParser(description='player协议')
    parser1.description = 'player协议'
    parser1.add_argument("parg1", type=str, help='对第一个位置参数的说明')
    args = parser1.parse_args()
    protocol_str = args.parg1
    protocol_str = urllib.parse.unquote(protocol_str)  # url字符转义

    # check protocol title
    protocol_name = "cl"
    if protocol_str[:len(protocol_name)+3] != r"cl://":
        raise RuntimeError("protocol title is not 'cl://' !")
    else:
        protocol_str = protocol_str[len(protocol_name)+3:]

    # analysis 
    number = re.match("[^/]*", protocol_str).group()
    print(f"number: {number}")
    try:
        kind = protocol_str[len(number)+1:]
    except:
        kind = ""
    print(f"kind: {kind}")

    # 
    if kind == "def":
        command = f'explorer "obsidian://search?vault=Note&query=/{number}(?!\/def)/"'
    else:
        command = f'explorer "obsidian://search?vault=Note&query={number}/def"'
    print(f"command:{command}")
    subprocess.Popen(command)  # run(command) os.popen(command) os.system(command)
    os.system("exit")  # 如果要调试，就注释掉这一句
    # time.sleep(5)
except Exception:
    traceback.print_exc()
    input()