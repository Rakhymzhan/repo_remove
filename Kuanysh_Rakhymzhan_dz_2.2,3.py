
sentence = ['в', str(5), 'часов', str(17), 'минут', 'температура', 'воздуха', 'была', '+' + str(+5), 'градусов']
print(sentence)
sentence.insert(1, '"')
sentence.insert(3, '"')
sentence.insert(5, '"')
sentence.insert(7, '"')
sentence.insert(12, '"')
sentence.insert(14, '"')
print(sentence)
new_sent = ' '.join(sentence)
print(new_sent)

digits = None
for el in sentence:
    if el.isdigit():
        digits = int(el)
        digits = '%02d' % digits
        new_sent = new_sent.replace(el, digits)

print(new_sent)









