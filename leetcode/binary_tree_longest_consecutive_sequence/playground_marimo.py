import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_longest_consecutive, run_longest_consecutive
    from solution import Solution

    return Solution, assert_longest_consecutive, run_longest_consecutive


@app.cell
def _():
    # Example test case
    root_list: list[int | None] = [1, None, 3, 2, 4, None, None, None, 5]
    expected = 3
    return expected, root_list


@app.cell
def _(Solution, root_list: list[int | None], run_longest_consecutive):
    result = run_longest_consecutive(Solution, root_list)
    result
    return (result,)


@app.cell
def _(assert_longest_consecutive, expected, result):
    assert_longest_consecutive(result, expected)
    return


if __name__ == "__main__":
    app.run()
