def richardson_method(A,b,eps=0.001,exit_param=2):
    eig = np.linalg.eigvals(A).astype("float64")
    tau = 2/(max(eig) + min(eig))
    res = np.zeros(len(b))
    last = np.zeros(len(b))
    k = 0
    while np.linalg.norm(res - last) > eps or k== 0:
        last= np.copy(res)
        res = (np.eye(len(b)) - tau*A).dot(res) + tau*b
        k+=1
        if k > exit_param*len(b)*-np.log10(eps):
            break
    return (res,k)
