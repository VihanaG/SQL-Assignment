select sum(arr_delay),dest
from flights
group by 2
order by 1 desc;