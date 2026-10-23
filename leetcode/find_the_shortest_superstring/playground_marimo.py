import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_shortest_superstring, run_shortest_superstring
    from solution import Solution

    return Solution, assert_shortest_superstring, run_shortest_superstring


@app.cell
def _():
    # Example test case
    words = ["alex", "loves", "leetcode"]
    expected = 17
    return expected, words


@app.cell
def _(Solution, run_shortest_superstring, words):
    result = run_shortest_superstring(Solution, words)
    result
    return (result,)


@app.cell
def _(assert_shortest_superstring, expected, result):
    assert_shortest_superstring(result, expected)
    return


if __name__ == "__main__":
    app.run()
