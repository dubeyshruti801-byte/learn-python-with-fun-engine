import  questionBank 
import keyword

def main():
      answer 
      score= 0

      print("Learn python with Fun 🚀")
      print (f"RULES:" \
      "you should not use eval() , exec ,or keywords" \
      "keywordd list: ",{keyword.kwlist})
      questions= questions ()

      print("Game Started!!🎯")
      if answer == "eval()" or "exec":
          print("You are breaking the RULES , eval and exec are not allowed ❌")
      elif answer == keyword.kwlist:
            print("You are breaking the RULES , KEYWORDS are not allowed ❌")
      print(f"Score of a player: {score}")
            
         

if __name__ == "__main__":
    main()