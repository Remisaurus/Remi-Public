import re

def remove_chat_metadata(chat_export_file):
    date_time = r"(\d+\/\d+\/\d+,\s\d+:\d+)"  # e.g. "9/16/22, 06:34"
    dash_whitespace = r"\s-\s"  # " - "
    username = r"([\w\s]+)"  # e.g. "Martin"
    metadata_end = r":\s"  # ": "
    pattern = date_time + dash_whitespace + username + metadata_end

    with open(chat_export_file, "r", encoding='utf8') as corpus_file:
        content = corpus_file.read()
    cleaned_corpus = re.sub(pattern, "", content)
    return list(cleaned_corpus.split("\n"))

def remove_non_message_text(export_text_lines):
    messages = []
    filter_out_msgs = ['<Media omitted>', 'terry', 'Terry', 'TERRY', 'Yorick', 'yorick', 'YORICK', 'tomas', 'Tomas', 'TOMAS', 'Remi', 'remi', 'REMI', 'nigel', 'Nigel', 'NIGEL', 'Bart', 'bart', 'BART', 'Maarten', 'maarten', 'MAARTEN', 'martijn', 'Martijn', 'MARTIJN', 'baldwin', 'Baldwin', 'BALDWIN', 'joeri', 'Joeri', 'JOERI', 'Roel', 'roel', 'ROEL', 'Boris', 'dwayne', 'Lyr', 'Kara', 'Nanda', 'https://']
    for every in export_text_lines:
        x = 0
        for all in filter_out_msgs:
            if all in every:
                x += 1
        if x == 0:
            messages.append(every)
        else:
            continue
    return tuple((msg for msg in messages))

def clean_corpus(chat_export_file):
    message_corpus = remove_chat_metadata(chat_export_file)
    cleaned_corpus = remove_non_message_text(message_corpus)
    return cleaned_corpus
