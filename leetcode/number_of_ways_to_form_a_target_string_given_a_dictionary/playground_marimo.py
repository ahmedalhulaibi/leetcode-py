import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_num_ways, run_num_ways
    from solution import Solution

    return Solution, assert_num_ways, run_num_ways


@app.cell
def _():
    # Example test case
    words = ["acca", "bbbb", "caca"]
    target = "aba"
    expected = 6
    return expected, target, words


@app.cell
def _(Solution, run_num_ways, target, words):
    result = run_num_ways(Solution, words, target)
    result
    return (result,)


@app.cell
def _(assert_num_ways, expected, result):
    assert_num_ways(result, expected)
    return


if __name__ == "__main__":
    app.run()
