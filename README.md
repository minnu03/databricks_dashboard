Project Overview

Data flow metrics visualization is a project designed to enhance the monitoring and
analytics capabilities of data processing pipelines. Dataflow ingestion jobs are spark structured
streaming jobs, which processes and transforms vast volumes of data continually. These streaming
jobs emit critical performance metrics, such as input Rate, Process Rate, Batch Duration etc. These
metrics are vital to determine the progress and latency of streaming pipelines.

Currently, These metrics are only accessible through Spark User Interface (Spark UI) for each
pipeline. However there are a few limitations to this approach. These metrics are reset every time
the pipeline restarts, making it challenging to maintain a historical perspective of pipeline
performance. Additionally, There are multiple pipelines for a single data source and there exists no
unified view to query or view the metrics.

In a bug identified in the Databricks, the pipeline runs fine but there is no progress made by
the pipeline, which gives a false impression that the pipeline is working fine. There is no log kept as
to which batch last ran successfully before the pipeline stopped progressing.

The primary objective of this project is to resolve these limitations by centralising these
metrics into a dedicated delta table, where all the metrics are stored consistently regardless of
pipeline restart. Developing dashboard and visualizations provides real time insights to maintain
health and efficiency of data processing streams.


**NOTE: This project is done as a part of internship. Hence the files uploaded are for demo purposes only and does not include all the code to build dashboard.**
