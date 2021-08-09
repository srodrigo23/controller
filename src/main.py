from controller import Controller
from view.main_view import MainView

if __name__ == "__main__":
    num_cam = 4 #max 4
    cont = Controller(num_cam)
    view = MainView(cont)
    cont.set_view(view)
    view.mainloop()