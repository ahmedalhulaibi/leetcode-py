import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_reorder_log_files, run_reorder_log_files
    from solution import Solution

    return Solution, assert_reorder_log_files, run_reorder_log_files


@app.cell
def _():
    # Example test case
    logs = ["dig1 8 1 5 1", "let1 art can", "dig2 3 6", "let2 own kit dig", "let3 art zero"]
    expected = ["let1 art can", "let3 art zero", "let2 own kit dig", "dig1 8 1 5 1", "dig2 3 6"]
    return expected, logs


@app.cell
def _(Solution, logs, run_reorder_log_files):
    result = run_reorder_log_files(Solution, logs)
    result
    return (result,)


@app.cell
def _(assert_reorder_log_files, expected, result):
    assert_reorder_log_files(result, expected)
    return


if __name__ == "__main__":
    app.run()
