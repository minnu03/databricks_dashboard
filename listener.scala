class CustomListener(javaMap: java.util.HashMap[String, String], app_name: String, 	pipeline_name: String) extends StreamingQueryListener
	{
   		 val props = new Properties()
   		 val allMap = javaMap.asScala
   		 val topicName = allMap.get("topic_name")
  		  val topicNameStr: String = topicName.getOrElse("")
   		 allMap.remove("topic_name")
  		  allMap.foreach{ case(key:String, value:String) => props.setProperty(key, 												value)}
    		val producer = new KafkaProducer[String, String](props)

    	override def onQueryStarted(event: QueryStartedEvent): Unit = {
     		 println(s"Query started: ${event.id}")
 		   }
           override def onQueryProgress(event: QueryProgressEvent): Unit = {
   		 var jsonString = event.progress.json
 		 val bd = ""","batchDuration":""" + event.progress.batchDuration.toString() + 							""","appName":""" + """"""" + 								app_name + """"""" + 									""","pipeLineName":""" 		+ 							""""""" + pipeline_name + """"""" + "}"
  		  val newJsonString = jsonString.substring(0, jsonString.length-1) + bd
		   val record = new ProducerRecord[String, String](topicNameStr,        											newJsonString)
    		producer.send(record)
   	 }
 	   override def onQueryTerminated(event: QueryTerminatedEvent): Unit = {
  		      println(s"Query Terminated: ${event.id}")
  	  }
	}
