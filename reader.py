import os
import tokenizer

filename = input("\033[92mDirectory of file (.dfs): \033[00m")
dirname = os.path.dirname(__file__)

if ".dfs" not in filename:
    filename = filename + ".dfs"

with open(os.path.join(dirname, filename), "r") as file:
    filecontents = file.read()
    tokenizer.tokenize(filecontents)
