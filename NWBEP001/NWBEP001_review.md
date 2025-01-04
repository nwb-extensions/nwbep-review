# Evaluation for NWBEP001

**NWBEP Title**: Events and TTL Data

**Working Group members**:

* Josh Siegle (Facilitator)  
* Alessandra Trapani  
* Kay Robbins  
* Chris Rodgers

**Review Date**: Dec 11, 2024

## Summary Statement

This is an important enhancement that will simplify interactions with NWB files for both data producers and consumers. 

Currently, NWB lacks a standardized approach for handling event data, which leads researchers to adopt idiosyncratic methods for storing events. By introducing new neurodata types dedicated to events, NWBEP001 will ensure:

* Uniformity in how event data is stored and accessed  
* Precise documentation of experimental events  
* Support for categorical data with mappings to descriptive meanings via `CategoricalVectorData` and a `MeaningsTable`

The proposal is clear and usable, alternative approaches are well considered, and the implementation has been carefully thought out. Prior to sharing with a broader audience, several additions to the proposal are recommended: example code demonstrating how to create a `MeaningsTable`, more detailed treatment of real-time applications, and draft API methods for transferring event data between NWB files and DataFrames/spreadsheets/CSV files.

Overall, the reviewers approve of this enhancement and recommend its adoption. 

## Review 1

**Reviewer**: Josh Siegle

### 1\. Significance and impact

**Evaluation criteria:**

- [x] **Significance:** *Does the NWBEP address an important problem or barrier to progress? Does the NWBEP provide functionality for others in the neurophysiology community besides the original proposers? Have different types of potential users from the community (e.g., different technical skill levels, language proficiency, use cases) used the proposed extension or been involved in developing the NWBEP?*  
- [x] **Impact:** *Does the NWBEP create a sustained, powerful influence on relevant research field(s) and users? Does the NWBEP add well-defined, unique capabilities to NWB?*   
- [x] **Alternatives:** *Have alternative solutions been reasonably considered?*

**Comments:**

Deciding how to store event data is currently one of the most confusing things about NWB. Integrating dedicated event types into the core schema will make it much easier for users to get up and running with NWB reading and writing. 

### 2\. Clarity and usability

**Evaluation criteria:**

- [x] **Precision:** *Is the NWBEP clear and unambiguous such that others can easily understand the proposal?*  
- [x] **Human and machine readability and usability:** *Does the NWBEP define data/metadata and features in ways that are easily interpretable and usable by others?*  
- [x] **Reusability and compliance with [FAIR principles](https://www.go-fair.org/fair-principles/):** *Does the NWBEP capture data/metadata required for discovery, interpretation, and reuse of the data?*

**Comments:**

If all of the possible column values are documented in a `MeaningsTable`, then the file should be easily interpretable. It’s probably overly stringent to require a `MeaningsTable` for every categorical column, but perhaps there should be a warning shown when a user tries to write an `EventsTable` without one. It would also be helpful to provide examples of how to create a `MeaningsTable` before sharing this proposal more broadly.

### 3\. Implementation

**Evaluation criteria:** 

- [x] **Implementability:** *Is the NWBEP implementable on all reasonable target platforms (hardware, program language, etc.) with reasonable effort, considering changes needed to the NWB schema, storage, software, community tools, and other relevant areas?*   
- [x] **Compatibility:** *Is the NWBEP compliant and compatible with the NWB standard, principles, and best practices ([1](https://github.com/hdmf-dev/hdmf-schema-language/pull/32/files)*, [*2*](https://nwbinspector.readthedocs.io/en/dev/best_practices/best_practices_index.html)*)?*  
- [x] **Maintainability:** *Is the NWBEP designed to be easy* to maintain (*e.g., dependencies) and build on (e.g., can new neurodata types be easily extended) in the future?*   
- [x] **Efficiency:** *Does the NWBEP define data/features in ways that allow for efficient storage, access, search and use of data and software?*

**Comments:**

I don’t have any concerns about usability within Python and Matlab. For real-time applications (often based on C++), the NWB developers should provide some recommendations for best practices, especially with respect to TTL events. For example, what column names are expected (e.g. “line” and “state”)? In addition, relevant event-writing functions should be incorporated into the AqNWB library soon after this specification is finalized.

Also, the developers should consider providing tutorials on taking event data stored in one of the four types of current implementations and making it compliant with the new standard.

## Review 2

**Reviewer**: Kay Robbins

### 1\. Significance and impact

**Evaluation criteria:**

- [x] **Significance:** *Does the NWBEP address an important problem or barrier to progress? Does the NWBEP provide functionality for others in the neurophysiology community besides the original proposers? Have different types of potential users from the community (e.g., different technical skill levels, language proficiency, use cases) used the proposed extension or been involved in developing the NWBEP?*  
- [x] **Impact:** *Does the NWBEP create a sustained, powerful influence on relevant research field(s) and users? Does the NWBEP add well-defined, unique capabilities to NWB?*   
- [x] **Alternatives:** *Have alternative solutions been reasonably considered?*

**Comments:**    
I think such an extension is necessary and the original extension was a little awkward. This extension will allow some useful tools to be built on top of the core functionality.

### 2\. Clarity and usability

**Evaluation criteria:**

- [x] **Precision:** *Is the NWBEP clear and unambiguous such that others can easily understand the proposal?*  
- [x] **Human and machine readability and usability:** *Does the NWBEP define data/metadata and features in ways that are easily interpretable and usable by others?*  
- [x] **Reusability and compliance with [FAIR principles](https://www.go-fair.org/fair-principles/):** *Does the NWBEP capture data/metadata required for discovery, interpretation, and reuse of the data?*

**Comments:**  
As stated in my summary, one of the things that NWB lacks is basic user tools for easy input and output of datasets.  I’m not sure the FAIR principles are really relevant at this level.  This definitely moves NWB in the right direction from a metadata perspective.

### 3\. Implementation

**Evaluation criteria:** 

- [x] **Implementability:** *Is the NWBEP implementable on all reasonable target platforms (hardware, program language, etc.) with reasonable effort, considering changes needed to the NWB schema, storage, software, community tools, and other relevant areas?*   
- [x] **Compatibility:** *Is the NWBEP compliant and compatible with the NWB standard, principles, and best practices ([1](https://github.com/hdmf-dev/hdmf-schema-language/pull/32/files)*, [*2*](https://nwbinspector.readthedocs.io/en/dev/best_practices/best_practices_index.html)*)?*  
- [x] **Maintainability:** *Is the NWBEP designed to be easy* to maintain (*e.g., dependencies) and build on (e.g., can new neurodata types be easily extended) in the future?*   
- [x] **Efficiency:** *Does the NWBEP define data/features in ways that allow for efficient storage, access, search and use of data and software?*

**Comments:**  
The NWB ecosystem is known for its high performance and clean core implementation. This proposal is not backwards-compatible with the original ndx-events extension, but my impression is that the old extension was not widely used nor were there many tools built on it. This revision has a much better chance of being adopted, particularly if there are easy input/output functions to spreadsheets so users can see what they have.

## Review 3

**Reviewer**: Alessandra Trapani

### 1\. Significance and impact

**Evaluation criteria:**

- [x] **Significance:** *Does the NWBEP address an important problem or barrier to progress? Does the NWBEP provide functionality for others in the neurophysiology community besides the original proposers? Have different types of potential users from the community (e.g., different technical skill levels, language proficiency, use cases) used the proposed extension or been involved in developing the NWBEP?*  
- [x] **Impact:** *Does the NWBEP create a sustained, powerful influence on relevant research field(s) and users? Does the NWBEP add well-defined, unique capabilities to NWB?*   
- [x] **Alternatives:** *Have alternative solutions been reasonably considered?*

**Comments:**

### 2\. Clarity and usability

**Evaluation criteria:**

- [x] **Precision:** *Is the NWBEP clear and unambiguous such that others can easily understand the proposal?*  
- [x] **Human and machine readability and usability:** *Does the NWBEP define data/metadata and features in ways that are easily interpretable and usable by others?*  
- [x] **Reusability and compliance with [FAIR principles](https://www.go-fair.org/fair-principles/):** *Does the NWBEP capture data/metadata required for discovery, interpretation, and reuse of the data?*

**Comments:**

The document is detailed and provides a clear rationale for the proposed changes, with concrete examples and comparisons to existing approaches.  
The language is precise and unambiguous, making it accessible to a technical audience.  
The proposed data structures are designed to be machine-readable and support interoperability with tools like PyNWB and MatNWB.  
Reusability is explicitly addressed by introducing structures like `MeaningsTable`, which helps annotate event metadata.

### 3\. Implementation

**Evaluation criteria:** 

- [x] **Implementability:** *Is the NWBEP implementable on all reasonable target platforms (hardware, program language, etc.) with reasonable effort, considering changes needed to the NWB schema, storage, software, community tools, and other relevant areas?*   
- [x] **Compatibility:** *Is the NWBEP compliant and compatible with the NWB standard, principles, and best practices ([1](https://github.com/hdmf-dev/hdmf-schema-language/pull/32/files)*, [*2*](https://nwbinspector.readthedocs.io/en/dev/best_practices/best_practices_index.html)*)?*  
- [x] **Maintainability:** *Is the NWBEP designed to be easy* to maintain (*e.g., dependencies) and build on (e.g., can new neurodata types be easily extended) in the future?*   
- [x] **Efficiency:** *Does the NWBEP define data/features in ways that allow for efficient storage, access, search and use of data and software?*

**Comments:**

The design is practical, and the authors have considered the effort required for integration.  
The modularity of the new types and their reliance on the existing NWB framework make them easy to maintain and extend.  
The maintainability plan is solid, with well-documented changes in each version of the proposal.

## Review 4

**Reviewer**: Chris Rodgers

### 1\. Significance and impact

**Evaluation criteria:**

- [x] **Significance:** *Does the NWBEP address an important problem or barrier to progress? Does the NWBEP provide functionality for others in the neurophysiology community besides the original proposers? Have different types of potential users from the community (e.g., different technical skill levels, language proficiency, use cases) used the proposed extension or been involved in developing the NWBEP?*  
- [x] **Impact:** *Does the NWBEP create a sustained, powerful influence on relevant research field(s) and users? Does the NWBEP add well-defined, unique capabilities to NWB?*   
- [x] **Alternatives:** *Have alternative solutions been reasonably considered?*

**Comments:**

Significance: High because there is currently no clarity on what the right way is to store event data, and there are many people in the community who need to do this. 

Impact: High because the new way of storing events will likely cover most of the users' use cases.

Alternatives: Well-considered especially in the "Current implementation" section of the document which reviews how users currently address this. 

### 2\. Clarity and usability

**Evaluation criteria:**

- [x] **Precision:** *Is the NWBEP clear and unambiguous such that others can easily understand the proposal?*  
- [x] **Human and machine readability and usability:** *Does the NWBEP define data/metadata and features in ways that are easily interpretable and usable by others?*  
- [x] **Reusability and compliance with [FAIR principles](https://www.go-fair.org/fair-principles/):** *Does the NWBEP capture data/metadata required for discovery, interpretation, and reuse of the data?*

**Comments:**

Precision: High because of the clear specification of `EventsTable`, `TimsestampVectorData`, and `DurationVectorData`. Ambiguity is minimized with clear documentation and the figure showing relationships. 

Usability: High because the standard features (`EventsTable`, `TimestampVectorData`, `DurationVectorData`) are intuitive for people \- we usually store events in this way. Machine readability is high because of the standardization of fields. I strongly approve the clarification of "Scope" which puts the `MeaningsTable` in experimental development. `MeaningsTable` is potentially powerful but also potentially confusing. 

Reusability: High because downstream users will likely want to extract behavioral data from these datasets, and making this approach more standard should encourage that.

### 3\. Implementation

**Evaluation criteria:** 

- [x] **Implementability:** *Is the NWBEP implementable on all reasonable target platforms (hardware, program language, etc.) with reasonable effort, considering changes needed to the NWB schema, storage, software, community tools, and other relevant areas?*   
- [x] **Compatibility:** *Is the NWBEP compliant and compatible with the NWB standard, principles, and best practices ([1](https://github.com/hdmf-dev/hdmf-schema-language/pull/32/files)*, [*2*](https://nwbinspector.readthedocs.io/en/dev/best_practices/best_practices_index.html)*)?*  
- [x] **Maintainability:** *Is the NWBEP designed to be easy* to maintain (*e.g., dependencies) and build on (e.g., can new neurodata types be easily extended) in the future?*   
- [x] **Efficiency:** *Does the NWBEP define data/features in ways that allow for efficient storage, access, search and use of data and software?*

**Comments:**

Implementability: I am not fully able to evaluate this because I am not well-equipped to test this code on multiple platforms. However, my experience with the developers suggests that this will be the case and proposal states it has been so implemented.

Compatibility: Appears to be compliant and compatible. I am again relying mostly on trust and past experience with the developers that they know what they are doing. 

Maintainability: No dependencies are introduced. A path for potentially building on the experimental features is described. 

Efficiency: I am not able to evaluate the computational efficiency. The user's time efficiency, which I regard as more important, is high because it is clear how to store, access, search, and use the new data types that are introduced. 
