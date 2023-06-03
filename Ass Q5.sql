select sum(a.distance),b.manufacturer from flights as a left join planes as b
on a.tailnum=b.tailnum
group by 2
order by 1 desc;