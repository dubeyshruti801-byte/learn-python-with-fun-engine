questions=[
    {
        "id" :
    }
]
        
("1.Print your Name."))
      self.answer=input(print("2.Print your family members name."))
      self.answer=input(print("3.Print 5 fruits Name."))
      self.answer=input(print("4.Print months of year ."))
      self.answer=input( print("5.Print days of week."))
      
      for item in self.answer:
         if self.answer.startswith("print()"):
            score += 2
         else:
            print("Wrong syntax ❌")
            score -= 1