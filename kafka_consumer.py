kafka_conf = {"kafka properties": "values"}
df = (spark.readStream.format("kafka").options(**kafka_conf) .load())
df = df.withColumn("value", df["value"].cast("string"))


schema = StructType([
          StructField('addBatch',IntegerType(),True),
          StructField('commitOffsets',IntegerType(),True),
          StructField('getBatch',IntegerType(),True),
          StructField('latestOffset',IntegerType(),True),
          StructField('queryPlanning',IntegerType(),True),
          StructField('triggerExecution',IntegerType(),True),
          StructField('walCommit',IntegerType(),True)]),True),
      StructField('stateOperators',
        ArrayType(StructType([
          StructField('operatorName',StringType(),True),
          StructField('numRowsTotal',IntegerType(),True),
          StructField('numRowsUpdated',IntegerType(),True),
          StructField('allUpdatesTimeMs',IntegerType(),True),
          StructField('numRowsRemoved',IntegerType(),True),
          StructField('allRemovalsTimeMs',IntegerType(),True),
          StructField('commitTimeMs',IntegerType(),True),
          StructField('memoryUsedBytes',IntegerType(),True),
          StructField('numRowsDroppedByWatermark',IntegerType(),True),
          StructField('numShufflePartitions',IntegerType(),True),
          StructField('numStateStoreInstances',IntegerType(),True),
          StructField('customMetrics',
            StructType([
              StructField('loadedMapCacheHitCount',IntegerType(),True),
              StructField('loadedMapCacheMissCount',IntegerType(),True),
              StructField('stateOnCurrentVersionSizeBytes',IntegerType(),True)]),True)])),True),
      StructField('sources',StringType(),True),
      StructField('sink',
        StructType([
          StructField('description',StringType(),True),
          StructField('numOutputRows',IntegerType(),True)]),True),
      StructField('batchDuration', IntegerType(), True),
      StructField('app',StringType(),True),
      StructField('created_at',TimestampType(),True),
      StructField('created_by',StringType(),True),
      StructField('updated_by',StringType(),True),
      StructField('schema_id',StringType(),True),
      StructField('table_name',StringType(),True)
      ])

