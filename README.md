# SPED-phase-mapping
Repository for the manuscript _Scanning precession electron diffraction data analysis approaches for phase mapping of precipitates in aluminium alloys_ by E. Thronsen _et al._ (2023). 

The code is run with [pyxem](https://github.com/pyxem/pyxem) 0.14.2 and the data used can be found [here](https://doi.org/10.5281/zenodo.6645396). 

### Workflow
The workflow is as follows:

1. [Preprocess](https://github.com/elisathr/SPED-phase-mapping/blob/main/Preprocessing.ipynb) the dataset
2. Do phase mapping with one of the approaches, [non-negative matrix factorisation (NMF)](https://github.com/elisathr/SPED-phase-mapping/tree/main/NMF), [vector analysis](https://github.com/elisathr/SPED-phase-mapping/tree/main/VectorAnalysis), [template matching](https://github.com/elisathr/SPED-phase-mapping/tree/main/TemplateMatching) or [artificial neural netowrk (ann)](https://github.com/elisathr/SPED-phase-mapping/tree/main/ANN).
3. [Create ground truth](https://github.com/elisathr/SPED-phase-mapping/blob/main/create_ground_truth.ipynb)
4. [Determine the accuracy](https://github.com/elisathr/SPED-phase-mapping/blob/main/Determine_accuracy.ipynb)



