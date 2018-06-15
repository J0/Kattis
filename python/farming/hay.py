inp = [int(x) for x in input().split()]
num_words = inp[0]
num_descriptions = inp[1]
dic = {}
for counter in range(num_words):
  wor = input().split()
  dic.update({wor[0]: int(wor[1])})

for other_counter in range(num_descriptions):
    value = 0
  
    while(True):
      other_inp = input()
      if other_inp == ".":
        break
      words_in_sentence = [y for y in other_inp.split()]
      for word in words_in_sentence:
        value += dic.get(word,0)
    print(value)
