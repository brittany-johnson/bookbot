def get_book_text(path):
    with open(path) as f:
      return f.read()

def get_num_of_words(text):
   return len(text.split())


def dictionary_to_list(dictionary):
  new_list = []
  for key in dictionary:
     if key.isalpha():
      new_list.append({"alpha": key, "num": dictionary[key]})
  return new_list


def get_num_of_letters(text):
  letter_count = {}
  for char in text:
      lower_char = char.lower()
      if char in letter_count:
        letter_count[lower_char] += 1
      else:
         letter_count[lower_char] = 1
  return letter_count

def sort_on(dict):
   return dict["num"]

def main():
  book_path = "books/frankenstein.txt"
  file_contents = get_book_text(book_path)
  num_of_words = get_num_of_words(file_contents)
  num_of_letters = get_num_of_letters(file_contents)
  list_of_char_count = dictionary_to_list(num_of_letters)

  list_of_char_count.sort(key=sort_on)

  print(f"--- Begin report of {book_path} ---")
  print(f"{num_of_words} found in document")

  for dic in list_of_char_count:
     print(f"The '{dic["alpha"]}' character was found {dic["num"]} times ")

  print("--- End report ---")



main()


