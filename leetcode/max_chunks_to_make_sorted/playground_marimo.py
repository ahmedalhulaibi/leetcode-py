import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_max_chunks_to_sorted, run_max_chunks_to_sorted
    from solution import Solution

    return Solution, assert_max_chunks_to_sorted, run_max_chunks_to_sorted


@app.cell
def _():
    # Example test case
    arr = [4, 3, 2, 1, 0]
    expected = 1
    return arr, expected


@app.cell
def _(Solution, arr, run_max_chunks_to_sorted):
    result = run_max_chunks_to_sorted(Solution, arr)
    result
    return (result,)


@app.cell
def _(assert_max_chunks_to_sorted, expected, result):
    assert_max_chunks_to_sorted(result, expected)
    return


if __name__ == "__main__":
    app.run()
