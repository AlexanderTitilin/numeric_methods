def generate_sym_pos_matrix(n):
    nums = np.random.choice(np.arange(2*n),n,replace=False)
    vecs = np.random.randint(100,size=(n,n))
    A = sum(k*v.reshape((n,1))@v.reshape((1,n)) for k,v in zip(nums,vecs))
    return A
