# =============================================================================
# Funkcije števil in logične vrednosti (1. del)
#
# V tem sklopu so funkcije števil, ki kot rezultat vračajo logične vrednosti.
# =====================================================================@014702=
# 1. podnaloga
# Definiraj funkcijo `manjse(x, y)`, ki vrne `True`, če je `x` manjše od `y` sicer `False`.
# Primer:
# 
#     >>> manjse(3, 7)
#     True
#     >>> manjse(9, 7)
#     False
# =============================================================================
def manjse(a,b):
	if( a < b ) :
		return True
	else :
		return False
print(manjse(33, 7))
print()
# =====================================================================@014703=
# 2. podnaloga
# Definiraj funkcijo `pozitivno(x)`, ki vrne `True`, če je `x` pozitivno ali `0` sicer `False`.
# Primer:
# 
#     >>> pozitivno(5)
#     True
#     >>> pozitivno(-1)
#     False
#     >>> pozitivno(0)
#     True
# =============================================================================

def pozitivno(x):
	if x >= 0 :
		return True
	return False
print(pozitivno(29))
print(pozitivno(0))
print(pozitivno(-11))

# =====================================================================@014704=
# 3. podnaloga
# Definiraj funkcijo `veliko(x)`, ki vrne `True`, če je `x` večje od `100` sicer `False`.
# Primer:
# 
#     >>> veliko(5)
#     False
#     >>> veliko(-1000)
#     False
#     >>> veliko(555)
#     True
# =============================================================================

def veliko(x):
	if x > 100:
		return True
	return False
print()
print(veliko(2),veliko(-321312),veliko(123),veliko(10*10))

# =====================================================================@014705=
# 4. podnaloga
# Definiraj funkcijo `prevec(x)`, ki vrne `True`, če je `abs(x)` večje od `10**20` sicer `False`.
# Primer:
# 
#     >>> prevec(5)
#     False
#     >>> prevec(-1000)
#     False
#     >>> prevec(555)
#     False
#     >>> prevec(10**20 + 5)
#     True
#     >>> prevec(-10**21 + 5)
#     True
# =============================================================================

def prevec(x):
	if abs(x) > 10 ** 20:
		return True
	return False
print()
print(prevec(-10**21 + 5))	
print(prevec(5))	



# =====================================================================@014706=
# 5. podnaloga
# Definiraj funkcijo `premalo(x)`, ki vrne `True`, če je `-10 < x < 50` sicer `False`.
# Primer:
# 
#     >>> premalo(5)
#     True
#     >>> premalo(-1000)
#     False
#     >>> premalo(555)
#     False
#     >>> premalo(-10)
#     False
#     >>> premalo(60)
#     False
#     >>> premalo(49)
#     True
# =============================================================================
print()
def premalo(x):
	if( -10 < x < 50):
		return True
	return False

print(premalo(5))
print(premalo(100))
print(premalo(-10))


# =====================================================================@014707=
# 6. podnaloga
# Definiraj funkcijo `zadosti(x)`, ki vrne `True`, če je  `x >= 50` ali `x <= -10` sicer `False`.
# Primer:
# 
#     >>> zadosti(5)
#     False
# =============================================================================


# =====================================================================@014708=
# 7. podnaloga
# Definiraj funkcijo `zares_zadosti(x)`, ki vrne `True`, če je  `x >= 50` ali `x < -300` sicer `False`.
# Primer:
# 
#     >>> zares_zadosti(5)
#     False
#     >>> zares_zadosti(-1000)
#     True
#     >>> zares_zadosti(555)
#     True
#     >>> zares_zadosti(-10)
#     False
#     >>> zares_zadosti(60)
#     True
#     >>> zares_zadosti(49)
#     False
# =============================================================================



# =====================================================================@014709=
# 8. podnaloga
# Vsaj 8 sicer 0. Definiraj funkcijo, `vsaj_osem_ali_nic(x)`, ki vrne `True`, 
# če je x enak 0 ali večji ali enak 8.
# 
#     >>> vsaj_osem_ali_nic(10)
#     True
#     >>> vsaj_osem_ali_nic(3)
#     False
#     >>> vsaj_osem_ali_nic(0)
#     True
#     >>> vsaj_osem_ali_nic(7)
#     False
# =============================================================================
