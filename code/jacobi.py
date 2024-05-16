def jacobi_method(A,b,eps=0.001,exit_param=2):
    res = np.zeros(len(b))
    last = np.zeros(len(b))
    k = 0
    while k == 0 or np.linalg.norm(res - last) > eps:
        last = np.copy(res)
        for i in range(len(b)):
            a = A[i]
            res[i] =  (1/a[i]) * (b[i] - (np.delete(a,i)*np.delete(last,i)).sum())
        k+=1
        if k >= len(b)*exit_param:
            break
    return (res,k)
