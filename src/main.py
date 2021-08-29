from controller import Controller
from view.main_view import MainView

def run():
    cont = Controller()
    view = MainView(cont)
    cont.set_view(view)
    view.mainloop()

if __name__ == "__main__":
    run()