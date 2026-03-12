import os
from decimal import Decimal, getcontext
from fastmcp import FastMCP

# Define the FastMCP server
mcp = FastMCP("Pi Calculator")

def arctan(x_val: int) -> Decimal:
    """Calculate arctan(1/x) using Taylor series expansion."""
    x = Decimal(x_val)
    x_squared = x * x
    term = Decimal(1) / x
    result = term
    n = Decimal(3)
    sign = Decimal(-1)

    while term:
        term /= x_squared
        current_term = term / n
        if not current_term:
            break
        result += sign * current_term
        sign = -sign
        n += Decimal(2)

    return result

@mcp.tool()
def calculate_pi(decimals: int) -> str:
    """Calculate pi to a given number of decimals using Machin-like formula (series expansion)."""
    if decimals < 0:
        return "Decimals cannot be negative."

    # Use extra precision for calculation
    getcontext().prec = decimals + 10

    # Machin's formula: pi/4 = 4*arctan(1/5) - arctan(1/239)
    pi = Decimal(16) * arctan(5) - Decimal(4) * arctan(239)

    pi_str = str(pi)
    if decimals == 0:
        return "3"

    # +2 accounts for the '3' and the '.'
    return pi_str[:decimals + 2]

# Create ASGI application with Streamable HTTP
app = mcp.http_app()

if __name__ == "__main__":
    # Ensure uvicorn runs when executing the script directly
    import uvicorn
    port = int(os.environ.get("PORT", 8080))
    uvicorn.run("server:app", host="0.0.0.0", port=port)
