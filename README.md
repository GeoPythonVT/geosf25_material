# Repository: geosf25_material
Description: Class Notebooks for VT class Geo Data Science with Python, Fall 2025

---
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


---

## B: Setting up your Computer 
Part B instructions will set up your GitHub connection with your computer, after you have already created your GitHub account and repository. These include:

- Install Python Anaconda, and Bash 
- Create new conda environment and install Python packages

#### 1. Install Anaconda, Bash and Git on your computer (skip this step on the lab computers)
Follow instructions (depending on your operating system) for installing Bash, Git and Python/Anaconda on this website: https://annajiat.github.io/2021-07-19-colorado-online/


#### 2. Install Python (skip this step on the lab computers) 
Open the bash terminal/console and execute the following commands one by one, to create a new python environment and install all packages needed for the class. This may take a while and you need to confirm the installation.

```
conda update --all
conda create --name geosf25
conda activate geosf25
conda install -c conda-forge boost python=3.9 nb_conda geopandas jupyterlab scipy cartopy scikit-learn basemap statsmodels netcdf4 hdf5 pywget lxml pydap pywavelets seaborn xarray
```

