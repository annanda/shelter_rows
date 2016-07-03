# coding: utf-8

from __future__ import division
import rows

table_3 = rows.import_from_csv('../0cleaning/clean_data.csv')

cats = filter(lambda r: r.animaltype == "Cat", table_3)
dogs = filter(lambda r: r.animaltype == "Dog", table_3)

def filter_string(substrings, string):
    for substring in substrings:
        string = string.replace(substring, "")
    return string

##############################################
# Colors
##############################################

##############################################
# Colors - Cats
##############################################

# cat_colors = set([cat.color for cat in cats])

# print(len(cat_colors)) # 146

# know_colors = 'Blue Cream Lilac White Brown Gray Black Tan Flame Orange Buff Apricot Chocolate Smoke Yellow Pink Silver'.split()
# know_patterns = 'Tabby Tortie Torbie Point Tiger Agouti Calico'.split()
# know_names_in_cat_colors = 'Tricolor Seal Lynx'.split() + know_colors + know_patterns

# # for color in cat_colors:
# #     print filter_string(know_names_in_cat_colors, color)
    
# colors = []
# for color in cat_colors:
#     colors += color.split('/')

# print(len(set(colors))) # 41

# for color in sorted(set(colors)):
#     print(color)
    
# for color in sorted(set(cat_colors)):
#     if 'Seam' in color:
#         print('>', color) 

# Leia isso: http://img00.deviantart.net/d82c/i/2015/114/7/3/cat_color_chart_by_paintbean-d5c0dou.jpg

# tabby == Agouti == Tiger é um gato com listras! 
# https://en.wikipedia.org/wiki/Tabby_cat 
# http://www.paws-and-effect.com/what-color-is-my-tabby-cat/

# Tricolors http://www.delightibles.com/calicos-torties-and-torbies-need-to-know-about-tricolor-cats/
# tortie é um gato com patches de cor: https://en.wikipedia.org/wiki/Tortoiseshell_cat
# calico é um gato tricolor com muito branco https://en.wikipedia.org/wiki/Calico_cat
# torbies (??) tortie + tabby

# Point https://en.wikipedia.org/wiki/Point_coloration

# Lynx é quando é um tabby com point http://fixnation.org/2010/07/what-color-is-that-cat/

# Seal point é especifico http://pets.thenest.com/seal-point-cat-mean-10861.html

# cream/buff/Lilac é um gato amarelo claro
# orange
# Red == Flame
# tan
# brown
# chocolate

# white

# gray
# silver
# smoke
# blue é um gato tão cinza que acaba sendo azul

# black

# União de cores proximas
# uma coluna para cor e outra para padrão
# Single/Bi/Tricolor
# Pink ????
# Exemplos de dados estranhos

##############################################
# Colors - Dogs
##############################################

dog_colors = set(map(lambda r: r.color, dogs))

print len(dog_colors) # 262

know_colors = 'Pink Ruddy Fawn Liver Smoke Orange Apricot Yellow White Brown Silver Black Cream Gold Grey Red Blue Buff Tan Chocolate Gray'.split()
know_patterns = 'Merle Brindle Sable Tiger Tick'.split()
know_names_in_dog_colors = 'Tabby Tricolor'.split() + know_colors + know_patterns

for color in dog_colors:
    print filter_string(know_names_in_dog_colors, color)

colors = []
for color in dog_colors:
    colors += color.split('/')

colors = sorted(set(colors))

for color in colors:
    print color

# Liver(Fígado) é um cor. Também conhecida como Chocolate
# http://www.caninest.com/dog-coat-patterns/

# Tiger dogs são pintados O.o https://pethelpful.com/dogs/11-Dogs-that-look-like-Lion-Leopard-Tiger-Panda-andother-wild-animals
# Pode estar querendo dizer "Brindle: A mixture of black with brown, tan, or gold; usually in a "tiger stripe" pattern." https://en.wikipedia.org/wiki/Coat_(dog)#Patterns
# Tick é um tipo de parasita. Não. Quer dizer pontilhado!
# Black/Tricolor zueragem né?
# Pink também. 
# Tabby??? (só um tabby)

##############################################
# Breeds
##############################################

##############################################
# Breeds - Cats
##############################################

# cat_breeds = set([cat.breed for cat in cats])

# print len(cat_breeds) # 60

# resumed_breeds = []

# for breed in cat_breeds:
#     clean_breed = breed.replace('Mix', '')
#     resumed_breeds += [breed.strip() for breed in clean_breed.split('/')]

# cat_breeds = set(resumed_breeds)

# print len(cat_breeds) # 34

# for breed in cat_breeds:
#     print(breed)

# breeds = ""
# for breed in cat_breeds:
#     breeds += '"' + breed + '"' + ', '
    
# print(breeds)

##############################################
# Breeds - Dogs
##############################################

# dog_breeds = set([dog.breed for dog in dogs])

# print len(dog_breeds) # 1320

# resumed_breeds = []

# for breed in dog_breeds:
#     clean_breed = breed.replace('Mix', '')
#     resumed_breeds += [breed.strip() for breed in clean_breed.split('/')]

# dog_breeds = set(resumed_breeds)

# print len(dog_breeds) # 191

# for breed in sorted(dog_breeds):
#     print breed

# #s =''
# #for breed in dog_breeds:
# #    s += '"' + breed + '",'
# #print s