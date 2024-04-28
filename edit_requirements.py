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
                and "mdurl" not in line \
                and "blinker" not in line \
                and "absl-py" not in line \
                and "google-pasta" not in line \
                and "grpcio" not in line \
                and "itsdangerous" not in line \
                and "click" not in line \
                and "h5py" not in line \
                and "six" not in line \
                and "astunparse" not in line \
                and "flatbuffers" not in line \
                and "tensorboard-data-server" not in line \
                and "pygments" not in line \
                and "certifi" not in line \
                and "charset-normalizer" not in line \
                and "idna" not in line \
                and "urllib3" not in line:
            f.write(line)
