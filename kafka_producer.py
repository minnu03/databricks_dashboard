event = spark.readStream.format("delta").table("sample_table")
mydf = event.groupBy("timestamp").count()
query = mydf.writeStream.outputMode("complete").format("console").start()

dict_kafka_config = {"kafka properties": "values"}
app_name = "aappname"
pipeline_name = "pipelinename"

spark._jvm.com.adp.ssot.ScalaListener.ListenerObject.add_listener(dict_kafka_config, app_name, pipeline_name)

