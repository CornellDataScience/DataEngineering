## Server Architecture

For the purposes of understanding why frameworks like Spark can offer such significant performance improvements and how to best optimize such systems, it is helpul to know the basic structure of modern computers. Typically, computers can be split into three major components: a processor and memory pair that operate in concert, and an interface to IO devices.

### Processor

The processor takes the form of a CPU, usually with a number of seperate processing cores (each CPU in the CDS servers has 16 discrete logical processors). The CPU has a small amount of very high performance memory available to store active data (the register file), an arithmetic logic unit (ALU) that handles mathematical and logical operations, and a number of transparent (that is, invisible to programs operating in the processor) caches to store instructions and data fetched from main memory. The operation of the register file and ALU is fairly self-explanatory; the registers serve as temporary storage for values that the ALU requires or operates on. More relevant to us are the multiple levels of caches present in modern processors. 

#### Caches

Key Term: Block - some number of bytes that represents a single unit of memory; handled as discrete components for the purposes of caching.

Typically, several caches are present in a processor in order to minimize the latency involved with reading from or writing to main memory, which is often physically distant from the processor itself. To compensate, a series of progressively larger caches around the processor itself serve to provide rapid access to data stored in main memory. To understand how this works, consider a single-core processor without caching. Each assembly language instruction must be read from the appropriate location from main memory and each operation involving IO to or from main memory will require the full delay implied by the relative slowness of system RAM and the distance between main memory and the processor. Combined, these properties can greatly reduce performance. To mitigate this problem, we might add a L1 (the lowest level and smallest volume cache) cache to the processor, between it and the channels to main memory. Successive levels of larger and correspondingly slower caches may be added above the L1 cache to provide greater redundancy and further reduce the chance of a cache miss (a block of memory is not present in any cache, requiring the processor to wait for main memory IO).

#### Cache Operation

The L1 cache in this example may operate in a number of different ways, depending on the associativity policy in the hardware. In the simplest case, a direct-mapped cache, every block in main memory is mapped to a single position in the cache, which is where a block will be located if it is present in the cache. This is a many-to-one relation, as there are obviously more blocks in main memory than in the cache. 

The Cache improves processor performance by allowing recently used data to stay physically close to the processor and in high-speed SRAM memory. This means that when the processor attemtps to access a block, it gets either a cache "hit" (block present in cache) or "miss" (block not present in cache). In the event of a hit, the data in the cache allows the processor to operate immediately, instead of waiting for main memory. In the event of a miss, the block requested is brought into the cache, replacing whatever block occupies its mapped location in the cache.

Note that other replacement strategies (i.e. replace the least recently used block) are possible, but require more complex cache layouts.

Cache writing policy varies between processor implementations. Two common strategies are write-back and write-through. In a write-back cache, if the memory block to be written is hit, only the copy stored in the cache is modified, with the corresponding block in main memory being updated only when the updated copy in the cache is replaced. This method increases efficiency, but requires additional management overhead to track stale blocks (unupdated copies in main memory). Write through caches behave much more simply; when writing to a hit block, both the block in main memory and its copy in the cache are updated. This negates the benefit provided by the cache for memory writes but simplifies cache-memory interactions.

The performance increase offered by caches in general (and multi-layered caches in particular) can be demonstrated by examining the cycles per instruction (CPI) for memory operations in a processor with caching. First consider a processor with no caching. Assume that main memory requies 70 processor cycles per interaction, and 35% of all instructions require interaction with main memory. Additionally recall that instructions themselves are housed main memory, and must be read in order to be executed. We would then expect the CPI of a *single instruction* on a processor without caching to be:

```
70 [instruction load penalty] + (.35 * 70) [expected memory IO penalty] = 95. 
```
Although these numbers are not necessarily representative, this should indicate how severe a problem memory access time can be without a cache.

Now consider the same processor with only an L1 cache added, and assume that the cache has an instruction miss rate (the likelihood that an instruction fetch misses) of 2% and a data (the likelihood that an data IO operation misses) miss rate of 4%. For the L1 cache, we don't consider access times, because the cache is directly integrated into the processor and does not introduce a relevant delay when hit. The CPI for this processor is:
```
(0.02 * 70) [expected instruction load penalty with cache] + (0.35 * 0.04 * 70) [expected memory load penalty with cache] = 2.4. 
```
This is an enormous improvement over the uncached processor.

We can get additional improvements by adding successive layers of caching, but the returns in performance gain decrease quickly, as each successive layer must be larger (increasing read/write time requirements) and further away from the processor.

### 

<br>

![](https://lh6.googleusercontent.com/S1PT4HcPFaXhMgf5lUkYJJ9LAGUMHBQHeus5EiUbpZsxF3ytqE-hC0zRTp6T6kwrZw6y4y4SrsePH9mGp0UO=w1680-h919-rw)
![](https://sanjayachauwal.files.wordpress.com/2017/10/overall.gif =550x300)  
<br>

 
