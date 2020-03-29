import module_for_task030_1 as f_helpers
import module_for_task030_2 as str_helpers

fulltext = f_helpers.get_text('alice.txt',750)
clean_text = str_helpers.clean_whitespaces(fulltext).lower()
no_punc_txt = str_helpers.remove_punctuation(clean_text)

words = no_punc_txt.split()
final_words = str_helpers.remove_words(words)

unique_words = str_helpers.get_words_freq(final_words).keys()
clusters_freq = str_helpers.get_clusters_freq(unique_words)

keys = sorted(clusters_freq.keys())
for key in keys:
    print(key, clusters_freq[key])
