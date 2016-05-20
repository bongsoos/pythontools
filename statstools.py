'''
statstools.py

Statistical tools for analyzing data

author: Bongsoo Suh
created: 2015-03-08

(C) 2015 bongsoos
'''

import numpy as _np
from numpy.linalg import eig as _eig

def corrcoef(x, y):
    '''
    computes correlation coefficient (pearson's r)
    '''

    V = _np.sqrt(_np.array([_np.var(x, ddof=1), _np.var(y, ddof=1)])).reshape(1, -1)
    cc = (_np.matrix(_np.cov(x, y)) / (V*V.T + 1e-12))

    return cc[0,1]


def variance_explained(y, y_est):
    '''
    Computes explained variance
    '''
    SYY = sum((y - _np.mean(y))**2)
    RSS = sum((y - y_est)**2)

    R2 = 1 - RSS/SYY

    return R2

def normalizeX(X):
    '''
    Normalize data matrix
    mean subtraction, and variance normalization

    Inputs
    ------
    X (ndarray): mxn data matrix(each column feature, each row is one data point)

    Outputs
    -------
    Bn (ndarray): mxn normalized matrix
    '''
    mu = _np.array([list(_np.mean(X, axis=0))]*X.shape[0])
    B = X-mu
    sigma = _np.sqrt(_np.var(B, axis=0))
    Bn = B/_np.outer(_np.ones(B.shape[0]), sigma)

    return Bn

def cov(X):
    '''
    Compute covariance matrix
    (mean subtraction, and variance normalization)

    Inputs
    ------
    X (ndarray): mxn data matrix(each column feature, each row is one data point)

    Outputs
    -------
    C (ndarray): nxn covariance matrix
    '''
    Bn = normalizeX(X)

    C = _np.dot(Bn.T, Bn) / (Bn.shape[0]-1)

    return C

def eig(X):
    '''
    Inputs
    ------
    X (ndarray): nxn square matrix
    '''
    eigval, eigvec = _eig(X)
    idx = _np.argsort(eigval)[::-1]
    eigval = eigval[idx]
    eigvec = eigvec[:,idx]

    return eigvec, eigval

def pca(X):
    '''
    Principal Component Analysis
    Inputs
    ------
    X (ndarray): mxn data matrix(each column feature, each row is one data point)

    Outputs
    -------
    eigvec (ndarray): nxn eigenvector matrix, each column is the eigenvector corresponding to the eigen values
    eigval (ndarray): n eigenvalues, from highest to lowest
    proj (ndarray): mxn projection matrix, each column is the projection of the data points to the corresponding eigenvectors
    '''
    Bn = normalizeX(X)
    C = _np.dot(Bn.T, Bn) / (Bn.shape[0]-1)
    eigvec, eigval = eig(C)

    proj = _np.dot(Bn, eigvec)

    return eigvec, eigval, proj

