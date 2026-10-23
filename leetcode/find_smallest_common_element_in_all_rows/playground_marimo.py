import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_smallest_common_element, run_smallest_common_element
    from solution import Solution

    return (
        Solution,
        assert_smallest_common_element,
        run_smallest_common_element,
    )


@app.cell
def _():
    # Example test case
    mat = [[1, 2, 3, 4, 5], [2, 4, 5, 8, 10], [3, 5, 7, 9, 11], [1, 3, 5, 7, 9]]
    expected = 5
    return expected, mat


@app.cell
def _(Solution, mat, run_smallest_common_element):
    result = run_smallest_common_element(Solution, mat)
    result
    return (result,)


@app.cell
def _(assert_smallest_common_element, expected, result):
    assert_smallest_common_element(result, expected)
    return


if __name__ == "__main__":
    app.run()
