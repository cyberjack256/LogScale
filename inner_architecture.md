# How LogScale Uses Kafka
## How LogScale uses Kafka Summary

- LogScale is a log analytics system that can run both On-Prem and as a Hosted offering and is designed for "On-Prem first" due to security and volume limitations.
- LogScale uses Kafka for two main purposes: buffering ingest and as a sequencer of events among the nodes of a LogScale cluster.
- The ingest queue is used for buffering ingest during peak loads and also serves as a commit log, allowing for data to be restarted with no loss in the event of a system failure.
- The primary coordination mechanism of the LogScale cluster state is maintained using an event sourcing model, where updates are pushed through a single-partition/multiple-replica topic called global-events.
- Nodes periodically dump a snapshot of their internal state to local disk, and when a node starts up, it will read its own snapshot and re-load updates starting at the offset written in the snapshot.
- The Kafka cluster ID is also recorded as the epoch of Kafka offsets, so manual intervention is required if the Kafka cluster is wiped or redirected to a different cluster.


### Kafa Explained as a Scorecard
Okay, so imagine you have a group of friends who are playing a game together. Each of your friends has their own scorecard where they keep track of their score in the game. They also have a way to communicate with each other to update their scorecards with the latest scores. This way, they can all see the current scores of each other and know who's winning.

This is similar to how LogScale uses Kafka. Each node in the LogScale cluster is like one of your friends, and it has its own "scorecard" (or internal state) where it keeps track of the data it's processing. They also use a "communication" mechanism (Kafka) to update each other's scorecards with the latest data. This way, all the nodes in the cluster can see the current state of the data and work together.

The last part is about a situation where you all decide to change the game or the rules and you need to start a new game. In this case, you will have to throw away the old scorecards and start a new one. But in order to not lose the previous game's score, your friends write down their current score and the game's rules before they throw away the old scorecard. This way they can continue the new game from where they left off the previous one.

Similarly, in LogScale, they also record the current state and the rules (Kafka cluster ID) before they throw away the old state, so they can continue with the new data without losing the previous one.


## Summary of LogScale Configurations On-prem
- LogScale supports three configurations for running Kafka: Single node, Dedicated Kafka/Zookeeper, and Bring-Your-Own Kafka
- Single node option is great for small-medium instances on a single server, but other options can be more complex
- Many users run both LogScale and Kafka as a cluster for scale and resilience
- Customers who are not knowledgable with Kafka can use the LogScale/Zookeeper and LogScale/Kafka containers, with LogScale performing reconfigurations for the user
- Customers who already manage their own Kafka solution can use HUMIO_KAFKA_TOPIC_PREFIX to namespace the topics
-LogScale does not use Kafka's built-in compression due to issues with JNI and garbage collection




# How LogScale Does Scale-Out Clustering
https://medium.com/LogScale/how-LogScale-does-scale-out-clustering-75e423ac16c2

## Data Arrives
- When scaling a LogScale cluster, there are two main concerns: ingest and search.
Scaling out can be used to deal with high ingest and to improve query performance.
- In a LogScale cluster, some nodes are arrival nodes (they receive data from the real world), and others are designated for ingest processing and search.
- Any node in the cluster can act as a point of arrival, and a load balancer or other means outside of LogScale can be used to control which nodes are arrival nodes.
- When data arrives, the request is validated, parsed, and sent to the correct ingest partition and Kafka partition.
- In larger setups, it is recommended to have a designated "arrival node" that is only responsible for arrival processing, not ingest or search.
- Arrival nodes are also responsible for coordinating, gathering, and merging the final result of queries that span multiple nodes.

### Data Arrives as A School Assembly
Okay, so imagine you're in charge of organizing a big school event, and you want to make sure everything runs smoothly. You have a lot of different tasks that need to be done, like setting up tables and chairs, decorating the gym, and selling tickets at the door. You also want to make sure everyone can find their way around the school and that everyone is safe.

This is similar to how LogScale works. When they receive a lot of data (like a lot of people coming to the school event), they need to make sure they can handle all of it and that it's organized properly. They have different "nodes" that are in charge of different tasks. Some of them are in charge of receiving the data (like people coming to the school event), some are in charge of organizing the data (like setting up tables and chairs), and some are in charge of searching for information in the data (like making sure everyone can find their way around the school).

When they receive a lot of data, they can "scale out" by adding more nodes to help handle it. For example, they can add more people to sell tickets at the door to make sure everyone gets in quickly.

They also have a way of making sure the data is organized properly and sent to the right place. For example, if someone comes to the door with a ticket that's not valid, they won't let them in. Similarly, if someone sends LogScale data that's not in the right format, it won't be accepted. And if someone is looking for information in the data, they can make sure they find the right information quickly.

In larger setups, they also have a designated node that is only in charge of receiving the data (like the people coming to the school event) and not in charge of organizing or searching for information in the data. They do this to make sure the other nodes can focus on their tasks and the event runs smoothly.


## Ingest
- Ingest nodes in a LogScale cluster are responsible for reading data off of Kafka, assembling segment files, and processing real-time queries.
- The assignment of ingest partitions to nodes can be controlled using the ingest partitions HTTP API.
- The task of an ingest node is to receive logs on its designated ingest partitions and create segments out of the data and process live queries.
- The assembly of segment files involves maintaining a 1MB work-in-progress buffer which is flushed to the segment when the buffer is full or when 10 minutes has passed.
- Whenever a 1MB block is done and flushed, the ingest queue may be pruned to the index of the oldest entry in that block.
- Once an entire segment is full, it is passed on to a storage node. Storage nodes are responsible for processing interactive searches of ‘old’ data, whereas ingest nodes participate in interactive search of data segments under assembly.
= In addition to building segments, ingest nodes also deal with real-time queries. This involves pushing all events through the pipelines corresponding to current real-time queries.
- The coordinating arrival node is typically the node that received the HTTP request to initiate the real-time query, but may be some other node in case of e.g. alerts.


## Ingest Explained as a School Project
Okay, so imagine you're in charge of organizing a big school project, and you have a lot of different tasks that need to be done, like researching information, writing a report and presenting it to the class. To make sure everything runs smoothly and the project is completed on time, you've divided the tasks among different group members.

This is similar to how LogScale works. They have different "nodes" that are in charge of different tasks when handling a lot of data. Some of them are in charge of receiving the data (like your group members researching information), some are in charge of organizing the data (like writing the report), and some are in charge of searching for information in the data (like presenting the report to the class).

To make sure everything runs smoothly, they use something called "ingest nodes" to manage the data. These nodes are responsible for reading data off of something called "kafka", organizing the data into segments and processing real-time queries. These nodes work like a team, each one focusing on a specific task and working together to complete the project.

When these nodes receive a lot of data, they need to make sure they can handle it and that it's organized properly. They do this by dividing the data into "ingest partitions" and assigning each partition to a specific node. This way, each node can focus on managing a specific part of the data and the data is organized properly.

When the data is organized into segments, the nodes then pass it on to another set of nodes called "storage nodes". These nodes are responsible for processing searches of "old" data, while the ingest nodes focus on interactive searches of data segments that are currently being assembled.

In addition to building segments, the ingest nodes also have to deal with real-time queries. This means that they need to constantly check for new queries and push all the data through the necessary pipelines to make sure the right information is being provided.

To make sure everything runs smoothly, there is a designated "coordinating arrival node" which is responsible for making sure the different nodes are working together properly. This node is typically the one that receives the request to start a real-time query, but it can also be another node in case of special situations such as alerts.

Overall, the ingest nodes in a LogScale cluster play a crucial role in managing and organizing large amounts of data effectively and efficiently.


## Scaling out Search  in LogScale
- Scaling out search in LogScale improves the speed of searching through large amounts of data.
When a segment file is full, it is copied to one or more storage nodes for searching. More storage nodes = faster search.
- Segments are placed on nodes using a storage-partitioning scheme and allocation can be viewed using the segment-partitioning HTTP API.
- All nodes in the system have knowledge of the current placement of segments, relevant time intervals, and data sources.
- When an interactive search is received, the relevant segments and hosts for the search are determined in order to increase processing power and speed up the search.
- LogScale is a logging tool that can efficiently handle large amounts of data by compressing it and using tags to optimize storage and search.
- Theoretically, LogScale can search through 1GB of data at a speed of 37GB/s, but in practice the speed is around 6GB/s due to other factors influencing the outcome.
- LogScale works best when there is a lot of data being ingested but relatively few queries being made, making it a good fit for a logging tool where logs arrive continually and queries are made infrequently.
- LogScale can handle a large volume of data, with successful single-node deployments having ingested over 1TB/day.


# Understanding LogScale's Data Sources
https://medium.com/LogScale/understanding-humios-data-sources-a23db019a90f


LogScale can organize and search through large amounts of data, called logs. The logs are separated into different categories called tags, which help guide and optimize how the data is stored and searched. These tags are important because they limit the amount of data that needs to be scanned through during a search. Data sources are identified by the unique combination of tags. As data arrives at LogScale, it is split into data sources and processed sequentially on one machine in the LogScale cluster. However, there can be challenges with high velocity data sources, low velocity data sources, and high variability tags. LogScale deals with these challenges by creating more data sources for high velocity, merging small segment files for low velocity and limiting the number of data sources for high variability.

## Data Sources Summarized
- LogScale uses tags to guide and optimize data storage and search, and managing tags impacts both ingest speed and query performance.
- Data sources in LogScale are identified by the unique combination of tags.
- Tags are important for query performance because they allow you to limit what data to search through.
- Each data source's ingest is processed sequentially on one machine in the LogScale cluster, and data is collected in a work-in-progress buffer of ~1MB.
- High-velocity data sources can be handled by creating more data sources by adding a random tag to it, such as #humioAutoShard=0 or #humioAutoShard=1, to artificially split the data source and increase ingest capacity by parallelizing the ingest processing.
- Low-velocity data sources can be handled by periodically merging small segment files into larger ones.
- High variability tags can be handled by limiting the number of data sources by periodically merging data sources with similar tags.

### Can you explain Velocity and Variability?
- High-velocity data sources: These are data sources that are receiving a large amount of data in a short period of time, typically around 10,000 events/sec. An example of this could be a website that receives a lot of traffic and generates a large number of access logs in a short period of time.
- Low-velocity data sources: These are data sources that are receiving a small amount of data in a longer period of time, which can lead to inefficiency. An example of this could be a sensor that generates temperature readings every few minutes.
- High-variability tags: These are data sources that have many distinct combinations of tags, which can lead to having too many data sources, using too many 1MB work-in-progress buffers, and too many directories which may push the limits of the file system. An example of this could be a system that generates logs with many different types of events and many different types of devices or systems, leading to many distinct combinations of tags.


# How fast can you search in LogScale:
https://medium.com/LogScale/how-fast-can-you-grep-256ebfd5513


- To improve search performance, data can be compressed before being searched through '
- Decompressing and searching through the data can be parallelized across multiple cores and machines
- Loading data from disk can be done concurrently with processing, and can be the limiting factor in search performance
- The better the input compresses, the faster the search will be
- This method can be applied to other data processing problems in LogScale's query language, such as extracting data and doing aggregations.


## Searching Fast in LogScale Explained as School Project
Imagine you're a high school student and you have a big research project due in a week. You've been collecting information from various sources like books, articles, and websites and have saved them in a big text document on your computer. You now need to quickly find all the information related to a specific topic from this big document before your deadline.

Now, imagine you have a magic tool that can search through the 1GB text document for you and find all the relevant information in seconds. This tool is called LogScale and it can make your research work a lot faster and easier.

LogScale uses something called "compression" to make the search process faster. It takes the 1GB text document and compresses it into a smaller size using a technique called lz4. This means that instead of scanning through the whole 1GB text, it only needs to scan through a smaller compressed version, which takes less time.

It also uses something called "parallelism" to make the search even faster. It splits the compressed text into smaller chunks and uses multiple cores of your computer to search through these chunks at the same time. This means that instead of using only one core of your computer to search, it can use multiple cores to search simultaneously, which makes the process even faster.

Finally, if the text document is already stored in your computer's memory, it can search even faster because it doesn't have to read it from the disk. This is similar to how you can quickly find a word in a book you're reading because it's already in your memory.

So, in short, LogScale is a powerful tool that uses compression and parallelism to make searching through large text documents faster and more efficient. With LogScale, you can finish your research project in no time and impress your teacher.