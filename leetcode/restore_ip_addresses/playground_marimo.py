import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_restore_ip_addresses, run_restore_ip_addresses
    from solution import Solution

    return Solution, assert_restore_ip_addresses, run_restore_ip_addresses


@app.cell
def _():
    # Example test case
    s = "25525511135"
    expected = ["255.255.11.135", "255.255.111.35"]
    return expected, s


@app.cell
def _(Solution, run_restore_ip_addresses, s):
    result = run_restore_ip_addresses(Solution, s)
    result
    return (result,)


@app.cell
def _(assert_restore_ip_addresses, expected, result):
    assert_restore_ip_addresses(result, expected)
    return


if __name__ == "__main__":
    app.run()
