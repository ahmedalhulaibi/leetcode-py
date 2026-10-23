import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_does_valid_array_exist, run_does_valid_array_exist
    from solution import Solution

    return Solution, assert_does_valid_array_exist, run_does_valid_array_exist


@app.cell
def _():
    # Example test case
    derived = [1, 1, 0]
    expected = True
    return derived, expected


@app.cell
def _(Solution, derived, run_does_valid_array_exist):
    result = run_does_valid_array_exist(Solution, derived)
    result
    return (result,)


@app.cell
def _(assert_does_valid_array_exist, expected, result):
    assert_does_valid_array_exist(result, expected)
    return


if __name__ == "__main__":
    app.run()
