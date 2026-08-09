# wg-events: Event Support & Speaker Travel (PROPOSED)

> **Status: PROPOSED / RFC**
>
> This working group and its processes are not yet funded or active.
> This document describes how we believe the program could work if
> budget is approved. Nothing here is final.
>
> **Discussion of any aspect of this proposal should go to
> dev@community.apache.org** -- not to this repo's issue tracker.
> Please use subject prefix `[wg-events]` for threading.

---

## Charter (proposed)

wg-events manages the intake, evaluation, and disbursement of ComDev
event support funds. This includes:

- Evening meetup funding for ALC chapters and project communities
- Contributor sprint underwriting
- Single-day project summit support
- Speaker Travel Grants for non-Apache conferences
- Event materials reimbursement

## Structural Rules

- **Chair:** [TBD -- elected by WG members, confirmed by ComDev PMC]
- **Membership:** Open to any ASF committer; active participation
  required (at least one action per quarter)
- **Sunset clause:** If this WG produces no funded events in 6 months,
  it dissolves and responsibility reverts to the ComDev PMC directly
- **Reporting:** Quarterly summary to dev@community.apache.org showing
  events funded, amounts disbursed, and outcomes reported
- **Decision-making:** Lazy consensus on the WG private list for
  routine grants; PMC vote required for contingency spend

## Coordination

This WG operates in close coordination with:

- **VP Conferences / planners@apachecon.com** -- for events co-located
  with Community Over Code or using ApacheCon infrastructure
- **Travel Assistance Committee (TAC)** -- Speaker Travel Grant criteria
  and process should align with TAC precedent
- **VP Brand Management** -- trademark review for event naming

## Programs

| Program | Process |
|---------|---------|
| Evening meetups | [meetup-request.md](meetup-request.md) |
| Contributor sprints | [sprint-request.md](sprint-request.md) |
| Single-day summits | [summit-request.md](summit-request.md) |
| Speaker Travel Grants | [speaker-travel-grant.md](speaker-travel-grant.md) |
| Event materials | [materials-reimbursement.md](materials-reimbursement.md) |

Budget allocations across these programs are managed internally by the
ComDev PMC and are not published to avoid gaming the system.

## Mailing List

All grant requests and processing happen on a private mailing list:

    events-grants@community.apache.org

Subscribers: ComDev PMC members + Travel Grant Committee members (TBD).

Private because applications may contain personal financial information
(employer status, inability to self-fund, etc.) that applicants should
not be required to share publicly.

**All processing happens on-list in structured formats** defined in
this directory. No side-channel approvals.

## Record-Keeping

Actual grant amounts, award decisions, and financial records are stored
in the private ComDev PMC SVN repository:

    https://svn.apache.org/repos/private/pmc/comdev/

This information is not public. Only aggregate statistics (number of
events funded, number of grants awarded) are reported in the quarterly
summary to dev@community.apache.org.

## Eligibility (all programs)

This fund targets projects and contributors who **cannot get support
elsewhere**:

- Individual contributors whose employers don't cover travel/events
- Communities growing in regions without big-tech presence
- ALC chapters hosting regular community events

**Not eligible:**

- Projects with multiple vendor sponsors already funding their events
- Speakers whose employers routinely cover conference travel
- Events with existing corporate sponsorship covering costs

Principle: **ASF resources go where the market won't.**

## Files in this directory

| File | Purpose |
|------|---------|
| README.md | This file -- WG charter and overview |
| speaker-travel-grant.md | Full process for Speaker Travel Grants |
| application-form.md | Copy-paste form for applicants |
| evaluation-criteria.md | How the committee evaluates applications |
| meetup-request.md | Process for meetup funding requests |
| sprint-request.md | Process for sprint funding requests |
| summit-request.md | Process for summit funding requests |
| materials-reimbursement.md | How to get event materials reimbursed |
| svn-data-format.md | Private SVN directory structure and record formats |
| summary-format.md | summary.yml schema reference and field documentation |
| COMMITTEE-HOWTO.md | Step-by-step operations guide for committee members |
| SKILL.md | AI-assisted cost estimation skill |
