import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_kth_smallest_prime_fraction, run_kth_smallest_prime_fraction
    from solution import Solution

    return (
        Solution,
        assert_kth_smallest_prime_fraction,
        run_kth_smallest_prime_fraction,
    )


@app.cell
def _():
    # Example test case
    arr = [1, 2, 3, 5]
    k = 3
    expected = [2, 5]
    return arr, expected, k


@app.cell
def _(Solution, arr, k, run_kth_smallest_prime_fraction):
    result = run_kth_smallest_prime_fraction(Solution, arr, k)
    result
    return (result,)


@app.cell
def _(assert_kth_smallest_prime_fraction, expected, result):
    assert_kth_smallest_prime_fraction(result, expected)
    return


if __name__ == "__main__":
    app.run()
