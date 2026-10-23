import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_shortest_to_char, run_shortest_to_char
    from solution import Solution

    return Solution, assert_shortest_to_char, run_shortest_to_char


@app.cell
def _():
    # Example test case
    s = "loveleetcode"
    c = "e"
    expected = [3, 2, 1, 0, 1, 0, 0, 1, 2, 2, 1, 0]
    return c, expected, s


@app.cell
def _(Solution, c, run_shortest_to_char, s):
    result = run_shortest_to_char(Solution, s, c)
    result
    return (result,)


@app.cell
def _(assert_shortest_to_char, expected, result):
    assert_shortest_to_char(result, expected)
    return


if __name__ == "__main__":
    app.run()
