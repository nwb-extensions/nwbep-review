# NWBEP004: Optical Devices and Microscopy

## Quick links:


- **NWBEP004**: Optical Devices and Microscopy
- **Lead**: Alessandra Trapani (CatalystNeuro)
- **Extensions**: [ndx-ophys-devices](https://github.com/catalystneuro/ndx-ophys-devices), [ndx-microscopy](https://github.com/catalystneuro/ndx-microscopy)
- **Google Doc**: https://docs.google.com/document/d/1-dVEBuacvoM3hZk8GeinmQpNF4yh3Uvxz7WOWUpdvFY/edit
- **Local .md copy**: [./doc/NWBEP004.md](./doc/NWBEP004.md)
- **Reviews**: [nwbep-review PR #7](https://github.com/nwb-extensions/nwbep-review/pull/7) (**merged 2026-08-31**)

## Timeline

| Date       | Event                                                                                                                                                                       |
| ---------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 2025-05-30 | Alessandra submitted updated NWBEP004 document for external review                                                                                                         |
| 2025-06-16 | YOH sent review invitations (CS, RD, GM, Dan Birman)                                                                                                                       |
| 2025-09-30 | Virtual meeting with reviewers and Alessandra (video: `2025-09-30_NWB-TAB-NWBEP004-review.mp4`, available from @yarikoptic on request)                                      |
| 2025-10-09 | Reviews posted to [nwbep-review PR #7](https://github.com/nwb-extensions/nwbep-review/pull/7)                                                                              |
| 2025-12-03 | Alessandra delivered revised Google Doc (v0.4.0) and PRs addressing feedback                                                                                               |
| 2026-03-17 | @yarikoptic emailed Alessandra with [clarification questions](./notes/20260317-questions.md)                                                                                |
| 2026-03-25 | All substantive PRs merged: ndx-ophys-devices [#25](https://github.com/catalystneuro/ndx-ophys-devices/pull/25); ndx-microscopy [#73](https://github.com/catalystneuro/ndx-microscopy/pull/73), [#74](https://github.com/catalystneuro/ndx-microscopy/pull/74), [#75](https://github.com/catalystneuro/ndx-microscopy/pull/75) |
| 2026-03-26 | Alessandra completed her changes in response to reviews                                                                                                                     |
| 2026-08-31 | [nwbep-review PR #7](https://github.com/nwb-extensions/nwbep-review/pull/7) merged — review process finalized; PR against core invited                                     |

---

## Review summaries

### Reviewer: Carsen Stringer (CS)

**Affiliation**: Janelia / HHMI
**ORCID**: 0000-0002-9229-4100
**Overall**: Very positive. All 12 evaluation checkboxes marked. Recommends inclusion.

| ID   | Concern                                                                                                                                                                                                                                                                                          | Status              | Where Addressed                                                                                                                                                                                                           |
| ---- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| CS-1 | ["OpticalLensModel" vs "OpticalLens" confusing — rename to "ObjectiveLensModel"](https://github.com/nwb-extensions/nwbep-review/pull/7/files#diff-1e0f44955b22571c0fc8b050393b0f72287ebd9bd10282c719dfa619cf98ab86R31)                                                                           | **ADDRESSED**       | ndx-ophys-devices [PR #25](https://github.com/catalystneuro/ndx-ophys-devices/pull/25) (merged 2026-03-25): renames OpticalLens → ObjectiveLens + consolidates StereotacticPositioning. ndx-microscopy [PR #73](https://github.com/catalystneuro/ndx-microscopy/pull/73): ObjectiveLens rename + ndx-ophys-devices bumped to 0.4.0 |
| CS-2 | ["Good examples of the ophys-devices would be very helpful, perhaps for some standard microscopes used in the field"](https://github.com/nwb-extensions/nwbep-review/pull/7/files#diff-1e0f44955b22571c0fc8b050393b0f72287ebd9bd10282c719dfa619cf98ab86R44)                                       | **CLOSED**          | Documentation concern addressed in updated Google Doc (v0.4.0, sections 5.1/5.2). PRs merged without outstanding objection from CS.                                                                                      |

---

### Reviewer: Robin Dard (RD)

**Affiliation**: EPFL
**ORCID**: 0009-0000-6221-0407
**Overall**: Positive and detailed. All 12 checkboxes marked including Alternatives.

| ID     | Concern                                                                                                                                                                                                                                                                                                                                  | Status                    | Where Addressed                                                                                                                                                                                                                                                  |
| ------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| RD-1   | [Detailed use case for multi-plane (ETL, 3 depths) + multi-channel (1 indicator + 2 anatomical markers) — how to use new datatypes and link them](https://github.com/nwb-extensions/nwbep-review/pull/7/files#diff-d43b322f0f7103054c56fa1c48d0206b8572c27d550d1353ad17b399b86abd7aR28-R34)                                                | **CLOSED**                | Addressed in updated Google Doc examples. PRs merged without outstanding objection from RD.                                                                                                                                                                      |
| RD-2   | [Schematic diagram of data types with mandatory/optional fields and links between them](https://github.com/nwb-extensions/nwbep-review/pull/7/files#diff-d43b322f0f7103054c56fa1c48d0206b8572c27d550d1353ad17b399b86abd7aR47) (like [PyNWB ophys tutorial](https://pynwb.readthedocs.io/en/stable/tutorials/domain/ophys.html))           | **CLOSED**                | Documentation/Google Doc concern. PRs merged without outstanding objection from RD.                                                                                                                                                                              |
| RD-3   | [Optional link to `Images` object (`pynwb.base.Images`) for annotated microscope/optical path scheme in `MicroscopyRig`](https://github.com/nwb-extensions/nwbep-review/pull/7/files#diff-d43b322f0f7103054c56fa1c48d0206b8572c27d550d1353ad17b399b86abd7aR53)                                                                            | **ADDRESSED**             | ndx-microscopy [PR #74](https://github.com/catalystneuro/ndx-microscopy/pull/74) (merged 2026-03-25) adds `PlanarMicroscopyStaticImage` and `VolumetricMicroscopyStaticImage`; ndx-microscopy PR #76 (pending) explicitly lists this link as completed (`[x]`). |
| RD-4   | [FAIR concern: rig metadata should be easily repeated across NWB files from same rig](https://github.com/nwb-extensions/nwbep-review/pull/7/files#diff-d43b322f0f7103054c56fa1c48d0206b8572c27d550d1353ad17b399b86abd7aR52-R53)                                                                                                            | **NOTED**                 | Design philosophy comment. The `MicroscopyRig` + `MicroscopyExperimentMetadata` approach addresses this implicitly.                                                                                                                                              |

---

### Reviewer: Giacomo Mazzamuto (GM)

**Affiliation**: National Research Council — National Institute of Optics (CNR-INO) & European Laboratory for Non-Linear Spectroscopy (LENS, University of Florence)
**ORCID**: 0000-0003-3077-3904
**Overall**: Positive. All 12 checkboxes marked. Recommends inclusion "upon further refinement where appropriate."

| ID   | Concern                                                                                                                                                                                                                                              | Status              | Where Addressed                                                                                                                                                                                                                                                                                    |
| ---- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| GM-1 | ["Small suggestions added as comments in the shared draft"](https://github.com/nwb-extensions/nwbep-review/pull/7/files#diff-4c67c5bd305d65baa14feb4e6e68f0a0838232d5879fe26ac2a89d6dedd728b0R21-R23) — no specific written concerns in review form | **ADDRESSED**       | Comments were inline in the Google Doc. The .docx export (2026-03-17) shows only 1 unresolved comment (from YOH); all reviewer comments were **resolved** by Alessandra. Alessandra confirmed Dec 2025 revision contains "all corrections from reviewers". |

---

### Reviewer: Daniel Birman (DB)

**Affiliation**: Allen Institute
**ORCID**: 0000-0003-3748-6289
**Overall**: All 12 checkboxes marked. No written comments. Review submitted via PR #1 (merged).

| Date       | Event                                         |
| ---------- | --------------------------------------------- |
| 2025-06-16 | YOH sent invitation                           |
| 2025-06-16 | Dan replied: "Yes I can help review for this proposal" |
| 2025-09-30 | Participated in review panel meeting          |
| 2025-10-02 | YOH requested review submission               |
| 2025-10-09 | Review submitted via PR dbirman/patch-1 (merged into nwbep-review) |

---

## Summary of PRs (Dec 2025 revision)

### ndx-ophys-devices

| PR                                                              | Title              | Status                              | Key Changes                                                                                                      |
| --------------------------------------------------------------- | ------------------ | ----------------------------------- | ---------------------------------------------------------------------------------------------------------------- |
| [#25](https://github.com/catalystneuro/ndx-ophys-devices/pull/25) | NWBEP004_reviews | **Merged 2026-03-25**               | OpticalLens → ObjectiveLens rename; unified `StereotacticPositioning` replacing `FiberInsertion`/`LensPositioning`; new coordinate/angle attributes |

### ndx-microscopy

| PR                                                              | Title                         | Status                              | Key Changes                                                                                                                     |
| --------------------------------------------------------------- | ----------------------------- | ----------------------------------- | ------------------------------------------------------------------------------------------------------------------------------- |
| [#73](https://github.com/catalystneuro/ndx-microscopy/pull/73) | NWBEP0004 reviews - part 1    | **Merged 2026-03-25**               | ObjectiveLens rename; `LabMetadataObject` for `VirusInjection`/`Virus`; fix ImagingSpace redundancy (#71); bump ndx-ophys-devices to 0.4.0 |
| [#74](https://github.com/catalystneuro/ndx-microscopy/pull/74) | NWBEP0004 reviews - part 2    | **Merged 2026-03-25**               | `PlanarMicroscopyStaticImage`, `VolumetricMicroscopyStaticImage` (linked to issue #7)                                          |
| [#75](https://github.com/catalystneuro/ndx-microscopy/pull/75) | NWBEP0004 reviews - part 3    | **Merged 2026-03-25**               | `ImagingSpace` refactor — removes coordinate system, delegates to ndx-anatomical-localization                                   |
| [#76](https://github.com/catalystneuro/ndx-microscopy/pull/76) | Bump version to 0.4.0         | **Open** (pending doc review)       | Version bump + CHANGELOG; includes link to `Images` for `MicroscopyRig` optical path                                           |

---

## Resolution Summary

| Status          | Count | IDs                       |
| --------------- | ----- | ------------------------- |
| **ADDRESSED**   | 3     | CS-1, RD-3, GM-1          |
| **CLOSED**      | 3     | CS-2, RD-1, RD-2          |
| **NOTED**       | 1     | RD-4                      |
| **PENDING**     | 1     | ndx-microscopy PR #76 (version bump + doc review) |

## Overall Status

**Review process finalized.** [nwbep-review PR #7](https://github.com/nwb-extensions/nwbep-review/pull/7) merged 2026-08-31. All four reviewers (CS, RD, GM, DB) submitted reviews recommending inclusion. All substantive implementation PRs merged 2026-03-25. ndx-microscopy PR #76 (version bump to 0.4.0) remains open pending final documentation review. PR against the NWB core has been invited.
