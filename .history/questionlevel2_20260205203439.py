questions2= [
    {
        "id" : 1,                                                                                                        
        "prompt": "Take the given name from user, save it in variable a  and Print it- shruti" ,
        "expects": {
         "requires_input": True,
         "min_inputs": 1,
         "input_type": str,
         "requires_print": True
  }
   },
   {
        "id" : 2,
        "prompt": "Take 1-10 numbers from user , save it in variable 'num' and print it." ,
        "expects": {
          "requires_input": bool,
          "input_count": int | None,
          "input_type": type | None,

          "requires_operation": bool,
          "operation": "add" | "sub" | "mul" | "div" | "mod" | None,

          "requires_collection": bool,
          "collection_type": list | set | dict | None,

          "requires_print": bool
           }

       },

   {
        "id" : 3,
        "prompt": "Take 1-10 even numbers from user , save it in variable 'even' and print it." ,
        "expects": {
         "requires_input": True,
         "min_inputs": 10,
         "input_type": list,
         "requires_print": True
        }
       },
     {
     "id" : 4, 
        "prompt": "Take 1-10 odd numbers from user , save it in variable 'odd' and print it.",
        "expects": {
         "requires_input": True,
         "min_inputs": 10,
         "input_type": list,
         "requires_print": True
        }
     } ,
    {
        "id" : 5,
        "prompt": "take days of week from user, save it in 'week' and print it.",
       "expects": {
         "requires_input": True,
         "min_inputs": 7,
         "input_type": list,
         "requires_print": True
        }
     }
  ]

