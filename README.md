# Calculating the value of employee stock options
This code is created to make it easier to calculate the value of employee stock options with the black scholes formula.

## The formula used
- k1
$$\frac{{\frac{1}{2} \cdot \sigma^2 - r + \sqrt{{(\frac{1}{2} \cdot \sigma^2 - r)^2 + 2 \cdot \sigma^2 \cdot (r + \lambda)}}}}{{\sigma^2}}$$

- k2
$$\frac{{\frac{1}{2} \cdot \sigma^2 - r - \sqrt{{(\frac{1}{2} \cdot \sigma^2 - r)^2 + 2 \cdot \sigma^2 \cdot (r + \lambda)}}}}{{\sigma^2}}$$

- b1
$$\frac{1}{k1 - k2}$$

- b2
$$-\frac{1}{k1 - k2}$$

- V(S, t, K) Formula
$$V(S, t, K) = b_1 \cdot K \left(\frac{S_0}{K}\right)^{\kappa_1} + b_2 \cdot K \left(\frac{S_0}{K}\right)^{\kappa_2}$$

- S* Formula
$$S^* = \frac{{S_0 \cdot \omega + K \cdot \theta}}{{\omega + \theta}}$$

- V(S*, t, K) Formula
$$V(S^s, t, K) = b_1 \cdot K \left(\frac{S^s}{K}\right)^{\kappa_1} + b_2 \cdot K \left(\frac{S^s}{K}\right)^{\kappa_2}$$

## Input
- Stock Price (S0)
- Strike Price (K)
- Interest Rate (r)
- Volatility (sigma)
- Stock Outstanding (omega)
- Due Date (T)
- Vesting Rate (lambda)
- Many ESO granted by the company (theta)

## Output
- K1 Value
- K2 Value
- b1 Value
- b2 Value
- Before Delusion Value  
- After Delusion Value
- Option Value
