questions3=[
    
    {"id": 1,
      "prompt": "Take two numbers and print their sum.",
       "expects": {
            "requires_input": True,
            "input_count": 2,
            "input_type": int,

            "requires_operation": True,
            "operation": "add" ,

            "requires_collection":False,
            "collection_type": None,

            "requires_split": True or False,

            "requires_print": True
        }
  
    },
      
   {
        "id" : 2,
        "prompt": "Take two numbers 8 and 3 as A and B and print their subtraction" ,
         "expects": {
            "requires_input": True,
            "input_count": 2,
            "input_type": int,

            "requires_operation": True,
            "operation": "sub",

            "requires_collection":False,
            "collection_type":  None,

            "requires_split": True or False,

            "requires_print": True
        }
    },

      {
        "id" : 3,
        "prompt": "Take two numbers 3 and 5 as A and B and print their Multiplication." ,
         "expects": {
            "requires_input": True,
            "input_count": 2,
            "input_type": int,

            "requires_operation": True,
            "operation": "mul",

            "requires_collection":False,
            "collection_type":  None,

            "requires_split": True or False,

            "requires_print": True
        }
      },
   {
        "id" : 4, 
        "prompt": "Take two numbers 10 and 5 as A and B and print their Division",
         "expects": {
            "requires_input": True,
            "input_count": 2,
            "input_type": int,

            "requires_operation": True,
            "operation": "div" ,

            "requires_collection":False,
            "collection_type":  None,

            "requires_split": True or False,

            "requires_print": True
        }
    } ,
   {
        "id" : 5,
        "prompt": "Take two numbers 12 and 5 as A and B and print their Modulus",
            "expects": {
            "requires_input": True,
            "min_value": 2,
            "input_type": int,

            "requires_operation": True,
            "operation": "mod" ,

            "requires_collection":False,
            "collection_type":  None,

            "requires_split": True or False,

            "requires_print": True
        }
         }
    
  ]

