def count_frequency(wordlist):
	wordDict={}
	for item in wordlist:
		if item in wordDict.keys():
			count=wordDict[item]
			count=count+1
			wordDict[item]=count
		else:
			wordDict[item]=1
	return wordDict

if __name__=="__main__":
	mylist=["one","two","eleven","one","three","two","eleven","three","seven","eleven"]
	print(count_frequency(mylist))