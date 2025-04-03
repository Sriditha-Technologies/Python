from scipy import integrate
help(integrate.quad)
i=scipy.integrate.quad(lambda x:special.exp10(x),0,1)
print(i)