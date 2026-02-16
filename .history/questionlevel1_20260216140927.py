questions1=[
    {
          "id": 1,
          "prompt": "Print your name: shruti",
          "instructions": [],
          "expects": {
            "requires_input": False,
            "coerce_output_to_string": True,
            "input_type": None,

            "requires_collection": False,
            "collection_type": None,

            "requires_loop":False,
            "loop_type": None,

            "requires_operation":False,
            "operation_type": None,

            "requires_condition":False,
      
            "requires_print": True,

            "variable_flow": False,
            "min_variables": None
          },
          "test_case":[
            {
              "input": None,
              "expected_output":"shruti"
            }
          ]
     },
   {
        "id" : 2,
        "prompt": "Print these names-Deepak Priya Dimple" ,
        "instructions": [],
        "expects": {
            "requires_input": False,
            "coerce_output_to_string": True,
            "input_type": None,

            "requires_collection": False,
            "collection_type": None,

            "requires_loop":False,
            "loop_type": None,

            "requires_operation":False,
            "operation_type": None,

            "requires_condition":False,
      
            "requires_print": True,

            "variable_flow": False,
            "min_variables": None
          },
          "test_case":[
            {
              "input": None,
              "expected_output": '["Deepak", "Priya", "Dimple"]'
            }
          ]
   },
   {
        "id" : 3,
        "prompt": "Print 5 fruits Name-Apple Banana Mango Orange Grapes" ,
        "instructions": [],
        "expects": {
            "requires_input": False,
            "coerce_output_to_string": True,
            "input_type": None,

            "requires_collection": False,
            "collection_type": None,

            "requires_loop":False,
            "loop_type": None,

            "requires_operation":False,
            "operation_type": None,

            "requires_condition":False,
      
            "requires_print": True,

            "variable_flow": False,
            "min_variables": None
          },
          "test_case":[
              {
              "input": None,
              "expected_output": '["Apple", "Banana", "Mango", "Orange", "Grapes"]'
              }
            ]
   },
   {
        "id" : 4,
        "prompt": "Print months of year-January February March April May June July August September October November December" ,
        "instructions": [],
        "expects": {
            "requires_input": False,
            "coerce_output_to_string": True,
            "input_type": None,
            
            "requires_collection": False,
            "collection_type": None,

            "requires_loop":False,
            "loop_type": None,

            "requires_operation":False,
            "operation_type": None,

            "requires_condition":False,
      
            "requires_print": True,

            "variable_flow": False,
            "min_variables": None
          },
          "test_case":[
            {
              "input": None,
              "expected_output": '["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]'
              }
          ]
          
   },
   {
        "id" : 5,
        "prompt": "Print days of week-Monday Tuesday Wednesday Thursday Friday Saturday Sunday",
        "instructions": ["Do NOT use input().",
                         "Print days in list format.",
                         "Must match:'["Monday, ..., "Sunday"]'",
                         "Use print() only.",
                         "No loops or operations."],
        "expects": {
            "requires_input": False,
            "coerce_output_to_string": True,
            "input_type": None,

            "requires_collection": False,
            "collection_type": None,

            "requires_loop":False,
            "loop_type": None,

            "requires_operation":False,
            "operation_type": None,

            "requires_condition":False,
      
            "requires_print": True,

            "variable_flow": False,
            "min_variables": None
          },
          "test_case":[
            {
              "input": None,
              "expected_output": '["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]'
            }
          ]
          
   }
     
  ]
