# ClassInitializer
Simple Python script to spit out a class init method for given variables.

making __init__ methods for new classes with tons of variables is tedious. This script lets you type the all the variable names you want once and spits out a string in the following format for you to copy/paste into your code.

for an input string `var1 var2 var3` the output is as follows:

```
def __init__(self, var1 = None, var2 = None, var3 = None):
	self.var1 = var1
	self.var2 = var2
	self.var3 = var3
```
the input string can have as many variables as needed, each seperated by a space.
