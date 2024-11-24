<!-- Update title header and author list -->

# Review for NWBEP000: Title

## Review Authors
- Name1, Affiliation1 (facilitator)
- Name2, Affiliation2
- Name3, Affiliation3
- Name4, Affiliation4

## Summary

<!-- Write summary here including points of merit and concern -->



<!-- List specific concerns as separate sections following this format. These can include
points of disagreement among the authors, where some authors are concerned about a point
and others are not. For example:

## Concern 1: Time units are inconsistent with NWB standard and best practices

The proposed new neurodata type `TimestampVectorData` stores timestamps in milliseconds from
a user-specified starting time stored in the type. This is inconsistent with how timestamps
are stored in all other NWB objects, which is in seconds from the `timestamps_reference_time`
stored at the root of the file, so that all timestamps in the file are aligned to the same
clock.

**Proposed resolution**: Units of the proposed type `TimestampVectorData` should be
changed to seconds from the file's timestamps reference time.

## Concern 2: Space efficiency of design

Two of the authors are concerned that under the proposed design, the same values would be
repeated in the table, potentially thousands of times, if there are thousands of events. 
This scheme is inefficient in space and is susceptible to user error that results in
inconsistent data.
...

The other two authors believe the impact of this inefficiency is negligible for the most common
use cases and is tolerable given the convenience of inspecting the file and not having to
resolve foreign keys.
...
-->

## Recommendation

<!-- Select one of: Accept, Accept with Minor Changes, Request Major Changes, Reject -->
