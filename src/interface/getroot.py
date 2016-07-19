try:
    from Tkinter import Tk
except ImportError:
    Tk = None
    print("veuillez installer python-tk : sudo apt-get install python-tk")
from Tkinter import Canvas

(dimx_, dimy_) = (850, 600)


def main_root():
    iam_root = Tk()
    iam_root.title("Projet Python DIC1")
    w_ = iam_root.winfo_screenwidth()
    h = iam_root.winfo_screenheight()
    x = w_ / 2 - dimx_ / 2
    y = h / 2 - dimy_ / 2
    iam_root.geometry("%dx%d+%d+%d" % ((dimx_, dimy_) + (x, y)))
    iam_root.resizable(False, False)
    return iam_root


def root_operation(n, title):
    root_op = Tk()
    canvas = Canvas(root_op, width=200 * n - 100, height=100 * n - 50, bg="#cdd")
    w_ = root_op.winfo_screenwidth()
    h = root_op.winfo_screenheight()
    x = w_ / 2 - (200 * n - 100) / 2
    y = h / 2 - (100 * n - 50) / 2
    root_op.title(title)
    root_op.geometry("%dx%d+%d+%d" % ((200 * n - 100, 100 * n - 50) + (x, y)))
    root_op.resizable(False, False)
    return root_op, canvas


root = main_root()
