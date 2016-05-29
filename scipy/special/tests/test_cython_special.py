# This file is automatically generated by generate_ufuncs.py.
# Do not edit manually!

from itertools import product

import numpy as np
from numpy.testing import assert_allclose

from scipy import special
from scipy.special import cython_special
from scipy.special.cython_special import (_float, _double, _long_double,
                                   _complex, _double_complex,
                                   _long_double_complex, _int, _long)
                                   

real_points = [-10, -1, 1, 10]
complex_points = [complex(*tup) for tup in product(real_points, repeat=2)]

TEST_POINTS = {
    'f': map(lambda x: _float(x).val, real_points),
    'd': map(lambda x: _double(x).val, real_points),
    'g': map(lambda x: _long_double(x).val, real_points),
    'F': map(lambda x: _complex(x).val, complex_points),
    'D': map(lambda x: _double_complex(x).val, complex_points),
    'G': map(lambda x: _long_double_complex(x).val, complex_points),
    'i': map(lambda x: _int(x).val, real_points),
    'l': map(lambda x: _long(x).val, real_points),
}


def _generate_test_points(typecodes):
    axes = tuple(map(lambda x: TEST_POINTS[x], typecodes))
    pts = list(product(*axes))
    return pts


def test_cython_api():
    params = [
        (special.bdtr, cython_special.bdtr, ('lld', 'ddd')),
        (special.bdtrc, cython_special.bdtrc, ('lld', 'ddd')),
        (special.bdtri, cython_special.bdtri, ('lld', 'ddd')),
        (special.bdtrik, cython_special.bdtrik, ('ddd',)),
        (special.bdtrin, cython_special.bdtrin, ('ddd',)),
        (special.bei, cython_special.bei, ('d',)),
        (special.beip, cython_special.beip, ('d',)),
        (special.ber, cython_special.ber, ('d',)),
        (special.berp, cython_special.berp, ('d',)),
        (special.besselpoly, cython_special.besselpoly, ('ddd',)),
        (special.beta, cython_special.beta, ('dd',)),
        (special.betainc, cython_special.betainc, ('ddd',)),
        (special.betaincinv, cython_special.betaincinv, ('ddd',)),
        (special.betaln, cython_special.betaln, ('dd',)),
        (special.binom, cython_special.binom, ('dd',)),
        (special.boxcox, cython_special.boxcox, ('dd',)),
        (special.boxcox1p, cython_special.boxcox1p, ('dd',)),
        (special.btdtr, cython_special.btdtr, ('ddd',)),
        (special.btdtri, cython_special.btdtri, ('ddd',)),
        (special.btdtria, cython_special.btdtria, ('ddd',)),
        (special.btdtrib, cython_special.btdtrib, ('ddd',)),
        (special.cbrt, cython_special.cbrt, ('d',)),
        (special.chdtr, cython_special.chdtr, ('dd',)),
        (special.chdtrc, cython_special.chdtrc, ('dd',)),
        (special.chdtri, cython_special.chdtri, ('dd',)),
        (special.chdtriv, cython_special.chdtriv, ('dd',)),
        (special.chndtr, cython_special.chndtr, ('ddd',)),
        (special.chndtridf, cython_special.chndtridf, ('ddd',)),
        (special.chndtrinc, cython_special.chndtrinc, ('ddd',)),
        (special.chndtrix, cython_special.chndtrix, ('ddd',)),
        (special.cosdg, cython_special.cosdg, ('d',)),
        (special.cosm1, cython_special.cosm1, ('d',)),
        (special.cotdg, cython_special.cotdg, ('d',)),
        (special.dawsn, cython_special.dawsn, ('d', 'D')),
        (special.ellipe, cython_special.ellipe, ('d',)),
        (special.ellipeinc, cython_special.ellipeinc, ('dd',)),
        (special.ellipkinc, cython_special.ellipkinc, ('dd',)),
        (special.ellipkm1, cython_special.ellipkm1, ('d',)),
        (special.entr, cython_special.entr, ('d',)),
        (special.erf, cython_special.erf, ('d', 'D')),
        (special.erfc, cython_special.erfc, ('d', 'D')),
        (special.erfcx, cython_special.erfcx, ('d', 'D')),
        (special.erfi, cython_special.erfi, ('d', 'D')),
        (special.eval_chebyc, cython_special.eval_chebyc, ('dd', 'dD', 'ld')),
        (special.eval_chebys, cython_special.eval_chebys, ('dd', 'dD', 'ld')),
        (special.eval_chebyt, cython_special.eval_chebyt, ('dd', 'dD', 'ld')),
        (special.eval_chebyu, cython_special.eval_chebyu, ('dd', 'dD', 'ld')),
        (special.eval_gegenbauer, cython_special.eval_gegenbauer, ('ddd', 'ddD', 'ldd')),
        (special.eval_genlaguerre, cython_special.eval_genlaguerre, ('ddd', 'ddD', 'ldd')),
        (special.eval_hermite, cython_special.eval_hermite, ('ld',)),
        (special.eval_hermitenorm, cython_special.eval_hermitenorm, ('ld',)),
        (special.eval_jacobi, cython_special.eval_jacobi, ('dddd', 'dddD', 'lddd')),
        (special.eval_laguerre, cython_special.eval_laguerre, ('dd', 'dD', 'ld')),
        (special.eval_legendre, cython_special.eval_legendre, ('dd', 'dD', 'ld')),
        (special.eval_sh_chebyt, cython_special.eval_sh_chebyt, ('dd', 'dD', 'ld')),
        (special.eval_sh_chebyu, cython_special.eval_sh_chebyu, ('dd', 'dD', 'ld')),
        (special.eval_sh_jacobi, cython_special.eval_sh_jacobi, ('dddd', 'dddD', 'lddd')),
        (special.eval_sh_legendre, cython_special.eval_sh_legendre, ('dd', 'dD', 'ld')),
        (special.exp1, cython_special.exp1, ('d', 'D')),
        (special.exp10, cython_special.exp10, ('d',)),
        (special.exp2, cython_special.exp2, ('d',)),
        (special.expi, cython_special.expi, ('d', 'D')),
        (special.expit, cython_special.expit, ('f', 'd', 'g')),
        (special.expm1, cython_special.expm1, ('d', 'D')),
        (special.expn, cython_special.expn, ('ld', 'dd')),
        (special.exprel, cython_special.exprel, ('d',)),
        (special.fdtr, cython_special.fdtr, ('ddd',)),
        (special.fdtrc, cython_special.fdtrc, ('ddd',)),
        (special.fdtri, cython_special.fdtri, ('ddd',)),
        (special.fdtridfd, cython_special.fdtridfd, ('ddd',)),
        (special.gamma, cython_special.gamma, ('d', 'D')),
        (special.gammainc, cython_special.gammainc, ('dd',)),
        (special.gammaincc, cython_special.gammaincc, ('dd',)),
        (special.gammainccinv, cython_special.gammainccinv, ('dd',)),
        (special.gammaincinv, cython_special.gammaincinv, ('dd',)),
        (special.gammasgn, cython_special.gammasgn, ('d',)),
        (special.gdtr, cython_special.gdtr, ('ddd',)),
        (special.gdtrc, cython_special.gdtrc, ('ddd',)),
        (special.gdtria, cython_special.gdtria, ('ddd',)),
        (special.gdtrib, cython_special.gdtrib, ('ddd',)),
        (special.gdtrix, cython_special.gdtrix, ('ddd',)),
        (special.hankel1, cython_special.hankel1, ('dD',)),
        (special.hankel1e, cython_special.hankel1e, ('dD',)),
        (special.hankel2, cython_special.hankel2, ('dD',)),
        (special.hankel2e, cython_special.hankel2e, ('dD',)),
        (special.huber, cython_special.huber, ('dd',)),
        (special.hyp0f1, cython_special.hyp0f1, ('dd', 'dD')),
        (special.hyp1f1, cython_special.hyp1f1, ('ddd', 'ddD')),
        (special.hyp2f1, cython_special.hyp2f1, ('dddd', 'dddD')),
        (special.hyperu, cython_special.hyperu, ('ddd',)),
        (special.i0, cython_special.i0, ('d',)),
        (special.i0e, cython_special.i0e, ('d',)),
        (special.i1, cython_special.i1, ('d',)),
        (special.i1e, cython_special.i1e, ('d',)),
        (special.inv_boxcox, cython_special.inv_boxcox, ('dd',)),
        (special.inv_boxcox1p, cython_special.inv_boxcox1p, ('dd',)),
        (special.it2struve0, cython_special.it2struve0, ('d',)),
        (special.itmodstruve0, cython_special.itmodstruve0, ('d',)),
        (special.itstruve0, cython_special.itstruve0, ('d',)),
        (special.iv, cython_special.iv, ('dd', 'dD')),
        (special.ive, cython_special.ive, ('dd', 'dD')),
        (special.j0, cython_special.j0, ('d',)),
        (special.j1, cython_special.j1, ('d',)),
        (special.jv, cython_special.jv, ('dd', 'dD')),
        (special.jve, cython_special.jve, ('dd', 'dD')),
        (special.k0, cython_special.k0, ('d',)),
        (special.k0e, cython_special.k0e, ('d',)),
        (special.k1, cython_special.k1, ('d',)),
        (special.k1e, cython_special.k1e, ('d',)),
        (special.kei, cython_special.kei, ('d',)),
        (special.keip, cython_special.keip, ('d',)),
        (special.ker, cython_special.ker, ('d',)),
        (special.kerp, cython_special.kerp, ('d',)),
        (special.kl_div, cython_special.kl_div, ('dd',)),
        (special.kn, cython_special.kn, ('ld', 'dd')),
        (special.kolmogi, cython_special.kolmogi, ('d',)),
        (special.kolmogorov, cython_special.kolmogorov, ('d',)),
        (special.kv, cython_special.kv, ('dd', 'dD')),
        (special.kve, cython_special.kve, ('dd', 'dD')),
        (special.log1p, cython_special.log1p, ('d', 'D')),
        (special.log_ndtr, cython_special.log_ndtr, ('d', 'D')),
        (special.loggamma, cython_special.loggamma, ('D',)),
        (special.logit, cython_special.logit, ('f', 'd', 'g')),
        (special.lpmv, cython_special.lpmv, ('ddd',)),
        (special.mathieu_a, cython_special.mathieu_a, ('dd',)),
        (special.mathieu_b, cython_special.mathieu_b, ('dd',)),
        (special.modstruve, cython_special.modstruve, ('dd',)),
        (special.nbdtr, cython_special.nbdtr, ('lld', 'ddd')),
        (special.nbdtrc, cython_special.nbdtrc, ('lld', 'ddd')),
        (special.nbdtri, cython_special.nbdtri, ('lld', 'ddd')),
        (special.nbdtrik, cython_special.nbdtrik, ('ddd',)),
        (special.nbdtrin, cython_special.nbdtrin, ('ddd',)),
        (special.ncfdtr, cython_special.ncfdtr, ('dddd',)),
        (special.ncfdtri, cython_special.ncfdtri, ('dddd',)),
        (special.ncfdtridfd, cython_special.ncfdtridfd, ('dddd',)),
        (special.ncfdtridfn, cython_special.ncfdtridfn, ('dddd',)),
        (special.ncfdtrinc, cython_special.ncfdtrinc, ('dddd',)),
        (special.nctdtr, cython_special.nctdtr, ('ddd',)),
        (special.nctdtridf, cython_special.nctdtridf, ('ddd',)),
        (special.nctdtrinc, cython_special.nctdtrinc, ('ddd',)),
        (special.nctdtrit, cython_special.nctdtrit, ('ddd',)),
        (special.ndtr, cython_special.ndtr, ('d', 'D')),
        (special.ndtri, cython_special.ndtri, ('d',)),
        (special.nrdtrimn, cython_special.nrdtrimn, ('ddd',)),
        (special.nrdtrisd, cython_special.nrdtrisd, ('ddd',)),
        (special.obl_cv, cython_special.obl_cv, ('ddd',)),
        (special.pdtr, cython_special.pdtr, ('ld', 'dd')),
        (special.pdtrc, cython_special.pdtrc, ('ld', 'dd')),
        (special.pdtri, cython_special.pdtri, ('ld', 'dd')),
        (special.pdtrik, cython_special.pdtrik, ('dd',)),
        (special.poch, cython_special.poch, ('dd',)),
        (special.pro_cv, cython_special.pro_cv, ('ddd',)),
        (special.pseudo_huber, cython_special.pseudo_huber, ('dd',)),
        (special.psi, cython_special.psi, ('d', 'D')),
        (special.radian, cython_special.radian, ('ddd',)),
        (special.rel_entr, cython_special.rel_entr, ('dd',)),
        (special.rgamma, cython_special.rgamma, ('d', 'D')),
        (special.round, cython_special.round, ('d',)),
        (special.sindg, cython_special.sindg, ('d',)),
        (special.smirnov, cython_special.smirnov, ('ld', 'dd')),
        (special.smirnovi, cython_special.smirnovi, ('ld', 'dd')),
        (special.spence, cython_special.spence, ('d', 'D')),
        (special.sph_harm, cython_special.sph_harm, ('lldd', 'dddd')),
        (special.stdtr, cython_special.stdtr, ('dd',)),
        (special.stdtridf, cython_special.stdtridf, ('dd',)),
        (special.stdtrit, cython_special.stdtrit, ('dd',)),
        (special.struve, cython_special.struve, ('dd',)),
        (special.tandg, cython_special.tandg, ('d',)),
        (special.tklmbda, cython_special.tklmbda, ('dd',)),
        (special.wofz, cython_special.wofz, ('D',)),
        (special.xlog1py, cython_special.xlog1py, ('dd', 'DD')),
        (special.xlogy, cython_special.xlogy, ('dd', 'DD')),
        (special.y0, cython_special.y0, ('d',)),
        (special.y1, cython_special.y1, ('d',)),
        (special.yn, cython_special.yn, ('ld', 'dd')),
        (special.yv, cython_special.yv, ('dd', 'dD')),
        (special.yve, cython_special.yve, ('dd', 'dD')),
        (special.zetac, cython_special.zetac, ('d',))
    ]

    def check(param):
        pyfunc, cyfunc, specializations = param
        for typecodes in specializations:
            pts = _generate_test_points(typecodes)
            pyres, cyres = [], []
            for pt in pts:
                pyres.append(pyfunc(*pt))
                cyres.append(cyfunc(*pt))
            pyres = np.asarray(pyres)
            cyres = np.asarray(cyres)
            assert_allclose(pyres, cyres)

    for param in params:
        yield check, param
