questions3=[
    
    {"id": 1,
      "prompt": "Take two numbers and print their sum.",
        "expects": {
            "requires_input": True,
            "input_type": int,
            "min_value": 2,

            "requires_collection": False,
            "collection_type": None,

            "requires_loop":False,
            "loop_type": None,

            "requires_operation":True,
            "operation_type": "Addition",

            "reqires_condition":False,
      
            "requires_print": True,

            "variable_flow": False,
            "min_variable": 2
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
         "expects": {
            "requires_input": True,
            "input_type": int,
            "min_value": 2,

            "requires_collection": False,
            "collection_type": None,

            "requires_loop":F,
            "loop_type": None,

            "requires_operation":True,
            "operation_type": "Subtraction",

            "reqires_condition":None,
      
            "requires_print": True,

            "variable_flow": False,
            "min_variable": 2
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
         "expects": {
            "requires_input": True,
            "input_type": int,
            "min_value": 2,

            "requires_collection": False,
            "collection_type": None,

            "requires_loop":None,
            "loop_type": None,

            "requires_operation":True,
            "operation_type": "Multiplication",

            "reqires_condition":None,
      
            "requires_print": True,

            "variable_flow": False,
            "min_variable": 2
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
         "expects": {
            "requires_input": True,
            "input_type": int,
            "min_value": 2,

            "requires_collection": False,
            "collection_type": None,

            "requires_loop":None,
            "loop_type": None,

            "requires_operation":True,
            "operation_type": "Division",

            "reqires_condition":None,
      
            "requires_print": True,

            "variable_flow": False,
            "min_variable": 2
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
         "expects": {
            "requires_input": True,
            "input_type": int,
            "min_value": 2,

            "requires_collection": False,
            "collection_type": None,

            "requires_loop":None,
            "loop_type": None,

            "requires_operation":True,
            "operation_type": "Modulus",

            "reqires_condition":None,
      
            "requires_print": True,

            "variable_flow": False,
            "min_variable": 2
       },
           "test_case":[
            {
              "input": [ "12","5"],
              "expected_output":"2",
            }
          ]
         }
    
  ]

