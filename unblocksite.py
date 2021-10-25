import ctypes, sys
import os
def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False
if is_admin():
        site=sys.argv[1]
        path_to_hosts=os.path.join("C:",os.sep,"Windows","System32","Drivers","etc","hosts")
        with open(path_to_hosts, "r") as f:
            lines = f.readlines()
        with open(path_to_hosts, "w") as f:
            for line in lines:
                if site not in line.strip("\n") :
                    f.write(line)
else:
    # Re-run the program with admin rights
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)
