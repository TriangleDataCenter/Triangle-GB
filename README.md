# Triangle-GB
This repository provides the fast time-delay interferometry (TDI) response model of Galactic binaries (GBs) for space-based detectors, together with tutorials for the corresponding data-analysis tasks. The response model is inspired by the "TDI on the fly" approach proposed in [N. J. Cornish et al, PRD (2025)](https://doi.org/10.1103/y718-c1xl), and has been reformulated to support arbitrary detector orbit​ and arbitrary TDI combination, and further extended to a space-detector **network** of arbitrary configuration (e.g. LISA-Taiji-TianQin). 
Our implementation of the fast response model has been validated against the more precise (but slower) time-domain simulation implemented in ``Triangle-Simulator``, with residuals well below the instrumental noise level. 

The tutorials cover time-domain vs frequency-domain waveform modeling and cross-validation, rapid search of GB signals with $\mathcal{F}$-statistics, posterior inference of individual GBs with nested sampling, GB reconstruction on **LISA Data Challenge** data, and joint parameter estimation with a **LISA-Taiji-TianQin** network. 

The response model is shipped as the Python package ``Triangle_GB``, whose source lives in the ``Triangle_GB/`` folder of this repository: 

| Path | Content | 
| --- | --- | 
| ``Triangle_GB/`` | Source of the ``Triangle_GB`` package: the ``TDIFly`` / ``TDIFlyGB`` / ``TDIFlyGBNetwork`` classes | 
| ``Examples/`` | Tutorial notebooks | 

# Installation 
``Triangle_GB`` uses [Triangle-Simulator](https://github.com/TriangleDataCenter/Triangle-Simulator) for essential constants, utilities, orbit and TDI response functions, so **Triangle-Simulator must be installed first**. 

1. **Install Triangle-Simulator**    
   Install [Triangle-Simulator](https://github.com/TriangleDataCenter/Triangle-Simulator) and activate the tri_env environment by
   ```sh 
   conda activate tri_env 
   ```

2. **Download or Clone the Repository, then**    
   ```sh
   cd Triangle-GB
   ```

3. **Install Triangle_GB**    
   Install the package contained in the ``Triangle_GB`` folder into the active ``tri_env`` environment by
   ```sh   
   pip install -e . 
   ```
   After that the fast response model can be imported from anywhere, without being inside this repository:
   ```python
   from Triangle_GB.TDIFly import *   # TDIFly, TDIFlyGB, TDIFlyGBNetwork
   ```
   The response model can also be run on GPU (``use_gpu=True``), which requires ``cupy``. 

4. **Install Nested Sampling Tools to Run the Examples** 
   ```sh
   pip install bilby nessai-bilby
   ```

# References 
- [The TDC II paper](https://arxiv.org/abs/2505.16500). 
- [The fast GB response model for arbitray detector orbit, TDI combinations, and space detector network](http://arxiv.org/abs/2609.16477)

