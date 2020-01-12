import module_for_task025_1 as read
import module_for_task025_2 as string
# to find a file in another directory: directory.filename

text = read.get_text('alice_for_019task.txt', 710)

cleaned_text = string.clean_whitespaces(text)

sentences = string.get_sentences(cleaned_text)
print(sentences)