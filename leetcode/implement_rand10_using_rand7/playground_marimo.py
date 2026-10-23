import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_rand10, run_rand10
    from solution import Solution

    return Solution, assert_rand10, run_rand10


@app.cell
def _():
    # Example test case
    seed = 42
    n = 20
    expected = 20
    return expected, n, seed


@app.cell
def _(Solution, n, run_rand10, seed):
    values, calls = run_rand10(Solution, seed, n)
    print(values)
    calls
    return calls, values


@app.cell
def _(assert_rand10, calls, expected, values):
    assert_rand10((values, calls), expected)
    return


if __name__ == "__main__":
    app.run()
