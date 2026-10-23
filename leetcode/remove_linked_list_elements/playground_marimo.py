import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_remove_linked_list_elements, run_remove_linked_list_elements
    from solution import Solution

    return (
        Solution,
        assert_remove_linked_list_elements,
        run_remove_linked_list_elements,
    )


@app.cell
def _():
    # Example test case
    head_vals: list[int] = [1, 2, 6, 3, 4, 5, 6]
    val: int = 6
    expected_vals: list[int] = [1, 2, 3, 4, 5]
    return expected_vals, head_vals, val


@app.cell
def _(
    Solution,
    head_vals: list[int],
    run_remove_linked_list_elements,
    val: int,
):
    result = run_remove_linked_list_elements(Solution, head_vals, val)
    result
    return (result,)


@app.cell
def _(assert_remove_linked_list_elements, expected_vals: list[int], result):
    assert_remove_linked_list_elements(result, expected_vals)
    return


if __name__ == "__main__":
    app.run()
