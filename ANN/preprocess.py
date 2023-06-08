import numpy as np
from numpy import log10
from tqdm import tqdm
import pyxem as px

def rotate_signal(signal, rot_angle):
    print('Rotating data..')
    return signal.rotate_diffraction(rot_angle)

def normalize(stack, only_one_image=False):
    ''''
    Normalizes one or multiple DPs between [0,1].
    
    Parameters
    -------
    stack : np.array((nx,ny)) or list of np.array((nx,ny)). Single or multiple DPs to be normalized.
    only_one_image : boolean. If set to True, stack is one image. If set to False, stack is a list of numpy arrays.
    
    Returns
    -------
    normalized_stack : numpy array with same shape as stack. 
    '''
    normalized_stack = np.zeros_like(stack, dtype='float32')
    if only_one_image:
        normalized_stack = stack/(float(np.max(stack) - np.min(stack)))
        return normalized_stack
    
    n_images = stack.shape[0]
    print('Normalizing between 0 and 1..')
    for i in tqdm(range(n_images)):
        normalized_stack[i] = stack[i]/(float(np.max(stack[i]) - np.min(stack[i])))
    return normalized_stack


def log_shift(raw,base=10,shift=0.1):
    ''''
    Parameters
    -------
    raw : np.array((nx, ny)). The raw data.
    shift : float. Introduces a shift for the log. To account for pixels with 0 value.
    
    Returns
    -------
    log_shift : np.array((nx, ny)). The log transformation of the raw data.
    '''
    log_shift = log10(raw+shift) - log10(shift)
    return log_shift

def preprocess_NN(signal, rot_angle, mask_size, shift):
    ''''
    Preprocesses the experimental prior to NN prediction: A log shift is imposed before a mask is applied to mask out the central beam. The 4D dataset is reshaped to (nx*ny, kx, ky)
    
    Parameters
    -------
    signal : pyxem.signals.electron_diffraction2d.ElectronDiffraction2D((nx,ny,kx,ky)
    rot_angle : float - The angle of rotation of the diffraction patterns
    mask_size : int - The size of the central beam mask
    shift : float - The shift in Eq. 3.
    
    Returns
    -------
    signal_preprocessed : numpy.ndarray((nx*ny, kx, ky))
    '''
    signal = rotate_signal(signal, rot_angle)
    central_beam_mask = px.utils.expt_utils.circular_mask((128,128), mask_size)
    DP_scale = signal.axes_manager[2].scale
    signal_masked_px = signal*~central_beam_mask
    nx, ny = signal_masked_px.data.shape[0], signal_masked_px.data.shape[1]
    kx, ky = signal_masked_px.data.shape[2], signal_masked_px.data.shape[3]
    signal_masked = signal_masked_px.data.reshape(nx*ny, kx, ky)
    print('Scaling the intensity..')
    for i in tqdm(range(len(signal_masked))):
         signal_masked[i] = log_shift(signal_masked[i], shift=shift)
    return normalize(signal_masked)