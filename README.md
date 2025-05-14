# Triangle-GB
Frequency-domain GB TDI-2.0 response, modified from GBGPU (the GPU implementation of FastGB algorithm) to support the numerical orbit of Taiji and TDI-2.0. 
The responses are consistent with the time-domain simulations of **Triangle-Simulator** (see Example 0). 
Also offered is an illustrative example (Example 1) for the preliminary analysis of **Taiji Data Challenge**, while it **should not** be regarded as a solution to all the challenges. 
Especially, only individual GBs are analyzed in the example, while for realistic data, the major challenge we face would be the overlap of numerous signals. 

# Installation 
1. **Install Triangle-Simulator**    
   install [Triangle-Simulator](https://github.com/TriangleDataCenter/Triangle-Simulator) and activate the tri_env environment by
   ```sh 
   conda activate tri_env 
   ```
2. **Clone the Repository**    
   ```sh
   git clone https://github.com/TriangleDataCenter/Triangle-GB
   cd Triangle-GB
   ```
3. **Install Modified GBGPU**    
- on **linux**:   
  ```sh
    cd GBGPU_numorbit
    conda install -c conda-forge gcc_linux-64 gxx_linux-64 gsl Cython
  ```
  to get GPU support (optional), install cupy by pip (replace 92 by your own cuda toolkit version): 
  ```sh
    pip install cupy-cuda92
  ```
  install package from source:
  ```sh
    python setup.py install
  ```
  
- on **macos** (arm chip):
  ```sh
    cd GBGPU_numorbit
    conda install -c conda-forge clang_osx-arm64 clangxx_osx-arm64 gsl Cython
  ```
  there is currently no GPU support on macos 

4. **Install MCMC Tools to Run the Tutorial**
  ```sh
    pip install eryn corner
  ```

# Comparison with time-domain simulation 
![image](Figures/TD_vs_FD.jpg)

# References 
(Please make sure to cite FastGB and GBGPU if Triangle-BBH is used in your published research).

- Taiji Data Challenge \& Triangle: [the TDC \& Triangle paper](TBD)
- The fast frequency-domain detector response of galactic binaries: [N. J. Cornish et al, Phys.Rev.D76:083006,2007](https://doi.org/10.1103/PhysRevD.76.083006)
- GBGPU: [GBGPU documentations](https://mikekatz04.github.io/GBGPU/html/index.html)

