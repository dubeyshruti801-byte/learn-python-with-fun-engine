questions=[
    {
        "id" : 1,
        "prompt": "Print your Name." ,
        "expected_output": "shruti" 
    },
     {
        "id" : 2,
        "prompt": "Print your family members name." ,
        "expected_output":
    },
     {
        "id" : 3,
        "prompt": "Print 5 fruits Name." ,
        "expected_output":
    }
     {
        "id" : 4,
        "prompt": "Print months of year ." ,
        "expected_output":
    }
     {
        "id" : 5,
        "prompt": "Print days of week." ,
        "expected_output":
    }
     
]
        
("1."))
      self.answer=input(print())
      self.answer=input(print())
      self.answer=input(print("4.))
      self.answer=input( print("5."))
      
      for item in self.answer:
         if self.answer.startswith("print()"):
            score += 2
         else:
            print("Wrong syntax ❌")
            score -= 1