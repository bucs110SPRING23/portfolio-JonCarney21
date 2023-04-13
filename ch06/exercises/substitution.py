import json

# Open the news.txt and subs.json files
with open("news.txt", "r") as news_file, open("subs.json", "r") as subs_file:

    # Read the entire news.txt file
    article = news_file.read()

    # Load the substitutions from the subs.json file
    subs = json.load(subs_file)

    # Make the substitutions in the article string
    for old_word, new_word in subs.items():
        article = article.replace(old_word, new_word)

    # Write the updated article to a new file called betternews.txt
    with open("betternews.txt", "w") as output_file:
        output_file.write(article)

# Close the files
news_file.close()
subs_file.close()
output_file.close()
