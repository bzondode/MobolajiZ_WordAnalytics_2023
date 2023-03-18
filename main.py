# This function returns the entirety of "Dracula" as a string
def readBook():
  f = open("dracula.txt", "r")
  s = f.read().replace("-", " ")
  f.close()
  return ''.join(c for c in s if c.isalnum() or c == " ")

# Create a variable to hold the story of Dracula
draculaText = readBook()

# Split the text into words using the split() method
words = draculaText.lower().split()

# How many unique four-letter words are in the book
fourLetterWords = []
for word in words:
  if(len(word)) == 4:
    fourLetterWords.append(word)
numOfFourLetterWords = len(fourLetterWords)

# Find the most common word
wordCounts = {}
for word in words:
  if(word in wordCounts):
    wordCounts[word] += 1
  else:
    wordCounts[word] = 1

mostCommonWord = max(wordCounts, key=wordCounts.get)
mostCommonWordCount = wordCounts[mostCommonWord]
    
# Find every word that shows up more 500 times and how many times that word shows up throughout the book
words_appearing_500_times = [(word, count) for word, count in wordCounts.items() if count >= 500]

# Print the results
print("=== Results ===")
print()
print(f"'{mostCommonWord}' is the word that appears the most throughout the text, a total of {mostCommonWordCount} times")
print()
print(f"There are {numOfFourLetterWords} words that are four letters long")
print()
print("I noticed that these Words show up ten or more times:")
for word in words_appearing_500_times:
  print(word)
