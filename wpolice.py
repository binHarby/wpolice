#!usr/bin/env python
import ctypes, sys
import os
import platform
os_type=platform.system().lower()
def block(pathh,site):
    with open(pathh,"a") as hsts:
        line="\n0.0.0.0       "+site
        hsts.write(line)
def unblock(pathh,site):
    with open(pathh, "r") as f:
        lines = f.readlines()
    with open(pathh, "w") as f:
        for line in lines:
            if site not in line.strip("\n") :
                f.write(line)
def logic(pathh):
    arg1=sys.argv[1]
    site=sys.argv[2]
    if(arg1=="-b"):
        block(pathh,site)
    elif(arg1=="-u"):
        unblock(pathh,site)
    else:
        print("Erorr: please use appropriate flags")
        sys.exit(1)

if(os_type=="windows"):
    def is_admin():
        try:
            return ctypes.windll.shell32.IsUserAnAdmin()
        except:
            return False
    if is_admin():
            path_to_hosts=os.path.join("C:",os.sep,"Windows","System32","Drivers","etc","hosts")
            logic(path_to_hosts)
    else:
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)
else:
    path_to_hosts="/etc/hosts"
    logic(path_to_hosts)