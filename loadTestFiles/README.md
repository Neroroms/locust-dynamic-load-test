# How to config csv
* Column 1: Request Method
* Column 2: url - /path/{{pathvar}}/
  path -> fix path name
  {{pathvar}} -> Get from json file 
* Column 3: url variable file name.
  replace {{pathvar}} with same variable name
* Column 4: headers file name. json file
  - {
      ###Header object
    }
* Column 5: body content type.
* Column 6: body content file name. json file
  - {
      data:[
        {
          ###Body object
        },
        {
          ###Body object
        }
      ]
    }
* Column 7: expect status code.
  if not set, default is between 200 - 399
