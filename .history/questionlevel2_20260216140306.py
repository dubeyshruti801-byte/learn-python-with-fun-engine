questions2= [
    {
        "id" : 1,                                                                                                        
        "prompt": "Take the given name from user, save it in variable a  and Print it- shruti" ,
        "instructions": [],
        "expects": {
            "requires_input": True,
            "coerce_output_to_string": True,
            "input_type": str,

            "requires_collection": False,
            "collection_type": None,

            "requires_loop":False,
            "loop_type": None,

            "requires_operation":False,
            "operation_type": None,

            "requires_condition":False,
      
            "requires_print": True,

            "variable_flow": False,
            "min_variables": 1
      },
          "test_case":[
            {
              "input": ["shruti"],
              "expected_output":"shruti",
            }
          ]
   },
   {
        "id" : 2,
        "prompt": "Take 1-10 numbers from user , save it in variable 'num' and print it." ,
        "instructions": [],
        "expects": {
            "requires_input": True,
            "coerce_output_to_string": True,
            "input_type": int,

            "requires_collection": True,
            "collection_type": "list",

            "requires_loop":False,
            "loop_type": None,

            "requires_operation":False,
            "operation_type": None,

            "requires_condition":False,
      
            "requires_print": True,

            "variable_flow": False,
            "min_variables": 1
       },
          "test_case":[
            {
              "input": ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"],
              "expected_output": '["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]',
            }
          ]
       },

   {
        "id" : 3,
        "prompt": "Take 1-10 even numbers from user , save it in variable 'even' and print it." ,
        "instructions": ["Take 5 integer inputs.",
                         "Store them in list named even.",
                         "Do NOT check if they are even (validation already ensures input)."],
        "expects": {
            "requires_input": True,
            "coerce_output_to_string": True,
            "input_type": int,

            "requires_collection": True,
            "collection_type": "list",

            "requires_loop":False,
            "loop_type": None,

            "requires_operation":False,
            "operation_type": None,

            "requires_condition":False,
      
            "requires_print": True,

            "variable_flow": False,
            "min_variables": 1
       },
           "test_case":[
            {
              "input":  ["2",  "4",  "6",  "8",  "10"],
              "expected_output":'["2",  "4",  "6",  "8",  "10"]',
            }
          ]
        
       },
     {
     "id" : 4, 
        "prompt": "Take 1-10 odd numbers from user , save it in variable 'odd' and print it.",
        "instructions": ["Take 5 integer inputs.",
                         "Store them in list odd.",
                         "No validation required.",
                         "No loop required.",
                         "Print the list."],
        "expects": {
            "requires_input": True,
            "coerce_output_to_string": True,
            "input_type": int,

            "requires_collection": True,
            "collection_type": "list",

            "requires_loop":False,
            "loop_type": None,

            "requires_operation":False,
            "operation_type": None,

            "requires_condition":False,
      
            "requires_print": True,

            "variable_flow": False,
            "min_variables": 1
       },
           "test_case":[
            {
              "input":  ["1", "3", "5", "7", "9"],
              "expected_output": '["1", "3", "5", "7", "9"]',
            }
          ]
     } ,
    {
        "id" : 5,
        "prompt": "take days of week from user, save it in 'week' and print it.",
        "instructions": ["Take 7 string inputs.",
                         "Store them in list week.",
                         "No loops.",
                         "Print the list."],
        "expects": {
            "requires_input": True,
            "coerce_output_to_string": True,
            "input_type": str,

            "requires_collection": True,
            "collection_type": "list",

            "requires_loop":False,
            "loop_type": None,

            "requires_operation":False,
            "operation_type": None,

            "requires_condition":False,
      
            "requires_print": True,

            "variable_flow": False,
            "min_variables": 1
       },
           "test_case":[
            {
              "input": ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"],
              "expected_output": ' ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]',

            }
          ]
     }
]

