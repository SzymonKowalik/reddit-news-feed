
# reddit-news-feed

This is a Python application that allows you to view the top 5 posts of any subreddit from the past week.

## Running the windowed application

1.  Clone the repository and install the required packages:

    ```
    git clone https://github.com/szymon-kowalik/reddit-top-posts
    cd reddit-top-posts
    pip install -r requirements.txt
    ```

2.  Run the application:

     `python main_app.pyw`
    
3. In the application window, select a subreddit from the dropdown menu to view its top 5 posts. You can click on a post title to open the post's webpage.


## Running email sender

1.  Set the environment variables `GMAIL_EMAIL` and `GMAIL_PASSWORD` to your Gmail email and password, respectively.
    
2.  Run the following command:

    `python email_sender.py`

This will email all recipients in the `recipients.txt` file with the top 5 posts of each subreddit from the past week. The email will be sent through your Gmail account.

## Customizing the application

You can customize the list of subreddits and recipients by editing the `subreddits.txt` and `recipients.txt` files, respectively. Add one subreddit or recipient per line.

## Requirements

-   The required packages are listed in `requirements.txt`.