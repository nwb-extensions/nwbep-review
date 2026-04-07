Version: *0.4.0 (see [<u>https://www.nwb.org/versioning-guidelines/</u>](https://www.nwb.org/versioning-guidelines/))*

Last modified: 02 December *2025*

**Extension moderators/leads:**

**Point of Contact:** Alessandra Trapani \<[<u>alessandra.trapani@catalystneuro.com</u>](mailto:alessandra.trapani@catalystneuro.com)\>

**Contributors:\**
Alessandra Trapani \<[<u>alessandra.trapani@catalystneuro.com</u>](mailto:alessandra.trapani@catalystneuro.com)\>,\
Cody Baker [<u>\<cody.baker@catalystneuro.com\></u>](mailto:alessandra.trapani@catalystneuro.com),\
Paul Adkisson \<[<u>paul.adkisson@catalystneuro.com</u>](mailto:paul.adkisson@catalystneuro.com)\>

**Summary:** Experimenters employ various different types of microscopy systems to image neural activity, including widefield, light-sheet, confocal, 2-photon, 3-photon, holographic, etc.  Currently, users have to choose between TwoPhotonSeries and OnePhotonSeries to represent their time series imaging data, neither of which captures the variety of methods commonly employed. To address these problems, we propose a more generic MicroscopySeries with detailed descriptions to capture the variety in the field. The extension enhances the current NWB ophys module by adding detailed metadata about optical components, light paths, and imaging spaces. It integrates with ndx-ophys-devices which provides a standardized way to store and organize metadata about devices used in optical experimental setups, including microscopy, fiber photometry, and optogenetic stimulation. The extension enhances the current NWB device module by adding comprehensive support for various optical components, and detailed specifications for excitation sources, filters, detectors, and other components.

# 1. Table of Contents

[**1. Table of Contents 2**](#table-of-contents)

[**2. Instructions 3**](#instructions)

[**3. Rationale 3**](#rationale)

> [3.1. Background 3](#background)
>
> [3.2. Current implementation 5](#current-implementation)
>
> [3.3. Scope 6](#scope)

[**4. Implementation 6**](#implementation)

> [4.1. Proposed changes to schema and software 6](#proposed-changes-to-schema-and-software)
>
> [4.3. Discussion 13](#discussion)

[**5. Public Examples 17**](#public-examples)

> [5.1. Example 1 17](#example-1)
>
> [5.2. Example 2 18](#example-2)

[**6. Changelog 18**](#changelog)

> [6.1. NDX-OPHYS-DEVICES Version 0.1.0 (Date) 18](#ndx-ophys-devices-version-0.1.0-dec-18-2024)
>
> [6.2. NDX-OPHYS-DEVICES Version 0.1.1 (Date) 18](#ndx-ophys-devices-version-0.1.1-feb-25-2025)
>
> [6.3. NDX-MICROSCOPY Version 0.1.0 (Date) 19](#ndx-ophys-devices-version-0.2.0-jun-3-2025)

[**7. References 19**](#appendix)

[**8. Appendix 19**](#_4i7ojhp)

# 

\
=

# 2. Instructions

*Please fill out the Proposed Enhancement section below and replace the boilerplate text. Instructions are italicized.*

The keywords “MUST”, “MUST NOT”, “REQUIRED”, “SHALL”, “SHALL NOT”, “SHOULD”, “SHOULD NOT”, “RECOMMENDED”, “MAY”, and “OPTIONAL” in this document are to be interpreted as described in [<u>RFC2119</u>](https://www.ietf.org/rfc/rfc2119.txt).

# 3. Rationale

## 3.1. Background

*What application problem and use cases does the enhancement address? What is the target audience for this enhancement? How would the broader neurophysiology community benefit from the enhancement?*

*\*
Optical techniques are widely used in neuroscience research to study neural activity, structure, and function. These techniques include microscopy, fiber photometry, and optogenetic stimulation, each with its own set of specialized optical components and devices, but also sharing most of the basic optical components.

|  | Microscopy | Fiber Photometry | Optogen (microscope) | Optogen (fiber) |
|----|----|----|----|----|
| Excitation Source | **V** | **V** | **V** | **V** |
| Photodetector | **V** | **V** |  |  |
| Excitation Filter | **V** | **V** | **V** | **V** |
| Emission Filter | **V** | **V** |  |  |
| Dichroic Mirror | **V** | **V** | **V** | **V** |
| Objective Lens | **V** |  | **V** |  |
| Optical Fiber |  | **V** |  | **V** |
| Interaction with the specimen | Indicator | Indicator | Effector | Effector |

The ndx-ophys-devices extension will enable the description of optical components that can be shared across multiple optical setups in different experiments. This facilitates resource sharing and ensures standardized metadata representation for optical components across all setups.

<img src="./media/image9.png" style="width:6.5in;height:7.47222in" />\
Experimenters employ various different types of microscopy systems to image neural activity including widefield, light-sheet, confocal, 2-photon, multiphoton, holographic, etc. Currently, users have to choose between TwoPhotonSeries and OnePhotonSeries to represent their time series imaging data, neither of which captures the variety of methods commonly employed. To address these problems we propose a more generic MicroscopySeries with fields to more fully specify which type of microscopy was used.

Researchers frequently opt to analyze their volumetric imaging data in two distinct ways depending on the context: treating each depth plane as a separate, disjoint stream of data OR considering the full imaged volume together during analysis. Currently, users can add a series of 3D images to OnePhotonSeries and TwoPhotonSeries but these TimeSeries still only link to a single ImagingPlane, which does not properly describe the full imaging volume. We propose two new types: PlanarImagingSpace and VolumetricImagingSpace, to facilitate the storage of both 2D and 3D imaging data.

Neuroscientists are rapidly incorporating various different types of fluorescent indicators (GECIs, GEVIs, NT Indicators, Anatomical Indicators, etc.) into their imaging experiments, often with two or more imaged simultaneously. Currently, NWB users can specify only one indicator per ImagingPlane, despite the fact that they can link multiple OpticalChannels, with the mapping between indicators and optical channels only indirectly specified by emission_lambda. To resolve this issue we propose a new neurodata type Indicator, which more directly specifies fluorophore properties and will be contained in the corresponding MicroscopyChannel object. We would deprecate the indicator reference in the ImagingPlane to allow for more flexible structures with multiple indicators.

The target audience for this enhancement includes neuroscientists and data scientists working with microscopy data in neuroscience research. This includes researchers studying calcium imaging, voltage imaging, and other microscopy-based techniques.

The broader neurophysiology community would benefit from these enhancements in several ways:

1.  Detailed metadata about the optical components

2.  Standardize representation of optical components across different optical experiments: microscopy, fiber photometry, optogenetics, etc..

3.  Detailed metadata about the imaging setup would improve reproducibility

4.  Support for various microscopy techniques would accommodate diverse research needs

5.  Better organization of metadata.

6.  More aligned to other imaging standards:

    1.  DORY: [<u>https://doryworkspace.org/metadata</u>](https://doryworkspace.org/metadata)

    2.  BIDS: [<u>https://bids-specification.readthedocs.io/en/stable/04-modality-specific-files/10-microscopy.html</u>](https://bids-specification.readthedocs.io/en/stable/04-modality-specific-files/10-microscopy.html)

    3.  OME-XML: [<u>https://www.openmicroscopy.org/Schemas/Documentation/Generated/OME-2016-06/ome_xsd.html#OME_OME_BinaryOnly_MetadataFile</u>](https://www.openmicroscopy.org/Schemas/Documentation/Generated/OME-2016-06/ome_xsd.html#OME_OME_BinaryOnly_MetadataFile)

## 3.2. Current implementation

*How is the data currently being stored? What are the advantages and disadvantages of the current implementation? Are there existing standards or conventions relevant to the data?*

Currently, the NWB format includes basic support for devices through the Device class, which provides minimal metadata about experimental equipment. However, this class lacks the specific attributes needed to fully describe optical components and their configurations.

The current implementation has several limitations:

1.  **Limited Device Metadata**: The current schema provides only a name, description, and manufacturer for devices, without specific attributes for optical components.

2.  **No Support for Indicators/Effectors**: The current schema does not provide a way to document the fluorescent indicators or optogenetic effectors used in experiments.

3.  **No Support for Optical Path Documentation**: The current schema does not provide a way to document the complete optical path of an experiment.

Currently, the NWB format includes basic support for optical physiology data through the ophys module. This module provides classes for storing two-photon and one-photon imaging data, as well as basic segmentation and fluorescence analysis.

The current implementation has several limitations:

1.  **Limited Device Metadata**: The current schema provides minimal metadata about the microscope. The ImagingPlane class includes basic information about the optical setup, but lacks detailed specifications for excitation sources, filters, detectors, and other components.

2.  **Restricted Imaging Space Representation**: The ImagingPlane class is designed primarily for 2D imaging and lacks support for volumetric imaging or multi-plane acquisition.

3.  **Limited Microscopy Series Types**: The current schema includes TwoPhotonSeries and OnePhotonSeries for storing imaging data, but lacks support for the variety of methods commonly employed.

4.  **Basic Segmentation Capabilities**: The ImageSegmentation and PlaneSegmentation classes provide support for ROI definition, but does not distinguish between 2D or 3D segmentation.

5.  **No Light Path Tracking**: The current schema does not provide a way to track the complete optical path, including excitation and emission components.

List of issues associated with the current schema implementation, we aim to solve with these extensions:

1.  essential device metadata for 2p. [<u>https://github.com/NeurodataWithoutBorders/nwb-schema/issues/460</u>](https://github.com/NeurodataWithoutBorders/nwb-schema/issues/460)

2.  how to store non-TwoPhotonSeries ophys? [<u>https://github.com/NeurodataWithoutBorders/nwb-schema/issues/431</u>](https://github.com/NeurodataWithoutBorders/nwb-schema/issues/431)

3.  Ophys and device improvements\
    [<u>https://github.com/NeurodataWithoutBorders/nwb-schema/issues/406</u>](https://github.com/NeurodataWithoutBorders/nwb-schema/issues/406)

4.  Documentation for the two photon series\
    [<u>https://github.com/NeurodataWithoutBorders/nwb-schema/issues/522</u>](https://github.com/NeurodataWithoutBorders/nwb-schema/issues/522)

5.  Improved optogenetics support in vanilla NWB.\
    [<u>https://github.com/NeurodataWithoutBorders/nwb-schema/issues/517</u>](https://github.com/NeurodataWithoutBorders/nwb-schema/issues/517)

6.  Support 4D colored, static images\
    [<u>https://github.com/NeurodataWithoutBorders/nwb-schema/issues/536</u>](https://github.com/NeurodataWithoutBorders/nwb-schema/issues/536)

7.  \[Discussion\] Representation of data in microscopy series.\
    [<u>https://github.com/catalystneuro/ndx-microscopy/issues/10</u>](https://github.com/catalystneuro/ndx-microscopy/issues/10)

8.  Light Beads Microscopy\
    [<u>https://github.com/catalystneuro/ndx-microscopy/issues/8</u>](https://github.com/catalystneuro/ndx-microscopy/issues/8)

9.  Multi-channel, multi-plane TwoPhotonSeries / ImageSeries\
    [<u>https://github.com/NeurodataWithoutBorders/helpdesk/discussions/64#discussioncomment-8026504</u>](https://github.com/NeurodataWithoutBorders/helpdesk/discussions/64#discussioncomment-8026504)

## 3.3. Scope

*What aspects are within the scope of this proposal? What aspects are outside the scope of this proposal?*

1.  **Adding comprehensive device metadata:** Extending the base Device class to include detailed specifications for optical components.

2.  **Adding support for optical components:** Creating dedicated neurodata types for excitation sources, filters, detectors, mirrors, and other optical components.

3.  **Adding support for indicators/effectors:** Creating dedicated neurodata types for fluorescent indicators and optogenetic effectors.

4.  **Improving integration with optical data:** Providing a clear way to link optical data with the devices used to acquire it.

5.  **Supporting optical path documentation:** Enabling researchers to document the complete optical path (emission and excitation) of their experiments.

6.  **Enhancing imaging space representation**: Adding support for planar and volumetric imaging spaces with detailed metadata.

7.  **Expanding microscopy series types**: Adding support for volumetric imaging and multi-plane acquisition. Generalize across excitation modes: one-photon, two-photon, multi-photon, etc.

8.  **Enhancing segmentation capabilities**: Adding support for 2D and 3D segmentation.

The proposal focuses on the data structures and metadata needed to represent optical devices and microscopy data in NWB. It does not address: static images, and an improved representation of motion-corrected data, although there is a plan to include them with the support of these extensions.

# 4. Implementation

## 4.1. Proposed changes to schema and software

*How should the schema of the extension be structured?*

*What changes to software should be made to support the extensions?*

*Are there any [<u>best practices</u>](https://nwbinspector.readthedocs.io/en/dev/best_practices/best_practices_index.html) or conventions that are not enforced by the proposed enhancements to the schema (if any) that should be implemented in the NWB Inspector when encountering relevant data?*

*Please provide examples.*

*Use the [<u>NDX template</u>](https://github.com/nwb-extensions/ndx-template) to implement the extension proposal.*

The **ndx-ophys-devices extension** introduces several new neurodata types to enhance the NWB format for optical device metadata. These types are organized into four main categories, each addressing specific aspects of optical experimental setups.

### Optical Components

The extension introduces several neurodata types for documenting various optical components:

**StereotacticPosition**: Extends NWBContainer to hold metadata about the stereotactic position of a device relative to the brain. It includes:

Attributes:

- **anatomical_target:** text, required, the targeted anatomical location.

- **origin**: text, required, a description of where (0,0,0) is in the space. For example, 'bregma' is a common origin for mice.

- **orientation**: text, required, a 3-letter string. One of A,P,L,R,S,I for each of x, y, and z. For example, the most common orientation is 'RAS', which means x is right, y is anterior, and z is superior (a.k.a. dorsal). For dorsal/ventral use 'S/I' (superior/inferior). In the AnatomicalCoordinatesTable, an orientation of 'RAS' corresponds to coordinates in the order of (ML (x), AP (y), DV (z)).

- **x_in_mm**: float, required, X coordinate in millimeters of the device insertion point, in the stereotactic coordinate system defined by \`origin\` and \`orientation\`.

- **y_in_mm**: float, required, Y coordinate in millimeters of the device insertion point, in the stereotactic coordinate system defined by \`origin\` and \`orientation\`.

- **z_in_mm**: float, required, Z coordinate in millimeters of the device insertion point, in the stereotactic coordinate system defined by \`origin\` and \`orientation\`.

- pitch_in_deg: float, optional, pitch angle in degrees of the device insertion (rotation around left-right axis, + is rotating the nose upward).

- yaw_in_deg: float, optional, yaw angle in degrees of the device insertion (rotation around dorsal-ventral axis, + is rotating the nose rightward).

- roll_in_deg: float, optional, roll angle in degrees of the device insertion (rotation around anterior-posterior axis, + is rotating the right side downward).

**OpticalFiberModel**: Extends DeviceModel to represent optical fibers used in fiber photometry or optogenetic experiments. It includes:

Attributes:

- **numerical_aperture**: float, required, e.g., 0.39 NA.

- core_diameter_in_um: float, optional, core diameter in micrometers.

- active_length_in_mm: float, optional, e.g., Active length in mm for a tapered fiber, e.g., Optogenix Lambda fiber. See [<u>https://www.optogenix.com/lambda-fibers/</u>](https://www.optogenix.com/lambda-fibers/) for details of one example.

- ferrule_name: text, optional, product name of the ferrule.

- ferrule_model: text, optional, model (or product ID) of the ferrule from the manufacturer.

- ferrule_diameter_in_mm: float, optional, ferrule diameter in mm, e.g., 1.25 mm (LC) or 2.5 mm (FC).

- manufacturer: text, optional (from DeviceModel)

- model_number: text, optional (from DeviceModel)

- description: text, optional (from DeviceModel)

**OpticalFiber**: Extends Device to represent optical fibers used in fiber photometry or optogenetic experiments. It includes the attributes of Device and:

Attributes:

- serial_number: text, optional (from Device)

Groups:

- fiber_insertion: StereotacticPosition, required. Information about the insertion of an optical fiber into the brain.

Links:

- model: link (from Device)

**ObjectiveLensModel**: Extends DeviceModel to represent objective lenses used in microscopy. It includes:

Attributes:

- **numerical_aperture**: float, required, e.g., 0.39 NA.

- magnification: float, optional, magnification of the lens as specified by the manufacturer, i.e. '60.0' is a 60X lens.

- manufacturer: text, optional (from DeviceModel)

- model_number: text, optional (from DeviceModel)

- description: text, optional (from DeviceModel)

**ObjectiveLens**: Extends Device to hold metadata on the Objective Lens instance. It includes:

Attributes:

- serial_number: text, optional (from Device)

Groups:

- lens_positioning: StereotacticPosition, optional. Information about the positioning of the objective lens relative to the brain.

Links:

- model: link (from Device)

**ExcitationSourceModel**: Extends DeviceModel to represent excitation source models used for excitation in optical experiments. It includes:

Attributes:

- **source_type**: text, required. Type of source. Suggested values: LED, Gas Laser (e.g., Argon, Krypton), Solid-State Laser (e.g., Diode, DPSS).

- **excitation_mode**: text, required. The type of excitation used in the light path (e.g., 'one-photon', 'two-photon', 'three-photon', 'other').

- **wavelength_range_in_nm**: float, optional, shape (2). The range of wavelengths that can be produced by the source.

- manufacturer: text, optional (from DeviceModel)

- model_number: text, optional (from DeviceModel)

- description: text, optional (from DeviceModel)

**ExcitationSource**: Extends Device to represent excitation sources used in the optical experiments. It includes:

Attributes:

- power_in_W: float, optional. Incident power of stimulation device (in Watts).

- intensity_in_W_per_m2: float, optional. Intensity of the excitation in W/m^2, if known.

- exposure_time_in_s: float, optional. Exposure time of the sample (in sec).

- serial_number: text, optional (from Device)

Links:

- model: link (from Device)

**PulsedExcitationSource**: Extends ExcitationSource to represent pulsed light sources used in multi-photon microscopy or optogenetic stimulation. It includes:

Attributes:

- peak_power_in_W: float, optional. Incident peak power of stimulation device (in Watts).

- peak_pulse_energy_in_J: float, optional, pulse energy (in Joules).

- pulse_rate_in_Hz: float, optional, pulse rate (in Hz) used for stimulation.

- serial_number: text, optional (from Device)

Links:

- model: link (from Device)

**PhotodetectorModel**: Extends DeviceModel to represent photodetector models used in optical experiments. It includes:

Attributes:

- **detector_type**: text, required. Type of source. Technology used to detect the light. Suggested values: CCD, Intensified CCD, PMT, Photodiode, CMOS, EBCCD, FTIR.

- gain: float, optional. Gain on the photodetector.

- gain_unit: text, optional. Unit of the gain value.

- wavelength_range_in_nm: float, optional, shape (2). The range of wavelengths that can be detected.

- manufacturer: text, optional (from DeviceModel)

- model_number: text, optional (from DeviceModel)

- description: text, optional (from DeviceModel)

**Photodetector**: Extends Device to represent photodetectors used in the optical experiments. It includes the attributes of Device.

Attributes:

- serial_number: text, optional (from Device)

Links:

- model: link (from Device)

**DichroicMirrorModel**: Extends DeviceModel to represent dichroic mirror models used in optical setups. It includes:

- **cut_on_wavelength_in_nm**: float, optional. Wavelength at which the mirror starts to transmit light more than reflect.

- **cut_off_wavelength_in_nm**: float, optional. Wavelength at which transmission shifts back to reflection, for mirrors with complex transmission spectra.

- **reflection_band_in_nm**: float, optional, shape (2). The range of wavelengths that are primarily reflected.The start and end wavelengths needs to be specified.

- **transmission_band_in_nm**: float, optional, shape (2). The range of wavelengths that are primarily transmitted.The start and end wavelengths needs to be specified.

- **angle_of_incidence_in_degrees**: float, optional. Intended angle at which light strikes the mirror.

- manufacturer: text, optional (from DeviceModel)

- model_number: text, optional (from DeviceModel)

- description: text, optional (from DeviceModel)

**DichroicMirror**: Extends Device to represent dichroic mirrors used in the optical experiments. It includes the attributes of Device.

Attributes:

- serial_number: text, optional (from Device)

Links:

- model: link (from Device)

**OpticalFilterModel**: An abstract base class that extends DeviceModel and provides a common attribute for all optical filter models:

Attributes:

- **filter_type**: text, required. Type of filter (e.g., 'Bandpass', 'Bandstop', 'Longpass', 'Shortpass').

- manufacturer: text, optional (from DeviceModel)

- model_number: text, optional (from DeviceModel)

- description: text, optional (from DeviceModel)

**OpticalFilter**: An abstract base class that extends Device and provides a common attribute for all optical filters. It includes the attributes of Device.

Attributes:

- serial_number: text, optional (from Device)

Links:

- model: link (from Device)

**BandOpticalFilterModel**: Extends OpticalFilterModel to represent bandpass or bandstop filter models. It adds:

Attributes:

- **center_wavelength_in_nm**: float, required. The midpoint of the band of wavelengths that the filter transmits or blocks.

- **bandwidth_in_nm**: float, required. The width of the wavelength range that the filter transmits or blocks (full width at half maximum).

- manufacturer: text, optional (from DeviceModel)

- model_number: text, optional (from DeviceModel)

- description: text, optional (from DeviceModel)

**BandOpticalFilter**: Extends OpticalFilter to represent bandpass or bandstop filters used in the optical experiments. It includes the attributes of Device.

Attributes:

- serial_number: text, optional (from Device)

Links:

- model: link (from Device)

**EdgeOpticalFilterModel**: Extends OpticalFilter to represent longpass or shortpass filter models. It adds:

Attributes:

- **cut_wavelength_in_nm**: float, required. The wavelength at which the filter transmits half as much as its peak transmission.

- slope_in_percent_cut_wavelength: float, optional. The steepness of the transition from high blocking to high transmission (or vice versa). Specified as a percentage of the cut wavelength.

- slope_starting_transmission_in_percent: float, optional. The percent transmission that defines the starting point for the slope (e.g. 10%).

- slope_ending_transmission_in_percent: float, optional.The percent transmission that defines the ending point for the slope (e.g. 80%).

- manufacturer: text, optional (from DeviceModel)

- model_number: text, optional (from DeviceModel)

- description: text, optional (from DeviceModel)

**EdgeOpticalFilter**: Extends OpticalFilter to represent longpass or shortpass filters used in the optical experiments. It includes the attributes of Device.

Attributes:

- serial_number: text, optional (from Device)

Links:

- model: link (from Device)

***Comparison with current schema:*** The current NWB schema does not have dedicated types for these optical components. These new types provide a standardized way to document the detailed specifications of optical component models and thire instances used in experiments.

### Fluorescent Indicators and Effectors

The extension introduces two neurodata types for documenting fluorescent indicators and optogenetic effectors:

**ViralVector**: This type extends the NWBContainer class and represents the virus construct/vector for the indicator/effector.

Attributes:

- **construct_name**: text, required. Name of the virus construct/vector, e.g., "AAV-EF1a-DIO-hChR2(H134R)-EYFP".

- **titer_in_vg_per_ml**: float, requiredTiter of the virus, in vg/ml, e.g., 1x10^12 vg/ml.

- **manufacturer**: text, required. Manufacturer of the virus.

- description: text, optional.Description of the virus.

**ViralVectorInjection**: This type extends the NWBContainer class and stores information about the injection of a viral vector that delivers indicators or effectors for ophys experiments. Use two ViralVectorInjection objects for a bilateral injection, one per hemisphere.

Attributes:

- volume_in_uL: float, required. Volume of injection, in uL., e.g., 0.45 uL (450 nL)

- description: text, optional.

- injection_date: text, optional. Date of injection.

Groups:

- viral_injection_coordinates: StereotacticPosition, optional. Stereotactic coordinates of the viral vector injection site.

Links:

- viral_vector: ViralVector, required. Link to ViralVector object with metadata about the name, manufacturer, and titer.

**Indicator**: This type extends the NWBContainer class and represents fluorescent indicators used in optical experiments. It includes:

Attributes:

- **label**: text, required. Indicator notation.

- manufacturer: text, optional. Indicator manufacturer.

- description: text, optional. Indicator description.

Links:

- viral_vector_injection: ViralVectorInjection, optional. Link to ViralVectorInjection object with metadata about the injection of the indicator.

**Effector**: This type also extends the NWBContainer class and represents optogenetic effectors (opsins) used in optogenetic experiments.

Attributes:

- **label**: text, required. Effector notation.

- manufacturer: text, optional. Effector manufacturer.

- description: text, optional. Effector description.

Links:

- viral_vector_injection: ViralVectorInjection, optional. Link to ViralVectorInjection object with metadata about the injection of the effector.

***Comparison with current schema:*** The current NWB schema does not have dedicated types for fluorescent indicators or optogenetic effectors. These new types provide a standardized way to document these critical components of optical experiments.

The **ndx-microscopy extension** introduces several new neurodata types to enhance the NWB format for microscopy data. These types are organized into five main categories, each addressing specific aspects of microscopy data representation.

### Device Components

The extension introduces a specialized **MicroscopeModel** neurodata type that extends the base DeviceModel class, and **Microscope** neurodata type that extends the base DeviceInstance class, both from the ndx-ophys-devices extension. This dedicated type allows for better identification the microscope devices within the NWB file.

**MicroscopeModel**: This type extends the DeviceModel class and represents the model of a microscope. It includes:

Attributes:

- manufacturer: text, optional (from DeviceModel)

- model_number: text, optional (from DeviceModel)

- description: text, optional (from DeviceModel)

**Microscope**: This type extends the Device class and represents the instance of a microscope. It includes:

Attributes:

- technique: text, optional. Imaging technique used by the microscope (e.g. scan mirrors, light sheet, temporal focusing, acusto-optical modulation, piezo z-scan mirrors).

- serial_number: text, optional (from Device)

Links:

- model: link (from Device)

Comparison with current schema: The current NWB schema uses the generic Device class for all devices, including microscopes. This approach lacks specificity and makes it difficult to identify and work with microscope devices. The new Microscope type provides a dedicated class for microscopes, making it easier to identify and work with microscope devices in analysis and visualization tools.

**MicroscopyRig:** This type extends the NWBContainer class and represents a collection of devices and metadata that make up the microscopy rig. It includes:

Attributes:

- description: text, required.

Links:

- **microscope**: Microscope, required. Link to Microscope object which contains metadata about the microscope used to acquire imaging data.

- excitation_source: ExcitationSource, optional. Link to ExcitationSource object which contains metadata about the excitation source device. If it is a pulsed excitation source link a PulsedExcitationSource object.

- excitation_filter: OpticalFilter, optional. Link to OpticalFilter object which contains metadata about the excitation filter. It can be either a BandOpticalFilter (e.g., 'Bandpass', 'Bandstop', 'Longpass', 'Shortpass') or a EdgeOpticalFilter (Longpass or Shortpass).

- dichroic_mirror: DichroicMirror, optional. Link to DichroicMirror object which contains metadata about the dichroic mirror.

- photodetector: Photodetector, optional. Link to Photodetector object which contains metadata about the photodetector device.

- emission_filter: OpticalFilter, optional. Link to OpticalFilter object which contains metadata about the emission filter. It can be either a BandOpticalFilter (e.g., 'Bandpass', 'Bandstop', 'Longpass', 'Shortpass') or a EdgeOpticalFilter (Longpass or Shortpass).

- objective_lens: ObjectiveLens, optional. Link to ObjectiveLens object which contains metadata about the objective lens used in the microscopy rig.

***Comparison with current schema:*** The current NWB schema does not have dedicated types for tracking the light path. The ImagingPlane class includes some basic information about the optical setup, but lacks the detailed tracking provided by these new types. This enhancement allows for complete documentation of the optical configuration, which is essential for experimental reproducibility and data interpretation.

### Microscopy Experiment Metadata

The extension introduce the MicroscopyExperimentMetadata neurodatatype:

**MicroscopyExperimentMetadata:** This type extends the NWBContainer class and holds metadata about the microscopy experiment. Note that the container classes (such as MicroscopyRig, ViralVector, ViralVectorInjection, Indicator) cannot be directly added to the NWB file, but instead require extending LabMetaData to contain one or more of these container classes in a separate extension.It includes:

Groups:

- **MicroscopyRig**: Group containing of one or more MicroscopyRig objects.

- **ViralVector**: Group containing of one or more ViralVector objects.

- **ViralVectorInjection**: Group containing one or more ViralVectorInjection objects.

- **Indicator**: Group containing one or more Indicator objects.

### MicroscopyChannel Component

The extension updates the OpticalChannel neurodatatype:

**MicroscopyChannel:** This type extends the NWBContainer class and represents a channel in a microscope that contains metadata about the indicator, the excitation and emission wavelengths. This will be contained in the MicroscopySeries object to univocally identify the channel that generates that series.

Attributes:

- **name**: text, required. Name of the channel.

- **excitation_wavelength_in_nm**: float, required.Wavelength of the excitation light in nanometers.

- **emission_wavelength_in_nm**: float, required. Wavelength of the emission light in nanometers.

- description: text, optional. Description of the channel.

Links:

- **indicator**: Indicator, required. Link to Indicator object which contains metadata about the indicator used in this light path.

### Illumination Pattern

**IlluminationPattern**: This type extends the NWBContainer class for describing the illumination pattern used to acquire. It only have one attribute:

- description: text, optional.General description of the illumination pattern used.

**LineScan**: Extends IlluminationPattern to represent line scanning method, and provides addition attributes, including:

Attributes:

- scan_direction: text, optional. Direction of line scanning (horizontal or vertical).

- line_rate_in_Hz: float, optional. Rate of line scanning in lines per second.

- dwell_time_in_s: float, optional.Average time spent at each scanned point.

**PlaneAcquisition**: Extends IlluminationPattern to represent whole plane acquisition, common for light sheet techniques, and provides addition attributes, including:

Attributes:

- point_spread_function_in_um: text, optional.Estimated plane spatial profile or point spread function, expressed as mean \[um\] ± s.d \[um\].

- illumination_angle_in_degrees: float, optional. Angle of illumination in degrees.

- plane_rate_in_Hz: float, optional. Rate of plane acquisition in planes per second.

**RandomAccessScan**: Extends IlluminationPattern to represent Random access method for targeted, high-speed imaging of specific regions. Provides addition attributes, including:

Attributes:

- max_scan_points: int, optional.Maximum number of points that can be scanned in a single frame.

- dwell_time_in_s: float, optional. Average time spent at each scanned point.

- scanning_pattern: text, optional. Description of the point selection strategy.

### Imaging Space Components

The extension introduces a hierarchy of neurodata types for representing imaging spaces:

**ImagingSpace:** An abstract base class that extends NWBContainer and provides common attributes for all imaging spaces, including:

Attributes:

- **anatomical_target**: text, required. Name of the targeted anatomical location being subset by this space. Specify the area, layer, etc. Use standard atlas names for anatomical regions when possible. Use 'whole brain' if the entire brain is strictly contained within the space.

- description: text, optional. Description of the imaging space.

Groups:

- **IlluminationPattern**: required. IlluminationPattern object containing metadata about the method used to acquire this imaging data.

**PlanarImagingSpace:** Extends ImagingSpace for 2D imaging planes, adding:

Datasets:

- pixel_size_in_um: float\[x, y\], optional. The physical dimensions of the pixel in micrometers.

- dimensions_in_pixels: float\[x, y\], optional. The number of pixels in the x and y dimensions of the imaging space.

It include a method to compute the FOV size: get_FOV_size()

**VolumetricImagingSpace:** Extends ImagingSpace for 3D imaging volumes, adding:

Datasets:

- voxel_size_in_um: float\[x, y, z\], optional. The physical dimensions of the voxel in micrometers.

- dimensions_in_voxels: float\[x, y, z\], optional. The number of voxels in the x, y and z dimensions of the imaging space.

It include a method to compute the FOV size: get_FOV_size()

***Comparison with current schema:*** The current NWB schema uses the ImagingPlane class to represent imaging spaces. This class is designed primarily for 2D imaging and lacks support for volumetric imaging. The new types provide a more flexible and comprehensive representation of imaging spaces. The ImagingSpace class should only store information about the imaging space. The localization with respect to a specific coordinate system, either stereotactic or common coordinate framework, is delegated to the [<u>ndx-anatomical-localization</u>](https://github.com/catalystneuro/ndx-anatomical-localization).

### MicroscopyStaticImage Components

The extension introduces a hierarchy of neurodata types for storing microscopy static images:

**MicroscopyStaticImage:** An abstract base class that extends NWBDataInterface and provides common attributes for all microscopy static images, including:

Attributes:

- name: text, required. Name of the static image.

- description: text, required. Description of the static image.

Links:

- microscopy_rig: MicroscopyRig, required. Link to a MicroscopyRig object containing metadata about the microscopy rig used to acquire this imaging data.

Groups:

- MicroscopyChannel: required. MicroscopyChannel object containing metadata about the channel used to acquire this imaging data.

**PlanarMicroscopyStaticImage:** Extends MicroscopyStaticImage for 2D imaging data acquired from an optical channel in a microscope while a light source illuminates a planar imaging space. It includes:

Datasets:

- data: float\[ height, width\], required. Recorded imaging data, shaped by (frame height, frame width).

Groups:

- PlanarImagingSpace: required. PlanarImagingSpace object containing metadata about the region of physical space this imaging data was recorded from.

**VolumetricMicroscopyStaticImage:** Extends MicroscopyStaticImage for 3D imaging data acquired from an optical channel in a microscope while a light source illuminates a volumetric imaging space. It includes:

Datasets:

- data: float\[ height, width, depth\], required. Recorded imaging data, shaped by (frame height, frame width, number of depth planes).

Groups:

- VolumetricImagingSpace: required. VolumetricImagingSpace object containing metadata about the region of physical space this imaging data was recorded from.

### MicroscopySeries Components

The extension introduces a hierarchy of neurodata types for storing microscopy time series data:

**MicroscopySeries:** An abstract base class that extends TimeSeries and provides common attributes for all microscopy series, including:

Links:

- microscopy_rig: MicroscopyRig, required. Link to a MicroscopyRig object containing metadata about the microscopy rig used to acquire this imaging data.

Groups:

- MicroscopyChannel: required. MicroscopyChannel object containing metadata about the channel used to acquire this imaging data.

**PlanarMicroscopySeries:** Extends MicroscopySeries for 2D imaging data acquired over time from an optical channel in a microscope while a light source illuminates a planar imaging space. It includes:

Datasets:

- data: float\[frames, height, width\], required. Recorded imaging data, shaped by (number of frames, frame height, frame width).

Groups:

- PlanarImagingSpace: required. PlanarImagingSpace object containing metadata about the region of physical space this imaging data was recorded from.

**VolumetricMicroscopySeries:** Extends MicroscopySeries for 3D imaging data acquired over time from an optical channel in a microscope while a light source illuminates a volumetric imaging space. It includes:

Datasets:

- data: float\[frames, height, width, depth\], required. Recorded imaging data, shaped by (number of frames, frame height, frame width, number of depth planes).

Groups:

- VolumetricImagingSpace: required. VolumetricImagingSpace object containing metadata about the region of physical space this imaging data was recorded from.

**MultiPlaneMicroscopyContainer:** A container class that extends NWBDataInterface and holds multiple PlanarMicroscopySeries or PlanarMicroscopyStaticImage objects, each representing a different imaging plane. This is particularly useful for multi-plane acquisition systems like those using electrically tunable lenses. The multi-plane acquisition allows for storing imaging data acquired at different depths (e.g. irregular spacing along the z-axis), and/or planes with different FOV sizes. This is achieved by separating imaging data from metadata describing the imaging space associated with each plane.

Groups:

- PlanarMicroscopyStaticImage: \[0,..\], optional. PlanarMicroscopyStaticImage object(s) each containing imaging data for a single depth scan.

- PlanarMicroscopySeries: \[0,..\], optional. PlanarMicroscopyStaticImage object(s) each containing imaging data for a single depth scan.

**MultiChannelMicroscopyContainer:** A container class that extends NWBDataInterface and holds multiple PlanarMicroscopySeries/PlanarMicroscopyStaticImage objects or multiple VolumetricMicroscopySeries/VolumetricMicroscopyStaticImage objects, each representing a different channel. This is particularly useful for multi-channel acquisition systems like those using different indicators. This is achieved by separating imaging data from metadata describing the microscopy channel and microscopy rig associated with each series.

Groups:

- MicroscopyStaticImage: \[0,..\], optional. MicroscopyStaticImage object(s) each containing imaging data for a single channel.

- MicroscopySeries: \[0,..\], optional. MicroscopySeries object(s) each containing imaging data for a single channel.

- MultiPlaneMicroscopyContainer: \[0,..\], optional. MultiPlaneMicroscopyContainer object(s) containing imaging data acquired over several depths.

***Comparison with current schema:*** The current NWB schema includes TwoPhotonSeries and OnePhotonSeries for storing imaging data. These classes are designed for specific microscopy techniques and lack support for other types of microscopy setup or multi-plane or multi-channel acquisition. The new types provide a more flexible and comprehensive representation of microscopy data, with better support for different acquisition modalities.

### Segmentation Components

The extension introduces several neurodata types for segmentation and ROI analysis:

**SegmentationContainer:** A container class that extends NWBDataInterface and holds the results of a segmentation algorithm applied to a MicroscopySeries. It includes:

Groups:

- Segmentation: \[1,..\], required. Results from image segmentation.

**Segmentation:** Abstract class that extends DynamicTable to contain the spatial components resulting from image segmentation of a specific imaging space. It includes:

Attributes:

- description: text, required. Description of the segmentation method used.

Groups:

- SummaryImage: \[0,..\], optional. Summary images that are related to the segmentation, e.g., mean, correlation, maximum projection.

**PlanarSegmentation:** Extends Segmentation to contain the ROI spatial components resulting from image segmentation of a specific planar imaging space. It includes:

Datasets (columns of the DynamicTable):

- image_mask: float\[num_roi, height, width \], optional. ROI masks for each ROI. Each image mask is the size of the original planar imaging space and members of the ROI are finite non-zero.

- pixel_mask: optional. Pixel masks for each ROI: a list of indices and weights for the ROI. Pixel masks are concatenated and parsing of this dataset is maintained by the PlanarSegmentation

dtype:

\- name: x

dtype: int

doc: Pixel x-coordinate.

\- name: y

dtype: int

doc: Pixel y-coordinate.

\- name: weight

dtype: float

doc: Weight of the pixel.

Groups:

- PlanarImagingSpace: required. PlanarImagingSpace object from which this data was generated.

**VolumetricSegmentation:** Extends Segmentation to contain the ROI spatial components resulting from image segmentation of a specific volumetric imaging space. It includes:

Datasets (columns of the DynamicTable):

- volume_mask: float\[num_roi, height, width, depth\], optional. ROI masks for each ROI. Each image mask is the size of the original volumetric imaging space and members of the ROI are finite non-zero.

- voxel_mask: optional. Voxel masks for each ROI: a list of indices and weights for the ROI. Voxel masks are concatenated and parsing of this dataset is maintained by the VolumetricImagingSpace

dtype:

\- name: x

dtype: int

doc: Pixel x-coordinate.

\- name: y

dtype: int

doc: Pixel y-coordinate.

\- name: z

dtype: int

doc: Pixel z-coordinate.

\- name: weight

dtype: float

doc: Weight of the pixel.

Groups:

- VolumetricImagingSpace: required. VolumetricImagingSpace object from which this data was generated.

***Comparison with current schema:*** The current NWB schema includes ImageSegmentation and PlaneSegmentation for ROI definition. These classes are designed primarily for 2D imaging and lack support for 3D segmentation or multi-plane organization. The new types provide a more flexible and comprehensive representation of segmentation data, with better support for different ROI representations and organizations.

**MicroscopyResponseSeries**: Extendes TimeSeries to store ROI responses extracted from imaging data, linked in the microscopy_series field. This object contains the temporal components from multiple ROIs, that can result from different processing steps, e.g., raw, deconvolved, or denoised fluorescence traces.

Datasets:

- **data**: float\[number_of_frames, number_of_rois\], required. Extracted signals from ROIs.

- **rois**: DynamicTableRegion, required. DynamicTableRegion referencing Segmentation table containing information about the ROIs spatial components.

Links:

- microscopy_series: MicroscopySeries, optional. Link to a MicroscopySeries object containing the imaging data this response series is derived from.

### Software Implementation

The ndx-microscopy extension is implemented in Python using the PyNWB framework. The implementation includes:

**API Functions:** The extension provides helper functions for common operations, such as:

- Adding ROIs to segmentation tables

- Converting between image/volume and pixel/voxel mask representations

- Creating table regions for referencing subsets of ROIs

- Computing FOV size

**Integration with ndx-ophys-devices:** The extension integrates with the ndx-ophys-devices extension to provide comprehensive optical component specifications.

The extensions are available as Python packages that can be installed via pip, and the source code is available on GitHub. The implementation follows best practices for NWB extensions, including comprehensive documentation, type checking, and validation.

## 4.3. Discussion

*Does the implementation consider and meet the [<u>NWBEP quality metrics and evaluation criteria</u>](https://docs.google.com/document/d/1g8NWD-5q8SBLvoedOm4jWBXvY6aOG7VSAZ0owjjTUkY/edit)?*

*What alternatives for implementing were considered?*

*What are the advantages and disadvantages of the alternative implementations?*

*Are there reasons why this enhancement should NOT be made?*

### Significance and Impact of the ndx-ophys-devices extension 

**Significance**: The ndx-ophys-devices extension addresses a critical gap in the NWB ecosystem by providing comprehensive support for documenting optical device metadata. The current implementation of the device module has significant limitations in representing the detailed specifications of optical components used in experiments.

The extension serves a broad audience within the neurophysiology community, including:

- Researchers using microscopy techniques

- Researchers using fiber photometry experiments

- Researchers using optogenetic stimulation

**Impact**: The ndx-ophys-devices extension can:

- Enable standardized documentation of optical experimental setups

- Add capabilities to NWB that were previously unavailable, particularly for documenting optical components

- Create a framework that can evolve with advances in optical technologies. The extension has been designed to be easily extended by the user to include specific devices in their setup.

- Be smoothly integrated into already existing extensions:

  - ndx-fiber-photometry: [<u>https://github.com/catalystneuro/ndx-fiber-photometry</u>](https://github.com/catalystneuro/ndx-fiber-photometry)

  - ndx-patterned-ogen: [<u>https://github.com/catalystneuro/ndx-patterned-ogen</u>](https://github.com/catalystneuro/ndx-patterned-ogen)

  - ndx-optogenetics: [<u>https://github.com/rly/ndx-optogenetics</u>](https://github.com/rly/ndx-optogenetics)

  - ndx-multichannel: [<u>https://github.com/focolab/ndx-multichannel-volume</u>](https://github.com/focolab/ndx-multichannel-volume)

### Clarity and Usability of the ndx-ophys-devices extension 

**Precision**: Each neurodata type has detailed documentation explaining its purpose, attributes, and relationships to other types. The schema is precisely defined with explicit data types, dimensions, and relationships, making it easy for users to understand the structure and purpose of each component.

**Human and Machine Readability and Usability:** The extension prioritizes both human and machine readability:

- Intuitive naming conventions that clearly indicate the purpose of each component

- Hierarchical organization that mirrors the conceptual organization of optical experimental setups

- Consistent patterns for similar components (e.g., different types of optical filters)

- Comprehensive example notebooks demonstrating common use cases

**Reusability and FAIR Principles:** The extension strongly supports the FAIR (Findable, Accessible, Interoperable, Reusable) principles by:

- Capturing comprehensive metadata about the experimental setup, including detailed optical component specifications

- Providing standardized structures for storing metadata that can be easily queried and further extended to include new devices.

- Complying with already existing standards in the microscopy field:

  - [<u>DORY</u>](https://doryworkspace.org/metadata)

  - [<u>BIDS</u>](https://bids-specification.readthedocs.io/en/stable/04-modality-specific-files/10-microscopy.html)

  - [<u>OME XML</u>](https://www.openmicroscopy.org/Schemas/Documentation/Generated/OME-2016-06/)

### Implementation of the ndx-ophys-devices extension 

**Implementability**: The ndx-ophys-devices extension is designed to be implementable across all reasonable target platforms:

- Built on the PyNWB framework, ensuring compatibility with Python-based workflows

- Minimal dependencies beyond the core NWB ecosystem

- The implementation requires minimal changes to existing NWB infrastructure while providing significant new capabilities.

**Compatibility**: The extension maintains strict compliance with NWB standards and best practices:

- Extends existing NWB base classes appropriately

- Follows NWB naming conventions and design patterns

- Integrates with the existing device module rather than replacing it

**Maintainability**: The extension is designed for long-term maintainability:

- Modular design with clear separation of concerns

- Minimal external dependencies

- Comprehensive test suite

- Well-documented code and API

- Open source development model with community contributions

The extension is structured to allow for future enhancements and additions as optical technologies evolve, without requiring major restructuring.

### Significance and Impact of the ndx-microscopy extension

**Significance**: The ndx-microscopy extension addresses a critical gap in the NWB ecosystem by providing comprehensive support for modern microscopy techniques. The current implementation of the ophys module has significant limitations for representing volumetric imaging data, multi-plane acquisitions, multi-channel acquisitions, and detailed optical component specifications. This extension removes these barriers to progress by enabling researchers to store and share complex microscopy datasets in a standardized format.

The extension serves a broad audience within the neurophysiology community, including:

- Researchers using one-photon, two-photon, three-photon, and light sheet microscopy

- Labs conducting calcium and voltage imaging experiments

- Computational neuroscientists analyzing microscopy data

**Impact**: The ndx-microscopy extension can:

- Enable standardized storage of microscopy data, even for complex microscopy setups.

- Add unique capabilities to NWB that were previously unavailable, particularly for volumetric and multi-plane imaging

- Create a framework that can evolve with advances in microscopy technology

The extension's impact extends beyond data storage to enable better integration with analysis pipelines and visualization tools.

### Clarity and Usability of the ndx-microscopy extension

**Precision:** The ndx-microscopy extension is designed with clear and unambiguous definitions. Each neurodata type has detailed documentation explaining its purpose, attributes, and relationships to other types. The schema is precisely defined with explicit data types, dimensions, and relationships, making it easy for users to understand the structure and purpose of each component.

**Human and Machine Readability and Usability:** The extension prioritizes both human and machine readability:

- Intuitive naming conventions that clearly indicate the purpose of each component

- Hierarchical organization that mirrors the conceptual organization of microscopy experiments

- Consistent patterns for similar components (e.g., 2D vs. 3D structures)

- Clear separation of metadata from data

- Comprehensive example notebooks demonstrating common use cases

The API is designed to be intuitive for researchers, with helper methods for common operations like ROI manipulation and data extraction.

**Reusability and FAIR Principles:** The extension strongly supports the FAIR (Findable, Accessible, Interoperable, Reusable) principles by:

- Capturing comprehensive metadata about the experimental setup, including detailed optical component specifications

- Providing standardized structures for storing both raw data and derived results

- Including spatial reference information that enables integration with anatomical atlases

### Implementation of the ndx-microscopy extension

**Implementability:** The ndx-microscopy extension is designed to be implementable across all reasonable target platforms:

- Built on the PyNWB framework, ensuring compatibility with Python-based workflows

- Minimal dependencies beyond the core NWB ecosystem and ndx-ophys-devices

**Compatibility:** The extension maintains strict compliance with NWB standards and best practices:

- Extends existing NWB base classes appropriately

- Follows NWB naming conventions and design patterns

The extension also integrates with the ndx-ophys-devices extension to provide comprehensive optical component specifications.

**Maintainability:** The extension is designed for long-term maintainability:

- Modular design with clear separation of concerns

- Comprehensive test suite

- Well-documented code and API

- Open source development model with community contributions

The extension is structured to allow for future enhancements and additions as microscopy techniques evolve, without requiring major restructuring.

**Efficiency**: The extension is designed for efficient data storage and access:

- Appropriate use of data types and compression

- Support for both dense (image masks) and sparse (pixel/voxel masks) representations of ROIs

- Efficient linking between related components

- Hierarchical organization that enables targeted data access

- Container structures that facilitate the organization of related data

# 5. Public Examples

*Example datasets using the proposed extension?*

*Example use cases?*

## 5.1. Example 1

The ndx-ophys-devices extension includes example notebooks that demonstrate how to use the extension for various optical experimental setups:

**Basic Usage Example:** Demonstrates how to create and use all the neurodata types provided by the extension.

These examples are available in the *notebooks* directory of the ndx-ophys-devices repository: [<u>https://github.com/catalystneuro/ndx-ophys-devices/tree/main/notebooks</u>](https://github.com/catalystneuro/ndx-ophys-devices/tree/main/notebooks)

## 5.2. Example 2

The ndx-microscopy extension includes several example notebooks that demonstrate how to use the extension for various microscopy techniques:

1.  **Two-Photon Calcium Imaging Example:** Demonstrates how to use the extension for storing and analyzing two-photon calcium imaging data.

2.  **One-Photon Calcium Imaging Example:** Demonstrates how to use the extension for storing and analyzing one-photon calcium imaging data.

3.  **Volumetric Imaging Example:** Demonstrates how to use the extension for storing and analyzing volumetric imaging data.

4.  **Multi-Plane Imaging Example:** Demonstrates how to use the extension for storing and analyzing multi-plane imaging data.

These examples are available in the *examples* directory of the ndx-microscopy repository: [<u>https://github.com/catalystneuro/ndx-microscopy/tree/main/examples</u>](https://github.com/catalystneuro/ndx-microscopy/tree/main/examples)

# 6. Changelog

*For each main version of the enhancement proposal, briefly describe the main changes made. If the NWBEP is accompanied by a Neurodata Extension (NDX), then include a link to the corresponding changelog here.*

## 6.1. NDX-OPHYS-DEVICES Version 0.1.0 (Dec 18, 2024)

Initial release of the ndx-ophys-devices extension, including:

- Base device model (DeviceModel)

- Fluorescent indicators and effectors (Indicator, Effector)

- Optical components (OpticalFiber, ExcitationSource, PulsedExcitationSource, Photodetector, DichroicMirror, OpticalFilter, BandOpticalFilter, EdgeOpticalFilter, ObjectiveLens)

## 6.2. NDX-OPHYS-DEVICES Version 0.1.1 (Feb 25, 2025)

**Deprecations and Changes:**

- Add excitation mode as a required field for ExcitationSource, and internal check for excitation_mode argument [<u>PR#7</u>](https://github.com/catalystneuro/ndx-ophys-devices/pull/7)

**Improvements:**

- Add example notebook [<u>PR#8</u>](https://github.com/catalystneuro/ndx-ophys-devices/pull/8)

## 6.3. NDX-OPHYS-DEVICES Version 0.2.0 (Jun 3, 2025)

**Major Refactoring:**

- Implemented a clear distinction between device models and device instances:

  - Added DeviceModel as a base class for all device model classes

  - Added DeviceInstance as a base class for all device instance classes

  - Refactored all device classes into model and instance pairs (e.g., OpticalFiberModel and OpticalFiber)

  - Renamed ObjectiveLens to OpticalLens for consistency

**New Features:**

- Added new neurodata types:

  - LensPositioning: Extends NWBContainer to hold metadata on the positioning of a lens relative to the brain.

  - FiberInsertion: Extends NWBContainer to hold metadata on the insertion of a fiber into the brain.

**Changes:**

- Changed illumination_type to source_type in ExcitationSourceModel for better clarity.

- Removed excitation_wavelength_in_nm from ExcitationSourceModel as it's often redundant with filter specifications.

- Removed detected_wavelength_in_nm from PhotodetectorModel as it's often redundant with filter specifications.

- Added wavelength_range_in_nm to ExcitationSourceModel and PhotodetectorModel to specify the range of wavelengths.

## 6.4. NDX-OPHYS-DEVICES Version 0.3.2 (Sep 19, 2025)

**New Features:**

- Added ViralVector and ViralVectorInjection classes to hold metadata about viral vectors used for gene delivery [<u>PR \#14</u>](https://github.com/catalystneuro/ndx-ophys-devices/pull/14)

- Updated injection_date in ViralVectorInjection to plain text [<u>PR \#18</u>](https://github.com/catalystneuro/ndx-ophys-devices/pull/18)

**Changes:**

- Added extra optional attributes to OpticalFiberModel [<u>PR \#13</u>](https://github.com/catalystneuro/ndx-ophys-devices/pull/13)

- Switched to core pynwb DeviceModel and Device classes now that they are available in pynwb 3.1.0 [<u>PR \#20</u>](https://github.com/catalystneuro/ndx-ophys-devices/pull/20)

## 6.5. NDX-OPHYS-DEVICES Version 0.4.0 (Upcoming)

**New Features:**

- Added auto-publish.yml GitHub Action to automatically publish new versions to PyPI upon GitHub Release.

**Deprecations and Changes:**

- Renamed OpticalLens to ObjectiveLens [<u>PR#25</u>](https://github.com/catalystneuro/ndx-ophys-devices/pull/25)

<!-- -->

- Replace FiberInsertion with StereotacticPosition [<u>PR#25</u>](https://github.com/catalystneuro/ndx-ophys-devices/pull/25)

- Replace LensPositioning with StereotacticPosition [<u>PR#25</u>](https://github.com/catalystneuro/ndx-ophys-devices/pull/25)

- Replace ViralVectorInjection fields related to coordinates and angles with StereotacticPosition group [<u>PR#25</u>](https://github.com/catalystneuro/ndx-ophys-devices/pull/25)

## 6.6. NDX-MICROSCOPY Version 0.1.0 (Mar 10, 2025)

The initial release of the ndx-microscopy extension, including:

- Device components (Microscope)

- Light path components (ExcitationLightPath, EmissionLightPath)

- Imaging space components (ImagingSpace, PlanarImagingSpace, VolumetricImagingSpace)

- Microscopy series components (MicroscopySeries, PlanarMicroscopySeries, VolumetricMicroscopySeries, MultiPlaneMicroscopyContainer)

- Segmentation components (Segmentation, Segmentation2D, Segmentation3D, SegmentationContainer, SummaryImage, MicroscopyResponseSeries, MicroscopyResponseSeriesContainer)

- Integration with ndx-ophys-devices for optical component specifications

- Example notebooks for various microscopy techniques

## 6.7. NDX-MICROSCOPY Version 0.2.0 (Mar 19, 2025)

**Deprecations and Changes**

- Change grid_spacing_in_um in pixel_size_in_um and voxel_size_in_um (and relative doc string) to better represent the physical dimension of the fundamental unit of the image (pixel or voxel).

**Improvements**

- New illumination pattern classes to represent different microscopy scanning methods:

  - IlluminationPattern: Base class for describing the illumination pattern used to acquire images

  - LineScan: Line scanning method commonly used in two-photon microscopy

  - PlaneAcquisition: Whole plane acquisition method, common for light sheet and one-photon techniques

  - RandomAccessScan: Random access method for targeted, high-speed imaging of specific regions

- Added technique attribute to the Microscope class to describe the imaging technique used.

- Updated ImagingSpace classes to include an illumination_pattern parameter, creating a direct link between the imaging space and the acquisition method.

- Added mock implementations for all new classes in \_mock.py for testing purposes.

- Updated example notebooks to demonstrate the use of different scanning methods

**Notes**

- These changes are backward compatible and add new functionality without removing existing features

- The illumination_pattern parameter is now required when creating ImagingSpace objects

## 6.8. NDX-MICROSCOPY Version 0.3.0 (June 3, 2025)

**NWB TAB reviews [<u>Issue#48</u>](https://github.com/catalystneuro/ndx-microscopy/issues/48)**

**Deprecations and Changes**

- Removed ExcitationLightPath and EmissionLightPath classes in favor of a more integrated approach with MicroscopyRig

- Changed Microscope to inherit from DeviceInstance instead of Device [<u>Sub-Issue#51</u>](https://github.com/catalystneuro/ndx-microscopy/issues/51)

- Updated MicroscopySeries to use MicroscopyRig instead of individual microscope, excitation_light_path, and emission_light_path references [<u>Sub-Issue#51</u>](https://github.com/catalystneuro/ndx-microscopy/issues/51)

- Refactored segmentation classes: [<u>Sub-Issue#56</u>](https://github.com/catalystneuro/ndx-microscopy/issues/56)

- Renamed Segmentation2D to PlanarSegmentation

- Renamed Segmentation3D to VolumetricSegmentation

- Changed image_to_voxel in volume_to_voxel, voxel_to_image in voxel_to_volume, and image_mask in volume_mask in VolumetricSegmentation [<u>Sub-Issue#57</u>](https://github.com/catalystneuro/ndx-microscopy/issues/57)

**Features**

- Added MicroscopyRig object [<u>Sub-Issue#51</u>](https://github.com/catalystneuro/ndx-microscopy/issues/51)

- Added MicroscopeModel that inherit from DeviceModel [<u>Sub-Issue#51</u>](https://github.com/catalystneuro/ndx-microscopy/issues/51)

- Added MicroscopyChannel object [<u>Sub-Issue#49</u>](https://github.com/catalystneuro/ndx-microscopy/issues/49)

- Added dimensions_in_pixels to PlanarImagingSpace and dimensions_in_voxels to VolumetricImagingSpace object [<u>Sub-Issue#52</u>](https://github.com/catalystneuro/ndx-microscopy/issues/52)

- Added MultiChannelMicroscopyContainer object [<u>Sub-Issue#53</u>](https://github.com/catalystneuro/ndx-microscopy/issues/53)

- Added get_FOV_size() method to both PlanarImagingSpace and VolumetricImagingSpace classes for calculating Field of View size in micrometers [<u>Sub-Issue#53</u>](https://github.com/catalystneuro/ndx-microscopy/issues/53)

- Added microscopy_series link to MicroscopyResponseSeries class [<u>Sub-Issue#58</u>](https://github.com/catalystneuro/ndx-microscopy/issues/58)

## 6.9. NDX-MICROSCOPY Version 0.4.0 (Upcoming)

**Deprecations and Changes:**

- **Breaking Change:** MicroscopyChannel.indicator changed from a nested group to a link reference [<u>PR#73</u>](https://github.com/catalystneuro/ndx-microscopy/pull/73)

- **Breaking Change:** MicroscopySeries.microscopy_rig changed from a nested group to a link reference [<u>PR#73</u>](https://github.com/catalystneuro/ndx-microscopy/pull/73)

- **Breaking Change:** Simplified ImagingSpace class by removing coordinate system metadata: [<u>PR#75</u>](https://github.com/catalystneuro/ndx-microscopy/pull/75)

  - Removed origin_coordinates dataset and its unit attribute

  - Renamed location attribute to anatomical_target for clearer semantics

  - Removed reference_frame attribute

  - Removed orientation attribute

<!-- -->

- Updated ndx-ophys-devices dependency from v0.2.0 to v0.4.0 [<u>PR#76</u>](about:blank)

**Features:**

- Added static image support for microscopy experiments: [<u>PR#74</u>](https://github.com/catalystneuro/ndx-microscopy/pull/74)

  - MicroscopyStaticImage: Base class for static images

  - PlanarMicroscopyStaticImage: For 2D static images

  - VolumetricMicroscopyStaticImage: For 3D static images

- Added MicroscopyExperimentMetadata (extends LabMetaData) as a centralized container for experiment metadata, including: [<u>PR#73</u>](https://github.com/catalystneuro/ndx-microscopy/pull/73)

  - MicroscopyRig objects

  - ViralVector objects (from ndx-ophys-devices)

  - ViralVectorInjection objects (from ndx-ophys-devices)

  - Indicator objects (from ndx-ophys-devices)

- Added support for ViralVector and ViralVectorInjection imports from ndx-ophys-devices [<u>PR#73</u>](https://github.com/catalystneuro/ndx-microscopy/pull/73)

**Notes:**

- These changes improve metadata organization by centralizing all experiment-related objects in MicroscopyExperimentMetadata

- The use of links instead of nested groups provides better data reusability and reduces duplication

- Users should add MicroscopyExperimentMetadata to NWBFile using nwbfile.add_lab_meta_data()

# 7. Evaluation

*Please identify potential reviewers of this proposal who did not contribute to this proposal and are not part of the NWB Core Development Team, NWB Technical Advisory Board, NWB Executive Board. Please try to select reviewers who can represent experimentalists, tool builders, and data reusers.*

- Radek Chrapkiewicz \<[<u>radekch@stanford.edu</u>](mailto:radekch@stanford.edu)\>

- Josh Moore \<josh@openmicroscopy.org\> - NGFF/OME-Zarr

- Giacomo Mazzamuto \<[<u>mazzamuto@lens.unifi.it</u>](mailto:mazzamuto@lens.unifi.it)\> - BIDS microscopy paper + contributor of microscopy data to [<u>https://dandiarchive.org/dandiset/000026</u>](https://dandiarchive.org/dandiset/000026) BIDS dataset

- Marie-Helene Bourget \<[<u>bourgetmarieh@gmail.com</u>](mailto:bourgetmarieh@gmail.com)\> - BIDS Microscopy paper-lead/contributor

- Juan Nunez-Iglesias ([<u>https://github.com/jni</u>](https://github.com/jni)*)* \<<span class="mark">[<u>juan.nunez-iglesias@monash.edu</u>](mailto:juan.nunez-iglesias@monash.edu)\> - [<u>https://github.com/napari/napari</u>](https://github.com/napari/napari) co-founder/developer</span>

- Carsen Stringer \<[<u>stringerc@janelia.hhmi.org</u>](mailto:stringerc@janelia.hhmi.org)\> - developer of suite2p, has experience with NWB (inviting as a facilitator)

- Andrea Pierré \<[<u>andrea_pierre@brown.edu</u>](mailto:andrea_pierre@brown.edu)\> or Tuan Pham \<tuan_pham@brown.edu\> - experience with suite2p and NWB

- Robin Dard \<[<u>dardrobin@gmail.com</u>](mailto:dardrobin@gmail.com)\> - developer of CICADA, has experience with 2p and NWB

- Biafra Ahanonu \<[<u>bahanonu@alum.mit.edu</u>](mailto:bahanonu@alum.mit.edu)\> - developer of CIAtah, has experience with various microscopy methods and NWB and MatNWB

- Dan Birman \<[<u>daniel.birman@alleninstitute.org</u>](mailto:daniel.birman@alleninstitute.org)\> - SWE at Allen

# 8. Appendix

## 8.1 ndx-ophys-devices relation diagrams

### [<u>Molecular tools</u>](https://github.com/catalystneuro/ndx-ophys-devices?tab=readme-ov-file#molecular-tools)

<img src="./media/image6.png" style="width:6.5in;height:7.1291in" />

### [<u>Photodetector and ExcitationSource</u>](https://github.com/catalystneuro/ndx-ophys-devices?tab=readme-ov-file#device-models-and-devices)

<img src="./media/image7.png" style="width:7.14063in;height:7.79289in" />

### [<u>Optical Fiber and Objective Lens</u>](https://github.com/catalystneuro/ndx-ophys-devices?tab=readme-ov-file#optical-fiber-and-objective-lens)

<img src="./media/image1.png" style="width:7.18181in;height:6.4337in" />

### [<u>Optical Filters and Dichroic Mirrors</u>](https://github.com/catalystneuro/ndx-ophys-devices?tab=readme-ov-file#optical-filters-and-dichroic-mirrors)

<img src="./media/image8.png" style="width:6.97099in;height:6.88162in" />

# 

## 8.2 ndx-microscopy relation diagrams

### [<u>Experiment Metadata Components</u>](https://github.com/catalystneuro/ndx-microscopy/tree/v0.4.x?tab=readme-ov-file#experiment-metadata-components)

<img src="./media/image3.png" style="width:6.71354in;height:7.56322in" />

### [<u>Illumination Pattern Components</u>](https://github.com/catalystneuro/ndx-microscopy/tree/v0.4.x?tab=readme-ov-file#illumination-pattern-components)

<img src="./media/image5.png" style="width:6.5in;height:5in" />

### [<u>Microscopy Series and Imaging Space Components</u>](https://github.com/catalystneuro/ndx-microscopy/tree/v0.4.x?tab=readme-ov-file#microscopy-series-and-imaging-space-components)

<img src="./media/image2.png" style="width:7.26731in;height:5.20454in" />

### [<u>Segmentation Components</u>](https://github.com/catalystneuro/ndx-microscopy/tree/v0.4.x?tab=readme-ov-file#segmentation-components)

### <img src="./media/image4.png" style="width:7.38953in;height:5.13162in" />
