print('Please enter a number and it\'ll rased to the power of 2')
print('Enter "stop" to stop')

while True:
 reply = input('Enter text:')
 if reply == 'stop': break
 try:
  num = float(reply)
 except:
  print('Bad!' * 8)
 else:
  print(num ** 2)
print('Bye')
