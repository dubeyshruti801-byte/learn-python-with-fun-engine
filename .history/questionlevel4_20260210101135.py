question4=[
    {
      "id": 1,
      "prompt": "Take 5 numbers and print only even numbers",

      "expected_output": [2,4,6,8,10],   # logical check

      "expects": {

        "requires_input": True,
        "input_type": int,
        "input_call": 1,
        "min_value":5,

        "requires_collection": True,
        "collection_type": "list",

        "requires_loop": True,
        "loop_type": "for",

        "requires_condition": True,

        "requires_operation": True,
        "operation": "modulus",

        "requires_print": True,

        "variable_flow": True,
        "min_variables": 2
    }
  },
  {
      "id":2,
      "prompt": "Take 5 numbers and print only odd numbers",

      "expected_output": [1,3,5,7,9],
      "expects":{
          "requires_input": True,
          "input_type": int,
          "input_call":1,
          "min_value": 5,

          "requires_collection":True,
          "collection_type": list,
          
          "requires_loop":
      }

  }

]