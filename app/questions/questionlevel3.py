questions3=[
    
    {"id": 1,
      "prompt": "Take two numbers and print their sum.",
      "instruction": ["Take two integers using input() (multi-line).",
                       "Store in 2 variables.",
                       "Perform Addition (+).",
                       "Print result.",
                       "No loop, no condition.",
                       "Minimum 2 variables required."],
      "expects": {
            "requires_input": True,
            "input_type": int,
            "input_mode": "multi_line",

            "requires_collection": False,
            "collection_type": None,

            "requires_loop":False,
            "loop_type": None,

            "requires_operation":True,
            "operation_type": "Addition",

            "requires_condition":False,
      
            "requires_print": True,

            "variable_flow": False,
            "min_variables": 2
       },
           "test_case":[
            {
              "input": ["2","4"],
              "expected_output":"6",
            }
          ]
    },
      
   {
        "id" : 2,
        "prompt": "Take two numbers  A and B and print their subtraction" ,
        "instruction": ["Take 2 integers.",
                         "Subtract B from A",
                         "Print result.",
                         "Use - operator.",
                         "No loops."],
        "expects": {
            "requires_input": True,
            "input_type": int,
            "input_mode": "multi_line",

            "requires_collection": False,
            "collection_type": None,

            "requires_loop":False,
            "loop_type": None,

            "requires_operation":True,
            "operation_type": "Subtraction",

            "requires_condition":False,
      
            "requires_print": True,

            "variable_flow": False,
            "min_variables": 2
       },
           "test_case":[
            {
              "input": ["4","2"],
              "expected_output":"2",
            }
          ]
    },

      {
        "id" : 3,
        "prompt": "Take two numbers A and B and print their Multiplication." ,
        "instruction": ["Take 2 integers.",
                         "Multiply using * .",
                         "Print result.",
                         "No loop."],
        "expects": {
            "requires_input": True,
            "input_type": int,
            "input_mode": "multi_line",

            "requires_collection": False,
            "collection_type": None,

            "requires_loop":False,
            "loop_type": None,

            "requires_operation":True,
            "operation_type": "Multiplication",

            "requires_condition":False,
      
            "requires_print": True,

            "variable_flow": False,
            "min_variables": 2
       },
           "test_case":[
            {
              "input": ["2","4"],
              "expected_output":"8",
            }
          ]
      },
   {
        "id" : 4, 
        "prompt": "Take two numbers  A and B and print their Division",
        "instruction": ["Take 2 integers.",
                         "Divide A by B using /.",
                         "Print result.",
                         "No loops.",
                         "Must use modulus operator"],
        "expects": {
            "requires_input": True,
            "input_type": int,
            "input_mode": "multi_line",

            "requires_collection": False,
            "collection_type": None,

            "requires_loop":False,
            "loop_type": None,

            "requires_operation":True,
            "operation_type": "Division",

            "requires_condition":False,
      
            "requires_print": True,

            "variable_flow": False,
            "min_variables": 2
       },
           "test_case":[
            {
              "input": ["10", "5"],
              "expected_output":"2",
            }
          ]
    } ,
   {
        "id" : 5,
        "prompt": "Take two numbers  A and B and print their Modulus",
        "instruction": ["Take 2 integers.",
                         "Print remainder using %.",
                         "No loops.",
                         "Must use modulus operator."],
        "expects": {
            "requires_input": True,
            "input_type": int,
            "input_mode": "multi_line",

            "requires_collection": False,
            "collection_type": None,

            "requires_loop":False,
            "loop_type": None,

            "requires_operation":True,
            "operation_type": "Modulus",

            "requires_condition":False,
      
            "requires_print": True,

            "variable_flow": False,
            "min_variables": 2
       },
           "test_case":[
            {
              "input": [ "12","5"],
              "expected_output":"2",
            }
          ]
         }
    
  ]

