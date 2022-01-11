

# simluating the situation where i import core in other projects
import sys
# sys.path.append("/home/alexzander/Alexzander__/programming/dev/python3_core")
# adding to sys path because when you import a package
# python will add the full path to the package root into the sys path; and im doing the same thing, but just manually

from _core.aesthetics import warning
warning("asdasdasd")


from _core._rich import *
error("asdasdasd")



