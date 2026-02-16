questions2= [
    {
        "id" : 1,                                                                                                        
        "prompt": "Take the given name from user, save it in variable a  and Print it- shruti" ,
        "expected_output": None,
        "expects": {
         "requires_input": True,
          "min_value": 1,
         "input_type": str,

         "requires_operation": False,
         "operation":  None,

         "requires_collection":False,
         "collection_type": list ,

         "requires_print": True
        }
   },
   {
        "id" : 2,
        "prompt": "Take 1-10 numbers from user , save it in variable 'num' and print it." ,
        "expected_output": None,
         "expects": {
            "requires_input": True,
            "input_type": int,
            "input_call": 1,
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
         }
       },

   {
        "id" : 3,
        "prompt": "Take 1-10 even numbers from user , save it in variable 'even' and print it." ,
        "expected_output": None,
        "expects": {
            "requires_input": True,
            "input_type": int,
            "input_call": 1,
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
        
       },
     {
     "id" : 4, 
        "prompt": "Take 1-10 odd numbers from user , save it in variable 'odd' and print it.",
        "expected_output": None,
    
        "expects": {
            "requires_input": True,
            "input_type": int,
            "input_call": 1,
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
     } ,
    {
        "id" : 5,
        "prompt": "take days of week from user, save it in 'week' and print it.",
        "expected_output": None,
        "expects": {
            "requires_input": True,
            "input_type": int,
            "input_call": 1,
            "min_value": 7,

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
     }
  ]

