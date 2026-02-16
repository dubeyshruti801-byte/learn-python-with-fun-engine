question4=[
    {
      "id": 1,
      "prompt": "Take 5 numbers and print only even numbers",

      "expects": {

        "requires_input": True,
        "input_type": int,
        "min_value":5,

        "requires_collection": True,
        "collection_type": "list" | "dict" | "tuple" | "set",

        "requires_loop": True,
        "loop_type": "for",

        "requires_condition": True,

        "requires_operation": True,
        "operation": "Modulus",

        "requires_print": True,

        "variable_flow": True,
        "min_variables": 2
     },
      "test_case":[
        {
         "input": [],
         "expected_output": "2,4"
        }
        ]
  },
  {
      "id":2,
      "prompt": "Take 5 numbers and print only odd numbers",

      "expects":{
          "requires_input": True,
          "input_type": int,
          "min_value": 5,

          "requires_collection":True,
          "collection_type": "list" | "dict" | "tuple" | "set",
          
          "requires_loop":True,
          "loop_type":"for",

          "requires_condition":True,

          "requires_operation":True,
          "operation_type": "Modulus",

          "requires_print": True,

          "requires_flow":True,
          "min_variable":2
      },
      "test_cases": [
       {
        "input": "1, 2, 3, 4, 5",
        "expected_output": "1,3,5"
       } 
        ]

  },
  {
      "id": 3,
      "prompt": "Take 5 students marks  and print their result in grade",

      "expects": {

        "requires_input": True,
        "input_type": int,
        "min_value":5,

        "requires_collection": True,
        "collection_type": "list" | "dict" | "tuple" | "set",

        "requires_loop": True,
        "loop_type": "for",

        "requires_condition": True,

        "requires_operation": True,
        "operation": "Comparison",

        "requires_print": True,

        "variable_flow": True,
        "min_variables": 2
    },
    "test_cases": [
       {
        "input": "60,70,50,35,80",
        "expected_output": "C, B, D, D, A "
       } 
        ]
    },
  {
      "id": 4,
      "prompt": "Take 5 salary of employees  and print who have highest , lowest , or average salary",

      "expects": {

        "requires_input": True,
        "input_type": int,
        "min_value":5,

        "requires_collection": True,
        "collection_type": "list" | "dict" | "tuple" | "set",

        "requires_loop": True,
        "loop_type": "for",

        "requires_condition": True,

        "requires_operation": True,
        "operation": "Comparison",

        "requires_print": True,

        "variable_flow": True,
        "min_variables": 2
    },
    "test_cases": [
       {
        "input": "20000 , 30000, 3000, 50000, 90000",
        "expected_output": "lowest, average, lowest, average, highest"
       } 
        ]
  },
  {
      "id": 5,
      "prompt": "Take 5 inputs of age by different citizens and print only who is eligible for vote.",

      "expects": {

        "requires_input": True,
        "input_type": int,
        "min_value":5,

        "requires_collection": True,
        "collection_type": "list" | "dict" | "tuple" | "set",

        "requires_loop": True,
        "loop_type": "for",

        "requires_condition": True,

        "requires_operation": True,
        "operation": "Comparison",

        "requires_print": True,

        "variable_flow": True,
        "min_variables": 2
    },
    "test_cases": [
       {
        "input": "10, 19, 33, 22, 56",
        "expected_output": "Not eligible for vote, eligible for vote, eligible for vote, eligible for vote, eligible for vote"
       } 
        ]
  },
  
]