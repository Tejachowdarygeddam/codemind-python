p,r,t=map(int,input().split())
ci=p*(pow((1+r/100),t))
q=("{:.2f}".format(ci))
print(q)