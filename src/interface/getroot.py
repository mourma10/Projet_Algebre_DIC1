try:
    from Tkinter import Tk
except ImportError:
    Tk = None
    print("veuillez installer python-tk : sudo apt-get install python-tk")

(dimx_, dimy_) = (800, 600)


def create_root():
    iam_root = Tk()
    iam_root.title("Projet Python DIC1")
    w_ = iam_root.winfo_screenwidth()
    h = iam_root.winfo_screenheight()
    x = w_ / 2 - dimx_ / 2
    y = h / 2 - dimy_ / 2
    iam_root.geometry("%dx%d+%d+%d" % ((dimx_, dimy_) + (x, y)))
    iam_root.resizable(False, False)
    return iam_root


root = create_root()
