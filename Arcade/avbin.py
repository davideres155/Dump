from distutils.sysconfig import get_python_lib
site_pkg_path = get_python_lib()
if appveyor:
    if is64bit:
        path = "D:\Desktop\Python\Python3.7/lib/site-packages/arcade/Win64/avbin"
    else:
        path = "D:\Desktop\Python\Python3.7/lib/site-packages/arcade/Win32/avbin"

else:
    if is64bit:
        path = os.path.join(site_pkg_path, r"D:\Desktop\Python\Python3.7/lib/site-packages/arcade/Win64/avbin")
    else:
        path = os.path.join(site_pkg_path, r"D:\Desktop\Python\Python3.7/lib/site-packages/arcade/Win32/avbin")
