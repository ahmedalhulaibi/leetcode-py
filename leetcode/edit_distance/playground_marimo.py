import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_min_distance, run_min_distance
    from solution import Solution

    return Solution, assert_min_distance, run_min_distance


@app.cell
def _():
    # Example test case
    word1 = "horse"
    word2 = "ros"
    expected = 3
    return expected, word1, word2


@app.cell
def _(Solution, run_min_distance, word1, word2):
    result = run_min_distance(Solution, word1, word2)
    result
    return (result,)


@app.cell
def _(assert_min_distance, expected, result):
    assert_min_distance(result, expected)
    return


if __name__ == "__main__":
    app.run()
