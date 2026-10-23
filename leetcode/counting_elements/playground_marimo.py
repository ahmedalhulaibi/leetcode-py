import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_count_elements, run_count_elements
    from solution import Solution

    return Solution, assert_count_elements, run_count_elements


@app.cell
def _():
    # Example test case
    arr: list[int] = [1, 2, 3]
    expected = 2
    return arr, expected


@app.cell
def _(Solution, arr: list[int], run_count_elements):
    result = run_count_elements(Solution, arr)
    result
    return (result,)


@app.cell
def _(assert_count_elements, expected, result):
    assert_count_elements(result, expected)
    return


if __name__ == "__main__":
    app.run()
