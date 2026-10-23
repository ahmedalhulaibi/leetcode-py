import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_find_closest_elements, run_find_closest_elements
    from solution import Solution

    return Solution, assert_find_closest_elements, run_find_closest_elements


@app.cell
def _():
    # Example test case
    arr = [1, 2, 3, 4, 5]
    k = 4
    x = 3
    expected = [1, 2, 3, 4]
    return arr, expected, k, x


@app.cell
def _(Solution, arr, k, run_find_closest_elements, x):
    result = run_find_closest_elements(Solution, arr, k, x)
    result
    return (result,)


@app.cell
def _(assert_find_closest_elements, expected, result):
    assert_find_closest_elements(result, expected)
    return


if __name__ == "__main__":
    app.run()
