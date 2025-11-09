import os
import string
from collections import defaultdict, Counter

# build
def build_inverted_index(folder_path):
    index = defaultdict(list)
    for filename in os.listdir(folder_path):
        if filename.endswith(".txt"):
            with open(os.path.join(folder_path, filename), "r", encoding="utf-8") as f:
                text = f.read().lower()
                text = text.translate(str.maketrans('', '', string.punctuation))
                words = text.split()
                for word in set(words):
                    index[word].append(filename)
    return index

# search
def search_query(index, query):
    query_words = query.lower().split()
    results = Counter()
    for word in query_words:
        for doc in index.get(word, []):
            results[doc] += 1
    return results.most_common()

# running
if __name__ == "__main__":
    folder = "docs"
    inverted_index = build_inverted_index(folder)
    print(" Built successfully!")

    while True:
        query = input("\nEnter your query (or 'exit' to quit): ")
        if query.lower() == "exit":
            break
        results = search_query(inverted_index, query)
        if results:
            print(" Relevant documents:")
            for doc, score in results:
                print(f"{doc} (score: {score})")
        else:
            print("No results found.")
