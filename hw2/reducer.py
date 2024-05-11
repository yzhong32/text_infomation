from collections import defaultdict
import sys

current_word = None
word_doc = {}

for line in sys.stdin:
    line = line.strip()

    word, count, docid = line.split()
    try:
        count = int(count)
        docid = int(docid)
    except ValueError:
        continue

    if current_word == word:
        word_doc[word][0] += count
        word_doc[word][1].add(docid)
    else:
        word_doc[word] = [count, {docid}]
        current_word = word

for k, v in word_doc.items():
    print(k + ': ' + str(v))