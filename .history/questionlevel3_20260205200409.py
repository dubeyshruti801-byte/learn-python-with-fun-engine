questions2=[
    {
       
      "id": 1,
      "prompt": "Take two numbers and print their sum.",
      "expects": {
      "requires_input": True,
      "min_inputs": 2,
      "input_type": int,
      "operation": "add",
      "requires_print": True
  }
    },
      
   {
        "id" : 2,
        "prompt": "Take two numbers 8 and 3 A and B and print their subtraction" ,
        "expected_output": {
              "inputs": ["8 3"],
              "variables": {
                 "A" :int,
                 "B" :int
                },
               "printed_output": 5
        }
    },

   {
        "id" : 3,
        "prompt": "Take two numbers 3 and 5 as A and B and print their Multiplication." ,
        "expected_output": {
              "inputs": ["3 5"],
              "variables": {
                 "A" :int,
                 "B" :int
                },
              "printed_output": 15
        }
   },
   {
        "id" : 4, 
        "prompt": "Take two numbers 10 and 5 as A and B and print their Division",
        "expected_output": {
              "inputs": ["10 5"],
              "variables": {
                 "A" :int,
                 "B" :int
                },
             "printed_output": 2
        }
    } ,
   {
        "id" : 5,
        "prompt": "Take two numbers 12 and 5 as A and B and print their Modulus",
        "expected_output": {
              "inputs": ["12 5"],
              "variables": {
                 "A" :int,
                 "B" :int
              },
             "printed_output": 2
            }
    }
  ]

