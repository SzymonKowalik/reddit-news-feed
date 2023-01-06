import customtkinter as ctk
from utils.functions import create_header
from utils.application_widgets import RightPanel


class App(ctk.CTk):
    """This class represents the main application window.
    It contains a dropdown menu for choosing a subreddit, and a panel for displaying
    the posts of the chosen subreddit."""
    def __init__(self, subreddits, posts):
        """Args:
        - subreddits: a list of subreddit names
        - posts: a dictionary mapping subreddit names to lists of (url, title) tuples
        """
        super().__init__()
        self.posts = posts
        self.geometry('1000x380')
        self.title(create_header())
        # Create the header label
        ctk.CTkLabel(self, text=create_header(), font=('Arial', 19), width=110, height=40).grid(row=0, column=1, sticky='w')
        # Create the "Choose subreddit" label
        ctk.CTkLabel(self, text='Choose subreddit').grid(row=0, column=0, padx=10, pady=10)
        # Create the subreddit dropdown menu
        self.option_menu = ctk.CTkOptionMenu(self, values=subreddits, command=self.list_posts)
        self.option_menu.grid(row=1, column=0, padx=10, pady=10, sticky='n')
        # Create the right panel for displaying posts
        self.right_panel = RightPanel(self)

    def list_posts(self, choice):
        """Populate the right panel with buttons for the chosen subreddit."""
        posts_data = self.posts[choice]
        self.right_panel.destroy()
        self.right_panel = RightPanel(self, posts_data)
        self.right_panel.grid(row=1, column=1, rowspan=2)