#______________________________________________________________________________
# Termin 1, 16.5.2019
# Logični operatorji
#______________________________________________________________________________


# Logični operator *konjunkcija* ima naslednjo resničnostno tabelo, kjer
# `F` predstavlja neresnično (`False`), `T` pa resnično (`True`) vrednost:
# 
#     A  B | A /\ B
#     -----+-------
#     F  F |   F
#     F  T |   F
#     T  F |   F
#     T  T |   T
# 
# S pomočjo vgrajenega operatorja `and` enostavno sestavimo funkcijo
# `konjunkcija(a, b)`, ki sprejme logični vrednosti `a` in `b` ter vrne logično
# vrednost konjunkcije `a /\ b`:
# 
#     def konjunkcija(a, b):
#         return a and b
# =====================================================================
# 1. podnaloga
# Logični operator *disjunkcija* ima naslednjo resničnostno tabelo:
# 
#     A  B | A \/ B
#     -----+-------
#     F  F |   F
#     F  T |   T
#     T  F |   T
#     T  T |   T
# 
# Sestavite funkcijo `disjunkcija(a, b)`, ki sprejme logični vrednosti
# `a` in `b` ter vrne logično vrednost disjunkcije `a \/ b`. Pri tem si
# pomagajte z vgrajenim operatorjem `or`.
# =============================================================================



# =====================================================================
# 2. podnaloga
# Logični operator *negacija* ima naslednjo resničnostno tabelo:
# 
#     A | ~A
#     --+----
#     F | T
#     T | F
# 
# Sestavite funkcijo `negacija(a)`, ki vrne logično vrednost disjunkcije `~a`.
# =============================================================================

# =====================================================================
# 3. podnaloga
# Logični operator *implikacija* ima naslednjo resničnostno tabelo:
# 
#     A  B | A => B
#     -----+-------
#     F  F |   T
#     F  T |   T
#     T  F |   F
#     T  T |   T
# 
# Sestavite funkcijo `implikacija(a, b)`, ki vrne logično vrednost
# implikacije `a => b`.
# =============================================================================

# =====================================================================
# 4. podnaloga
# Logični operator *ekvivalenca* ima naslednjo resničnostno tabelo:
# 
#     A  B | A <=> B
#     -----+--------
#     F  F |    T
#     F  T |    F
#     T  F |    F
#     T  T |    T
# 
# Sestavite funkcijo `ekvivalenca(a, b)`, ki vrne logično vrednost ekvivalence
# `a <=> b`.
# 
# Namig: Pomagajte si lahko s funkcijo `implikacija`.
# =============================================================================

# =====================================================================
# 5. podnaloga
# Logični operator *ekskluzivni ali* (*exclusive or* ali XOR) ima naslednjo
# resničnostno tabelo:
# 
#     A  B | A XOR B
#     -----+--------
#     F  F |    F
#     F  T |    T
#     T  F |    T
#     T  T |    F
# 
# Sestavite funkcijo `xor(a, b)`, ki vrne logično vrednost `a XOR b`.
# =============================================================================

# =====================================================================
# 6. podnaloga
# Logični operator *NAND* (*not and*) ima naslednjo
# resničnostno tabelo:
# 
#     A  B | A NAND B
#     -----+---------
#     F  F |    T
#     F  T |    T
#     T  F |    T
#     T  T |    F
# 
# Sestavite funkcijo `nand(a, b)`, ki vrne logično vrednost `a NAND b`.
# =============================================================================



