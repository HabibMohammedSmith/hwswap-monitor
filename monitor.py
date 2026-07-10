import praw
import yaml


def load_config():
    with open("config.yaml", "r") as file:
        return yaml.safe_load(file)


def contains_keyword(submission, keywords):
    text = (
        submission.title + " " +
        submission.selftext
    ).lower()

    return any(
        keyword.lower() in text
        for keyword in keywords
    )


def main():
    config = load_config()

    reddit = praw.Reddit(
        client_id=config["reddit"]["client_id"],
        client_secret=config["reddit"]["client_secret"],
        username=config["reddit"]["username"],
        password=config["reddit"]["password"],
        user_agent=config["reddit"]["user_agent"],
    )

    subreddit_name = config["monitor"]["subreddit"]

    subreddit = reddit.subreddit(subreddit_name)

    print(f"Monitoring r/{subreddit_name}...")

    for submission in subreddit.stream.submissions(
        skip_existing=True
    ):
        if contains_keyword(
            submission,
            config["monitor"]["keywords"]
        ):
            print("MATCH FOUND:")
            print(submission.title)
            print(submission.url)
            print("-" * 40)


if __name__ == "__main__":
    main()
