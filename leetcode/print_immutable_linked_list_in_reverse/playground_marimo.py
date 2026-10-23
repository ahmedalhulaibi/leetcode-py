import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_print_linked_list_in_reverse, run_print_linked_list_in_reverse
    from solution import Solution

    return (
        Solution,
        assert_print_linked_list_in_reverse,
        run_print_linked_list_in_reverse,
    )


@app.cell
def _():
    # Example test case
    values = [1, 2, 3, 4]
    expected = [4, 3, 2, 1]
    return expected, values


@app.cell
def _(Solution, run_print_linked_list_in_reverse, values):
    result = run_print_linked_list_in_reverse(Solution, values)
    result
    return (result,)


@app.cell
def _(assert_print_linked_list_in_reverse, expected, result):
    assert_print_linked_list_in_reverse(result, expected)
    return


if __name__ == "__main__":
    app.run()
