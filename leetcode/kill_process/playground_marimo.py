import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_kill_process, run_kill_process
    from solution import Solution

    return Solution, assert_kill_process, run_kill_process


@app.cell
def _():
    # Example test case
    pid = [1, 3, 10, 5]
    ppid = [3, 0, 5, 3]
    kill = 5
    expected = [5, 10]
    return expected, kill, pid, ppid


@app.cell
def _(Solution, kill, pid, ppid, run_kill_process):
    result = run_kill_process(Solution, pid, ppid, kill)
    result
    return (result,)


@app.cell
def _(assert_kill_process, expected, result):
    assert_kill_process(result, expected)
    return


if __name__ == "__main__":
    app.run()
