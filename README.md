# Robotic Fabrication Workshop ZHAW HSLU

Repository for the "Robotic Fabrication for Architectural Design" workshop, ZHAW at HSLU

## Requirements and Installation

* Windows 10 Pro
* [Rhino 7 & Grasshopper](https://www.rhino3d.com/download)
* [compas_rrc](https://github.com/compas-rrc/compas_rrc_start#installation): Please follow the installation steps for required software here


## Getting started

1. If you are using `conda` for the first time, run:

    ```
    conda config --add channels conda-forge
    ```
    
2. Then, to create your compas_rrc environment, run (make sure to change ``ENVIRONMENT_NAME`` to a name of your choice):

    ```
    conda create -c conda-forge -n ENVIRONMENT_NAME compas_rrc python=3.8
    conda activate ENVIRONMENT_NAME
    python -m compas_rhino.install -v 7.0
    ```
    Note: If you are using a different version of Rhino please specify

3. Clone the [ws_zhaw_hslu](https://github.com/DavidJenny/ws_zhaw_hslu) repository to your local drive.


To verify your setup, start the ``Anaconda Prompt`` as administrator and run the following:

    python
    >>> import compas
    >>> import compas_fab
    >>> import compas_rrc



## Credits

This package was created by David Jenny <[jend@zhaw.ch]>(jend@zhaw.ch) [@DavidJenny](https://github.com/DavidJenny)
