def greet(lang):
    if lang == 'en':
        print('Hello!')
    elif lang == 'fr':
        print('Bonjour!')
    elif lang == 'es':
        print('Hola!')


inpt = int(input('\nSelect language to greet:\n1 - English\n2 - French\n3 - Spanish\n'))

if inpt == 1:
    greet('en')
elif inpt == 2:
    greet('fr')
elif inpt == 3:
    greet('es')
else:
    print('Select correct language.')
