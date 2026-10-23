import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_subdomain_visits, run_subdomain_visits
    from solution import Solution

    return Solution, assert_subdomain_visits, run_subdomain_visits


@app.cell
def _():
    # Example test case
    cpdomains = ["9001 discuss.leetcode.com"]
    expected = ["9001 com", "9001 discuss.leetcode.com", "9001 leetcode.com"]
    return cpdomains, expected


@app.cell
def _(Solution, cpdomains, run_subdomain_visits):
    result = run_subdomain_visits(Solution, cpdomains)
    result
    return (result,)


@app.cell
def _(assert_subdomain_visits, expected, result):
    assert_subdomain_visits(result, expected)
    return


if __name__ == "__main__":
    app.run()
