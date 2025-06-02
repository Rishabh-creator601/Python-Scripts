from collections import Counter

'''

counts the values of list 

'''


words = [
 'look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes',
 'the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not', 'around', 'the',
 'eyes', "don't", 'look', 'around', 'the', 'eyes', 'look', 'into',
 'my', 'eyes', "you're", 'under'
]


c = Counter(words)

print(c.keys())  # items 
print(c.values()) # count of that items 
print(c.most_common())


#adding similar items or updating it 


print("-"*50)
print("eyes count : "  ,  c['eyes'])
c.update(['eyes','the','eyes'])
print("eyes count : "  ,  c['eyes'])