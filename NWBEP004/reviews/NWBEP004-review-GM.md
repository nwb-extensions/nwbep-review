## Individual Review for NWBEP004: Optical Devices and Microscopy

### Reviewer

- **Name**: Giacomo Mazzamuto
- **Affiliation**: National Research Council - National Institute of Optics (CNR - INO) & European Laboratory for Non-Linear Spectroscopy (LENS - University of Florence)
- **ORCID**: 0000-0003-3077-3904

### 1. Significance and impact

#### Evaluation criteria:

- [X] **Significance:** *Does the NWBEP address an important problem or barrier to progress? Does the NWBEP provide functionality for others in the neurophysiology community besides the original proposers? Have different types of potential users from the community (e.g., different technical skill levels, language proficiency, use cases) used the proposed extension or been involved in developing the NWBEP?*
- [X] **Impact:** *Does the NWBEP create a sustained, powerful influence on relevant research field(s) and users? Does the NWBEP add well-defined, unique capabilities to NWB?*
- [X] **Alternatives:** *Have alternative solutions been reasonably considered?*

#### Comments:

The proponents present two extensions for the NWB Format Specification, with a particular focus on optical devices and microscopy. The proposal originates from real needs by the authors and by the broader community, addressing several shortcomings in the current specification. As far as optical devices are concerned, the proposal enhances the current specification by adding fields for device metadata for optical components, support for indicators/effectors and optical path documentation. On the microscopy side, the proposal addresses shortcomings in the imaging space representation, allowing e.g. to store planar and volumetric data, both for imaging and for segmentation.

The proposal is well-thought-out, I don't have specific remarks other than the small suggestions added as comments in the shared draft. I would recommend it for inclusion in the NWB specification upon further refinement where appropriate.

### 2. Clarity and usability

#### Evaluation criteria

- [X] **Precision:** *Is the NWBEP clear and unambiguous such that others can easily understand the proposal?*
- [X] **Human and machine readability and usability:** *Does the NWBEP define data/metadata and features in ways that are easily interpretable and usable by others?*
- [X] **Reusability and compliance with [FAIR principles](https://www.go-fair.org/fair-principles/):** *Does the NWBEP capture data/metadata required for discovery, interpretation, and reuse of the data?*

#### Comments:

### 3. Implementation

#### Evaluation criteria 

- [X] **Implementability:** *Is the NWBEP implementable on all reasonable target platforms (hardware, program language, etc.) with reasonable effort, considering changes needed to the NWB schema, storage, software, community tools, and other relevant areas?*
- [X] **Compatibility:** *Is the NWBEP compliant and compatible with the NWB standard, principles, and best practices ([1](https://github.com/hdmf-dev/hdmf-schema-language/pull/32/files)*, [*2*](https://nwbinspector.readthedocs.io/en/dev/best_practices/best_practices_index.html)*)?*
- [X] **Maintainability:** *Is the NWBEP designed to be easy* to maintain (*e.g., dependencies) and build on (e.g., can new neurodata types be easily extended) in the future?*
- [X] **Efficiency:** *Does the NWBEP define data/features in ways that allow for efficient storage, access, search and use of data and software?*

#### Comments

