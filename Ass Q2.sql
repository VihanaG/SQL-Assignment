select sum(a.air_time) as'hours spend',b.manufacturer from flights as a inner join planes as b on a.tailnum=b.tailnum
group by 2
order by 1 desc;