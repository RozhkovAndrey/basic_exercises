# Вывести последнюю букву в слове

word = 'Архангельск'
print(word[-1])


# Вывести количество букв "а" в слове
word = 'Архангельск'
print(word.lower().count('а'))
# ???


# Вывести количество гласных букв в слове
word = 'Архангельск'.lower()
def countVowels(string):
   vowels = ['а','е','и','о','у', 'ы', 'э', 'ю', 'я']
   total = 0
   for s in word:
      if s in vowels:
         total += 1
   return total

print(countVowels('Архангельск'))
# ???



# Вывести количество слов в предложении
sentence = 'Мы приехали в гости'
print(len(sentence.split()))
# ???


# Вывести первую букву каждого слова на отдельной строке

sentence = 'Мы приехали в гости'.split()
for word in sentence:
    print(word[0])
# ???


# Вывести усреднённую длину слова в предложении

sentence = 'Мы приехали в гости'
total = 0
sen = sentence.split()
for word in sen:
   total += len(word)
print(total/len(sen))
