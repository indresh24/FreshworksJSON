JSON-Merge:

The program is developed using python 3.7

Functional Requirements:
1)Initially using built-in "json" package the json files that were created are imported
  and converted into a dictionary format(Key:value) pair
2)The files are read dynamically until the format "inputfilename suffix" filename is not found
3)When we use Dicitonary format, an additional list is encoded over the actual list while retrieving
the values of the dictionary
4)Hence we use a list "temporary" to store the values which stores the values read from the dictionary
5)In order to extract the individual player features ,another list is used "temp" which is then
assigned to the resultJSON dictionary
6)Since it is a key value pair it also accepts non-English characters

Non-Functional Requirements:

TIME COMPLEXITY:

1)Merging Files: 
O(n*m) where n=number of files
             m=number of lines

a)Inserting values to a player profile in output file
	The time complexity in this is O(n^2) since hashmap has average O(n)
b)Updating the values of a player profile in output file
        The time complexity involved in this is O(n^2) for traversing and checking for characters in a string 
c)Ability to change the root key of the output file
	The time complexity involved in this is O(n^2) because of hashmap
The program checks for the exceedence of outputfile and the mentioned size.If it incase occurs
the program terminates immediately