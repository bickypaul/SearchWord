import operator 

word_count = {} 
words = []
with open('word_search.tsv') as f: 					#opening the tab sepearted value file
	for line in f:
		word, frequency = line.split('\t') 			#splitting it into word and occurence
		word_count[word] = int(frequency.strip())	#inserting into the wordcount dictionary key as word and value as frequency
		words.append(word)							#inserting only the word in words

#Search method to check the input(partial) word is present in any word of words list.
def search(incomplete_word):						
	results = []
	for word in words:
		if incomplete_word in word:
			results.append(word)
	return results

#This part sorts the words based on a match with the search keyword.
# 1. Matches at the start of a word ranks higher.
# 2. Common words (those with a higher usage count) ranks higher than rare words.
# 3. Short words ranks higher than long words.
# 4. An exact match always ranks as the first result.
def sort_results(results, incomplete_word):
	result_distances = [(result, result.find(incomplete_word), word_count[result], len(result)) for result in results]
	result_distances.sort(key=operator.itemgetter(1))
	result_distances.sort(key=operator.itemgetter(3))
	searchResults = [result_distance[0] for result_distance in result_distances][:25]
	return searchResults
