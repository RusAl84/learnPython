from subprocess import Popen

while True:
    filename=".\\learnPython\\api\\send_data_cheets.py"
    print("\nStarting " + filename)
    p1 = Popen("python " + filename, shell=True)
    p2 = Popen("python " + filename, shell=True)
    p3 = Popen("python " + filename, shell=True)
    p4 = Popen("python " + filename, shell=True)
    p5 = Popen("python " + filename, shell=True)
    p6 = Popen("python " + filename, shell=True)
    p1.wait()
    # p2.wait()
    # p3.wait()