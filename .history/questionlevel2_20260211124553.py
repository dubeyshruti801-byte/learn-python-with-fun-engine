questions2= [
    {
        "id" : 1,                                                                                                        
        "prompt": "Take the given name from user, save it in variable a  and Print it- shruti" ,
         "expects": {
            "requires_input": True,
            "input_type": str,
            "min_value": 1,

            "requires_collection": False,
            "collection_type": None,

            "requires_loop":None,
            "loop_type": None,

            "requires_operation":None,
            "operation_type": None,

            "reqires_condition":None,
      
            "requires_print": True,

            "variable_flow": False,
            "min_variable": 1
      },
          "test_case":[
            {
              "input": None,
              "expected_output":None,
            }
          ]
   },
   {
        "id" : 2,
        "prompt": "Take 1-10 numbers from user , save it in variable 'num' and print it." ,
         "expects": {
            "requires_input": True,
            "input_type": int,
            "min_value": 10,

            "requires_collection": True,
            "collection_type": "list",

            "requires_loop":None,
            "loop_type": None,

            "requires_operation":None,
            "operation_type": None,

            "reqires_condition":None,
      
            "requires_print": True,

            "variable_flow": False,
            "min_variable": 1
       },
          "test_case":[
            {
              "input": None,
              "expected_output":None,
            }
          ]
       },

   {
        "id" : 3,
        "prompt": "Take 1-10 even numbers from user , save it in variable 'even' and print it." ,
        "expects": {
            "requires_input": True,
            "input_type": int,
            "min_value": 10,

            "requires_collection": True,
            "collection_type": "list",

            "requires_loop":None,
            "loop_type": None,

            "requires_operation":None,
            "operation_type": None,

            "reqires_condition":False
      
            "requires_print": True,

            "variable_flow": False,
            "min_variable": 1
       },
           "test_case":[
            {
              "input": None,
              "expected_output":None,
            }
          ]
        
       },
     {
     "id" : 4, 
        "prompt": "Take 1-10 odd numbers from user , save it in variable 'odd' and print it.",
        "expects": {
            "requires_input": True,
            "input_type": int,
            "min_value": 10,

            "requires_collection": True,
            "collection_type": "list",

            "requires_loop":False,
            "loop_type": None,

            "requires_operation":False,
            "operation_type": None,

            "reqires_condition":False,
      
            "requires_print": True,

            "variable_flow": False,
            "min_variable": 1
       },
           "test_case":[
            {
              "input": None,
              "expected_output":None,
            }
          ]
     } ,
    {
        "id" : 5,
        "prompt": "take days of week from user, save it in 'week' and print it.",
        "expects": {
            "requires_input": True,
            "input_type": int,
            "min_value": 7,

            "requires_collection": True,
            "collection_type": "list",

            "requires_loop":False,
            "loop_type": None,

            "requires_operation":False,
            "operation_type": None,

            "reqires_condition":False,
      
            "requires_print": True,

            "variable_flow": False,
            "min_variable": 1
       },
           "test_case":[
            {
              "input": None,
              "expected_output":None,
            }
          ]
     }
  ]

