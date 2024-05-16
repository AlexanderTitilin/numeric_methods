def generate_dominate_row(n,i):
    x = np.random.randint(10,max(100,n**2))
    nums = []
    s = 0
    m = x//2
    for _ in range(n-1):
        num = randint(-50,m)
        if s +abs(num) < x:
            nums.append(num)
            s+= abs(num)
            m-=1
        else:
            break
    nums.extend([0]* ((n-1) - len(nums)))
    nums.insert(i,x)
    return np.array(nums)

def generate_diagonal_dominate_matrix(n:int):
    return np.array([generate_dominate_row(n,i) for i in range(n)])
