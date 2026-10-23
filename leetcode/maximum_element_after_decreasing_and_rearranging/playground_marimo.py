import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_maximum_element, run_maximum_element
    from solution import Solution

    return Solution, assert_maximum_element, run_maximum_element


@app.cell
def _():
    # Example test case
    arr = [2, 2, 1, 2, 1]
    expected = 2
    return arr, expected


@app.cell
def _(Solution, arr, run_maximum_element):
    result = run_maximum_element(Solution, arr)
    result
    return (result,)


@app.cell
def _(assert_maximum_element, expected, result):
    assert_maximum_element(result, expected)
    return


if __name__ == "__main__":
    app.run()
