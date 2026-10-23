import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_find_longest_chain, run_find_longest_chain
    from solution import Solution

    return Solution, assert_find_longest_chain, run_find_longest_chain


@app.cell
def _():
    # Example test case
    pairs: list[list[int]] = [[1, 2], [2, 3], [3, 4]]
    expected = 2
    return expected, pairs


@app.cell
def _(Solution, pairs: list[list[int]], run_find_longest_chain):
    result = run_find_longest_chain(Solution, pairs)
    result
    return (result,)


@app.cell
def _(assert_find_longest_chain, expected, result):
    assert_find_longest_chain(result, expected)
    return


if __name__ == "__main__":
    app.run()
