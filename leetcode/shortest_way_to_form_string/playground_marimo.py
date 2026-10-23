import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_shortest_way, run_shortest_way
    from solution import Solution

    return Solution, assert_shortest_way, run_shortest_way


@app.cell
def _():
    # Example test case
    source = "abc"
    target = "abcbc"
    expected = 2
    return expected, source, target


@app.cell
def _(Solution, run_shortest_way, source, target):
    result = run_shortest_way(Solution, source, target)
    result
    return (result,)


@app.cell
def _(assert_shortest_way, expected, result):
    assert_shortest_way(result, expected)
    return


if __name__ == "__main__":
    app.run()
