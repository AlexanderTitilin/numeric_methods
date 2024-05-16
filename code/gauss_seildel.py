def gauss_seildel_method(A,b,eps=0.001,exit_param=2):
    res = np.zeros(b.size)
    last = np.zeros(b.size)
    k = 0
    while np.linalg.norm(res - last) > eps or k == 0:
        last = np.copy(res)
        for i in range(len(b)):
            a = A[i]
            res[i] = (1/a[i]) * (b[i] - (np.delete(a,i) * np.delete(res,i)).sum())
        k+=1
        if k > exit_param*res.size* -np.log10(eps)*exit_param:
            break
    return (res,k)
