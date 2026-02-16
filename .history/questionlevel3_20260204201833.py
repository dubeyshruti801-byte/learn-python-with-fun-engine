questions2= [
    {
        "id" : 1,
        "prompt": "Take two numbers 3 and 5 as A and B and print their addition." ,
        "expected_output": {
              "inputs":[],
              "variables":{
                    "A" :int,
                    "B" :int
              },
              "symbol": "+",
              "printed_output": "A+B"
        }
   },
   {
        "id" : 2,
        "prompt": "Take two numbers A and B and print their subtraction" ,
        "expected_output": {
              "input_prompt": "Enter the value of A and B:",
              "variables": {
                 "A" :int,
                 "B" :int
                },
                "symbol": "-",
               "printed_output": "A-B"
       }
    },

   {
        "id" : 3,
        "prompt": "Take two numbers A and B and print their Multiplication." ,
        "expected_output": {
              "input_prompt": "Enter the value of A and B:",
              "variables": {
                 "A" :int,
                 "B" :int
                },
              "symbol": "*",
              "printed_output": "A*B"
       }
   },
   {
        "id" : 4, 
        "prompt": "Take two numbers A and B and print their Division",
        "expected_output": {
              "input_prompt": "Enter the value of A and B:",
              "variables": {
                 "A" :int,
                 "B" :int
                },
             "symbol": "/",
             "printed_output": "A/B"
       }
     } ,
    {
        "id" : 5,
        "prompt": "Take two numbers A and B and print their Modulus",
        "expected_output": {
              "input_prompt": "Enter the value of A and B:",
              "variables": {
                 "A" :int,
                 "B" :int
              }
             "printed_output": "A%B"
     }
    }
  ]