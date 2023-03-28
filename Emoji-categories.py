# This program takes a gzip json file and counts the tweets and counts the emoji's per category



import json
import gzip
import re
import os

def process_file(file_path):
    texts = []
    with gzip.open(file_path, 'rt', encoding='utf8') as input:
        for line in input:
            text = json.loads(line)['text']
            if not text.startswith("RT"):
                texts.append(text)

    return texts

directory = "directory" # Change this to the directory containing your .gz files

texts = []

for file in os.listdir(directory):
    if file.endswith(".gz"):
        file_path = os.path.join(directory, file)
        texts.extend(process_file(file_path))

total_count = len(texts)

smileys_emotion_count = sum(1 for text in texts if re.search(u"[\U0001F600-\U0001F64F]", text))
people_body_count = sum(1 for text in texts if re.search(u"[\U0001F463-\U0001F4FF\U0001F9B0-\U0001F9FF]", text))
component_count = sum(1 for text in texts if re.search(u"[\U0001F3FB-\U0001F3FF]", text))
animals_nature_count = sum(1 for text in texts if re.search(u"[\U0001F400-\U0001F43E\U0001F980-\U0001F997]", text))
food_drink_count = sum(1 for text in texts if re.search(u"[\U0001F32D-\U0001F37F]", text))
travel_places_count = sum(1 for text in texts if re.search(u"[\U0001F680-\U0001F6FF]", text))
activities_count = sum(1 for text in texts if re.search(u"[\U0001F3A0-\U0001F3CA\U0001F3E0-\U0001F3F0\U0001F8F0-\U0001F8FF\U0001F9D0-\U0001F9FF]", text))
objects_count = sum(1 for text in texts if re.search(u"[\U0001F4A0-\U0001F4FF\U0001F6E0-\U0001F6EC]", text))
symbols_count = sum(1 for text in texts if re.search(u"[\U0001F300-\U0001F5FF]", text))
flags_count = sum(1 for text in texts if re.search(u"[\U0001F1E0-\U0001F1FF]", text))

print(f"Total Tweets: {total_count}")
print(f"Smileys & Emotion count: {smileys_emotion_count}")
print(f"People & Body count: {people_body_count}")
print(f"Component count: {component_count}")
print(f"Animals & Nature count: {animals_nature_count}")
print(f"Food & Drink count: {food_drink_count}")
print(f"Travel & Places count: {travel_places_count}")
print(f"Activities count: {activities_count}")
print(f"Objects count: {objects_count}")
print(f"Symbols count: {symbols_count}")
print(f"Flags count: {flags_count}")
