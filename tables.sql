-- Query to display table level average metrics.
select
  appName as app_name, pipelinename as pipeline_name,
  concat(
    '<a href="https://databricks.com/sql/dashboards/b2186018-c3f6-413e-a7e1-03a6c217d998?edit&f_37c7282a-1960-491a-a4d0-125eeabea250=',
    name,
    '&o=5680988378023941&p_hours=',
    {{hours}},
    '"',
    'target="_blank">',
    name
  ) as table_name, avg(inputRowsPerSecond) as average_input_rate,
  avg(processedRowsPerSecond) as average_process_rate
from (
    select  * from (
        select *, row_number() over ( partition by batchid,  name
            order by `timestamp` desc
          ) as rn
        from ssot_platform_meta_fit.streaming_query_metrics
      ) tmp
    where rn = 1
  )
where datediff(hour, timestamp, now()) >= {{hours}}
group by app_name, pipeline_name, table_name
order by app_name;
