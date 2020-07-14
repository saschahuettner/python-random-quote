def primary():
  # print("Keep it logically awesome.")
  import random

  f = open("quotes.txt")
  quotes = f.readlines()
  f.close()

  last = len(quotes) - 1
  rnd1 = random.randint(0, last)
  rnd2 = random.randint(0, last)
  while rnd2 == rnd1:
    rnd2 = random.randint(0, last)


  print(quotes[rnd1].replace("\n", ""))
  print(quotes[rnd2].replace("\n", ""))

if __name__== "__main__":
  primary()
