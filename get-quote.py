import random

def primary():
  option = int(input("Options:\n 1. Print Random Quote\n 2. Add Quote\n Enter your option : "))
  
  if option == 1:
      quotes = quoteReader()
      max_num_of_quotes = len(quotes) - 1
      random_quote_index = random.randint(0, max_num_of_quotes)
      print(quotes[random_quote_index])
  else:
      quoteWriter()

def quoteWriter():
  quote = input("Enter your quote : ")
  f = open("quotes.txt", "a")
  f.write(quote + "\n")
  f.close


def quoteReader():
  f = open("quotes.txt")
  quotes = f.readlines()
  f.close()
  return quotes

if __name__ == "__main__":
    primary()
  
