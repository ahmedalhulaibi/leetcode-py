import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_max_probability, run_max_probability
    from solution import Solution

    return Solution, assert_max_probability, run_max_probability


@app.cell
def _():
    # Example test case
    n = 3
    edges = [[0, 1], [1, 2], [0, 2]]
    succ_prob = [0.5, 0.5, 0.2]
    start_node = 0
    end_node = 2
    expected = 0.25
    return edges, end_node, expected, n, start_node, succ_prob


@app.cell
def _(
    Solution,
    edges,
    end_node,
    n,
    run_max_probability,
    start_node,
    succ_prob,
):
    result = run_max_probability(Solution, n, edges, succ_prob, start_node, end_node)
    result
    return (result,)


@app.cell
def _(assert_max_probability, expected, result):
    assert_max_probability(result, expected)
    return


if __name__ == "__main__":
    app.run()
