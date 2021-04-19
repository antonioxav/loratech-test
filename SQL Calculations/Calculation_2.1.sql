CREATE OR REPLACE FUNCTION month(date) RETURNS integer
AS $$
      SELECT extract(MONTH FROM $1)::integer;
$$ LANGUAGE sql IMMUTABLE;

CREATE OR REPLACE FUNCTION year(date) RETURNS integer
AS $$
      SELECT extract(YEAR FROM $1)::integer;
$$ LANGUAGE sql IMMUTABLE;

SELECT    imported_closes.ticker, MONTH(imported_closes.day), YEAR(imported_closes.day), max(imported_closes.price),min(imported_closes.price),AVG(imported_closes.price) 
FROM      imported_closes, monthly_members
WHERE	  imported_closes.ticker = monthly_members.ticker 
			AND monthly_members.index='HK' 
			AND imported_closes.day<=TO_DATE('2019-12-31', '%Y %M %D') 
			AND imported_closes.day>=TO_DATE('2008-01-01', '%Y %M %D')
GROUP BY  imported_closes.ticker, YEAR(imported_closes.day), MONTH(imported_closes.day)
ORDER BY  imported_closes.ticker, YEAR(imported_closes.day), MONTH(imported_closes.day);