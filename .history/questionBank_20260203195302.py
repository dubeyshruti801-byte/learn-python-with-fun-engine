questions_L1=[
    {
        "id" : 1,
        "prompt": "Print Name- shruti" ,
        "expected_output": "shruti"
   },
   {
        "id" : 2,
        "prompt": "Print these names-Deepak Priya Dimple" ,
        "expected_output":"Deepak Priya Dimple"
   },
   {
        "id" : 3,
        "prompt": "Print 5 fruits Name-apple banana mango orange grapes" ,
        "expected_output":"apple banana mango orange grapes"
   },
   {
        "id" : 4,
        "prompt": "Print months of year -January February march April May June July August September October November December" ,
        "expected_output":"January February march April May June July August September October November December"
   },
   {
        "id" : 5,
        "prompt": "Print days of week-Sunday Monday Tuesday Wednesday Thursday Friday Saturday" ,
        "expected_output":"Sunday Monday Tuesday Wednesday Thursday Friday Saturday"
   }
     
  ]
questions_L2= [
    {
        "id" : 1,
        "prompt": "Take the given name from user, save it in variable a  and Print it- shruti" ,
        "expected_output": {
              "input_prompt": "Enter the given name:",
              "variable":{
                    "name": "a",
                    "type": str
              },
              "printed_output": "a"
        }
   },
   {
        "id" : 2,
        "prompt": "Take 1-10 numbers from user , save it in variable 'num' and print it." ,
        "expected_output": {
              "input_prompt": "Enter 1-10 numbers:",
              "variable": {
                 "name": "num",
                 "type": list
                },
             "printed_output": "num"
       }
    },

   {
        "id" : 3,
        "prompt": "Take 1-10 even numbers from user , save it in variable 'even' and print it." ,
        "expected_output": {
              "input_prompt": "Enter 1-10 even numbers:",
              "variable": {
                 "name": "even",
                 "type": list
                },
             "printed_output": "even"
       }
   },
   {
        "id" : 4, 
        "prompt": "t ",
        "expected_output": {
              "input_prompt": "Enter table of 2:",
              "variable": {
                 "name": "table",
                 "type": list
                },
             "printed_output": "table"
       }
     } ,
    {
        "id" : 5,
        "prompt": "take days of week from user, save it in 'week' and print it-Sunday Monday Tuesday Wednesday Thursday Friday Saturday",
        "expected_output": {
              "input_prompt": "Enter Days of week:",
              "variable": {
                 "name": "week",
                 "type": list
                },
             "printed_output": "week"
     }
     
  ]