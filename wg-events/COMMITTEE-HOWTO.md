# Committee Member How-To

Step-by-step guide for wg-events committee members handling grant
applications, from arrival through reimbursement.

---

## 1. Moderating Incoming Messages

The events-grants@ list is moderated. Non-subscribers can send to it
but their messages are held for moderator approval.

### Check for held messages

Visit:

    https://webmod.apache.org/

Log in with your Apache credentials. Select the `events-grants` list.
Held messages appear in queue. For each:

- **Approve** if it's a legitimate application (matches one of our
  subject formats: `[TRAVEL GRANT]`, `[MEETUP]`, `[SPRINT]`,
  `[SUMMIT]`, `[MATERIALS]`)
- **Reject** if it's spam or clearly not an application
- **Hold** if you're unsure -- another moderator will see it

---

## 2. Acknowledging a New Application

When a new application arrives on-list:

1. Reply on-list within 5 business days:

```
Subject: Re: [TRAVEL GRANT] Name -- Conference, City, Date

Hi [Name],

Thank you for your application. I've received it and will begin
evaluation. You can expect a decision within 15 business days.

If we need any additional information, we'll reply to this thread.

-- [Your name], wg-events committee
```

2. Create the SVN record (see Section 5 below).

---

## 3. Evaluating a Speaker Travel Application

### 3a. Cost estimation (using the SKILL)

Use public flight/hotel search to verify the applicant's stated costs.
You can do this manually or use the AI-assisted skill.

**Manual method:**

1. Go to https://flights.google.com
2. Search: origin city → destination city, dates matching ~2 days
   before conference start to ~1 day after end
3. Note the median economy fare (not cheapest redeye, not business)
4. Go to https://www.booking.com or Google Hotels
5. Search the conference city for those dates
6. Look for 3-star hotels within 3 miles of the venue
7. Note the median nightly rate

**AI-assisted method:**

If you have an AI assistant available, you can ask it to estimate
travel costs using the procedure in SKILL.md:

```
Estimate travel costs for a speaker travel grant:
- From: [origin city]
- To: [destination city]  
- Conference dates: [dates]
- Hotel nights: [N]
- Venue address: [address]

Use public sources only (Google Flights, Booking.com, Skyscanner).
Produce a formatted cost estimate per the SKILL.md template.
```

The assistant should search public sources and produce a formatted
estimate. Verify the output against your own spot-check before posting.

**Post the estimate to the list:**

```
Subject: Re: [TRAVEL GRANT] Name -- Conference, City, Date

COST ESTIMATE
=============
Generated: [today's date]
Source: Google Flights, Booking.com

Flight (economy, median fare):      $[X]
Hotel ([N] nights x $[rate]):       $[X]
Ground transport (standard):        $[X]
Conference registration:            $[X] (or "waived for speakers")
                                    -----
ESTIMATED TOTAL:                    $[X]

Applicant's stated total:           $[X]
Variance:                           [X]% [over/under]

ASSESSMENT: [Reasonable / High / Low]
```

### 3b. Scoring

Score the application using the 5 criteria from `evaluation-criteria.md`.
Post your evaluation to the list:

```
Subject: Re: [TRAVEL GRANT] Name -- Conference, City, Date

EVALUATION: [Applicant Name] -- [Conference], [Date]
==================================================

Need:                    [0-3] -- [one-line rationale]
Apache Relevance:        [0-3] -- [one-line rationale]
Conference Quality:      [0-3] -- [one-line rationale]
Geographic/Demographic:  [0-3] -- [one-line rationale]
Cost Reasonableness:     [0-3] -- [one-line rationale]
                         -----
TOTAL:                   [X/15]

RECOMMENDATION: [APPROVE / DENY / DISCUSS]
AMOUNT: $[recommended amount]
NOTES: [any conditions]
```

### 3c. Decision

- **Two evaluations agree (score >= 8):** Approved. Chair posts
  approval notice. 72-hour objection window on list.
- **Disagreement:** Full committee discussion on-list. Majority vote.
- **Chair breaks ties.**

### 3d. Inter-continental override

If the travel crosses continents:
- Standard evaluation is not sufficient
- Requires explicit `+1` from a majority of committee members
- Chair posts: "This is inter-continental travel. Requesting override
  votes. +1 to approve, -1 to deny."
- 5 business day vote window

---

## 4. Evaluating Meetup/Sprint/Materials Requests

These are simpler:

**Meetups (<$400):**
- Single committee member can approve
- Reply on-list: "Approved. Please submit receipts after the event."
- 48-hour objection window

**Sprints ($1,800):**
- Two committee members must confirm
- Check: Are experienced reviewers confirmed to attend?
- Reply on-list with approval + any conditions

**Summits ($6,000):**
- **First:** Verify the PMC approval link is valid (click it, confirm
  the PMC actually discussed and approved)
- Full committee scores it (same rubric adapted for events)
- Requires ComDev PMC vote (since >$2,000)
- Chair posts recommendation to dev@community with `[VOTE]` subject

**Materials (pre-approval):**
- Under $100: single committee member approves
- $100-$200: single confirmation sufficient
- Reply: "Pre-approved for up to $[X]. Purchase and submit receipts."

---

## 5. Updating the SVN Repository

### One-time setup

Check out the private repo (requires ComDev PMC membership):

```bash
svn checkout https://svn.apache.org/repos/private/pmc/comdev/events-grants \
  ~/comdev-private/events-grants
```

### Creating a new grant record

When you acknowledge an application, create the record file:

```bash
cd ~/comdev-private/events-grants/FY2027/speaker-travel/
# (or meetups/, sprints/, summits/, materials/ as appropriate)

# Create from template
cp ../../templates/speaker-travel.txt 2027-03-garcia-kubecon-eu.txt

# Edit -- fill in applicant details, set Status: applied
vi 2027-03-garcia-kubecon-eu.txt

# Commit
svn add 2027-03-garcia-kubecon-eu.txt
svn ci -m "[events-grants] [speaker-travel] garcia-kubecon-eu: application received"
```

### Updating status after approval

```bash
cd ~/comdev-private/events-grants/FY2027/speaker-travel/
vi 2027-03-garcia-kubecon-eu.txt
# Change Status: applied → approved
# Fill in: Evaluated by, Score, Decision, Decision date, Approved amount

svn ci -m "[events-grants] [speaker-travel] garcia-kubecon-eu: APPROVED \$2800"
```

### Updating status after reimbursement

```bash
vi 2027-03-garcia-kubecon-eu.txt
# Change Status: approved → reimbursed
# Fill in: Actual spend, Receipts filed, Reimbursed date, Deliverable URL

svn ci -m "[events-grants] [speaker-travel] garcia-kubecon-eu: REIMBURSED \$2650"
```

### Updating summary.yml

After any approval or reimbursement, update the ledger:

```bash
cd ~/comdev-private/events-grants/FY2027/
vi summary.yml
# Add/update the grant entry in the relevant category
# Recompute totals

svn ci -m "[events-grants] totals: updated after garcia approval"
```

Or use the helper script (see Section 7 below).

---

## 6. Notifying the Applicant

### Approval notification

```
Subject: Re: [TRAVEL GRANT] Name -- Conference, City, Date

Hi [Name],

Your speaker travel grant has been approved for $[amount].

REIMBURSEMENT PROCESS:
1. Attend the conference and give your talk
2. Within 30 days, provide at least one deliverable:
   - Blog post, published slides, video link, or trip report
3. Within 30 days, email your receipts to this list:
   - Economy airfare receipt/confirmation
   - Hotel receipt (itemized -- room + tax only, no minibar)
   - Ground transport receipts (if claiming)
4. We will process reimbursement within 30 days of receiving
   complete receipts

IMPORTANT:
- Reimbursement covers actual costs up to $[amount]
- Keep all receipts (photos/scans are fine)
- Receipts must be itemized (credit card statements alone are
  not sufficient)

Congratulations, and thank you for representing Apache!

-- [Your name], wg-events committee
```

### Denial notification

```
Subject: Re: [TRAVEL GRANT] Name -- Conference, City, Date

Hi [Name],

Thank you for your application. Unfortunately, we are unable to
approve this request. The primary factors were:

- [Brief, specific reasons -- e.g., "The estimated costs
  significantly exceeded market rates for this route" or
  "Inter-continental travel was not approved by committee override"]

Suggestions for future applications:
- [Specific, actionable -- e.g., "Consider applying for a
  same-continent conference" or "Provide booking screenshots to
  support your cost estimates"]

We encourage you to apply again in the future.

-- [Your name], wg-events committee
```

---

## 7. Helper Scripts

Scripts live in `wg-events/bin/`. Both use inline PEP 723 metadata so
they run with `uv run` (no manual install step).

### bin/update-summary.py

Recalculates `summary.yml` totals from individual grant `.txt` files.

```bash
cd ~/comdev-private/events-grants/
uv run /path/to/comdev-working-groups/wg-events/bin/update-summary.py --fy FY2027
svn ci -m "[events-grants] totals: recalculated from grant files"
```

### bin/validate-application.py

Quick sanity check on a pasted application form -- verifies all
required fields are present and filled in.

```bash
# From clipboard
pbpaste | uv run /path/to/comdev-working-groups/wg-events/bin/validate-application.py

# From a saved file
uv run /path/to/comdev-working-groups/wg-events/bin/validate-application.py < application.txt
```

Output: lists any missing or blank required fields, or confirms the
form is complete.

---

## 8. Quarterly Reporting

Every quarter, the chair produces a public report for
dev@community.apache.org. This shows aggregate numbers only -- no
names, no dollar amounts for individual grants.

```bash
# Generate from summary.yml
cd ~/comdev-private/events-grants/FY2027/
uv run bin/update-summary.py --fy FY2027
# Then manually write the report email:
```

**Report template:**

```
Subject: [wg-events] Q[N] FY2027 Report

Hi dev@,

Here's the quarterly summary for the events grants program:

SPEAKER TRAVEL GRANTS
  Awarded this quarter: [N]
  Total awarded FY to date: [N] of [capacity]
  Continents represented: [list]

COMMUNITY EVENTS FUNDED
  Meetups this quarter: [N]
  Sprints this quarter: [N]
  Summits this quarter: [N]
  Total events FY to date: [N]
  Countries represented: [list]

DELIVERABLES PRODUCED
  Blog posts: [N]
  Published slide decks: [N]
  Trip reports: [N]

[Optional: brief narrative about notable outcomes]

Full details are in the private PMC records.

-- [Chair name], wg-events
```

---

## 9. Reimbursement Mechanics

Once receipts are received and validated:

1. Verify receipts match the approved scope (economy travel,
   mid-range hotel, no alcohol, no upgrades)
2. Calculate reimbursement amount (lesser of: actual spend or
   approved amount)
3. Update SVN record to `receipts_filed`
4. Email ASF Treasurer (treasurer@apache.org) with:
   - Recipient name and email
   - Amount to reimburse
   - Brief description ("Speaker Travel Grant -- [Conference]")
   - Attach receipts
5. Treasurer processes payment
6. Once confirmed, update SVN record to `reimbursed`
7. Update summary.yml

---

## 10. Annual Checklist

At the start of each fiscal year:

```bash
cd ~/comdev-private/events-grants/
mkdir FY20XX
mkdir FY20XX/{speaker-travel,meetups,sprints,summits,materials}
cp FY2027/summary.yml FY20XX/summary.yml
# Edit: reset all grants lists to empty, reset totals to 0,
# update budget numbers per PMC decision
vi FY20XX/summary.yml
svn add FY20XX
svn ci -m "[events-grants] FY20XX: initialized"
```

At end of fiscal year:
- Ensure all outstanding grants are resolved (reimbursed or withdrawn)
- Produce final annual summary
- Report unspent funds to ComDev PMC
- Archive completed FY (no deletion -- history stays in SVN)
