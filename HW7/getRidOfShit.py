import os

ext = ["jpg", "png", "gif"]
filenames = [os.remove(filename) for filename in os.listdir(".") if filename.endswith(tuple(code for code in ext))]



