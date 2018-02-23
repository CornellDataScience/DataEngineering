## Obvious Tradeoffs in Data Engineering

### Memory versus Time Tradeoff

It is frequently the case that a program's computation time requirements can be reduced at the expense of greater memory usage and vice versa. 

A very simplistic example might be a computer program that must calculate the products of some extremely large set of integer-integer pairs, where each integer is positive and less than 128. In theory, this program could be written such that it requies no in-memory data structures beyond those required to represent three integers: the multiplicand, multiplier, and product. Such a program (ignoring optimizations that might be done by the compiler) would have to calculate each product individually. Conversely, one could create a 128 by 128  two-dimensional array representing the multiplication table for all possible input values in memory when the program starts. This program would not have to rely on the processor's ability to multiply at all, as any multiplication could be performed by array lookups. Although this example may seem extreme, this type of pre-computed multiplication table is actually used in certain embedded systems. By installing a read only memory containing a multiplication table, a device manufacturer can avoid implementing a costly adder-subtracter dependent multiplication algorithm on a device with a very weak processor.

![Multiplication ROM](https://i.stack.imgur.com/TNLtQ.png =500x)

### RAM versus HDD Tradeoff

For the purposes of this subteam it is also important to understand the properties and behaviors of the hardware components that constitute a server. The performance differences between system memory (RAM) and the hard disk are particularly severe and motivate the use of Spark over MapReduce.

In terms of impact on process performance the disparity between disk and memory IO is extremely pronounced. Typically a memory operation even without caching requires only on the order of 100s of processor clock cycles (generally speaking, the time in which the CPU does a single calculation or other operation), whereas a disk operation might require up to 1000000 clock cycles to complete. This is a consequence of the fundamental physical difference between memory, which is volatile but stores information in circuit states (i.e. a bistable element's output) and a disk drive, which records binary data by magnetizing locations on magnetic film layered on a rotating metal disk. The fact that reading or writing information in a disk drive requires the disks to be physically rotated adds significant latency, which is not present for the purely circuit-based system memory.

From a performance perspective alone, it might seem that the disk drive is much less useful than RAM, but it is important to note tha a hard disk is both the only way to store information between system restarts and vastly less expensive per unit of storage. As a result, the RAM available on the master server is only 32 gigabytes, while there is nearly a terabyte of disk space. So, although it is preferable to handle all data operations in memory, it is frequently necessary to either "spill over" to disk (writing data to the disk when space in memory runs out) or stagger processing so that there is always sufficient space to manipulate data structures in memory while reading new information in from disk as the current batch is processed to avoid bottlenecking.

These concerns are extremely relevant for the Data Engineering subteam, because it is necessary to optimize high volume data processing for the hardware that is available. For example, on systems with particularly limited RAM, the performance advantage provided by Spark (which relies heavily on in-memory operations) over MapReduce (which requires significantly more disk IO) may be largely negated.

### Other Tradeoffs

Other potential trade offs in algorithm and program design are calculation accuracy (through an analytical solution) versus speed (numerical or approximation-based algorithms), storage fault tolerance (redundant copies and replication, ensuring data integrity but using more space and requiring additional time to update) versus efficiency and speed (only one copy, so quick to update but vulnerable to loss or corruption), and code efficiency vs readability (this dichotomy is a consequence of the fact that many programming languages allow computational shortcuts such as bitwise shifts to increase efficiency in special cases, at the expense of easy human interpretability).

# Hadoop and MapReduce

## Apache Hadoop

Apache hadoop is a distributed storage and processing framework for high-volume datasets. Hadoop has four major components:
*   Hadoop Common: Utilities common to other Hadoop components, folded out into their own module
*   Hadoop Distributed File System (HDFS): The file framework used by Hadoop to store data on multiple nodes to enable high speed access and redundancy
*   Hadoop YARN: The scheduling engine for Hadoop processing
*   Hadoop MapReduce: Parallel processing component of Hadoop, working in concert with the HDFS; see below for more details

### Properties of Hadoop

#### The HDFS
The distributed file system is used by Hadoop to provide data redundancy and replication. Files stored in the HDFS are split into blocks and distributed among data nodes with multiple copies stored across the network to ensure data integrity even in the event of a data node failure. Blocks are usually large, so during file access more time is typically spent on data transfer between nodes than on data lookup.

The HDFS is organized into three node types: the NameNode, SecondaryNameNode, and DataNodes. The NameNode is responsible for maintaining a table of file metadata (i.e. block locations, permissions, location in the HDFS, last access, etc.), the SecondaryNameNode provides redundancy and reduces latency for the NameNode, and the DataNodes store blocks of stored files.

#### MapReduce Architecture

Split into two major paralell components: mappers and reducers, with a data exchange "shuffle" between them. A JobTracker master node monitors pending client tasks and manages a number of subsidiary TaskTracker nodes. TaskTrackers execute jobs provided by the JobTracker, return results, and manage the shuffle when the system is switching from mapping to reducing.

#### YARN Architecture

Two master nodes: ResourceManager and ApplicationMaster. The ResourceManager acts as a resource allocator and provides event handling. The ApplicationMaster manages running applications, requests resources from the ResourceManager, and tracks NodeManager workers. NodeManagers provide compute resources that are allocated by the master nodes and maintain communication with the ApplicationMaster.

For more details, please see the [Hadoop Architecture Overview](https://ercoppa.github.io/HadoopInternals/HadoopArchitectureOverview.html)

### Mappers and Reducers

#### Mappers

Each mapper is an independent process that acts on some partition of the overall dataset concurrently with other mappers that are allocated other partitions. Each mapper gives a key-value pair of unique identifier for the input data and the output value that it produces when the process completes. The behavior of mappers can be thought of as a parallelized equivalent of a functional programming map operation, which applies a function to every element a list of inputs to procuce a list of corresponding outputs. 

In IBM’s [example](https://www.ibm.com/analytics/hadoop/mapreduce), each mapper might be assigned to a single input file of city-daily temperature pairs and be responsible for reading in relevant information.

#### Reducers

Reduce processes occur after the mappers whose outputs they depend on finish and take the set of values produced by the requisite map operations and reduce them to either one value or a set of values. This process may occur iteratively, with multiple sets of reducers that further reduce the previous set's results. This process is somewhat analogous to the fold left or fold right operations in some functional languages, which recursively apply a function to the adjacent elements of a list and the previous function output until a single result is obtained.

In IBM’s example, the reduce operation takes the temperatures for each city in the different input sets and averages the temperatures by city, to produce a set of city-temperature pairs without duplicates.

### The MapReduce Shuffle

![MR Shuffle Diagram](https://i.stack.imgur.com/aIGRQ.png) 

The shuffle process occurs between completion of mapping tasks and the beginning of the reduction process. First, mappers partition and sort their result data in memory, and then write the partitions to disk. 

Reducers then read their requisite partitions from the data node disk drives (potentially on different machines), and merges/reduces them to produce an output. This output might then either be written to the hadoop file system or passed into further reducers for additional refinement.


### MapReduce Shuffle Problems

MapReduce has a number of issues that make it unsuited for large and complex operations. In particular, the process of writing and reading paritions to and from the disk, adds significant overhead and can significantly impact performance. Additionally, the process of exchanging partitions between datanodes can be expensive in terms of network IO, and may further slow down the shuffle.
