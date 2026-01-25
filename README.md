# Triangle-GB
This repository provides examples for the fast time-delay interferometry (TDI) response model of Galactic binaries (GBs), along with tutorials for some simple data analysis tasks based on **Taiji Data Challenge II** and **LISA Data Challenge**. The response model is inspired by the "TDI on the fly" approach proposed in [N. J. Cornish et al, PRD (2025)](https://doi.org/10.1103/y718-c1xl), and has been reformulated to support arbitrary detector orbit​ and arbitrary TDI combination. 
Our implementation of the fast response model has been validated against the more precise (but slower) time-domain simulation implemented in ``Triangle-Simulator``, with residuals well between the detector noise levels.

# Installation 
Please ensure ``Triangle-Simulator`` is available in your Python environment, which provides essential constants, utilities, and response functions, and you may also need to install ``bilby`` for some examples. 

1. **Install Triangle-Simulator**    
   install [Triangle-Simulator](https://github.com/TriangleDataCenter/Triangle-Simulator) and activate the tri_env environment by
   ```sh 
   conda activate tri_env 
   ```

2. **Install Nested Sampling Tools for some Examples**
   ```sh
   pip install bilby 
   ```

# References 
- [The TDC II paper](https://arxiv.org/abs/2505.16500). 
- [The fast GB response model for arbitray orbit and TDI (in preparation)](???)

