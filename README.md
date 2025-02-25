# Code to Run AuDrA Model to Assess Originality in the Incomplete Shape Drawing Task
This repository contains code from Patterson et al.'s (2023) paper **AuDrA: An automated drawing assessment platform for evaluating creativity**.

## Github Repo Navigation
The following is the **top-level directory layout** of this repo:

    .
    ├── \__pycache__
    ├── \user_images                                  # Folder to store drawings to evaluate originality
    ├── .gitignore                                    
    ├── AuDrA tutorial.pdf                            # A detailed tutorial on how to use pre-trained AuDrA model
    ├── AuDrA_Class.py                                # A Pytorch class of AuDrA model
    ├── AuDrA_DataModule.py                           # A class related to loading data for model training
    ├── audra_environment_cpu.yml                     # Configure environment for running on CPU
    ├── audra_environment_gpu.yml                     # Configure environment for running on GPU
    ├── audra_EXACT_ENVIRONMENT_USED_GPU_LINUX.yml    # Configure environment for running on CPU (exact environment of original training)
    ├── AuDrA_predictions.csv                         # Predicted originality rating (output after running `AuDrA_run.py `)
    ├── AuDrA_run.py                                  # Main script to assess originality in the incomplete shape drawing task
    ├── AuDrA_trained.ckpt (gitignored)               # Checkpoint file of pre-trained AuDrA model
    ├── datafuncs.py                                  # A helper function
    ├── invert.py                                     # A helper function
    ├── store_user_images.py                          # A script to store user images from `analysis/data/drawings/png` direcotry in the `user_images` directory
    ├── README.md

## Environment Activation and Code Running
After installing miniconda, the first step is to create the virtual environment based on where you plan to run the code (CPU or GPU). For instance, for running on CPU:
```bash
conda env create -f audra_environment_cpu.yml
```
This will create a virtual environment called `audra_cpu`.

The next step is to activate the created environment (still suppose using CPU):
```bash
conda activate audra_cpu
```

Afterwards, we need to *copy* drawings from the `analysis/data/drawings/png` directory into the `user_images` directory in this repository:
```bash
python store_user_images.py
```

Finally, run `AuDrA_run.py` file (using the Python interpreter located at the virtual environment), which calculates originality ratings of drawings stored in `\user_images` and outputs the results into `AuDrA_predictions.csv` (default name of output csv file):
```bash
python AuDrA_run.py
```

## OSF Access
To acceess the the trained AuDrA model (with tutorial), analysis script, and ratings, go to [this website](https://osf.io/kqn9v/). 

## References
```
@article{patterson2023audra,
  title={AuDrA: An automated drawing assessment platform for evaluating creativity},
  author={Patterson, John D and Barbot, Baptiste and Lloyd-Cox, James and Beaty, Roger E},
  journal={Behavior research methods},
  pages={1--18},
  year={2023},
  publisher={Springer}
}
```
