import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_assign_tasks, run_assign_tasks
    from solution import Solution

    return Solution, assert_assign_tasks, run_assign_tasks


@app.cell
def _():
    # Example test case
    servers = [3, 3, 2]
    tasks = [1, 2, 3, 2, 1, 2]
    expected = [2, 2, 0, 2, 1, 2]
    return expected, servers, tasks


@app.cell
def _(Solution, run_assign_tasks, servers, tasks):
    result = run_assign_tasks(Solution, servers, tasks)
    result
    return (result,)


@app.cell
def _(assert_assign_tasks, expected, result):
    assert_assign_tasks(result, expected)
    return


if __name__ == "__main__":
    app.run()
