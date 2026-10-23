import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_valid_ip_address, run_valid_ip_address
    from solution import Solution

    return Solution, assert_valid_ip_address, run_valid_ip_address


@app.cell
def _():
    # Example test case
    query_ip = "172.16.254.1"
    expected = "IPv4"
    return expected, query_ip


@app.cell
def _(Solution, query_ip, run_valid_ip_address):
    result = run_valid_ip_address(Solution, query_ip)
    result
    return (result,)


@app.cell
def _(assert_valid_ip_address, expected, result):
    assert_valid_ip_address(result, expected)
    return


if __name__ == "__main__":
    app.run()
