# NWBEP004: Clarifications Before Re-Review Round from 2026/03/17

This document attempts to map each reviewer concern to the PRs and document changes.
The original reviews are in [nwbep-review PR #7](https://github.com/nwb-extensions/nwbep-review/pull/7). 

[../README.md](../README.md) provides overall summary and most of the reviewer comments were addressed.
A few items remain needing clarification to be provided to the reviewers.

## Questions About Remaining Items

### Carsen Stringer

1. **CS-2**: Carsen noted that ["good examples of the ophys-devices would be very helpful, perhaps for some standard microscopes used in the field"](https://github.com/nwb-extensions/nwbep-review/pull/7/files#diff-1e0f44955b22571c0fc8b050393b0f72287ebd9bd10282c719dfa619cf98ab86R44). Were examples for standard microscopes added or expanded in the Google Doc (e.g., sections 5.1/5.2)?

### Robin Dard

2. **RD-1**: Robin requested [a detailed use case for multi-plane acquisition (ETL, 3 depths) + multi-channel (1 indicator + 2 anatomical markers) — specifically how to use the new datatypes and link them](https://github.com/nwb-extensions/nwbep-review/pull/7/files#diff-d43b322f0f7103054c56fa1c48d0206b8572c27d550d1353ad17b399b86abd7aR28-R34). Was this worked example added to the document?

3. **RD-2**: Robin suggested adding [a schematic representation of data types together with their mandatory/optional fields and the links between them](https://github.com/nwb-extensions/nwbep-review/pull/7/files#diff-d43b322f0f7103054c56fa1c48d0206b8572c27d550d1353ad17b399b86abd7aR47) (similar to the PyNWB ophys tutorial diagram). Was such a diagram added?

4. **RD-3**: Robin suggested [an optional link to `Images` object (`pynwb.base.Images`) for an annotated microscope/optical path scheme in `MicroscopyRig`](https://github.com/nwb-extensions/nwbep-review/pull/7/files#diff-d43b322f0f7103054c56fa1c48d0206b8572c27d550d1353ad17b399b86abd7aR53). I see that ndx-microscopy [PR #74](https://github.com/catalystneuro/ndx-microscopy/pull/74) adds static image types — does this address Robin's suggestion, or is the `MicroscopyRig` → `Images` link a separate concern?

### Giacomo Mazzamuto

5. **GM-1**: Giacomo mentioned ["small suggestions added as comments in the shared draft"](https://github.com/nwb-extensions/nwbep-review/pull/7/files#diff-4c67c5bd305d65baa14feb4e6e68f0a0838232d5879fe26ac2a89d6dedd728b0R21-R23). I see that all inline comments in the Google Doc have been resolved. Could you please acknowledge that they were all addressed? (as no history accessible)

### General

6. **PR status**: All PRs ([#25](https://github.com/catalystneuro/ndx-ophys-devices/pull/25) for ndx-ophys-devices; [#73](https://github.com/catalystneuro/ndx-microscopy/pull/73), [#74](https://github.com/catalystneuro/ndx-microscopy/pull/74), [#75](https://github.com/catalystneuro/ndx-microscopy/pull/75), [#76](https://github.com/catalystneuro/ndx-microscopy/pull/76) for ndx-microscopy) are still open. When do you expect them to be merged? Should we ask reviewers to review against the individual open PRs, or would it be better to merge them all for a simpler way to review "as a whole"?

7. **Document version**: I (@yarikoptic) submitted suggestion in the Google Doc to have  "Version 0.4.0 | Last Modified: 02 December 2025" — can you confirm 0.4.0 reflects all the changes from the PRs above?
