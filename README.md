# earthquakemodels

Here is the code for generating Earthquake Risk Models using Genetic Algorithms. 

# notes

Some information outside the project frenquently used can be found at:
  
  http://www.corssa.org/articles/themevi/zechar
  
  http://www.cseptesting.org/
  
  https://github.com/stat157/background/issues/26
  
  http://www.jstor.org/stable/3085650?seq=2#page_scan_tab_contents

List of packages
-------------
The project uses the programming language Python, version 3.X.X. 
The python libraries used are:
sys
math
array
numpy
datetime
time
random
deap 

Getting Started
---------------

```bash
# Get the latest version
To get the last version you should clone the repository from gitHub to your local files.
git clone https://github.com/PyQuake/earthquakemodels.git

```bash
# How is the code organized
Most of the code were develop to be run in a python3 interpreter. You may find that some files can be bash executed.
In most cases, you can call the most important methods in two ways. The direct approach and the self-structured way. 

What i mean from direct approach: It is possible to simply call, for example, the method to genarate a model by GA. That method needs some arguments and you would have to provide them to be able to run the method. 

The self-structured way is an aprroach that allows you to call the method in the right sequence making it easier to run the methods.

```bash
# Executing the main methods

