select count(*) as 'no of flights',manufacturer
from planes
left join flights
on planes.tailnum=flights.tailnum
group by 2
order by 1 desc;


select count(a.flight), b.manufacturer from flights as a left join planes as b
on a.tailnum=b.tailnum
group by 2
order by 1 desc;