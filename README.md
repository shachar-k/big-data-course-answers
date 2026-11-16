# big-data-course-answers
Hadoop Training Questions
Please answer the questions below
Enter answers in your GitHub account and send the link
Exercise 1

initial
 Launched map tasks=9
 Launched reduce tasks=3
 Merged Map outputs=27

ex1
Launched map tasks=10
Launched reduce tasks=6
Merged Map outputs=54

Q1. How many files are there? 
7

Q2. Did the number of mappers change?
yes, from 9 to 10

Q3. Did the number of reducers change?
yes, from 3 to 6

Q4. Did the number of output files change? Why?
yes, becuase it depends on the number of reduce tasks

Q5. What does the value of 'Merged Map outputs' represent, and how is it calculated?
it counts the map-output partitions that reducers acually fetch and merge during the map reduce process. each mapper creates one partition for each reducer, so the calculation is:successful map tasks × reduce tasks.
in the case of this, 1 map task failed so its 9x6=54.


Exercise 2
Q1. Is your change in the mapper or in the reducer? mapper
Q2. Please provide your code on GitHub
______________________________
Exercise 3
Q1. Is your change in the mapper or in the reducer?
Q2. Please provide your code on GitHub
______________________________
Q3. Print the output of the MapReduce and put in your GitHub as an image
Note: you should not use external pipes, sort, or filters. All should be done inside the
MapReduce Python code
I want to see in the screenshot after you type the command:
$ > hadoop fs -ls /user/hduser/gutenberg-output
______________________________