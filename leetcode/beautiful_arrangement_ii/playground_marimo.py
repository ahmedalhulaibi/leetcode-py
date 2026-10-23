import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_construct_array, run_construct_array
    from solution import Solution

    return Solution, assert_construct_array, run_construct_array


@app.cell
def _():
    # Example test case
    n = 3
    k = 2
    return k, n


@app.cell
def _(Solution, k, n, run_construct_array):
    result = run_construct_array(Solution, n, k)
    result
    return (result,)


@app.cell
def _(assert_construct_array, k, result):
    assert_construct_array(result, k)
    return


if __name__ == "__main__":
    app.run()
