question4=[
    {
      "id": 1,
      "prompt": "Take 5 numbers and print only even numbers",
      "instructions": [],
      "expects": {

        "requires_input": True,
        "input_type": int,
        "input_mode": "multi_line",

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
      "instructions": ["Take 5 integers.",
                       "Store in list.",
                       "Use for loop.",
                       "Use condition num % 2 != 0.",
                       "Print list of odd numbers.",
                       ""],
      "expects":{
          "requires_input": True,
          "input_type": int,
          "input_mode": "multi_line",

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
      "instructions": ["Take 5 student names and marks,Store them in dictionary.",
                       "Use comparison operators.",
                       "Grade logic (suggested): 80+ → A, 70+ → B, 60+ → c, Below 60 → D",
                       "Print list of grades only.",
                       "Must use dictionary."],
      "expects": {

        "requires_input": True,
        "input_type": [int,str],
        "input_mode": "multi_line",

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
  #SPECIAL CASE -SET()
  {
      "id": 4,
      "prompt": "Take 10 numbers from user and print only unique values",
      "instructions": [",Take 10 integers.",
                       "Store them in a set.",
                       "Print the set.",
                       "No condition required.",
                       "Must use set collection."],
      "expects": {

        "requires_input": True,
        "input_type": int,
        "input_mode": "multi_line",

        "requires_collection": True,
        "collection_type": "set",
        
        "requires_loop": True,
        "loop_type": "for",

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
        "expected_output": '{1,2,3,4,55,66,88}'
        } 
        ]
  },
  {
       "id": 5,
       "prompt": "Take day,month,and year from user and store them in a tuple called bob. print the tuple.",
       "instructions": ["Take day, month, year as input.",
                        "Store in tuple named bob.",
                        "No loops required.",
                        "Print the tuple."],
       "expects": {

        "requires_input": True,
        "input_type": int,
        "input_mode": "multi_line",

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