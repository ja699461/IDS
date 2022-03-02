use ids2db;
SET SQL_SAFE_UPDATES = 0;
DELETE FROM Life_Expectancy
WHERE population = 0;

select
	@avg_AM:=avg(Adult_Mortality)
from Life_Expectancy;


UPDATE Life_Expectancy
SET Adult_Mortality = @avg_AM
where Adult_Mortality = 0;

select
	@avg_GDP:=avg(GDP)
from Life_Expectancy;


UPDATE Life_Expectancy
SET GDP = @avg_GDP
where GDP = 0;

select
	@avg_GDP:=avg(GDP)
from Life_Expectancy;


UPDATE Life_Expectancy
SET GDP = @avg_GDP
where GDP = 0;

select
	@avg_SC:=avg(Schooling)
from Life_Expectancy;


UPDATE Life_Expectancy
SET Schooling = @avg_SC
where Schooling = 0;

select
	@avg_AL:=avg(Alcohol)
from Life_Expectancy;


UPDATE Life_Expectancy
SET Alcohol = @avg_AL
where Alcohol = 0;

SELECT count(distinct Country)
from Life_Expectancy;

SELECT avg(Adult_Mortality),Country
from Life_Expectancy
group by Country
order by avg(Adult_Mortality) asc;

SELECT avg(Population),Country
from Life_Expectancy
group by Country
order by avg(Population) asc;

SELECT avg(GDP),Country
from Life_Expectancy
group by Country
order by avg(GDP) asc;

SELECT avg(Schooling),Country
from Life_Expectancy
group by Country
order by avg(Schooling) asc;

SELECT avg(Alcohol),Country
from Life_Expectancy
group by Country
order by avg(Alcohol) desc;

SELECT Life_Expectancy,Population
from Life_Expectancy
order by Population desc;