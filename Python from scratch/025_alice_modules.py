import module_for_task025_1 as read # to find a file in another directory: directory.filename
import module_for_task025_2 as string
import matplotlib.pyplot as plt


text = read.get_text('alice.txt', 710)

cleaned_text = string.clean_whitespaces(text)

sentences = string.get_sentences(cleaned_text)

trimmed_sentences = string.trim_sentences(sentences)

very_long = 0 # >= 30 words
long = 0 # >= 20
medium = 0 # >= 10
short = 0 # >= 5
very_short = 0 # < 5

for sentence in trimmed_sentences:
    count = string.get_word_count(sentence)
    if count >= 30:
        very_long += 1
    elif count >= 20:
        long += 1
    elif count >= 10:
        medium += 1
    elif count >= 5:
        short += 1
    else:
        very_short += 1

x_values = ["very short", "short", "medium", "long", "very long"]
y_values = [very_short, short, medium, long, very_long]

fig, ax = plt.subplots()
plt.title('The distribution of sentence types \n by word count', fontsize=18)
plt.xlabel('Sentence length', color="grey")
plt.ylabel('Number of sentences', color="grey")
plt.bar(x_values, y_values, color="darkgrey")
plt.xticks(x_values, ("very short", "short", "medium", "long", "very long"))
plt.plot(x_values, y_values, color="darkred")
plt.show()

plt.show()