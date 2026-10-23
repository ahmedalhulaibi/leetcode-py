import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_lowest_common_ancestor, run_lowest_common_ancestor
    from solution import Solution

    return Solution, assert_lowest_common_ancestor, run_lowest_common_ancestor


@app.cell
def _():
    # Example test case
    root_list = [6, 2, 8, 0, 4, 7, 9, None, None, 3, 5]
    p_val = 2
    q_val = 8
    expected_val = 6
    return expected_val, p_val, q_val, root_list


@app.cell
def _(Solution, p_val, q_val, root_list, run_lowest_common_ancestor):
    result = run_lowest_common_ancestor(Solution, root_list, p_val, q_val)
    result.val if result else None
    return (result,)


@app.cell
def _(assert_lowest_common_ancestor, expected_val, result):
    assert_lowest_common_ancestor(result, expected_val)
    return


if __name__ == "__main__":
    app.run()
