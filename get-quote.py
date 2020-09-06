import random

def primary():
  # print("Keep it logically awesome.")

  f = open("quotes.txt")
  quotes = f.readlines()
  f.close()

  max_num_of_quotes = len(quotes) - 1
  random_quote_index = random.randint(0, max_num_of_quotes)
  print(quotes[random_quote_index])

if __name__ == "__main__":
    primary()
  
