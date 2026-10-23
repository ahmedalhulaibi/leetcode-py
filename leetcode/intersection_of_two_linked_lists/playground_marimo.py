import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_get_intersection_node, run_get_intersection_node
    from solution import Solution

    return Solution, assert_get_intersection_node, run_get_intersection_node


@app.cell
def _():
    # Example test case
    list_a: list[int] = [4, 1, 8, 4, 5]
    list_b: list[int] = [5, 6, 1, 8, 4, 5]
    skip_a: int = 2
    skip_b: int = 3
    return list_a, list_b, skip_a, skip_b


@app.cell
def _(
    Solution,
    list_a: list[int],
    list_b: list[int],
    run_get_intersection_node,
    skip_a: int,
    skip_b: int,
):
    result, expected = run_get_intersection_node(Solution, list_a, list_b, skip_a, skip_b)
    result
    return expected, result


@app.cell
def _(assert_get_intersection_node, expected, result):
    assert_get_intersection_node(result, expected)
    return


if __name__ == "__main__":
    app.run()
