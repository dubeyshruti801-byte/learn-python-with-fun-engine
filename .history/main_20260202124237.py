from questionBank import questions
import keyword

def main():
      answer = questions,
      score= 0
      
      print("Learn python with Fun 🚀")
      print ("RULES:" \
      "you should not use eval() , exec ,or keywords" \
      "keywordd list: ")
      print(keyword.kwlist)
      while True:
        print("Game Started!!🎯")
        if answer == "eval()" or "exec":
          print("You are breaking the RULES , eval and exec are not allowed ❌")
        elif answer == keyword.kwlist:
            print("You are breaking the RULES , KEYWORDS are not allowed ❌")
        print(f"Score of a player: {score}")
        exi
            
         

if __name__ == "__main__":
    main()