import math

# Input Data
S_0 = float(input('Stock Price (S0) = '))
K = float(input('Strike Price (K) = '))
r = float(input('Interest Rate (r) = '))
sigma = float(input('Volatility = '))
omega = float(input('Stock Outstanding = '))
T = float(input('Due Date (T) = '))
lambd = float(input('Vesting Rate = '))
theta = float(input('Many ESO granted by the company = '))

# Calculate
kappa_1 = round((0.5 * sigma**2 - r + math.sqrt((0.5 * sigma**2 - r)**2 + 2 * sigma**2 * (r + lambd))) / sigma**2, 4)
kappa_2 = round((0.5 * sigma**2 - r - math.sqrt((0.5 * sigma**2 - r)**2 + 2 * sigma**2 * (r + lambd))) / sigma**2, 4)
b_2 = round(-1 / (kappa_1 - kappa_2), 4)
b_1 = round(1 / (kappa_1 - kappa_2), 4)

# V(S, t, K) Formula
V_S_t_K = b_1 * K * (S_0 / K)**kappa_1 + b_2 * K * (S_0 / K)**kappa_2

# S* Formula
S_star = (S_0 * omega + K * theta) / (omega + theta)

# V(S*, t, K) Formula
V_S_star_t_K = b_1 * K * (S_star / K)**kappa_1 + b_2 * K * (S_star / K)**kappa_2

# Output
print("K1 =", kappa_1)
print("K2 =", kappa_2)
print("b1 =", b_1)
print("b2 =", b_2)
print("Before Delusion =", round(V_S_t_K, 4))
print("After Delusion =", round(S_star, 4))
print("Option Value =", round(V_S_star_t_K, 4))