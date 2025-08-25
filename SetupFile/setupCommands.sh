
### 0) Install Anaconda Navigator
#> download from their website, for your operating system
#> latest version: 2.6.6


### 1) retrieve the file `environment.yml` (Anaconda-friendly, conda-forge only)
#> This file uses conda-forge, which avoids Cartopy build headaches and keeps versions current. This works even if the machines have the full Anaconda distribution installed.


### 2) Create the environment (Anaconda Prompt / Terminal)

# Create and activate via conda
conda env create -f environment.yml
conda activate geof25a

# Register the Jupyter kernel to see it in Notebook/Lab:
python -m ipykernel install --user --name geof25a --display-name "Python (geof25a)"

# Launch Jupyter Lab
jupyter lab


### 3) Maintenance shortcuts (during the term)

# Update to the latest spec (adds/removes to match file):
conda env update -n geof25a -f environment.yml --prune

# Rebuild from scratch:
conda deactivate
conda env remove -n geof25a
conda env create -f environment.yml

# Delete
conda deactivate
conda env remove -n geof25a
jupyter kernelspec remove geof25a   # if you registered a kernel


### 4) Lab-machine tips (common gotchas)
#> **Permissions:** Env creation is per-user by default; no admin needed. If home directories are redirected/locked down, create by path:

conda create -p ~/conda_envs/geof25a python=3.11

#> Stick to one channel (either all conda-forge as above, or all defaults). Channel mixing is the #1 source of solver conflicts.