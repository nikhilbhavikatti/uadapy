import numpy as np
import scipy as sp
import scipy.stats as st
import distribution



def test_distrib_class():

    model_1D = {
        st.alpha(1.0),
        st.anglit(),
        st.arcsine(),
        st.argus(1.0),
        st.beta(1.0, 1.0),
        st.betaprime(1.0, 1.0),
        st.bradford(1.0),
        st.burr(1.0, 1.0),
        st.burr12(1.0, 1.0),
        st.cauchy(),
        st.chi(1.0),
        st.chi2(1.0),
        st.cosine(),
        st.crystalball(1.0, 1.0),
        st.dgamma(1.0),
        st.dweibull(1.0),
        st.erlang(1),
        st.expon(),
        st.exponnorm(1.0),
        st.exponweib(1.0, 1.0),
        st.exponpow(1.0),
        st.f(1.0, 1.0),
        st.fatiguelife(1.0),
        st.fisk(1.0),
        st.foldcauchy(1.0),
        st.foldnorm(1.0),
        # some skipped, need to be added later
        st.norm(),
        st.t(1.0),
        st.uniform(1.0, 2.0)
    }

    n=2
    vec = np.ones(n)
    mat = np.eye(n)
    model_nD = {
        st.multivariate_normal(mean=vec, cov=mat),
        st.matrix_normal(mean=vec),
        st.dirichlet(alpha=vec),
        st.dirichlet_multinomial(alpha=vec, n=4),
        st.wishart(df=vec, scale=mat),
        st.invwishart(df=vec, scale=mat),
        st.multinomial(8, vec),
        st.multivariate_t(loc=vec, shape=mat),
        st.multivariate_hypergeom(m=vec, n=4),
        st.uniform_direction(dim=n),
        st.vonmises_fisher(mu=np.normalize(vec), kappa=1.0)
    }

    model_nxnD = {
        st.special_ortho_group(dim=n),
        st.ortho_group(dim=n),
        st.unitary_group(dim=n),
        st.random_correlation(eigs=vec),
    }


    