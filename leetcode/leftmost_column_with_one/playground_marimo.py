import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_leftmost_column_with_one, run_leftmost_column_with_one
    from solution import Solution

    return (
        Solution,
        assert_leftmost_column_with_one,
        run_leftmost_column_with_one,
    )


@app.cell
def _():
    # Example test case
    mat = [[0, 0], [0, 1]]
    expected = 1
    return expected, mat


@app.cell
def _(Solution, mat, run_leftmost_column_with_one):
    result, get_calls = run_leftmost_column_with_one(Solution, mat)
    print(get_calls)
    result
    return get_calls, result


@app.cell
def _(assert_leftmost_column_with_one, expected, get_calls, result):
    assert_leftmost_column_with_one((result, get_calls), expected)
    return


if __name__ == "__main__":
    app.run()
