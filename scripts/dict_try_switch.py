branch = {'spam': 1.25,
       'ham': 1.99,
       'eggs': 0.99,
       'bacon': 1.10}

def choice():
    inp = input('Enter your choice: ')
    try:
      print(branch[inp])
    except KeyError:
      print('Bad choice.')
      print('You should select from: {}'.format(list(branch.keys())))
      choice()

choice()

