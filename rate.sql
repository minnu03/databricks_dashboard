--Query to display the comparison between input and process rate for a table.
select
  appName as app_name,
  name as table_name,
  avg(inputrowspersecond),
  avg(processedrowspersecond),
  date_format(timestamp, 'yyyy-MM-dd HH') as datetime
from
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
where datediff(hour, timestamp, now()) <= {{hours}}
group by app_name, table_name, datetime;
