select a.tailnum as 'plane', sum(b.air_time)
from planes as a inner join flights as b
on a.tailnum=b.tailnum
group by 1
order by 2 desc;