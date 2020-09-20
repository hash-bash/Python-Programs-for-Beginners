import wordcloud
from matplotlib import pyplot as plt


def calculate_frequencies(file_contents):
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    uninteresting_words = ["the", "a", "to", "if", "is", "it", "of", "and", "or", "an", "as", "i", "me", "my",
                           "we", "our", "ours", "you", "your", "yours", "he", "she", "him", "his", "her", "hers", "its",
                           "they", "them", "their", "what", "which", "who", "whom", "this", "that", "am", "are", "was",
                           "were", "be", "been", "being", "have", "has", "had", "do", "does", "did", "but", "at", "by",
                           "with", "from", "here", "when", "where", "how", "all", "any", "both", "each", "few", "more",
                           "some", "such", "no", "nor", "too", "very", "can", "will", "just"]
    non_punctuation_text = ""

    for char in file_contents:
        if char not in punctuations:
            non_punctuation_text = non_punctuation_text + char
    words = non_punctuation_text.split()
    clean_words = []
    frequencies = {}
    for word in words:
        if word.isalpha():
            if word not in uninteresting_words:
                clean_words.append(word)
    for alpha_word in clean_words:
        if alpha_word not in frequencies:
            frequencies[alpha_word] = 1
        else:
            frequencies[alpha_word] += 1
    cloud = wordcloud.WordCloud()
    cloud.generate_from_frequencies(frequencies)
    return cloud.to_array()


myimage = calculate_frequencies(
    "The Ford GT is a mid-engine two-seater sports car manufactured and marketed by American automobile manufacturer "
    "Ford for the 2005 model year in conjunction with the company's 2003 centenary. The second generation Ford GT "
    "became available for the 2017 model year.[1] The GT recalls Ford's historically significant GT40, a consecutive "
    "four-time winner of the 24 Hours of Le Mans (1966–1969), including a 1-2-3 finish in 1966.")
plt.imshow(myimage, interpolation='nearest')
plt.axis('off')
plt.show()
