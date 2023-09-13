
path = f"logs/class_logs.txt"

def create_log(message:str):
    with open(path, mode="a") as f:
            f.write(message + "\n")
