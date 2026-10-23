import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_merge_triplets, run_merge_triplets
    from solution import Solution

    return Solution, assert_merge_triplets, run_merge_triplets


@app.cell
def _():
    # Example test case
    triplets = [[2, 5, 3], [1, 8, 4], [1, 7, 5]]
    target = [2, 7, 5]
    expected = True
    return expected, target, triplets


@app.cell
def _(Solution, run_merge_triplets, target, triplets):
    result = run_merge_triplets(Solution, triplets, target)
    result
    return (result,)


@app.cell
def _(assert_merge_triplets, expected, result):
    assert_merge_triplets(result, expected)
    return


if __name__ == "__main__":
    app.run()
