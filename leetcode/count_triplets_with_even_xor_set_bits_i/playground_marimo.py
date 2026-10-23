import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_triplet_count, run_triplet_count
    from solution import Solution

    return Solution, assert_triplet_count, run_triplet_count


@app.cell
def _():
    # Example test case
    a = [1]
    b = [2]
    c = [3]
    expected = 1
    return a, b, c, expected


@app.cell
def _(Solution, a, b, c, run_triplet_count):
    result = run_triplet_count(Solution, a, b, c)
    result
    return (result,)


@app.cell
def _(assert_triplet_count, expected, result):
    assert_triplet_count(result, expected)
    return


if __name__ == "__main__":
    app.run()
