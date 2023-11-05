--Query to display the time a pipeline was last run with average metrics.
	select
  app_name,  pipeline_name,  last_run,  average_input_rate,  average_process_rate
from
  (
    select
      appName as app_name,
      pipeLineName as pipeline_name,
      date_format(max(timestamp), 'yyyy-MM-dd HH:mm:ss') as last_run,
      avg(inputrowspersecond) as average_input_rate,
      avg(processedrowspersecond) as average_process_rate
    from
      (
        select *  from  (
            select
              *,  row_number() over ( partition by batchid, name	
                order by
                  `timestamp` desc
              ) as rn
            from   ssot_platform_meta_fit.streaming_query_metrics
          ) tmp
        where rn = 1
      )
    group by app_name, pipeline_name
    order by last_run
  ) where datediff(hour, last_run, now()) >= {{hours}}

