# SKILL: Travel Grant Cost Estimation

## Purpose

When a Speaker Travel Grant application arrives, a committee member
(or an AI assistant) uses this procedure to produce an independent
cost estimate for the proposed trip. This estimate is compared against
the applicant's stated costs to check reasonableness.

## Inputs (from application form)

- Origin city/country
- Destination city/country
- Conference dates (to determine travel dates)
- Number of hotel nights needed

## Estimation Procedure

### 1. Airfare Estimate

Use **public flight search engines** to estimate economy class airfare:

- **Google Flights** (https://flights.google.com): Search origin →
  destination for dates ~2 days before conference start and ~1 day
  after conference end. Note the median economy fare.
- **Skyscanner** (https://skyscanner.com): Cross-reference for the
  same route/dates.
- **Kiwi.com** (https://kiwi.com): Useful for multi-city or budget
  carrier routes.

Record:
- Cheapest reasonable fare (not 3-stop redeyes)
- Median fare across options
- Use median as the estimate

**Rules of thumb (2026):**
- US domestic: $250-600 depending on route/lead time
- US to Europe: $600-1200
- US to Asia: $800-1500
- Intra-Europe: $100-400
- Within Asia: $200-600
- Any route to/from remote locations: add 30% premium

### 2. Hotel Estimate

Use **public hotel search** to estimate mid-range accommodation:

- **Google Hotels** or **Booking.com**: Search for the conference
  city on the conference dates.
- Look for: 3-star hotel within reasonable distance of venue
- If the conference has a hotel block rate published on their
  website, use that.

Record:
- Conference hotel block rate (if published)
- Median 3-star rate near venue
- Use whichever is lower as the estimate

**Rules of thumb (2026):**
- US major cities: $150-250/night
- US smaller cities: $100-150/night
- European cities: $120-200/night
- Asian cities: $60-150/night
- Conference hotels (block rate): often 10-20% below market

### 3. Ground Transport

Standard estimates (don't research individually):
- Airport transfers (round trip): $50-100 (US/Europe), $20-50 (Asia)
- Local transit during conference: $20-50

### 4. Conference Registration

- Check conference website for registration fee
- If early-bird is still available, use that
- Many conferences waive fees for speakers -- check and note

### 5. Compile Estimate

```
COST ESTIMATE: [Applicant] -- [Conference]
==========================================
Generated: [date]
Source: Public fare search (Google Flights, Booking.com)

Flight (economy, median fare):      $[X]
Hotel ([N] nights x $[rate]):       $[X]
Ground transport (standard):        $[X]
Conference registration:            $[X] (or "waived for speakers")
                                    -----
ESTIMATED TOTAL:                    $[X]

Applicant's stated total:           $[X]
Variance:                           $[X] ([over/under] estimate)

ASSESSMENT: [Reasonable / High / Low]
NOTES: [any context -- peak dates, limited routes, etc.]
```

### 6. Post to List

Post the estimate to events-grants@ as a reply to the application
thread. The evaluating committee members use this as input for the
"Cost Reasonableness" criterion (0-3 score).

## Variance Guidelines

- Within 15% of estimate: Reasonable (score 3)
- 15-30% over estimate: Slight premium, justifiable? (score 2)
- 30-50% over estimate: Needs explanation (score 1)
- >50% over estimate: Ask applicant to clarify or revise (score 0)

## Tools NOT to Use

- Do NOT use employer-internal travel tools (AWS Travel, Concur, etc.)
- Do NOT use private/corporate rate databases
- All estimates must be reproducible from public sources so the
  applicant could verify the estimate themselves

## When to Skip Estimation

- If the requested amount is under $1,000, a formal cost estimate is
  optional (committee member can approve based on face-value
  reasonableness)
- If the applicant provides booking screenshots showing actual prices,
  those can substitute for an independent estimate
