
# Introduction to the CDS Data Engineering Team

## Our mission statement:
_"To expand the computational capabilities of Cornell Data Science in tackling industrial scale of data volume, speed and variety."_

## What is Data Engineering?
Data engineering usually refers to a broad field of process optimization for data science operations. It includes, but is not limited to, optimizations of resource allocation in data science operations, effective warehousing of large volumes of data, and efficiency of computations while maintaining integrity of the system. Note that our use of the term ‘resource’ refers to both physical things like CPUs, disk storage, network I/O and also intangible resources such as time and flexibility. Often these optimizations occur on a hardware level, where we adjust system settings on servers to accomodate for the diverse needs of different data tasks.

## What does the CDS Data Engineering Team do?
In the context of Cornell Data Science, we have a x-node cluster, that is to say, we have a system of x servers, with a total of x CPU cores, x amounts of RAM, and x TB of hard disk. We also have a GPU specifically for our deep learning needs. Our job is to understand how these work, how best to utilize them, identify good practices and protocols to stick to, and constantly explore ways to expand its capabilities. We will often say that our purpose is to “break the servers.” This is because only then can we understand what works/ doesn’t work, and what to do better.


## High-level take on performance enhancement
Speed is often the single most important factor in data engineering. With the current in extremely large and fast-paced data volumes, even the smallest inefficiencies can blow up to insurmountable problems in machine learning. Here we list certain ways we try to achieve faster speed in machines:

### 1. Parallelize operations

All computations can be broken down to constituent sub-operations that fall into these two categories: __Embarrassingly Parallel__ vs __Inherently sequential__. The first term refers to processes that can, given enough resources, be completed in one step in parallel, while the second term refers to processes that must follow non-concurrent steps to complete its objective. Parallelizing computations is an essential part of any industrial-scale data task and can have huge benefits. Let us see how this can be done.

Take, for example, a rather trivial process of creating a copy of an array stored in a certain location.(of course, the whole point of the example is to show that the trivial actually turns out to be the non-trivial!) The first element of the existing array is replicated as the first element of the new sequence, with all other elements following suit. This means that, if you have an original sequence of length n, all you need is n processors to transcribe one element each and complete the processes in one step. Therefore the transcription process can seem embarrassingly parallel.This is particularly useful if the said sequence is extremely large and the copy is urgently needed. If resources are available, the transcription can complete several magnitudes faster than what would take for a single processing unit could handle.

![Paralellism](https://computing.llnl.gov/tutorials/parallel_comp/images/parallelProblem.gif)

However, there are caveats to this nifty trick in reality: a machine, even with infinite resources, will not be able to complete the transcription in just one step. For instance, even before the transcription can take place, the machine must find an available storage location for the new sequence, determine the size of storage to allocate, and reserve such a space by creating a pointer. Moreover, these processes must be preceded by the task of determining which cpu gets which element of the array, which can be a complicated assignment task if we wish to coordinate an optimal schedule. In fact, we have also glossed over the complications that come from whether the original array already sits in RAM or in a hard disk. 
  
Therefore at a high level, copying an array from one place to another in storage can be vastly shortened in duration using parallelism, but cannot entirely avoid being inherently sequential. This is why parallelizing is only part of the solution for most data engineering problems.  
 
### 2. Remove redundant operations (Initialize and Vectorize)

We demonstrated from the toy example above that as a whole, copying an array to another location entails inherently sequential tasks. Therefore a good way to shorten the duration of the task can be to actually eliminate __redundant operations__, which would effectively reduce the total number of operations and consequently the total duration of the operation. Let's revisit the copying-an-array example again to see how this could possibly work, this time in code form:

```
original_array = [1,2,3,4,5,6,7,8]
copied_array = []
for element in array:
  copied_array.append(element)
```
The code looks rather simple, but has many avoidable redundancies lurking inside. To give a little background before we dive into these redundancies, it must be noted that a Python list is simply an array of pointers to different objects. Therefore elements of a list can be of diverse data structures and types, allowing substantial flexibility. However such flexibility comes at a cost: the python interpreter must constantly type-check when iterating or appending to a list to make sure that whatever operation is being done to the list is allowed and the appropriate action taken. For example, a '+' operation can be a numeric addition for a numeric type, but a concatenation when applied to strings. This flexibility in data structures and the implicit type-checking operations are parts of the reason why python is much, much slower compared to languages like C, C++ or Java. (keep in mind however that despite this Python is very widely used in data science for its interpretability and ease of editing)  


Therefore in the above example, even though our original sequence is in fact all numeric types, Python must constantly check the types of the elements of the original array before appending a copy of it to the new array. Moreover, at every iteration, the machine must locate and allocate new memory spaces. Such operations are clearly redundant, given that we already know before we create the copy the type and length of the sequence to be copied. A common way to tackle the redundant memory allocation problem is proper initialization, as shown below:


```
original_array = [1,2,3,4,5,6,7,8]
length_original = len(original_array)
copied_array = [] * length_original

for element_index in length_original:
  copied_array[element_index] = original_array[element_index]
```

Here, instead of initializing an empty list first and iteratively adding new elements, the new array is first _initialized_ as a list filled with null values with the same length as the original array. This memory allocation is done only once, therefore reducing the total duration of the operation. As for the type-checking problem, typically a way to avoid such prolbems is to use a specialized data structure called a _numpy array_. A numpy array coerces all its elements to a single type, allowing fast iterative operations that are type-specific. An example is shown below:

```
original_array = np.array([1,2,3,4,5,6,7,8])
copied_array = np.array(original_array)

# please note the np.array(original_array) makes sure that copied_array is indeed a pointer to a copy, and not to the original object
```
Reducing redundant type-checking and implicit interpreter operations this way is often referred to as _vectorization_ and is often one of the best ways to speed up data science operations in commonly used languages like Python and R. Initialization and vectorization are useful data engineering skills to have to speed up your executions.

For more information on numpy, please refer to the [numpy documentation](http://www.numpy.org/)


### 3. Making individual operations faster 


While this may sound like a trivial solution,(equivalent "How should I win a 100m sprint?" answered by "Make sure each step is fast") in data science operations often can be made faster either by choosing to solve a different problem that can approximate the true solution, or to choose a different type of machinery/platform to speed up operations. 

__Trying to approximate rather than solve directly__   


The above image shows the optimization setup for the support vector classifier, a popular classification algorithm. Not just SVMs, but amost all machine learning problems are optimization problems: certain assumption are incorporated into a loss/error function that must be minimized given some input information. Thus advances in this optimization techniques often lead to improvements in machine learning algorithms, as even a small improvement in efficiency can, in large scales, be the difference between the infeasible and the feasible. A detailed overview of optimization techniques is very much beyond the scope of this tutorial, and we would not be able to do the field justice even if we tried. However, we can say that a common theme in optimization is attempting to approximate the optimal solution by solving a different, but easier problem. This technique is commonly referred to as _relaxation_.

![Primal Problem for Support Vector Classifier](http://scikit-learn.sourceforge.net/0.5/_images/math/eb74783f01c85187766959706f842a74224e10f4.png)

Solving relaxations, rather than directly solve for the optimal solution, has several benefits. For instance, one can obtain a feasible, n5ar-optimal solution with relatively shorter amount of time. Also, if there is significant noise to the data, directly solving for the optimum may be infeasible, which could be a/voided. The trade-off is often between feasibility, computation time and accuracy of your solutions.   

A very prominent example of an approximation algorithm is _gradient descent_. For extremely high dimensional problems, directly computing global minima/maxima can be computationally challenging. Therefore gradient descent attempts to iteratively "traverse" a function and approximates the minimum/maximum. For a good intuitive reading on gradient descent, go [here](http://cs231n.github.io/optimization-1/#gd). A visualization of the technique is shown below, where the traversal of the function in iterative fashion is displayed:

![Gradient descent in action](http://charlesfranzen.com/images/gradient.png)

Techniques like gradient descent can significantly reduce runtime, and can also be more conducive to parallelism. Gradient descent also allows one to control error tolerance and learning rate(the rate of traversal), yielding some control of users to more quickly obtain reasonable results. 

__Changing to a faster interface/platform__

It is often the case that simply the platform being used is inferior in speed. For example, python inherently is very inefficient in scheduling parallel tasks - for libraries such as dispy and multiprocecssing. The same can be for languages like R. As was discussed in an earlier section, Python and R often has to carry out intrepreter operations before computations can be made, due to their flexibility and ease of deployment. One may, however, choose to use a platform such as C or C++, which are much faster. Shown below is a comparison of the computation speed of languages. One may use these speed differences as a consideration for switching or sticking to a particular platform.

![Performance Comparison of Languages](https://raid6.com.au/~onlyjob/_arena/speed_close.png)

It must be noted, however, that switching is not always the best answer. C/C++ usually lacks the diversity of available libraries and packages, which can significantly slow the speed of development. Sometimes newly developed languages that offer a significant advantage - like Julia, for example - may not gain widespread use because of the lack of community support and incompatibility to already existing data science infrastructure. This inertia can often be quite the dominant force and must be an important part of considerations when selecting the platform/language.

Moreover, it may be sufficient to make languages like Python and R faster by reducing interpreter operations. Essentialy these languages are wrapper languages that sit on top of low-level languages like C, C++, and Fortran. A very good example that strips as much python operations and rely on C is the aforementioned numpy package. Numpy operations are often in C, and is usually the sensible way to tackle large data volumes and iterative processes. 

### 4. Reduce intermediate outputs by changing the sequence of operations

### Introducing queries and joins
Another approach to process optimization is not to change the subprocesses themselves, but rather attempt to shift them around in order as to reduce the sizes of intermediate outputs. This is often the key idea behind query optimization in relational databases. For those of you not familiar with relational databases, they are in essence a database that stores data in multiple sub-tables, rather than choosing to store all the data in one table. A schema of a sample relational database is shown below:

![relational database](http://www.databaseanswers.org/data_models/imdb/images/version_showing_attributes.gif)


As shown above, the entire database is organized into sub-tables, which increases the usefulness of the information. If one is only interested in parts of the data that pertains to a certain category, one only needs to lookup information in a subset of the data. This helps reduce data loads and can enhance lookup speeds.

```
### A SQL query operation that performs a lookup on one of the sub-tables

SELECT * FROM Movies
WHERE Playing_time > 200;
```
The above SQL query is a good example of a lookup operation - called a _query_. All columns in the subtable Movies is selected, with the filtering condition that only movies with the field Playing_time having a value larger than 200. Notice that this lookup operation will have taken a considerably longer amount of time had this entire table been stored in a single tabular format.

Also notice that these tables are organized by some type of unique identifiers for each row. These identifiers are often one or two more columns that form a _key_ for the respective table. In many of the tables in the given example, these columns are made obvious by the suffix _ID_. These identifiers not only allow identification of unique elements in the sub-tables, but also connect different tables together, allowing these tables to be _joined_ when a query requires that information across multiple subtables be gathered and displayed in a single tabular format. An example is shown below:

```
SELECT MovieID, Movies.Star_Ratings, Movie_Genres.Movie_Genre_Type From Movies, Movie_Genres
WHERE Movies.MovieID = Movie_Genres.MovieID 
AND Movies.Star_Ratings > 4
AND Movie_Genres.Movie_Genre_Type != "Horror";
```

The above query outputs three columns: one that is shared (and in fact "connects" the two tables) by the tables _Movies_ and _Movie_Genre_Type_, and the other two are respectively unique to one table. This query is an example of a _join_, a process of merging two tables by some join condition that determines which rows of one table match with rows of a different table, and are column-wise concatenated. 

So in this query example, the following three things occur before the query completes its lookup and displays the results:

1) Two tables are first joined using column MovieID, which both tables have. The specific join here is a __inner join__ (there are left, right, outer, and natural joins - if interested, please read into these)  

2) The resulting joined table is filtered using the Star_Ratings and Movie_Genre_Type column in a process known as __selection__  

3) All other columns except MovieID, Star_Ratings, Movie_Genre_Type is dropped, in a process known as a __projection__

### A query optimization example: optimizing joins
Joins are typically one of the costliest procedures in queries. The process usually involves searching over the second table while blocks of the first table is sequentially read in (a block nested loop join) There are many additional types of join processes, such as the hash join, sort-merge join, and index-nested loop join, that we will not necessarily elaborate on, but strongly encourage you to read up on. 

While we won't go into too much detail on the actual mechanics of how machines may perform a join, what we can talk about is how the sequence of filter, join, and column selection processes can be rearranged to reduce the overall load and time of the query. Let us take the same join example as one directly before, but slightly modify the query.

```
SELECT temp1.MovieID, temp1.Star_Ratings, temp2.Movie_Genre_Type FROM

(SELECT MovieID, Star_Ratings FROM Movies
WHERE Star_Ratings > 4) AS temp1,

(SELECT MovieID, Movie_Genre_Type FROM Movie_Genres
WHERE Movie_Genre_Type != "Horror") AS temp2

WHERE temp1.MovieID = temp2.MovieID;
```
The output of this query is the same as the query example before. It also contains an inner join, selection, and projection process. Let's see how these two queries differ by looking at the __order__ of the operations.  


1) As SQL queries are done _inside out_, that is to say inner subqueries are executed first, the tables MOovies and Movie_Genres is first filtered using the Movie_Genre_Type and Star Ratings (__Selection__)  

2) Columns MovieID,Star_Ratings for table Movies, columns MovieID, Movie_Genre_Type for table Movie_Genres is selected and all other columns dropped. (__Projection__)  

3) The inner join is done using join condition on MovieID, which both intermediate outputs of the previous steps contain. (__Inner join__)  


Notice that nothing has really changed here, except that the join is done only after the selection and projection processes, unlike the previous case, where the join occurred before the selection and projections. Selection and projection effectively _reduces_ the inputs going into the join operation. This significantly reduces the workload of the join, and in some cases, reduce the total processing time of this query by several magnitudes, if selection and projection conditions are limiting enough.

Obviously there are a whole host of other join optimizations and query optimizations in general. One should, however, be able to grasp how this type of _reordering_ of operations can reduce intermediate results and speed up operations, without necessarily having to change the natuer of the subprocesses involved.
