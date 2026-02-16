questions2= [
    {
        "id" : 1,                                                                                                        
        "prompt": "Take the given name from user, save it in variable a  and Print it- shruti" ,
        "expects": {
         "requires_input": True,
         "input_count": 1,
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
        "expects": {
          "requires_input": True,
          : 10,
          "input_type": int,

          "requires_operation": False,
          "operation":  None,

          "requires_collection": True,
          "collection_type": list,

          "requires_print": True
           }

       },

   {
        "id" : 3,
        "prompt": "Take 1-10 even numbers from user , save it in variable 'even' and print it." ,
        "expects": {
         "requires_input": True,
          "min_value": 10,
         "input_type": int,

         "requires_operation":False,
         "operation":  None,

         "requires_collection": True,
         "collection_type":  list ,

         "requires_split": True,

         "requires_print": True
        }
       },
     {
     "id" : 4, 
        "prompt": "Take 1-10 odd numbers from user , save it in variable 'odd' and print it.",
        "expects": {
         "requires_input": True,
         "min_value": 10,
         "input_type": int,

         "requires_operation": False,
         "operation":  None,

         "requires_collection": True,
         "collection_type": list ,

         "requires_split": True,

         "requires_print": True
        }
     } ,
    {
        "id" : 5,
        "prompt": "take days of week from user, save it in 'week' and print it.",
       "expects": {
         "requires_input": True,
         "min_value": 7,
         "input_type": int,

         "requires_operation": False,
         "operation":  None,

         "requires_collection": True,
         "collection_type": list ,
         
         "requires_split": True,

         "requires_print": True
        }
     }
  ]

