# Repository: geosf25_material
Description: Class Notebooks for VT class Geo Data Science with Python, Fall 2025

------

# Cloning course material to your computer
The course material is available in a public repository (no setup or SSH connection necessary). It will be updated regularily.

#### Initial download
In a console/terminal, change directories to where you want the course material folder to live (below this is $home). The following command copies the entire course material repository to your computer to the folder './geosf25_material'.

```
cd $home
git clone https://github.com/GeoPythonVT/geosf25_material.git
```

You won't be able to push any content to this repository.

#### Update
Material will be added to the repository regularily. You can update the repository for new content (without repeatedly downloading the entire repository), whenever there is new material available. For that, enter the folder 'geosf25_material' on your computer and type in the terminal/console:

```
cd $home/geosf25_material
git pull
```

Alternatively, you can download the material directly from the repositories website:
https://github.com/GeoPythonVT/geosf25_material



------


# Setting up your Computer 
If you want to use your own computer, instead of the lab computers, install the following softwar and follow respective instructions. 

- Install Python Anaconda, and Bash 
- Create new conda environment and install Python packages

### 0. Install Anaconda, and Bash on your computer 
Follow instructions (depending on your operating system) for installing Bash, and Anaconda on the respective websites. Latest version of Anaconda is 2.6.6.

### 1. retrieve the file `environment.yml` (Anaconda-friendly, conda-forge only)
#> This file uses conda-forge, which avoids Cartopy build headaches and keeps versions current. This works even if the machines have the full Anaconda distribution installed.


### 2. Create the environment (Anaconda Prompt / Terminal)

Create and activate via conda
```
conda env create -f environment.yml
conda activate geof25a
```

Register the Jupyter kernel to see it in Notebook/Lab:
```
python -m ipykernel install --user --name geof25a --display-name "Python (geof25a)"
```

Launch Jupyter Lab
```
jupyter lab
```

### 3. Maintenance shortcuts (during the term)

Update to the latest spec (adds/removes to match file):
```
conda env update -n geof25a -f environment.yml --prune
```

Rebuild from scratch:
```
conda deactivate
conda env remove -n geof25a
conda env create -f environment.yml
```

Delete
```
conda deactivate
conda env remove -n geof25a
jupyter kernelspec remove geof25a   # if you registered a kernel
```

### 4. Lab-machine tips (common gotchas)
#> **Permissions:** Env creation is per-user by default; no admin needed. If home directories are redirected/locked down, create by path:
```
conda create -p ~/conda_envs/geof25a python=3.11
```
#> Stick to one channel (either all conda-forge as above, or all defaults). Channel mixing is the #1 source of solver conflicts.
