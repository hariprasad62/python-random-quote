"""This programme generates sentences by randomly picking up words"""
import random
def n() :
  n = ['dog', 'cat', 'poodle']
  return random.choice(n)
def det () :
  return random.choice(['a', 'the'])
def adj () :
  return random.choice(['small','white'])
def verb () :
    return random.choice(['saw','hit'])

for i in range(1, 50):
      np = (det() + ' ' + adj() + ' ' + n())
      vp = (verb() + ' ' + np)
      np = (det().capitalize() + ' ' + adj() + ' ' + n())
      s = np + ' ' + vp
      print (i, s)
