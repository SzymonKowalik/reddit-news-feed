import requests
from bs4 import BeautifulSoup
from datetime import datetime, timedelta
import threading


def read_file(filename):
    """Read and return the lines of a file as a list of strings.
    If the file does not exist, create it and return an empty list."""
    try:
        with open(f'./data/{filename}.txt' , 'r') as file:
            return [line.rstrip() for line in file]
    except FileNotFoundError:
        open(f'./data/{filename}.txt', 'w').close()
        return []


def create_header():
    """Create a header string for the current week."""
    date_today = datetime.now()
    date_7d_ago = date_today - timedelta(days=7)
    return f"Reddit top posts from {date_7d_ago:%d-%m-%Y} to {date_today:%d-%m-%Y}"


def get_subreddit_posts(subreddit):
    """Get the top 5 posts of a subreddit from the past week."""
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)'
    }

    print('Getting data...')
    response = requests.get(f'https://reddit.com/r/{subreddit}/top/?t=week', headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    elements = soup.find_all('a', href=True)
    post_links = []

    for elem in elements:
        if f'/r/{subreddit}/comments'.lower() in str(elem).lower():
            link = f"https://reddit.com{elem['href']}"
            title = elem.text
            if link not in (data[0] for data in post_links):
                post_links.append([link, title])
            if len(post_links) >= 5:
                break

    return post_links


def get_all_subreddit_posts(subreddits):
    """Get the top 5 posts of all given subreddits from the past week.
    This function retrieves the top 5 posts of each subreddit simultaneously using threads.
    Returns:a dictionary mapping subreddit names to lists of (url, title) tuples
    representing the top 5 posts of each subreddit"""
    all_posts = {subreddit: [] for subreddit in subreddits}

    # Get subreddit posts simultaneously
    def get_subreddit_posts_thread(subreddit):
        all_posts[subreddit] = get_subreddit_posts(subreddit)

    threads = []
    for subreddit in subreddits:
        thread = threading.Thread(target=get_subreddit_posts_thread, args=(subreddit,))
        thread.start()
        threads.append(thread)

    # Wait for all threads to finish
    for thread in threads:
        thread.join()

    return all_posts


def prepare_email_message(posts):
    """Create an HTML string representing the top 5 posts of each subreddit. Formatted for email body"""
    print('Preparing message...')
    text = f"<h2>{create_header()}</h2>\n"
    for subreddit, contents in posts.items():
        text += f"<h3>r/{subreddit}</h3>\n"
        text += f"<ol>\n"
        for post_data in contents:
            link, title = post_data
            text += f"<li><a href='{link}'>{title}</a></li>\n"
        text += f"</ol>\n"
    return text


def send_emails(server, message):
    """Send an email through the given server."""
    print('Sending emails...')
    for recipient in read_file('recipients'):
        server.sendmail('Reddit News Feed', recipient, message.as_string())


def data_for_email_sender():
    """Get the top 5 posts of all subreddits and create an HTML message."""
    posts = get_all_subreddit_posts(read_file('subreddits'))
    return prepare_email_message(posts)


def data_from_window_app():
    """Get the list of subreddit names and the top 5 posts of each subreddit."""
    subreddits = read_file('subreddits')
    return subreddits, get_all_subreddit_posts(subreddits)
