# OBwan
This repository contains the dataset mined from ChEMBL and the for predicting oral-bioavailability for molecules.

### **Oral-Bioavailability**
Oral bioavailability (F%) is the fraction of an oral administered drug that reaches systemic circulation. Predicting the Oral bioavailability aid in designing/optimizing drug molecules.

## Methodology:
### **Curation of dataset from ChEMBL:**
ChEMBL is a ‘chemogenomic’ database that brings together chemical, bioactivity and genomic data to aid the translation of genomic information into effective new drugs. ChEMBL includes information about how small molecules interact with their protein targets, how these compounds affect cells and whole organisms, and information on absorption, distribution, metabolism, excretion and toxicity (ADMET).

![image](https://user-images.githubusercontent.com/51278890/173230008-b7974b5a-b425-4561-86be-2a433244bcd7.png)

Molecules containing the oral-bioavailability data were downloaded using the ChEMBL webresource client API. A total of **13,836** molecules were found to have the oral bioavailability data in the ChEMBL database.

### **Descriptor generation using PaDEL:**
PaDEL is used for calculating molecular descriptors and fingerprints. It can calculate 797 descriptors (663 1D, 2D descriptors, and 134 3D descriptors) and 10 types of fingerprints.

PaDEL was used to generate descriptors/fetures for training the machine learning model. PaDEL requires an mdl format for calculating descriptors. The SDF file was converted to mdl file using openbabel.

### **Exploratory data analysis:**
