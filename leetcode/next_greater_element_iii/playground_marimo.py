import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_next_greater_element, run_next_greater_element
    from solution import Solution

    return Solution, assert_next_greater_element, run_next_greater_element


@app.cell
def _():
    # Example test case
    n = 12
    expected = 21
    return expected, n


@app.cell
def _(Solution, n, run_next_greater_element):
    result = run_next_greater_element(Solution, n)
    result
    return (result,)


@app.cell
def _(assert_next_greater_element, expected, result):
    assert_next_greater_element(result, expected)
    return


if __name__ == "__main__":
    app.run()
