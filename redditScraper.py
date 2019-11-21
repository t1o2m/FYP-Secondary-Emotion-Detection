import praw
import csv
import re
import reddit_tools

tools = reddit_tools

reddit = praw.Reddit(client_id='XVyMfJI3msk0-g',
                    client_secret='ZGGcc0zAimZgQ8oDZwiwx-zogCo',
                    username='AwkwardDragonfruit1',
                    password='548AJimpGKvRFrF',
                    user_agent='fypscraperv1')
subreddit = reddit.subreddit('depression')
hot_dep = subreddit.hot(limit=30)
reddit_data_list = []


for submission in hot_dep:
    if not submission.stickied:    
        
        #Split selftext into a list prior assigning to data_list 
        text_body = submission.selftext
        
        sentences = re.split('\.|\?|!|\n',text_body)
        sentences = tools.format_string_list(sentences)
        
        reddit_data = {'id':submission.id, 'author':submission.name, 'text':sentences} 
        reddit_data_list.append(reddit_data)


#csv writer with formatting
with open ('redditData.csv', 'w', newline='') as f:
    fieldnames = ['id','author','text']
    writer = csv.DictWriter(f, fieldnames = fieldnames)

    writer.writeheader()
    for reddit_data in reddit_data_list:
        
        reddit_id = tools.get_value_tostring(reddit_data, 'id')
        reddit_author = tools.get_value_tostring(reddit_data, 'author')
        reddit_sentence_list = tools.get_value_tolist(reddit_data, 'text')
        
        for sentence in reddit_sentence_list:
            writer.writerow({'id': reddit_id, 'author': reddit_author, 'text':sentence} )

    
