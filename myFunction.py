def hello():
    print("hello Dianna")
    print("how are you?")

def hello1(name):
    print(f"hello {name}")
    print("how are you?")

def command(cmd):
    import os
    os.system(cmd)

command('ls')