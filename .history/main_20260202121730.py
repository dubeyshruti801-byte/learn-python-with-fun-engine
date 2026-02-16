import  questionBank 
import keyword

class main():
   def __init__(self , questions, answer, score):
      
      self.answer= answer
      self.score= score

      print("Learn python with Fun 🚀")
      print (f"RULES:" \
      "you should not use eval() , exec ,or keywords" \
      "keywordd list: ",{keyword.kwlist})

      print("Game Started!!🎯")
      if self.answer == "eval()" or "exec":
          print("You are breaking the RULES , eval and exec are not allowed ❌")
      elif self.answer == keyword.kwlist:
            print("You are breaking the RULES , KEYWORDS are not allowed ❌")
            
         

