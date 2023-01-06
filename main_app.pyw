import customtkinter as ctk
from utils.application import App
from utils.functions import data_from_window_app


def main():
    """Run the Reddit top posts window application."""
    ctk.set_appearance_mode("dark")
    app = App(*data_from_window_app())
    app.mainloop()


if __name__ == '__main__':
    main()
