# This program takes a json as gzip and counts the tweets, tweets containing emojis and verage number of emojis in Tweets containing emojis
import json
import gzip
import re
import os

def count_emojis(text):
    emoji_pattern = re.compile("["
        u"\U0001F600-\U0001F64F"  # emoticons
        u"\U0001F300-\U0001F5FF"  # symbols & pictographs
        u"\U0001F680-\U0001F6FF"  # transport & map symbols
        u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                           "]+", flags=re.UNICODE)
    return len(emoji_pattern.findall(text))

def process_file(file_path):
    texts = []
    with gzip.open(file_path, 'rt', encoding='utf8') as input:
        for line in input:
            text = json.loads(line)['text']
            if not text.startswith("RT"):
                texts.append(text)

    return texts

directory = r"directory"  # Change this to the directory containing your .gz files

texts = []

for file in os.listdir(directory):
    if file.endswith(".gz"):
        file_path = os.path.join(directory, file)
        texts.extend(process_file(file_path))

total_count = len(texts)
emoji_count = sum(1 for text in texts if count_emojis(text) > 0)
total_emojis = sum(count_emojis(text) for text in texts)

emoticon_count = sum(1 for text in texts if re.search(u"[\U0001F600-\U0001F64F]", text))
symbol_pictograph_count = sum(1 for text in texts if re.search(u"[\U0001F300-\U0001F5FF]", text))
transport_map_count = sum(1 for text in texts if re.search(u"[\U0001F680-\U0001F6FF]", text))
flag_count = sum(1 for text in texts if re.search(u"[\U0001F1E0-\U0001F1FF]", text))

average_emojis = total_emojis / emoji_count if emoji_count > 0 else 0
emoji_ratio = emoji_count / total_count if total_count > 0 else 0

print(f"Total Tweets: {total_count}")
print(f"Tweets containing emojis: {emoji_count}")
print(f"Average number of emojis in Tweets containing emojis: {average_emojis}")
print(f"Percentage of tweets containing emoji's: {emoji_ratio*100}%")
