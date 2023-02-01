import numpy as np
import diffpy.structure
from diffpy.structure import loadStructure
from matplotlib import pyplot as plt


def create_Al(a,b):
    ''''
    Creates a diffpy.structure of Al. Has the option of varying the lattice parameter in-plane to account for strain.
    
    Parameters
    --------------
    a : The a lattice parameter of Al.
    b : The b lattice parameter of Al.
    
    Returns
    --------------
    structure_Al : diffpy.structure of Al
    '''
    Al_latt = diffpy.structure.Lattice(a=a,b=b,c=4.04, alpha=90,beta=90,gamma=90 )
    Al_atom=diffpy.structure.atom.Atom(atype='Al',xyz=[0,0,0], lattice=Al_latt)
    Al_atom1=diffpy.structure.atom.Atom(atype='Al',xyz=[0,0.5,0.5], lattice=Al_latt)
    Al_atom2=diffpy.structure.atom.Atom(atype='Al',xyz=[0.5,0,0.5], lattice=Al_latt)
    Al_atom3=diffpy.structure.atom.Atom(atype='Al',xyz=[0.5,0.5,0], lattice=Al_latt)
    structure_Al = diffpy.structure.Structure(atoms=[Al_atom, Al_atom1, Al_atom2, Al_atom3], lattice=Al_latt)
    return structure_Al

def gaussian_noise(raw_data):
    ''''
    Parameters
    --------
    raw_data : np.array((kx,ky)). Holding the raw DP.
    
    Returns:
    gaussian_noise + raw_data : np.array((kx,ky)). The resulting noisy DP.
    '''
    gaussian_noise = np.random.rand(128, 128)/(400 + 370*(np.random.rand() - 0.5)) 
    return gaussian_noise + raw_data

def radial_noise(raw_data, plot=False):
    ''''
    Takes the raw data and superimposes radial noise onto the pattern.
    
    Parameters
    -------
    raw_data : np.array((kx,ky)). Holding the raw DP.
    plot : if True, the resulting DP will be plotted.
    
    Returns:
    arr + raw_data : np.array((kx,ky)). The resulting noisy DP.
    '''
    x_axis = np.linspace(-1, 1, raw_data.shape[0])[:, None]
    y_axis = np.linspace(-1, 1, raw_data.shape[1])[None, :]
    arr = np.sqrt(x_axis**2 + y_axis**2)
    
    inner = 0.5 + (np.random.rand() - 0.5)*0.3 # 0.2 + (np.random.rand() - 0.5)*0.4
    outer = 0
    arr /= arr.max()
    
    exp = (6 + (2 * (np.random.rand() - 0.5))) # 5
    arr = ((1 - arr) * inner)**exp

    if plot:
        fig,ax=plt.subplots(1,2,sharex=True,sharey=True)
        ax[0].imshow(arr)
        ax[1].imshow(arr+raw_data)
    return arr + raw_data

def poisson_noise(raw_data):
    ''''
    Parameters
    --------
    raw_data: np.array((kx,ky))
    Returns:
    poisson_noise + raw_data : np.array((kx,ky)). The resulting noisy DP.
    '''
    poisson_noise = np.random.poisson(raw_data)/(9 + 5*(np.random.rand() - 0.5))
    return poisson_noise + raw_data

def structure_Al():
    a=np.random.normal(loc=4.04, scale = 0.007)
    b=np.random.normal(loc=4.04, scale = 0.007)
    i = np.random.randint(2)
    if i%2==0:
        struc_Al = create_Al(a, a)
    else:
        struc_Al = create_Al(a,b)
    return struc_Al