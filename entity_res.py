from google import google
import nltk
from nltk.tag import StanfordNERTagger
import spacy

spacy_nlp = spacy.load('en')

entity = []
print("Enter Name : ")
n = input()
entity.append(n.lower())
print("Enter Location : ")
n = input()
entity.append(n.lower())
print("Enter Organization : ")
n = input()
entity.append(n.lower())
#print(entity)

print("Enter Query : ")
query = input()

found = 0

# Set the no. of pages of google results that are searched
num_page = 8 

# stanford_ner_tagger = StanfordNERTagger(
# 	'stanford_ner/' + 'classifiers/english.all.3class.distsim.crf.ser.gz',
# 	'stanford_ner/' + 'stanford-ner-3.9.2.jar'
# )
ctr = 0
results = []
search_results = google.search(query,num_page)
for res in search_results:
	ctr += 1
	desc = (res.description)
	document = spacy_nlp(desc)
	for element in document.ents:
		labels = ["PERSON","ORG","LOC"]
		if element.label_ in labels:
			# print('Type: %s, Value: %s' % (element.label_, element))
			checker = str(element).lower()
			if (str(element.label_) == "PERSON" and entity[0] == checker) or (str(element.label_) == "ORG" and entity[2] == checker) or (str(element.label_) == "LOC" and entity[1] == checker):
				results.append(res)
				found += 1


print("No. of occurences : %d" % (len(results)))
print("Links : ")
ctr = 1
for i in range(len(results)):
	j = i+1
	print("Result %d ----> %s" % (j,results[i].link))
	print()
	ctr += 1

















