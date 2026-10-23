import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_count_prime_set_bits, run_count_prime_set_bits
    from solution import Solution

    return Solution, assert_count_prime_set_bits, run_count_prime_set_bits


@app.cell
def _():
    # Example test case
    left: int = 6
    right: int = 10
    expected: int = 4
    return expected, left, right


@app.cell
def _(Solution, left: int, right: int, run_count_prime_set_bits):
    result = run_count_prime_set_bits(Solution, left, right)
    result
    return (result,)


@app.cell
def _(assert_count_prime_set_bits, expected: int, result):
    assert_count_prime_set_bits(result, expected)
    return


if __name__ == "__main__":
    app.run()
