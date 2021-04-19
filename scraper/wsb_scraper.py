import praw
import pandas as pd

reddit = praw.Reddit(
    client_id='8GqlhQidDbZ3Fg', 
    client_secret='O1VFTQwQSHPyP5c-91zO5uym3jOp3Q', 
    user_agent='wsb_scraper'
)

wsb = reddit.subreddit("wallstreetbets")

posts = []

recent_posts = wsb.new(limit=40)
for post in recent_posts:
     posts.append([post.title, post.score,post.num_comments])
posts = pd.DataFrame(posts,columns=['title', 'score', 'num_comments'])
print(posts)
posts.to_csv('WSB_recent_40_2.csv')