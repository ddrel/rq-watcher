import shutil

def movefile(source,destination):
    shutil.move(source, destination)
    return "success"