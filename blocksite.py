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
        with open(path_to_hosts,"a") as hsts:
            line="\n0.0.0.0       "+site
            hsts.write(line)

        with open(path_to_hosts,"r") as res:
            lines=res.readlines()
            for ln in lines:
                print(ln)   # Code of your program here
else:
    # Re-run the program with admin rights
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)
