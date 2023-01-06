import customtkinter as ctk
import webbrowser


class RightPanel(ctk.CTkFrame):
    """This class represents a panel containing buttons for displaying data."""
    def __init__(self, root, posts_data=[]):
        """Args:
        - root: the parent widget of the RightPanel instance
        - posts_data: a list of (url, title) tuples representing the data to be displayed
        """
        super().__init__(master=root, fg_color='transparent')
        self.generate_buttons(posts_data)

    def generate_buttons(self, posts_data):
        """Generate buttons for each post in posts_data.
        If data is empty - display message"""
        if not posts_data:
            ctk.CTkLabel(self, text='There was an issue retrieving the data.', text_color='red', font=('Arial', 18)).pack()

        for i, post_data in enumerate(posts_data, 1):
            url, title = post_data
            # Truncate the title if it's too long
            if len(title) > 100:
                title = f'{title[:95]}...'
            btn = DisplayData(self, title, url)
            btn.grid(row=i, column=0, padx=10, pady=10)


class DisplayData(ctk.CTkFrame):
    """This class represents a button for displaying data.
    The button displays the title of a post. When clicked, the button opens
    the corresponding URL in a web browser."""
    def __init__(self, root, title, url):
        super().__init__(master=root)
        self.url = url
        ctk.CTkButton(self, text=f"{title:<100}", command=self.open_webpage, width=110, height=40, font=('Consolas', 14)).pack()

    def open_webpage(self):
        """Open the URL of the post in a web browser."""
        webbrowser.open(self.url)
