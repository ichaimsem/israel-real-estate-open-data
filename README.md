# Israel real estate open data

Open data from [Semerenko Group](https://semerenkogroup.com), an English-speaking real estate brokerage and data publisher
for Israel. Licence: [CC BY 4.0](LICENSE). Built automatically from our registries on 2026-10-18; released weekly.

| Dataset | Rows | What it is | Source |
|---|---|---|---|
| `data/glossary/hebrew-real-estate-terms.csv` | 90 | Hebrew and technical real estate terms with English definitions | our glossary pages |
| `data/places/cities.csv` | 218 | Cities and settlements: official code, Hebrew and English names, aliases, region, our market page | data.gov.il `citiesandsettelments` (Population and Immigration Authority, licence other-open) |
| `data/places/regions.csv` | 25 | Regions (nafot) | same dataset |
| `data/places/neighborhoods.csv` | 1458 | Neighbourhoods as used on our site, linked to the official city code | Semerenko Group taxonomy, not an official list |
| `data/market/recorded-sales-by-city-quarter.csv` | 391 | Recorded home sales by city and quarter: deal count, median and quartile prices in ILS, per-sqm and size medians where 20+ deals carry them (2000-Q2 to 2026-Q3) | Israel Tax Authority transaction records via GovMap layer 16, aggregated by us; cells under 20 deals are dropped and no individual deal is published |
| `data/facts/site-facts.csv` | 94 | Sourced facts behind our wiki and market pages (rates, LTV ceilings, housing starts, tax brackets), each with its official source URL, date and the pages that use it | Bank of Israel, CBS, Tax Authority and other primary publishers |
| `api/openapi.json` | 7 paths | OpenAPI 3.1 specification of our read-only Property API | https://semerenkogroup.com/api/docs/ |

Every CSV has a JSON twin where useful. `datapackage.json` describes fields and sources (Frictionless Data Package).
`data/manifest.json` carries the build time and counts.

## How to cite

Semerenko Group, *Israel real estate open data*, version 2026-10-18, https://github.com/ichaimsem/israel-real-estate-open-data, CC BY 4.0.
Values that come from an official source stay that source's; cite it as given in `source_url`.

## How it is built

`bin/sg-open-data build` in the Semerenko Group HQ repository reads the Supabase registries (places, market observations,
site facts), parses our own glossary pages and fetches the live OpenAPI document, then writes these files. No manual step.
`validate` refuses personal data, keys and any third-party listing data. A weekly job publishes and tags a release.

## What is not here

No listings scraped from other sites, no owner, landlord, agent or client details, no individual sale records, no keys.
The neighbourhood list is ours, not official. Market cells with fewer than 20 recorded deals are omitted.
Recorded-deal prices are what the Tax Authority recorded, not asking prices; they lag the market by weeks to months.

## Contact

hello@semerenkogroup.com · https://semerenkogroup.com
