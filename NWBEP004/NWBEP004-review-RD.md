## Individual Review for NWBEP004: Optical Devices and Microscopy

### Reviewer

- **Name**: Robin Dard
- **Affiliation**: EPFL
- **ORCID**: {ORCID} 

### 1. Significance and impact

#### Evaluation criteria:

- [x] **Significance:** *Does the NWBEP address an important problem or barrier to progress? Does the NWBEP provide functionality for others in the neurophysiology community besides the original proposers? Have different types of potential users from the community (e.g., different technical skill levels, language proficiency, use cases) used the proposed extension or been involved in developing the NWBEP?*  
- [x] **Impact:** *Does the NWBEP create a sustained, powerful influence on relevant research field(s) and users? Does the NWBEP add well-defined, unique capabilities to NWB?*   
- [ ] **Alternatives:** *Have alternative solutions been reasonably considered?*

#### Comments:

**Significance/Impact:**

The NWBEP addresses some strong limitations that experimenters and NWB users may have faced when trying to store and retrieve imaging data.
- First, this NWBEP offers the possibility to flexibly store volumetric, multiplanes and multichannels imaging data obtained from various imaging modalities. This is to me a major step forward, it would considerably extend the range of experimental conditions covered by the NWB scheme which should facilitate and standardize the conversion of various imaging dataset into NWB format. 
- Second, it will improve the quality and the richness of the metadata related to the acquisition system. This would make it possible to better describe various experimental setups.
Overall I think the NWBEP has a strong significance and would positively impact the imaging community.

**Specific use case:**

To better appreciate the significance of the NWBEP I would like more details on how it would cover a specific use case. 

Example experiment : multi-plane acquisition at 3 imaging depths (using ETL) combined with multi-channel acquisition (1 indicator for neuronal activity and 2 anatomical markers - genetically defined subpopulations, projection neurons, ….). I am still not sure how to best use the new datatypes offered by the NWBEP and how to link them. 

Should the user create one SegmentationContainer with 2 PlanarSegmentation (1 per channel ) linked to 1 PlanarImagingSpace and repeat for each of the 3 planes ? Then associate to each of the PlanarSegmentation a roi_table_region linked to a MicroscopyResponseSeries ? 

If there should be 1 segmentation for each imaging plan, how to best map the multi-channel information onto the multi-depths imaging ? 

### 2. Clarity and usability

#### Evaluation criteria

- [x] **Precision:** *Is the NWBEP clear and unambiguous such that others can easily understand the proposal?*  
- [x] **Human and machine readability and usability:** *Does the NWBEP define data/metadata and features in ways that are easily interpretable and usable by others?*  
- [x] **Reusability and compliance with [FAIR principles](https://www.go-fair.org/fair-principles/):** *Does the NWBEP capture data/metadata required for discovery, interpretation, and reuse of the data?*

#### Comments:

**Precision**:
The NWEP is overall clear. It proposes to extend already existing neurodata types and add substantial new ones. Both the extensions and new neurodata types (and their extension) are well described. The relationship between these new neurodata types is also described in the proposal. The public examples presented in 5.1 & 5.2 are also helpful to understand how these new neurodata types could be used. However I feel the clarity could have been further improved. For example I would have liked to see a schematic representation of these data types together with their mandatory and optional fields and the links between them (similar to the one made for the current NWB scheme -  https://pynwb.readthedocs.io/en/stable/tutorials/domain/ophys.html#sphx-glr-tutorials-domain-ophys-py). 

**Human and machine readability and usability:**
My overall impression is that the NWBEP would indeed make it easier to read and reuse data but this remains to be tested. 

**Reusability and compliance with FAIR principles:**
I have one comment / question regarding the metadata on the MicroscopyRig that would require a link to the Microscope as well as many optional links to new fields extending on the DeviceInstance. I appreciate the effort to include details on the microscopy rig and I think all the proposed metadata could be easily repeated over multiple NWB files when the data is acquired on the same rig. However in addition I think it could be good to have an optional link to Images object (pynwb.base.Images) that would provide an annotated scheme of the microscope and / or optical path. 


### 3. Implementation

#### Evaluation criteria 

- [x] **Implementability:** *Is the NWBEP implementable on all reasonable target platforms (hardware, program language, etc.) with reasonable effort, considering changes needed to the NWB schema, storage, software, community tools, and other relevant areas?*   
- [x] **Compatibility:** *Is the NWBEP compliant and compatible with the NWB standard, principles, and best practices ([1](https://github.com/hdmf-dev/hdmf-schema-language/pull/32/files)*, [*2*](https://nwbinspector.readthedocs.io/en/dev/best_practices/best_practices_index.html)*)?*  
- [x] **Maintainability:** *Is the NWBEP designed to be easy* to maintain (*e.g., dependencies) and build on (e.g., can new neurodata types be easily extended) in the future?*   
- [x] **Efficiency:** *Does the NWBEP define data/features in ways that allow for efficient storage, access, search and use of data and software?*

#### Comments

The implementation proposed in the NWBEP seems good to me at all levels cited above.
