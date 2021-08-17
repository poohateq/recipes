from pprint import pprint

string = "Składniki: makaron  boczek  cukinia  1 łyżka masła  około 4 łyżek tartego parmezanu SOS  2 żółtka  1"  \
         "pełna łyżka serka mascarpone (lub 3 łyżki gęstej śmietany) LOL  1 łyżka miękkiego masła  1 łyżka oliwy extra vergine" \
         "  + Makaron carbonara z cukinią   Przepis z: www.kwestiasmaku.com  Makaron ugotować al dente w osolonej wodzie. " \
         "Boczek pokroić w kostkę. Podsmażyć na patelni mieszając od czasu do czasu przez kilka minut aż będzie lekko " \
         "zrumieniony. Dodać cukinię startą na dużych oczkach tarki oraz 1 łyżkę masła, smażyć na dużym ogniu mieszając " \
         "od czasu do czasu przez około 3 minuty aż cukinia będzie miękka. Doprawić solą i świeżo zmielonym pieprzem. " \
         "Wymieszać składniki sosu: żółtka, mascarpone, masło i oliwa extra vergine. Odcedzony makaron razem z kilkoma " \
         "łyżkami wody z makaronu włożyć na patelnię z cukinią, wlać sos i wszystko razem wymieszać. Odstawić z ognia. " \
         "Na koniec dodać tarty parmezan.  Wskazówki Żółtka tworzące sos powinny pozostać w miarę płynne, nie mogą się " \
         "całkowicie ściąć.   Wszystkie przepisy  " \
         "Część 1 120https://www.kwestiasmaku.com/pasta/makaron_z_cukinia/makaron_z_cukinia_boczkiem_carbonara/przepis.html"

s = string.split('Składniki: ', 1)[1].split('+', 1)[0]
s = s.split('  ')
s = [x for x in s if x]

index = 0
s_index = 0

ingredients = {'main': []}

section_index = {}

for words in s:
    if ' ' in words:
        word = words.split()

        for w in word:
            if w.isupper():
                next_section = False
                ingredient_section = w
                word.remove(ingredient_section)
                word = ' '.join(word)
                s[index] = word

                if not ingredients.get('main'):
                    ingredients['main'] = s[:index + 1]
                ingredients[ingredient_section] = s[index + 1:]
                if ingredients.get(ingredient_section):
                    for section_word in ingredients.get(ingredient_section):
                        if next_section:
                            del ingredients.get(ingredient_section)[s_index:]
                        section_word = section_word.split()
                        for s_w in section_word:
                            if s_w.isupper():
                                section_word.remove(s_w)
                                next_section = True
                                section_word = ' '.join(section_word)
                                ingredients.get(ingredient_section)[s_index] = section_word
                        s_index += 1
    index += 1

print(s)
print(ingredients)
