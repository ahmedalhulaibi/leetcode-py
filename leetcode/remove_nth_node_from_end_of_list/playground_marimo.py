import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_remove_nth_from_end, run_remove_nth_from_end
    from solution import Solution

    return Solution, assert_remove_nth_from_end, run_remove_nth_from_end


@app.cell
def _():
    # Example test case
    head_list: list[int] = [1, 2, 3, 4, 5]
    n = 2
    expected: list[int] = [1, 2, 3, 5]
    return expected, head_list, n


@app.cell
def _(Solution, head_list: list[int], n, run_remove_nth_from_end):
    result = run_remove_nth_from_end(Solution, head_list, n)
    result
    return (result,)


@app.cell
def _(assert_remove_nth_from_end, expected: list[int], result):
    assert_remove_nth_from_end(result, expected)
    return


if __name__ == "__main__":
    app.run()
