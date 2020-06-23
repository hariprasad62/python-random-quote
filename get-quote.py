def primary():
  #print("Keep it logically awesome.")

  f = open("quotes.txt")
  quotes = f.readlines()
  f.close()

  print(quotes[1], quotes[3], quotes[5])

  f1 = open("quotes1.txt",'w')
  for i in quotes:
    f1.write(i)
  f1.close()

if __name__== "__main__":
  primary()
