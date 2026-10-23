import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_count_triplets, run_count_triplets
    from solution import Solution

    return Solution, assert_count_triplets, run_count_triplets


@app.cell
def _():
    # Example test case
    arr = [2, 3, 1, 6, 7]
    expected = 4
    return arr, expected


@app.cell
def _(Solution, arr, run_count_triplets):
    result = run_count_triplets(Solution, arr)
    result
    return (result,)


@app.cell
def _(assert_count_triplets, expected, result):
    assert_count_triplets(result, expected)
    return


if __name__ == "__main__":
    app.run()
