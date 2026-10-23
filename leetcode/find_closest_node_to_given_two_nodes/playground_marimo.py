import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_closest_meeting_node, run_closest_meeting_node
    from solution import Solution

    return Solution, assert_closest_meeting_node, run_closest_meeting_node


@app.cell
def _():
    # Example test case
    edges = [2, 2, 3, -1]
    node1 = 0
    node2 = 1
    expected = 2
    return edges, expected, node1, node2


@app.cell
def _(Solution, edges, node1, node2, run_closest_meeting_node):
    result = run_closest_meeting_node(Solution, edges, node1, node2)
    result
    return (result,)


@app.cell
def _(assert_closest_meeting_node, expected, result):
    assert_closest_meeting_node(result, expected)
    return


if __name__ == "__main__":
    app.run()
