# NWBEP004: Optical Devices and Microscopy

## Quick links:


- **NWBEP004**: Optical Devices and Microscopy
- **Lead**: Alessandra Trapani (CatalystNeuro)
- **Extensions**: [ndx-ophys-devices](https://github.com/catalystneuro/ndx-ophys-devices), [ndx-microscopy](https://github.com/catalystneuro/ndx-microscopy)
- **Google Doc**: https://docs.google.com/document/d/1-dVEBuacvoM3hZk8GeinmQpNF4yh3Uvxz7WOWUpdvFY/edit
- **Local .md copy**: [./doc/NWBEP004.md](./doc/NWBEP004.md)
- **Reviews**: [nwbep-review PR #7](https://github.com/nwb-extensions/nwbep-review/pull/7)

## Timeline

| Date | Event |
|------|-------|
| 2025-05-30 | Alessandra submitted updated NWBEP004 document for external review |
| 2025-06-16 | YOH sent review invitations (CS, RD, GM, Dan Birman) |
| 2025-09-30 | Virtual meeting with reviewers and Alessandra (video: `2025-09-30_NWB-TAB-NWBEP004-review.mp4`, available from @yarikoptic on request) |
| 2025-10-09 | Reviews posted to [nwbep-review PR #7](https://github.com/nwb-extensions/nwbep-review/pull/7) |
| 2025-12-03 | Alessandra delivered revised Google Doc (v0.4.0) and PRs addressing feedback |
| 2026-03-17 | @yarikoptic emailed Alessandra with [clarification questions](./notes/20260317-questions.md) |
| 2026-03-26 | Alessandra completed her changes in response to reviews |

---

## Review summaries

### Reviewer: Carsen Stringer (CS)

**Affiliation**: Janelia / HHMI
**ORCID**: 0000-0002-9229-4100
**Overall**: Very positive. All 12 evaluation checkboxes marked. Recommends inclusion.

| ID | Concern | Status | Where Addressed |
|----|---------|--------|-----------------|
| CS-1 | ["OpticalLensModel" vs "OpticalLens" confusing — rename to "ObjectiveLensModel"](https://github.com/nwb-extensions/nwbep-review/pull/7/files#diff-1e0f44955b22571c0fc8b050393b0f72287ebd9bd10282c719dfa619cf98ab86R31) | **ADDRESSED** | ndx-ophys-devices [PR #25](https://github.com/catalystneuro/ndx-ophys-devices/pull/25): renames OpticalLens → ObjectiveLens + consolidates StereotacticPositioning. ndx-microscopy [PR #73](https://github.com/catalystneuro/ndx-microscopy/pull/73): ObjectiveLens rename + ndx-ophys-devices bumped to 0.4.0 |
| CS-2 | ["Good examples of the ophys-devices would be very helpful, perhaps for some standard microscopes used in the field"](https://github.com/nwb-extensions/nwbep-review/pull/7/files#diff-1e0f44955b22571c0fc8b050393b0f72287ebd9bd10282c719dfa619cf98ab86R44) | **UNCLEAR** | Not visible in PR descriptions. May be in updated Google Doc sections 5.1/5.2. **Need to verify with Alessandra.** |

---

### Reviewer: Robin Dard (RD)

**Affiliation**: EPFL
**Overall**: Positive but detailed. 11 of 12 checkboxes marked (left **Alternatives** unchecked without explanation).

| ID | Concern | Status | Where Addressed |
|----|---------|--------|-----------------|
| RD-1 | [Detailed use case for multi-plane (ETL, 3 depths) + multi-channel (1 indicator + 2 anatomical markers) — how to use new datatypes and link them](https://github.com/nwb-extensions/nwbep-review/pull/7/files#diff-d43b322f0f7103054c56fa1c48d0206b8572c27d550d1353ad17b399b86abd7aR28-R34) | **UNCLEAR** | May be addressed in updated Google Doc examples. Not evident from PR descriptions. **Need to verify with Alessandra.** |
| RD-2 | [Schematic diagram of data types with mandatory/optional fields and links between them](https://github.com/nwb-extensions/nwbep-review/pull/7/files#diff-d43b322f0f7103054c56fa1c48d0206b8572c27d550d1353ad17b399b86abd7aR47) (like [PyNWB ophys tutorial](https://pynwb.readthedocs.io/en/stable/tutorials/domain/ophys.html)) | **UNCLEAR** | Documentation/Google Doc concern. Not visible in PRs. **Need to verify with Alessandra.** |
| RD-3 | [Optional link to `Images` object (`pynwb.base.Images`) for annotated microscope/optical path scheme in `MicroscopyRig`](https://github.com/nwb-extensions/nwbep-review/pull/7/files#diff-d43b322f0f7103054c56fa1c48d0206b8572c27d550d1353ad17b399b86abd7aR53) | **PARTIALLY ADDRESSED?** | ndx-microscopy [PR #74](https://github.com/catalystneuro/ndx-microscopy/pull/74) adds `PlanarMicroscopyStaticImage` and `VolumetricMicroscopyStaticImage`. This adds static image support but may not directly address the `MicroscopyRig` → `Images` link. **Need to verify.** |
| RD-4 | [FAIR concern: rig metadata should be easily repeated across NWB files from same rig](https://github.com/nwb-extensions/nwbep-review/pull/7/files#diff-d43b322f0f7103054c56fa1c48d0206b8572c27d550d1353ad17b399b86abd7aR52-R53) | **NOTED** | Design philosophy comment. The `MicroscopyRig` + `MicroscopyExperimentMetadata` approach may address this implicitly. |
| RD-ALT | [Left **Alternatives** checkbox unchecked](https://github.com/nwb-extensions/nwbep-review/pull/7/files#diff-d43b322f0f7103054c56fa1c48d0206b8572c27d550d1353ad17b399b86abd7aR15) (only reviewer to do so) | **NOTED** | No specific comment explaining why. Minor. |

---

### Reviewer: Giacomo Mazzamuto (GM)

**Affiliation**: lens.unifi.it
**ORCID**: 0000-0003-3077-3904
**Overall**: Positive but brief. Left ALL checkboxes unchecked (style difference, not substantive). Recommends inclusion "upon further refinement where appropriate."

| ID | Concern | Status | Where Addressed |
|----|---------|--------|-----------------|
| GM-1 | ["Small suggestions added as comments in the shared draft"](https://github.com/nwb-extensions/nwbep-review/pull/7/files#diff-4c67c5bd305d65baa14feb4e6e68f0a0838232d5879fe26ac2a89d6dedd728b0R21-R23) — no specific written concerns in the review form | **LIKELY ADDRESSED** | Comments were inline in the Google Doc. The .docx export (2026-03-17) shows only 1 unresolved comment (from YOH), meaning all reviewer comments were **resolved** by Alessandra. However, resolved comments are not preserved in exports, so we cannot verify content. Alessandra said Dec 3 revision contains "all corrections from reviewers". **Need Alessandra to confirm or summarize GM's inline comments.** |
| GM-CB | Left ALL evaluation criteria checkboxes unchecked | **NOTED** | Style difference — his text is positive and recommends inclusion. Not a substantive concern. |

---

### Reviewer: Dan Birman (DB)

**Affiliation**: Allen Institute
**Status**: **NO REVIEW SUBMITTED**

| Date | Event |
|------|-------|
| 2025-06-16 | YOH sent invitation |
| 2025-06-16 | Dan replied: "Yes I can help review for this proposal" |
| 2025-09-30 | Participated in review panel meeting |
| 2025-10-02 | YOH requested review submission |

**Action needed**: Re-invite Dan Birman to submit review alongside the re-review round.

---

## Summary of PRs (Dec 2025 revision)

All PRs are **still OPEN** (not merged) as of 2026-03-17.

### ndx-ophys-devices

| PR | Title | Status | Key Changes |
|----|-------|--------|-------------|
| [#25](https://github.com/catalystneuro/ndx-ophys-devices/pull/25) | NWBEP004_reviews | Open (1 approval from pauladkisson, h-mayorquin pending) | OpticalLens → ObjectiveLens rename; unified `StereotacticPositioning` replacing `FiberInsertion`/`LensPositioning`; new coordinate/angle attributes |

### ndx-microscopy

| PR | Title | Status | Key Changes |
|----|-------|--------|-------------|
| [#73](https://github.com/catalystneuro/ndx-microscopy/pull/73) | NWBEP0004 reviews - part 1 | Open (approved by h-mayorquin) | ObjectiveLens rename; `LabMetadataObject` for `VirusInjection`/`Virus`; fix ImagingSpace redundancy (#71); bump ndx-ophys-devices to 0.4.0 |
| [#74](https://github.com/catalystneuro/ndx-microscopy/pull/74) | NWBEP0004 reviews - part 2 | Open (h-mayorquin pending) | `PlanarMicroscopyStaticImage`, `VolumetricMicroscopyStaticImage` (linked to issue #7) |
| [#75](https://github.com/catalystneuro/ndx-microscopy/pull/75) | NWBEP0004 reviews - part 3 | Open (h-mayorquin pending) | `ImagingSpace` refactor — removes coordinate system, delegates to ndx-anatomical-localization |
| [#76](https://github.com/catalystneuro/ndx-microscopy/pull/76) | Bump version to 0.4.0 | Draft | Version bump + CHANGELOG |

---

## Resolution Summary

| Status | Count | IDs |
|--------|-------|-----|
| **ADDRESSED** | 1 | CS-1 |
| **PARTIALLY ADDRESSED?** | 1 | RD-3 |
| **UNCLEAR** (need verification) | 3 | CS-2, RD-1, RD-2 |
| **LIKELY ADDRESSED** (Google Doc comments) | 1 | GM-1 |
| **NOTED** (not actionable) | 3 | RD-4, RD-ALT, GM-CB |
| **MISSING REVIEW** | 1 | Dan Birman |

## Key Finding: Document Version Updated

The Google Doc now shows **Version 0.4.0 | Last Modified: 02 December 2025** (was previously 0.2.0 / May 30, 2025). This confirms substantive updates were made.

## Key Finding: Resolved Comments

The .docx export (downloaded 2026-03-17) contains only 1 unresolved comment (from YOH about matching PR #76 version). All reviewer inline comments have been **resolved** — meaning Alessandra addressed and marked them done. However, resolved comment content is not preserved in .docx exports.

---

**Next steps**: re-invite reviewers for re-review round.
