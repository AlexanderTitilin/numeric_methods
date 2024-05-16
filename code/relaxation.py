def relaxation_method(A,b,eps=0.001,omega=0.5,exit_param=2):
    res = np.zeros(len(b))
    last = np.zeros(len(b))
    k = 0
    while np.linalg.norm(res - last) > eps or k == 0:
        last = np.copy(res)
        for i in range(len(b)) :
            a = A[i]
            res[i] = (1- omega) * res[i] + (omega/a[i]) * (b[i] - (np.delete(a,i)*np.delete(res,i)).sum())
        k+=1
        if k > len(b)*exit_param*-np.log10(eps):
            break
    return (res,k)
