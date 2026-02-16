question5 =[
     {
       "id": 1,
       "prompt": "Take a list of numbers and write a function to return the second largest number.",
       "expects": {
       "requires_input": True,
       "requires_collection": True,
       "collection_type": "list",
       "requires_loop": True,
       "requires_condition": True,
       "requires_function": True,
       "function_must_return": True,
       "variable_flow": True,
       "min_variables": 2
      },
       "test_case": [
      {
         "input": "1 5 3 9 7",
         "expected_output": "7"
      }
        ]
    },
   {
      "id": 502,
      "prompt": "Write a function that takes a sentence and returns a dictionary of word frequencies.",
      "expects": {
          "requires_input": true,
          "requires_collection": true,
          "collection_type": "dict",
          "requires_loop": true,
          "requires_condition": true,
          "requires_function": true,
          "function_must_return": true,
          "variable_flow": true
        },
         "test_case": [
         {
           "input": "apple banana apple",
           "expected_output": "{'apple': 2, 'banana': 1}"
          }
      ]
 },
 {
  "id": 503,
  "prompt": "Write a function that takes student marks and returns grade (A,B,C,F).",
  "expects": {
    "requires_input": true,
    "requires_condition": true,
    "requires_function": true,
    "function_must_return": true,
    "variable_flow": true
  },
  "test_case": [
    {
      "input": "85",
      "expected_output": "'A'"
    }
   ]
  },
  {
  "id": 504,
  "prompt": "Create a menu-driven contact manager using while True and dictionary.",
  "expects": {
    "requires_collection": true,
    "collection_type": "dict",
    "requires_loop": true,
    "loop_type": "while",
    "requires_condition": true,
    "state_based": true,
    "variable_flow": true
  },
  "test_case": [
    {
      "input": ["1", "John", "12345", "4"],
      "expected_output": "Contact Added"
    }
   ]
 },
 {
  "id": 505,
  "prompt": "Write a function that takes multiple expense values and returns total expense.",
  "expects": {
    "requires_input": true,
    "requires_collection": true,
    "collection_type": "list",
    "requires_loop": true,
    "requires_function": true,
    "function_must_return": true,
    "requires_operation": true,
    "operation_type": "addition",
    "variable_flow": true
  },
  "test_case": [
    {
      "input": "100 200 50",
      "expected_output": "350"
    }
  ]
 }
]