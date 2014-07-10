
import numpy as np
import scipy.sparse as sp

a=sp.lil_matrix((5,5))
a[0,0]=1.0
a[1,1]=2.0
a[2,2]=3.0
print a
print "------"

a=a.tocsr()
b=sp.csr_matrix((np.tanh(a.data),a.indices,a.indptr),
               shape=a.shape)
print b
