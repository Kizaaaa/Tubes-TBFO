import os
import argparse


def argParse() -> tuple[str, str]:
    parser = argparse.ArgumentParser()
    parser.add_argument("txt", type=str, help="txt file path")
    parser.add_argument("html", type=str, help="html file path")
    txtArg = parser.parse_args().txt
    htmlArg = parser.parse_args().html.replace("\"", "")

    if (txtArg == None or htmlArg == None):
        print("Argument kurang lengkap! Silahkan jalankan dengan format `python main.py file.txt \"html.txt\"`")
        exit()
    
    if not os.path.isfile(htmlArg):
        print("tidak ditemukan file html yang dimaksud")
        exit()
    
    return (txtArg, open(htmlArg, "r").read())