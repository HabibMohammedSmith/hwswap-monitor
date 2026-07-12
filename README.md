# hwswap-monitor

A personal Python application that monitors Reddit's r/hardwareswap subreddit for hardware-related keywords and sends notifications when matching posts appear.


## Privacy and Usage

This application is:

- **Read-only**
- Non-commercial
- Intended for personal use only
- Not a posting, voting, moderation, or messaging bot
- Not used to redistribute Reddit content

The application only monitors publicly available submissions and sends notifications to the owner of the application.

The application is intended to reduce repetitive manual checking of new subreddit posts by notifying the user when relevant listings appear.


## Purpose

This project is a personal-use notification tool. It helps me discover relevant hardware listings more quickly by monitoring new subreddit submissions and alerting me when posts match my configured interests.


## Features

- Monitors new submissions in r/hardwareswap
- Searches post titles and bodies for user-configurable keywords
- Sends notifications for matching posts
- Uses Reddit's official API through PRAW
- Runs locally on a personal Linux machine


## Status

Early development. API access approval pending.


## Reddit API Usage

This application uses Reddit's Data API through the PRAW Python library.

API usage is limited to:
- Reading new submissions from r/hardwareswap
- Following notification, the application directs the user back to the original Reddit submission.
- Matching posts against user-configured keywords
- Sending notifications to the application owner

**The application does NOT**:
- Submit posts or comments
- Vote
- Send messages
- Moderate content
- Access private communities
- Share or redistribute Reddit data
