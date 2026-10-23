import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_ip_to_cidr, run_ip_to_cidr
    from solution import Solution

    return Solution, assert_ip_to_cidr, run_ip_to_cidr


@app.cell
def _():
    # Example test case
    ip = "255.0.0.7"
    n = 10
    expected = ["255.0.0.7/32", "255.0.0.8/29", "255.0.0.16/32"]
    return expected, ip, n


@app.cell
def _(Solution, ip, n, run_ip_to_cidr):
    result = run_ip_to_cidr(Solution, ip, n)
    result
    return (result,)


@app.cell
def _(assert_ip_to_cidr, expected, result):
    assert_ip_to_cidr(result, expected)
    return


if __name__ == "__main__":
    app.run()
