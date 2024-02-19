def maximizeSquareArea(hFences ,vFences,m,n):
        hFences=sorted(hFences)
        vFences=sorted(vFences)
        x=[1]+hFences+[n]
        y=[1]+vFences+[m]
        a=[]
        b=[]
        for j in range(1,len(x)):
            for i in range(len(x)-j):
                a.append(x[i+j]-x[i])
        for j in range(1,len(y)):
            for i in range(len(y)-j):
                b.append(y[i+j]-y[i])
        nmax=0
        for each in a:
            if each in b:
                nmax=max(each,nmax)
        if  nmax==0:
            return -1
        return (nmax**2)%(10**9 + 7)
h=[2]
v=[4]
m=7
n=6
print(maximizeSquareArea(h,v,7,6))