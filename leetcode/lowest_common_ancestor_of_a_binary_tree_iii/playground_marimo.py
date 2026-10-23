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
    root_list: list[int | None] = [3, 5, 1, 6, 2, 0, 8, None, None, 7, 4]
    p_val = 5
    q_val = 1
    expected_val = 3
    return expected_val, p_val, q_val, root_list


@app.cell
def _(
    Solution,
    p_val,
    q_val,
    root_list: list[int | None],
    run_lowest_common_ancestor,
):
    result = run_lowest_common_ancestor(Solution, root_list, p_val, q_val)
    result
    return (result,)


@app.cell
def _(assert_lowest_common_ancestor, expected_val, result):
    assert_lowest_common_ancestor(result, expected_val)
    return


if __name__ == "__main__":
    app.run()
