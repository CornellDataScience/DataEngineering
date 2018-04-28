# Data Engineering

## Who we are:
The CDS Data Engineering subteam exists to provide analysis and processing support to CDS project teams, and to develop institutional knowledge in high throughput computing. 

**Advisor:** [Professor Immanuel Trummer](http://www.itrummer.org/)  
**Team Leads:** [Dae Won Kim](https://github.com/dwkwvss) (ORIE MENG), [Haram Kim](https://github.com/haramkim-1) (A&S CS 2020) 

## Team objectives:
* Improve on existing high throughput computing frameworks
* Develop solutions for data analysis problems in CDS projects
* Provide a reservoir of reference information in data engineering
* Research and publish means of improving existing DE frameworks

## Current Projects:
* Spark ML Optimization: Apache Spark's machine learning modules are not as well-studied as those of other platforms. This project seeks to empirically identify optimal settings for Spark's ML modules to best utilize the platform's unique capabilities.
* SkinnerDB Parallelization: This project's objective is to experiment with parallelism in Professor Trummer's recently developed database engine, SkinnerDB. The SkinnerDB uses a machine learning approach to query optimization, in contrast to the heuristic model used by most current database engines, but has not yet been expanded to allow multi-core execution.
* [Deterministic Query Approximation](https://github.com/CornellDataScience/DE_Query_Approx): Several recent publications have outlined methods to allow high-speed query approximation with deteministic bounds, but have not yet been applied to a wide range of queries. The objective of this project is to apply several of these techniques to the TPC-H query benchmarks to demonstrate broader applicability.
* [GPU Acceleration](https://github.com/CornellDataScience/distributed_gpu_computing): The distributed GPU computing deals with the unique task of handling distributed deep learning tasks, which is currently well-optimized for multiple GPUs, but not necessarily across multiple machines. Our goal is to research and optimize current tools in development so that it can be adopted by CDS teams deploying large DL models.

## Previous Projects:
* [Data streaming](https://github.com/CornellDataScience/DataEngineering/tree/master/archive/kafka_streaming): Profiling of real time data streaming through [Apache Kafka](https://kafka.apache.org)

* Server monitoring: Real time visualization and monitoring of compute server resource utilization through [Cockpit](http://cockpit-project.org/)

* [File format optimization and profiling](https://github.com/CornellDataScience/DataEngineering/tree/master/archive/file_formats): Comparative analysis of a variety of file formats typically used in data science, focusing on CSVs and [Apache Parquet](https://parquet.apache.org)

* [Spark diagnostics](https://github.com/CornellDataScience/DataEngineering/tree/master/archive/diagnostics): Deliberate attempts to produce errors while running Apache Spark, both locally and on our servers. Problem specifics and solutions were recorded in case similar issues develop in the future.

## Members (SP2018):
* [Jo Chuang](https://github.com/josephch405)
* [Ethan Cohen](https://github.com/ethanblake97)
* [Audrey Fan](https://github.com/flsaudrey)
* [Katarina Jankov](https://github.com/kjankov)
* [Ryan Kannanaikal](https://github.com/rk635)
* [Eashaan Kumar](https://github.com/eashaank)
* [Jeong Hyun Lee](https://github.com/jeonghlee12)
* [Julia Ng](https://github.com/ngjulia)
* [Shoheb Ome](https://github.com/shohtime)
* [Alanna Perez](https://github.coecis.cornell.edu/aep82)
* [Abhinav Prasad](https://github.com/abhinavp99)
* [Ahad Rizvi](https://github.com/t40tds)
* [Deepti Talesra](https://github.com/deeptitalesra)
