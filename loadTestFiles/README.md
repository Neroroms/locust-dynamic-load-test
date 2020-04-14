# How to config csv
* Column 1: Request method type
* Column 2: url - /path/{{pathvar}}/
  path -> fix path name
  {{pathvar}} -> Get from json file 
* Column 3: url variable file name.
  replace {{pathvar}} with same variable name
* Colume 4: expect status code.
  if not set, default is between 200 - 399
