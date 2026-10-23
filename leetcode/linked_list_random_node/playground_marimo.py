import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_linked_list_random_node, run_linked_list_random_node
    from solution import Solution

    return (
        Solution,
        assert_linked_list_random_node,
        run_linked_list_random_node,
    )


@app.cell
def _():
    # Example test case
    operations = ["Solution", "get_random", "get_random", "get_random"]
    inputs = [[1, 2, 3], [], [], []]
    expected = [1, 2, 3]
    return expected, inputs, operations


@app.cell
def _(Solution, inputs, operations, run_linked_list_random_node):
    result = run_linked_list_random_node(Solution, operations, inputs)
    print(result)
    result
    return (result,)


@app.cell
def _(assert_linked_list_random_node, expected, result):
    assert_linked_list_random_node(result, expected)
    return


if __name__ == "__main__":
    app.run()
