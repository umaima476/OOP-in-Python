class FlashCard:
    def __init__(self, word, meaning):
        self.word = word
        self.meaning = meaning

    def __str__(self):
        return self.word + '(' +self.meaning +')'    


flash = []
while(True):
    word = input("Enter the questioning word. ")
    meaning = input("Enter the meaning of that word. ")
    flash.append(FlashCard(word, meaning))
    option = int(input("Enter 0 to add another flashcard. "))

    if(option):
        break

print("Your Flashcards\n")
for i in flash:
    print(">",i)


