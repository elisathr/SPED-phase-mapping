# SPED-phase-mapping
Repository for the manuscript _Scanning precession electron diffraction data analysis approaches for phase mapping of precipitates in aluminium alloys_ by E. Thronsen _et al._ (2023). 

The code is run with [pyxem](https://github.com/pyxem/pyxem) 0.14.2 and the data used can be found [here](https://doi.org/10.5281/zenodo.6645396). 

### Workflow
The workflow is as follows:

1. [Preprocess](https://github.com/elisathr/SPED-phase-mapping/blob/main/preprocess.ipynb) the dataset
2. Do phase mapping with one of the approaches, [non-negative matrix factorisation (NMF)](https://github.com/elisathr/SPED-phase-mapping/tree/main/NMF), [vector analysis](https://github.com/elisathr/SPED-phase-mapping/tree/main/VectorAnalysis), [template matching](https://github.com/elisathr/SPED-phase-mapping/tree/main/TemplateMatching) or [artificial neural netowrk (ann)](https://github.com/elisathr/SPED-phase-mapping/tree/main/ANN).
3. [Create ground truth](https://github.com/elisathr/SPED-phase-mapping/blob/main/create_ground_truth.ipynb)
4. [Determine the accuracy](https://github.com/elisathr/SPED-phase-mapping/blob/main/Determine_accuracy.ipynb)

### Contributors

<!-- ALL-CONTRIBUTORS-LIST:START - Do not remove or modify this section -->
<!-- prettier-ignore-start -->
<!-- markdownlint-disable -->
<table>
  <tbody>
    <tr>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/emichr"><img src= "https://avatars.githubusercontent.com/u/16645501?v=4" width="120px;" alt="Emil F. Christiansen"/><br /><sub><b>Emil F.      Christiansen</b></sub></a><br /><a href="https://github.com/elisathr/SPED-phase-mapping/commits?author=emichr" title="Preprocessing and NMF">💻</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/tinabe"><img src= "https://avatars.githubusercontent.com/u/22915119?v=4" width="120px;" alt="Tina Bergh"/><br /><sub><b>Tina Bergh</b></sub></a><br /><a href="https://github.com/elisathr/SPED-phase-mapping/commits?author=tinabe" title="Vector analysis">💻</a></td>
            <td align="center" valign="top" width="14.28%"><a href="https://github.com/JonasFrafjord"><img src= "https://avatars.githubusercontent.com/u/22909029?v=4" width="120px;" alt="Jonas Frafjord"/><br /><sub><b>Jonas Frafjord</b></sub></a><br /><a href="https://github.com/elisathr/SPED-phase-mapping/commits?author=JonasFrafjord" title="Vector analysis">💻</a></td>
              <td align="center" valign="top" width="14.28%"><a href="https://github.com/torit493"><img src= "https://avatars.githubusercontent.com/u/104507376?v=4" width="120px;" alt="Tor Inge Thorsen"/><br /><sub><b>Tor Inge Thorsen</b></sub></a><br /><a href="https://github.com/elisathr/SPED-phase-mapping/commits?author=torit493" title="Template matching">💻</a></td>
             <td align="center" valign="top" width="14.28%"><a href="https://github.com/elisathr"><img src= "https://avatars.githubusercontent.com/u/27852238?s=400&u=30efcf929070a5b8d854fe4b0652cfc7c42137fe&v=4" width="120px;" alt="Elisabeth Thronsen"/><br /><sub><b>Elisabeth Thronsen</b></sub></a><br /><a href="https://github.com/elisathr/SPED-phase-mapping/commits?author=elisathr" title="Artificial neural networks">💻</a></td>


  </tbody>
</table>

<!-- markdownlint-restore -->
<!-- prettier-ignore-end -->

<!-- ALL-CONTRIBUTORS-LIST:END -->


