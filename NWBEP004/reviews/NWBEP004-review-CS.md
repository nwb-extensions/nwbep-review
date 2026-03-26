## Individual Review for NWBEP004: Optical Devices and Microscopy

### Reviewer

- **Name**: Carsen Stringer
- **Affiliation**: janelia.hhmi.org
- **ORCID**: 0000-0002-9229-4100

### 1. Significance and impact

#### Evaluation criteria:

- [X] **Significance:** *Does the NWBEP address an important problem or barrier to progress? Does the NWBEP provide functionality for others in the neurophysiology community besides the original proposers? Have different types of potential users from the community (e.g., different technical skill levels, language proficiency, use cases) used the proposed extension or been involved in developing the NWBEP?*
- [X] **Impact:** *Does the NWBEP create a sustained, powerful influence on relevant research field(s) and users? Does the NWBEP add well-defined, unique capabilities to NWB?*
- [X] **Alternatives:** *Have alternative solutions been reasonably considered?*

#### Comments:

The support for multi-channel/multi-plane recordings is crucial - many users of two-photon imaging have different channels which processing pipelines need to process separately, our lab included. This also proposes an implementation of a 3D imaging schema, which is an important addition to NWB. I think this will help pipelines downstream decide how to process such datasets.

### 2. Clarity and usability

#### Evaluation criteria

- [X] **Precision:** *Is the NWBEP clear and unambiguous such that others can easily understand the proposal?*
- [X] **Human and machine readability and usability:** *Does the NWBEP define data/metadata and features in ways that are easily interpretable and usable by others?*
- [X] **Reusability and compliance with [FAIR principles](https://www.go-fair.org/fair-principles/):** *Does the NWBEP capture data/metadata required for discovery, interpretation, and reuse of the data?*

#### Comments:

The use of OpticalLensModel vs OpticalLens is a bit confusing, perhaps the “OpticalLensModel” be re-termed the “ObjectiveLensModel”?

### 3. Implementation

#### Evaluation criteria

- [X] **Implementability:** *Is the NWBEP implementable on all reasonable target platforms (hardware, program language, etc.) with reasonable effort, considering changes needed to the NWB schema, storage, software, community tools, and other relevant areas?*
- [X] **Compatibility:** *Is the NWBEP compliant and compatible with the NWB standard, principles, and best practices ([1](https://github.com/hdmf-dev/hdmf-schema-language/pull/32/files)*, [*2*](https://nwbinspector.readthedocs.io/en/dev/best_practices/best_practices_index.html)*)?*
- [X] **Maintainability:** *Is the NWBEP designed to be easy* to maintain (*e.g., dependencies) and build on (e.g., can new neurodata types be easily extended) in the future?*
- [X] **Efficiency:** *Does the NWBEP define data/features in ways that allow for efficient storage, access, search and use of data and software?*

#### Comments

It looks very clear and maintainable. Good examples of the ophys-devices would be very helpful, perhaps for some standard microscopes used in the field.
