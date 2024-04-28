with open("requirements.txt", "r") as f:
    lines = f.readlines()

with open("requirements.txt", "w") as f:
    for line in lines:
        if "libclang" not in line \
                and "ml-dtypes" not in line \
                and "optree" not in line \
                and "markdown" not in line \
                and "markdown-it-py" not in line \
                and "namex" not in line \
                and "packaging" not in line \
                and "pillow" not in line \
                and "protobuf" not in line \
                and "rich" not in line \
                and "termcolor" not in line \
                and "typing-extensions" not in line \
                and "werkzeug" not in line \
                and "mdurl" not in line:
            f.write(line)
