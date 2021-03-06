# Processing & Analysis for Radio Science Experiments (PARSE)
#### Elizabeth M. Palmer, Paul Sirri, Essam Heggy
#### University of Southern California, Department of Electrical and Computer Engineering
#### Developer Contact: paulsirri@gmail.com
*README [v1]*

![PARSE Logo](src/main/resources/base/PARSE_USC_logo_bw_red.png)

PARSE is a user-friendly GUI tool to assist planetary scientists in analyzing Deep Space Network (DSN) radio science datasets without requiring expertise in signal processing. PARSE can be used on bistatic radar (BSR) surface-scatter experiments, which use the radio communications antenna aboard a spacecraft to transmit X- or S-band radiowaves that scatter from the planetary object's surface and are then received by the DSN. BSR surface echoes can be used to quantify surface roughness at the cm-dm scale, for example, which can be used to constrain thermophysical models of planetary regoliths, support detailed geomorphological mapping, and reduce risk associated with site selection for landing and sampling missions. An example of such an experiment is given by [Palmer, Heggy & Kofman (2017)](https://doi.org/10.1038/s41467-017-00434-6).

An example workflow is shown in the following video:
[![Tutorial Video](youtube URL to video screenshot -*.jpg)](youtube short URL to video)

![PARSE flowchart](src/main/resources/base/softwareX_fig_flowchart_v5.png)

**Workflow Summary:** After choosing the data file and supplying basic target body information and spacecraft orbital parameters, users are then shown recommended processing parameters and given the ability to conveniently adjust them. Once the parameters are entered, the user can run the plotting animation to iterate over the time series, displaying a sequence of power spectral density plots, which show the frequency distribution of the signal power received by the DSN. This animation can be paused at any time to better view a single power spectral density. Once the animation is paused, the user can select the signal analysis tab to extract key features from the plot or export it as an image file.

## Installation & Getting Started

1. Find the installer package for your system:
- For Microsoft Windows: [build / windows / PARSESetup.exe](https://github.com/PARSE-team/PARSE/tree/main/build/windows/PARSESetup.exe) > Click the "Download" button
- For MacOS: [build / mac / PARSESetup.pkg](https://github.com/PARSE-team/PARSE/tree/main/build/mac/PARSESetup.pkg) > Click the "Download" button
2. Click OK to download even though warning messages will pop up that there is no named publisher. Note that the installer package is large (2-3 GB) since it includes large raw data files, and will take time to download depending on your connection speeds.
3. Click the downloaded file to start installation. Click OK to install even though may be a warning message saying there is no named publisher.
4. The first time you run PARSE, expect 5 to 10 second delays while it reads in the example raw files for the first time.

## Error Reporting:
If you run into issues with this process, please contact the developer at paulsirri@gmail.com
