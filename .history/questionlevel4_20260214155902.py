question4=[
    {
      "id": 1,
      "prompt": "Take 5 numbers and print only even numbers",

      "expects": {

        "requires_input": True,
        "input_type": int,

        "requires_collection": True,
        "collection_type": "list",

        "requires_loop": True,
        "loop_type": "for",

        "requires_condition": True,

        "requires_operation": True,
        "operation_type": "Modulus",

        "requires_print": True,

        "variable_flow": True,
        "min_variables": 2
     },
      "test_case":[
        {
         "input": ["1","2","3","4","5"],
         "expected_output": '["2", "4"]'
        }
        ]
  },
  {
      "id":2,
      "prompt": "Take 5 numbers and print only odd numbers",

      "expects":{
          "requires_input": True,
          "input_type": int,

          "requires_collection":True,
          "collection_type": "list" ,
    
          "requires_loop":True,
          "loop_type":"for",

          "requires_condition":True,

          "requires_operation":True,
          "operation_type": "Modulus",

          "requires_print": True,

          "variable_flow":True,
          "min_variables":2
      },
      "test_case": [
       {
        "input": ["1","2" ,"3","4","5"],
        "expected_output": '["1","3","5"]'
       } 
        ]

  },
  {
      "id": 3,
      "prompt": "Store 5 student names and  marks  and print their result in grade",

      "expects": {

        "requires_input": True,
        "input_type": [int,str],

        "requires_collection": True,
        "collection_type":  "dict" ,
       
        "requires_loop": True,
        "loop_type": "for",

        "requires_condition": True,

        "requires_operation": True,
        "operation_type": "Comparison",

        "requires_print": True,

        "variable_flow": True,
        "min_variables": 2
    },
    "test_case": [
       {
        "input": {
            "shruti" :60,
            "Deepak" :70,
            "Ashu"   :50,
            "Ram"    :35,
            "zara"   :80
            },
        "expected_output": '["C", "B", "D", "D" , "A"]'
       } 
        ]
  },
  {
      "id": 4,
      "prompt": "Take 10 numbers from user and print only unique values",

      "expects": {

        "requires_input": True,
        "input_type": int,

        "requires_collection": True,
        "collection_type": "set",
        
        "requires_loop": ,
        "loop_type": None,

        "requires_condition": False,

        "requires_operation": False,
        "operation_type": None,

        "requires_print": True,

        "variable_flow": True,
        "min_variables": 1
      },
    "test_case": [
       {
        "input":["1","1","2","3","3","4","55","66","66","88"],
        "expected_output": '{"1", "2", "3", "4", "55", "66", "88"}'
        } 
        ]
  },
  {
       "id": 5,
       "prompt": "Take day,month,and year from user and store them in a tuple called bob. print the tuple.",

       "expects": {

        "requires_input": True,
        "input_type": int,

        "requires_collection": True,
        "collection_type": "tuple",

        "requires_loop": False,
        "loop_type": None,

        "requires_condition": False,

        "requires_operation": False,
        "operation_type": None,

        "requires_print": True,

        "variable_flow": True,
        "min_variables": 1
    },
    "test_case": [
      {
        "input": ["15", "8", "2004"],
        "expected_output": '("15", "8", "2004")'
       }
 
      ]
  },
  
]