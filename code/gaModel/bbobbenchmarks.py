
import warnings
from pdb import set_trace
import numpy as np
from math import floor as floor
from numpy import dot, linspace, diag, tile, zeros, sign, resize
from numpy.random import standard_normal as _randn # TODO: may bring confusion
from numpy.random import random as _rand # TODO: may bring confusion
import sys
sys.path.insert(0, '../')
from csep.loglikelihood import calcLogLikelihood
from models.mathUtil import calcNumberBins
import models.model
"""
% VAL = BENCHMARKS(X, FUNCID)
% VAL = BENCHMARKS(X, STRFUNC)
%    Input: 
%       X -- solution column vector or matrix of column vectors
%       FUNCID -- number of function to be executed with X as input,
%                 by default 8. 
%       STRFUNC -- function as string to be executed with X as input
%    Output: function value(s) of solution(s)
%    Examples: 
%      F = BENCHMARKS([1 2 3]', 17); 
%      F = BENCHMARKS([1 2 3]', 'f1'); 
% 
% NBS = BENCHMARKS() 
% NBS = BENCHMARKS('FunctionIndices') 
%    Output: 
%      NBS -- array of valid benchmark function numbers, 
%             presumably 1:24
%
% FHS = BENCHMARKS('handles')
%    Output: 
%      FHS -- cell array of function handles
%    Examples:
%      FHS = BENCHMARKS('handles');  
%      f = FHS{1}(x);  % evaluates x on the sphere function f1
%      f = feval(FHS{1}, x);  % ditto 
%
% see also: functions FGENERIC, BENCHMARKINFOS, BENCHMARKSNOISY

% Authors (copyright 2009): Nikolaus Hansen, Raymond Ros, Steffen Finck
%    Version = 'Revision: $Revision: 1115 $'
%    Last Modified: $Date: 2009-02-09 19:22:42 +0100 (Mon, 09 Feb 2009) $

% INTERFACE OF BENCHMARK FUNCTIONS
% FHS = BENCHMARKS('handles');
% FUNC = FHS{1};
%
% [FVALUE, FTRUE] = FUNC(X)
% [FVALUE, FTRUE] = FUNC(X, [], IINSTANCE)
%   Input: X -- matrix of column vectors
%          IINSTANCE -- instance number of the function, sets function
%             instance (XOPT, FOPT, rotation matrices,...)
%             up until a new number is set, or the function is
%             cleared. Default is zero.
%   Output: row vectors with function value for each input column
%     FVALUE -- function value
%     FTRUE -- noise-less, deterministic function value
% [FOPT STRFUNCTION] = FUNC('any_even_empty_string', ...)
%   Output:
%     FOPT -- function value at optimum
%     STRFUNCTION -- not yet implemented: function description string, ID before first whitespace
% [FOPT STRFUNCTION] = FUNC('any_even_empty_string', DIM, NTRIAL)
%   Sets rotation matrices and xopt depending on NTRIAL (by changing the random seed). 
%   Output:
%     FOPT -- function value at optimum
%     STRFUNCTION -- not yet implemented: function description string, ID before first whitespace
% [FOPT, XOPT] = FUNC('xopt', DIM)
%   Output:
%     FOPT -- function value at optimum XOPT
%     XOPT -- optimal solution vector in DIM-D
% [FOPT, MATRIX] = FUNC('linearTF', DIM)  % might vanish in future
%   Output:
%     FOPT -- function value at optimum XOPT
%     MATRIX -- used transformation matrix 

"""

### FUNCTION DEFINITION ###

def compute_xopt(rseed, dim):
    """Generate a random vector used as optimum argument.
    
    Rounded by four digits, but never to zero.

    """
    xopt = 8 * np.floor(1e4 * unif(dim, rseed))/1e4 - 4
    idx = (xopt == 0)
    xopt[idx] = -1e-5
    return xopt

def compute_rotation(seed, dim):
    """Returns an orthogonal basis. 
    
    The rotation is used in several ways and in combination with
    non-linear transformations. Search space rotation invariant 
    algorithms are not expected to be invariant under this rotation. 
    
    """
    B = np.reshape(gauss(dim * dim, seed), (dim, dim))
    for i in range(dim):
        for j in range(0, i):
            B[i] = B[i] - dot(B[i], B[j]) * B[j]
        B[i] = B[i] / (np.sum(B[i]**2) ** .5)
    return B

def monotoneTFosc(f):
    """Maps [-inf,inf] to [-inf,inf] with different constants
    for positive and negative part.

    """
    if np.isscalar(f):
        if f > 0.:
            f = np.log(f) / 0.1
            f = np.exp(f + 0.49*(np.sin(f) + np.sin(0.79*f))) ** 0.1
        elif f < 0.:
            f = np.log(-f) / 0.1
            f = -np.exp(f + 0.49*(np.sin(0.55*f) + np.sin(0.31*f))) ** 0.1
        return f
    else:
        f = np.asarray(f)
        g = f.copy()
        idx = (f > 0)
        g[idx] = np.log(f[idx]) / 0.1
        g[idx] = np.exp(g[idx] + 0.49*(np.sin(g[idx]) + np.sin(0.79*g[idx]))) ** 0.1
        idx = (f < 0)
        g[idx] = np.log(-f[idx]) / 0.1
        g[idx] = -np.exp(g[idx] + 0.49*(np.sin(0.55*g[idx]) + np.sin(0.31*g[idx]))) ** 0.1
        return g

def defaultboundaryhandling(x, fac):
    """Returns a float penalty for being outside of boundaries [-5, 5]"""
    xoutside = np.maximum(0., np.abs(x) - 5) * sign(x)
    fpen = fac * np.sum(xoutside**2, -1) # penalty
    return fpen

def gauss(N, seed):
    """Samples N standard normally distributed numbers
    being the same for a given seed

    """
    r = unif(2*N, seed)
    g = np.sqrt(-2 * np.log(r[:N])) * np.cos(2 * np.pi * r[N:2*N])
    if np.any(g == 0.):
        g[g == 0] = 1e-99
    return g

def unif(N, inseed):
    """Generates N uniform numbers with starting seed."""

    # initialization
    inseed = np.abs(inseed)
    if inseed < 1.:
        inseed = 1.

    rgrand = 32 * [0.]
    aktseed = inseed
    for i in xrange(39, -1, -1):
        tmp = floor(aktseed/127773.)
        aktseed = 16807. * (aktseed - tmp * 127773.) - 2836. * tmp
        if aktseed < 0:
            aktseed = aktseed + 2147483647.
        if i < 32:
            rgrand[i] = aktseed
    aktrand = rgrand[0]

    # sample numbers
    r = int(N) * [0.]
    for i in xrange(int(N)):
        tmp = floor(aktseed/127773.)
        aktseed = 16807. * (aktseed - tmp * 127773.) - 2836. * tmp
        if aktseed < 0:
            aktseed = aktseed + 2147483647.
        tmp = int(floor(aktrand / 67108865.))
        aktrand = rgrand[tmp]
        rgrand[tmp] = aktseed
        r[i] = aktrand / 2.147483647e9
    r = np.asarray(r)
    if (r == 0).any():
        warning.warn('zero sampled(?), set to 1e-99')
        r[r == 0] = 1e-99
    return r

# for testing and comparing to other implementations, 
#   myrand and myrandn are used only for sampling the noise 
#   Rename to myrand and myrandn to rand and randn and
#   comment lines 24 and 25.

_randomnseed = 30. # warning this is a global variable...
def _myrandn(size):
    """Normal random distribution sampling.
    
    For testing and comparing purpose.
    
    """

    global _randomnseed
    _randomnseed = _randomnseed + 1.
    if _randomnseed > 1e9:
        _randomnseed = 1.
    res = np.reshape(gauss(np.prod(size), _randomnseed), size)
    return res

_randomseed = 30. # warning this is a global variable...
def _myrand(size):
    """Uniform random distribution sampling.
    
    For testing and comparing purpose.
    
    """

    global _randomseed
    _randomseed = _randomseed + 1
    if _randomseed > 1e9:
        _randomseed = 1
    res = np.reshape(unif(np.prod(size), _randomseed), size) 
    return res

def fGauss(ftrue, beta):
    """Returns Gaussian model noisy value."""
    # expects ftrue to be a np.array
    popsi = np.shape(ftrue)
    fval = ftrue * np.exp(beta * _randn(popsi)) # with gauss noise
    tol = 1e-8
    fval = fval + 1.01 * tol
    idx = ftrue < tol
    try:
        fval[idx] = ftrue[idx]
    except IndexError: # fval is a scalar
        if idx:
            fval = ftrue
    return fval

def fUniform(ftrue, alpha, beta):
    """Returns uniform model noisy value."""
    # expects ftrue to be a np.array
    popsi = np.shape(ftrue)
    fval = (_rand(popsi) ** beta * ftrue *
            np.maximum(1., (1e9 / (ftrue + 1e-99)) ** (alpha * _rand(popsi))))
    tol = 1e-8
    fval = fval + 1.01 * tol
    idx = ftrue < tol
    try:
        fval[idx] = ftrue[idx]
    except IndexError: # fval is a scalar
        if idx:
            fval = ftrue
    return fval

def fCauchy(ftrue, alpha, p):
    """Returns Cauchy model noisy value
    
    Cauchy with median 1e3*alpha and with p=0.2, zero otherwise

    P(Cauchy > 1,10,100,1000) = 0.25, 0.032, 0.0032, 0.00032

    """
    # expects ftrue to be a np.array
    popsi = np.shape(ftrue)
    fval = ftrue + alpha * np.maximum(0., 1e3 + (_rand(popsi) < p) *
                                          _randn(popsi) / (np.abs(_randn(popsi)) + 1e-199))
    tol = 1e-8
    fval = fval + 1.01 * tol
    idx = ftrue < tol
    try:
        fval[idx] = ftrue[idx]
    except IndexError: # fval is a scalar
        if idx:
            fval = ftrue
    return fval

### CLASS DEFINITION ###

class AbstractTestFunction():
    """Abstract class for test functions.
    
    Defines methods to be implemented in test functions which are to be
    provided to method setfun of class Logger.
    In particular, (a) the attribute fopt and (b) the method _evalfull.
    
    The _evalfull method returns two values, the possibly noisy value and 
    the noise-free value. The latter is only meant to be for recording purpose. 

    """
    def __call__(self, x): # makes the instances callable
        """Returns the objective function value of argument x. 
        
        Example:

            >>> from cocopp.eaf import bbobbenchmarks as bn
            >>> f3 = bn.F3(13) # instantiate function 3 on instance 13
            >>> f3([0, 1, 2])  # call f3, same as f3.evaluate([0, 1, 2])  # doctest: +ELLIPSIS
            59.8733529...

        """
        return self.evaluate(x)

    def evaluate(self, x):
        """Returns the objective function value (in case noisy).
        
        """
        return self._evalfull(x)[0]
    # TODO: is it better to leave evaluate out and check for hasattr('evaluate') in ExpLogger?

    def _evalfull(self, x):
        """return noisy and noise-free value, the latter for recording purpose. """
        raise NotImplementedError

    def getfopt(self):
        """Returns the best function value of this instance of the function."""
        # TODO: getfopt error: 
        # import bbobbenchmarks as bb
        # bb.instantiate(1)[0].getfopt()
        # AttributeError: F1 instance has no attribute '_fopt'

        if not hasattr(self, 'iinstance'):
            raise Exception('This function class has not been instantiated yet.')
        return self._fopt

    def setfopt(self, fopt):
        try:
            self._fopt = float(fopt)
        except ValueError:
            raise Exception('Optimal function value must be cast-able to a float.')

    fopt = property(getfopt, setfopt)

class BBOBFunction(AbstractTestFunction):
    """Abstract class of BBOB test functions.

    Implements some base functions that are used by the test functions
    of BBOB such as initialisations of class attributes.

    """
    def __init__(self, iinstance=0, zerox=False, zerof=False, param=None, **kwargs):
        """Common initialisation.

        Keyword arguments:
        iinstance -- instance of the function (int)
        zerox -- sets xopt to [0, ..., 0]
        zerof -- sets fopt to 0
        param -- parameter of the function (if applicable)
        kwargs -- additional attributes

        """
        # Either self.rrseed or self.funId have to be defined for BBOBFunctions
        # TODO: enforce
        try:
            rrseed = self.rrseed
        except AttributeError:
            rrseed = self.funId

        try:
            self.rseed = rrseed + 1e4 * iinstance
        except TypeError:
            # rrseed AND iinstance have to be float
            warnings.warn('self.rseed could not be set, reset to 1 instead.')
            self.rseed = 1

        self.zerox = zerox
        if zerof:
            self.fopt = 0.
        else:
            print("entrou?")
            self.fopt = min(1000, max(-1000, (np.round(100*100*gauss(1, self.rseed)[0]/gauss(1, self.rseed+1)[0])/100)))
            region="Kanto"
            year=2000
            observation = models.model.loadModelDB(region+'jmaData', year+6)
            self.fopt = calcLogLikelihood(observation, observation)
            print(self.fopt)
        self.iinstance = iinstance
        self.dim = None
        self.lastshape = None
        self.param = param
        for i, v in kwargs.iteritems():
            setattr(self, i, v)
        self._xopt = None

    def shape_(self, x):
        # this part is common to all evaluate function
        # it is assumed x are row vectors
        curshape = np.shape(x)
        dim = np.shape(x)[-1]
        return curshape, dim

    def getiinstance(self):
        """Designates the instance of the function class.

        An instance in this case means a given target function value, a
        given optimal argument x, and given transformations for the
        function. It needs to have a string representation. Preferably
        it should be a number or a string.

        """
        return self._iinstance

    def setiinstance(self, iinstance):
        self._iinstance = iinstance

    iinstance = property(getiinstance, setiinstance)

    def shortstr(self):
        """Gives a short string self representation (shorter than str(self))."""

        res = 'F%s' % str(self.funId)
        if hasattr(self, 'param'):
            res += '_p%s' % str(self.param)  # NH param -> self.param
        return res

    def __eq__(self, obj):
        return (self.funId == obj.funId
                and (not hasattr(self, 'param') or self.param == obj.param))
        # TODO: make this test on other attributes than param?

#    def dimensionality(self, dim):
#        """Return the availability of dimensionality dim."""
#        return True

    # GETTERS
#    def getfopt(self):
#        """Optimal Function Value."""
#        return self._fopt

#    fopt = property(getfopt)

    def _setxopt(self, xopt):
        """Return the argument of the optimum of the function."""
        self._xopt = xopt

    def _getxopt(self):
        """Return the argument of the optimum of the function."""
        if self._xopt is None:
            warnings.warn('You need to evaluate object to set dimension first.')
        return self._xopt

    xopt = property(_getxopt, _setxopt)

#    def getrange(self):
#        """Return the domain of the function."""
#        #TODO: could depend on the dimension
#        # TODO: return exception NotImplemented yet
#        pass

#    range = property(getrange)

#    def getparam(self):
#        """Optional parameter value."""
#        return self._param

#    param = property(getparam)

#    def getitrial(self):
#        """Instance id number."""
#        return self._itrial

#    itrial = property(getitrial)

#    def getlinearTf(self):
#        return self._linearTf

#    linearTf = property(getlinearTf)

#    def getrotation(self):
#        return self._rotation

#    rotation = property(getrotation)

class BBOBNfreeFunction(BBOBFunction):
    """Class of the noise-free functions of BBOB."""

    def noise(self, ftrue):
        """Returns the noise-free function values."""

        return ftrue.copy()

class BBOBGaussFunction(BBOBFunction):
    """Class of the Gauss noise functions of BBOB.

    Attribute gaussbeta needs to be defined by inheriting classes.
    
    """

    # gaussbeta = None

    def noise(self, ftrue):
        """Returns the noisy function values."""

        return fGauss(ftrue, self.gaussbeta)

    def boundaryhandling(self, x):
        return defaultboundaryhandling(x, 100.)

class BBOBUniformFunction(BBOBFunction, object):
    """Class of the uniform noise functions of BBOB.
    
    Attributes unifalphafac and unifbeta need to be defined by inheriting
    classes.
    
    """
    # unifalphafac = None
    # unifbeta = None

    def noise(self, ftrue):
        """Returns the noisy function values."""

        return fUniform(ftrue, self.unifalphafac * (0.49 + 1. / self.dim), self.unifbeta)

    def boundaryhandling(self, x):
        return defaultboundaryhandling(x, 100.)

class BBOBCauchyFunction(BBOBFunction):
    """Class of the Cauchy noise functions of BBOB.

    Attributes cauchyalpha and cauchyp need to be defined by inheriting
    classes.

    """
    # cauchyalpha = None
    # cauchyp = None

    def noise(self, ftrue):
        """Returns the noisy function values."""

        return fCauchy(ftrue, self.cauchyalpha, self.cauchyp)

    def boundaryhandling(self, x):
        return defaultboundaryhandling(x, 100.)

class _FSphere(BBOBFunction):
    """Abstract Sphere function.
    
    Method boundaryhandling needs to be defined.
    
    """
    rrseed = 1

    def initwithsize(self, curshape, dim):
        # DIM-dependent initialization
        if self.dim != dim:
            if self.zerox:
                self.xopt = zeros(dim)
            else:
                self.xopt = compute_xopt(self.rseed, dim)

        # DIM- and POPSI-dependent initialisations of DIM*POPSI matrices
        if self.lastshape != curshape:
            self.dim = dim
            self.lastshape = curshape
            self.arrxopt = resize(self.xopt, curshape)

    def _evalfull(self, x):
        fadd = self.fopt
        curshape, dim = self.shape_(x)
        # it is assumed x are row vectors

        if self.lastshape != curshape:
            self.initwithsize(curshape, dim)

        # BOUNDARY HANDLING
        fadd = fadd + self.boundaryhandling(x)

        # TRANSFORMATION IN SEARCH SPACE
        x = x - self.arrxopt # cannot be replaced with x -= arrxopt!

        # COMPUTATION core
        ftrue = np.sum(x**2, -1)
        fval = self.noise(ftrue)

        # FINALIZE
        ftrue += fadd
        fval += fadd
        return fval, ftrue

class F1(_FSphere, BBOBNfreeFunction):
    """Noise-free Sphere function"""
    funId = 1
    def boundaryhandling(self, x):
        return 0.


class F2(BBOBNfreeFunction):
    """Separable ellipsoid with monotone transformation
    
    Parameter: condition number (default 1e6)

    """
    funId = 2
    def _evalfull(self, x, modelOmega, mean):
        logValue = float('Inf')
        genomeModel=models.model.newModel(modelOmega[0].definitions)
        genomeModel.bins=list(individual)
        modelLambda=models.model.newModel(modelOmega[0].definitions)
        modelLambda.bins=calcNumberBins(genomeModel.bins, mean)
        for i in range(len(modelOmega)):
            tempValue=calcLogLikelihood(modelLambda, modelOmega[i])
            # calcLogLikelihood.cache_clear()
            if tempValue < logValue:
                logValue = tempValue
        return -logValue


    # def initwithsize(self, curshape, dim):
    #     # DIM-dependent initialization
    #     if self.dim != dim:
    #         if self.zerox:
    #             self.xopt = zeros(dim)
    #         else:
    #             self.xopt = compute_xopt(self.rseed, dim)
    #         if hasattr(self, 'param') and self.param: # not self.param is None
    #             tmp = self.param
    #         else:
    #             tmp = self.condition
    #         self.scales = tmp ** linspace(0, 1, dim)

    #     # DIM- and POPSI-dependent initialisations of DIM*POPSI matrices
    #     if self.lastshape != curshape:
    #         self.dim = dim
    #         self.lastshape = curshape
    #         self.arrxopt = resize(self.xopt, curshape)

    # def _evalfull(self, x, modelOmega, mean):
    #     fadd = self.fopt
    #     curshape, dim = self.shape_(x)
    #     # it is assumed x are row vectors

    #     if self.lastshape != curshape:
    #         self.initwithsize(curshape, dim)

    #     # TRANSFORMATION IN SEARCH SPACE
    #     x = x - self.arrxopt # cannot be replaced with x -= arrxopt!

    #     # COMPUTATION core
    #     ftrue = dot(monotoneTFosc(x)**2, self.scales)
    #     fval = self.noise(ftrue) # without noise

    #     # FINALIZE
    #     ftrue += fadd
    #     fval += fadd
    #     return fval, ftrue

#dictbbob = {'sphere': F1, 'ellipsoid': F2, 'Rastrigin': F3}
nfreefunclasses = (F1, F2) # hard coded
dictbbobnfree = dict((i.funId, i) for i in nfreefunclasses)
nfreeIDs = sorted(dictbbobnfree.keys())  # was: "nfreenames"
nfreeinfos = [str(i) + ': ' + dictbbobnfree[i].__doc__ for i in nfreeIDs]


funclasses = list(nfreefunclasses) 
dictbbob = dict((i.funId, i) for i in funclasses)

#TODO: pb xopt f9, 21, 22
class _FTemplate(BBOBNfreeFunction):
    """Template based on F1"""

    funId = 421337

    def initwithsize(self, curshape, dim):
        # DIM-dependent initialization
        if self.dim != dim:
            if self.zerox:
                self.xopt = zeros(dim)
            else:
                self.xopt = compute_xopt(self.rseed, dim)

        # DIM- and POPSI-dependent initialisations of DIM*POPSI matrices
        if self.lastshape != curshape:
            self.dim = dim
            self.lastshape = curshape
            self.arrxopt = resize(self.xopt, curshape)

        self.linearTf = None
        self.rotation = None

    def _evalfull(self, x):
        fadd = self.fopt
        curshape, dim = self.shape_(x)
        # it is assumed x are row vectors

        if self.lastshape != curshape:
            self.initwithsize(curshape, dim)

        # BOUNDARY HANDLING

        # TRANSFORMATION IN SEARCH SPACE
        x = x - self.arrxopt # cannot be replaced with x -= arrxopt!

        # COMPUTATION core
        ftrue = np.sum(x**2, 1)
        fval = self.noise(ftrue)

        # FINALIZE
        ftrue += fadd
        fval += fadd
        return fval, ftrue

def instantiate(ifun, iinstance=0, param=None, **kwargs):
    """Returns test function ifun, by default instance 0."""
    res = dictbbob[ifun](iinstance=iinstance, param=param, **kwargs)  # calling BBOBFunction.__init__(iinstance, param,...)
    return res, res.fopt

def get_param(ifun):
    """Returns the parameter values of the function ifun."""
    try:
        return dictbbob[ifun].paramValues
    except AttributeError:
        return (None, )

if __name__ == "__main__":
    import doctest
    doctest.testmod()  # run all doctests in this module
    