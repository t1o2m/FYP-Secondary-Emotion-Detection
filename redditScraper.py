import praw
import csv
import re

def format_string_list(string_list):
    new_string_list = []
    if len(string_list) > 0:
       
        for string in string_list:
            new_string = string.replace(',', '')
            new_string_list.append(new_string)
        new_string_list = list(filter(None,new_string_list)) 
        return new_string_list
    
    else: 
        return string_list    

reddit = praw.Reddit(client_id='XVyMfJI3msk0-g',
                    client_secret='ZGGcc0zAimZgQ8oDZwiwx-zogCo',
                    username='',
                    password='',
                    user_agent='fypscraperv1')

subreddit = reddit.subreddit('depression')
hot_dep = subreddit.hot(limit=30)
reddit_data_list = []
for submission in hot_dep:
    
    if not submission.stickied:    
        
        #Split selftext into a list prior assigning to data_list 
        text_body = submission.selftext
   
        sentences = re.split('\.|\?|!|\n',text_body)     
        sentences = format_string_list(sentences)
        
        reddit_data = {'id':submission.id, 'author':submission.name, 'text':sentences} 
        reddit_data_list.append(reddit_data)




#Getters for reddit data dicts
def get_id(r_data):
    return str(r_data['id'])

def get_author(r_data):
    return str(r_data['author'])

def get_text(r_data):
    return list(r_data['text'])

#Method for formatting list of strings (removing commas)

#csv writer with formatting
with open ('redditData.csv', 'w', newline='') as f:
    fieldnames = ['id','author','text']
    writer = csv.DictWriter(f, fieldnames = fieldnames)

    writer.writeheader()
    for reddit_data in reddit_data_list:
        
        reddit_id = get_id(reddit_data)
        reddit_author = get_author(reddit_data)
        reddit_sentence_list = get_text(reddit_data)
        
        #print("#######", reddit_sentence_list[1])

        for sentence in reddit_sentence_list:
            writer.writerow({'id': reddit_id, 'author': reddit_author, 'text':sentence} )

    
