from scipy.integrate import quad 
fffffffffffffff
def beta(R, T, M, Q, a, p):
	"""
	Gravity force to light pressure force fractoin.

	R - radius  (star)
	T - temperature  (star)
	M - mass  (star)
	Q - Plank factor of light pressure
	a - radius (dust)
	p - density (dust)
	"""
	return 2.12*10e-8*R**2*T**4*Q/(M*a*p)

print(beta(7*10e10, 6*10e3, 2*10e33, 1, 10e-4, 2.5))

