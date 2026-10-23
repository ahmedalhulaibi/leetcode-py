import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_replace_elements, run_replace_elements
    from solution import Solution

    return Solution, assert_replace_elements, run_replace_elements


@app.cell
def _():
    # Example test case
    arr = [17, 18, 5, 4, 6, 1]
    expected = [18, 6, 6, 6, 1, -1]
    return arr, expected


@app.cell
def _(Solution, arr, run_replace_elements):
    result = run_replace_elements(Solution, arr)
    result
    return (result,)


@app.cell
def _(assert_replace_elements, expected, result):
    assert_replace_elements(result, expected)
    return


if __name__ == "__main__":
    app.run()
