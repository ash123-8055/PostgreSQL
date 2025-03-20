-- Regional Summary
SELECT "WHO_Region", SUM("Confirmed") AS total_cases, SUM("Deaths") AS total_deaths, SUM("Recovered") AS total_recoveries FROM country_wise_latest GROUP BY "WHO_Region" ORDER BY total_cases DESC;

-- Top 10 Countries By COVID-19 Recovery Rates
select "Country_Region", ("Recovered"* 100.0 / "Confirmed") as recovery_rate from country_wise_latest order by recovery_rate DESC limit 10;

--Comparison Of Recovery And Fatality Rates By Country
SELECT "Country_Region", ("Deaths" * 100.0 / "Confirmed") AS death_rate, ("Recovered" * 100.0 / "Confirmed") AS recovery_rate FROM country_wise_latest WHERE "Confirmed" > 0 ORDER BY "Country_Region";

-- Countries with the Lowest Number of COVID-19 Deaths
SELECT "Country_Region", "Deaths" FROM country_wise_latest WHERE "Deaths" > 0 ORDER BY "Deaths" ASC LIMIT 10;

-- Countries with the Highest Number of COVID-19 Cases
SELECT "Country_Region", "Confirmed" FROM country_wise_latest ORDER BY "Confirmed" DESC LIMIT 10;

-- Global Recovery Rate
SELECT (SUM("TotalRecovered")+SUM("NewRecovered")) * 100 / SUM("TotalCases") as recovery_rate from worldometer_data;

-- COVID-19 Trends By Continent
SELECT "Continent" , SUM("TotalCases") as TotalCases, SUM("TotalDeaths") as TotalDeaths, SUM("TotalRecovered") as TotalRecovered from worldometer_data group by "Continent";

-- Continent That Has The Lowest Cases
SELECT "Continent", SUM("TotalCases") AS total_cases FROM worldometer_data GROUP BY "Continent" ORDER BY total_cases ASC LIMIT 1;

-- Recovery Rate by Continent
SELECT "Continent", SUM("TotalRecovered") * 100.0 / SUM("TotalCases") AS recovery_rate FROM worldometer_data WHERE "TotalCases" > 0 GROUP BY "Continent" ORDER BY recovery_rate DESC;

-- 1. To find out the death percentage locally and globally
--Global Death %
SELECT SUM("Deaths") * 100.0 / SUM("Confirmed") AS global_death_percentage FROM country_wise_latest WHERE "Confirmed" > 0;

--Local Death %
SELECT "Country_Region", "Deaths" * 100.0 / "Confirmed" AS death_percentage FROM country_wise_latest WHERE "Confirmed" > 0 ORDER BY "Country_Region";

-- 2. To find out the infected population percentage locally and globally
--Global Infection %
SELECT SUM(cwl."Confirmed")*100.0/ NULLIF(SUM(wd."Population"), 0) AS infect_percent from country_wise_latest cwl left join worldometer_data wd on cwl."Country/Region"=wd."Country/Region";

--Local Infection %
SELECT cwl."Country/Region", (cwl."Confirmed"*100.0 / wd."Population") as infect_percent from country_wise_latest cwl left join worldometer_data wd on cwl."Country/Region"=wd."Country/Region" order by "Country/Region";

--3. To find out the countries with the highest infection rates
SELECT cwl."Country/Region", (cwl."Confirmed"*100.0 / NULLIF(wd."Population",0)) as infect_percent from country_wise_latest cwl left join worldometer_data wd on cwl."Country/Region"=wd."Country/Region" where cwl."Confirmed">0 AND wd."Population" is not null order by infect_percent DESC limit 1;

-- 4. To find out the countries and continents with the highest death counts
SELECT "Country/Region", "Continent", "TotalDeaths" from worldometer_data where "TotalDeaths" is not null order by "TotalDeaths" DESC;

-- 5. Average number of deaths by day (Continents and Countries)
-- global
select "Country/Region", "Date",avg("Deaths") as average_death from full_grouped where "Deaths" is not null group by "Country/Region","Date" order by "Date" desc;
-- local
SELECT fg."Country/Region", wd."Continent", fg."Date", avg(fg."Deaths") as average_death from full_grouped fg left join worldometer_data wd on fg."Country/Region"=wd."Country/Region" where fg."Deaths" is not null group by fg."Country/Region", wd."Continent",fg."Date" order by average_death DESC;

-- 6. Average of cases divided by the number of population of each country (TOP 10)
select "Country/Region", avg("TotalCases"* 100.0 /NULLIF("Population",0)) as average_case from worldometer_data where "Population" is not null group by "Country/Region" order by average_case DESC limit 10;
