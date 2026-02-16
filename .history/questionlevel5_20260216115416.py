question5 =[
     {
       "id": 1,
       "prompt": "Take a list of numbers and write a function to return the second largest number.",
       "instructions": ["Take numbers in single line input",
                        "Convert to list.",
                        "Write a function.",
                        "Must return value (not just print).",
                        "Use loop and condition.",
                        "Do not use built-in sorted() shortcut.",
                        "Return second largest number."],
       "expects": {
       "requires_input": True,
       "input_mode": "single_line",
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
      "id": 2,
      "prompt": "Write a function that takes a sentence and returns a dictionary of word frequencies.",
      "instructions": ["Take sentence input.",
                       "Split into words.",
                       "Use dictionary.",
                       "Use loop.",
                       "Use condition to count.",
                       "Return dictionary.",
                       "Must use function."],
      "expects": {
          "requires_input": True,
          "input_mode": "single_line",
          "requires_collection": True,
          "collection_type": "dict",
          "requires_loop": True,
          "requires_condition": True,
          "requires_function": True,
          "function_must_return": True,
          "variable_flow": True
        },
      "test_case": [
         {
           "input": "apple banana apple",
           "expected_output": "{'apple': 2, 'banana': 1}"
          }
        ]
    },
    {
         "id": 3,
         "prompt": "Write a function that takes student marks and returns grade (A,B,C,F).",
         "instructions": ["Take marks as input.",

                          "Write function that returns grade:",

                          "90+ → A, 75+ → B, 60+ → C, Below 60 → F",

                          "Must return value.",

                          "Must use condition."],
         "expects": {
          "requires_input": True,
          "input_mode": "single_line",
          "requires_condition": True,
          "requires_function": True,
          "function_must_return": True,
          "variable_flow": True
        },
      "test_case": [
         {
           "input": "85",
           "expected_output": "'A'"
         }
         ]
    },
    {
         "id": 4,
         "prompt": "Create a menu-driven contact manager using while True and dictionary.",
         "instructions": ["Create dictionary to store contacts.",
                          "Use while True loop.",
                          "Show menu: Add, View, Delete, Exit",
                          "Use condition for choices.",

                          "Must maintain state.",


                        ],
         "expects": {
             "requires_input": True,
             "input_mode": "multi_line",
             "requires_collection": True,
             "collection_type": "dict",
             "requires_loop": True,
             "loop_type": "while",
             "requires_condition": True,
             "state_based": True,
             "variable_flow": True
             },
           "test_case": [
            {
              "input": ["1", "John", "12345", "4"],
              "expected_output": "Contact Added"
             }
         ]
    },
   {
           "id": 5,
           "prompt": "Write a function that takes multiple expense values and returns total expense.",
           "instructions": [],
           "expects": {
              "requires_input": True,
              "input_mode": "single_line",
              "requires_collection": True,
              "collection_type": "list",
              "requires_loop": True,
              "requires_function": True,
              "function_must_return": True,
              "requires_operation": True,
              "operation_type": "addition",
              "variable_flow": True
             },
         "test_case": [
           {
              "input": "100 200 50",
              "expected_output": "350"
           }
       ]
    }
 ]