# Preassignment for future touchsoft ML course

Technical requirements:

* Python 3.6+

And libraries:

* numpy
* pandas
* matplotlib
* sklearn
* jupyter notebook

I'd recommend you to use special distribution [Anaconda](https://docs.anaconda.com/anaconda/install/) or [Miniconda](https://docs.conda.io/en/latest/miniconda.html), or if you have a linux environment you use system python (with [virtualenv](https://virtualenv.pypa.io/en/latest/) if you don't want to touch system libraries) 

Task preview is available [here](https://nbviewer.jupyter.org/gist/MaximAntonovich/1b73200a250f0b4e2b0c082a30b90f86)

## Quick start on local machine

1. Install [Miniconda](https://docs.conda.io/en/latest/miniconda.html). Select latest miniconda3 for python3.

**For Windows users**

If you experienced package installation error 'maximum recursion depth exceeded', reinstall miniconda and just after installation modify file *conda-dir*\Lib\site-packages\conda\gateways\connection\download.py as follows [link](https://github.com/conda/conda/issues/6994#issuecomment-374891087)

2. Clone repository
```
git clone ssh://git@stash.touchcommerce.com:7999/~maksim_antanovich/touchsoft_ml.git
cd touchsoft_ml/preassignment
```
3. Create environment
```
conda deactivate
conda create --name touchsoftml
conda activate touchsoftml
```
4. Install necessary libraries
```
conda install numpy pandas matplotlib scikit-learn jupyterlab
```
5. Run assignment file
```
jupyter-notebook Wine\ Data.ipynb
```
6. Follow instructions. Jupyter reference is [here](https://jupyter-notebook.readthedocs.io/en/stable/notebook.html)

## Quick start on cloud

1. Visit [https://colab.research.google.com](https://colab.research.google.com)
2. Upload notebook file and run it
3. Upload data to `Files` tab
4. Follow instructions