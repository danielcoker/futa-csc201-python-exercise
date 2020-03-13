# Write a program that sum all numeric values in a sentence 
# (-Sample Sentence: 3 eggs in 2 baskets. The output will be 5.)

sentence = input('Enter a sentence with numeric values: ')

sentence_list = sentence.split(' ')

numeric_total = 0

for word in sentence_list:
  if word.isdigit():
    numeric_total += int(word)

print(numeric_total)