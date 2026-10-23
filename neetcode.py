# /// script
# requires-python = ">=3.10"
# dependencies = ["marimo==0.25.2", "leetcode-py-sdk==0.0.0"]
# [tool.uv.sources]
# leetcode-py-sdk = { path = ".", editable = true }
# ///

import marimo

__generated_with = "0.25.2"
app = marimo.App(width="medium", app_title="NeetCode practice")


@app.cell(hide_code=True)
def _():
    import json
    from urllib.parse import quote

    import marimo as mo
    from leetcode_py.cli.utils.problem_finder import find_problems_by_tag, get_problem_json_path

    repo_dir = mo.notebook_dir()
    return (
        find_problems_by_tag,
        get_problem_json_path,
        json,
        mo,
        quote,
        repo_dir,
    )


@app.cell(hide_code=True)
def introduction(mo):
    mo.md("""
    # NeetCode practice

    Choose a collection, select a row to read the problem, and open its notebook.
    Your problem notebooks and notes stay in this repository.
    """)
    return


@app.cell(hide_code=True)
def filters(mo):
    collection = mo.ui.dropdown(
        {"NeetCode 150": "neetcode-150", "NeetCode 250": "neetcode-250", "NeetCode All": "neetcode"},
        value="NeetCode 150", allow_select_none=False, label="Collection",
    )
    difficulty = mo.ui.dropdown(
        ["All", "Easy", "Medium", "Hard"], value="All", allow_select_none=False, label="Difficulty",
    )
    mo.hstack([collection, difficulty], justify="start")
    return collection, difficulty


@app.cell(hide_code=True)
def catalog(
    collection,
    difficulty,
    find_problems_by_tag,
    get_problem_json_path,
    json,
    mo,
    quote,
    repo_dir,
):
    problem_rows = []
    for _slug in dict.fromkeys(find_problems_by_tag(collection.value)):
        _data = json.loads(get_problem_json_path(_slug).read_text(encoding="utf-8"))
        if difficulty.value != "All" and _data["difficulty"] != difficulty.value:
            continue
        _notebook = repo_dir / "leetcode" / _slug / "playground_marimo.py"
        _url = "?file=" + quote(str(_notebook.relative_to(repo_dir)), safe="")
        problem_rows.append({
            "#": int(_data["problem_number"]),
            "Problem": _data["problem_title"],
            "Difficulty": _data["difficulty"],
            "Topics": _data["topics"],
            "Notebook": mo.Html(f'<a href="{_url}" target="_blank" rel="noopener">Open notebook</a>')
                if _notebook.is_file() else "Run scripts/gen_marimo.py",
            "slug": _slug,
        })
    problem_rows.sort(key=lambda row: ({"Easy": 0, "Medium": 1, "Hard": 2}[row["Difficulty"]], row["#"]))
    return (problem_rows,)


@app.cell(hide_code=True)
def problems(mo, problem_rows):
    problem_table = mo.ui.table(
        problem_rows, selection="single", initial_selection=[0], page_size=15,
        hidden_columns=["slug"], show_column_summaries=False, show_data_types=False,
        show_download=False, label=f"{len(problem_rows)} problems · search by title or topic",
    )
    problem_table
    return (problem_table,)


@app.cell(hide_code=True)
def statement(get_problem_json_path, json, mo, problem_table):
    if problem_table.value:
        _selected = problem_table.value[0]
        _spec = json.loads(get_problem_json_path(_selected["slug"]).read_text(encoding="utf-8"))
        _examples = "\n\n".join(item["content"] for item in _spec["_readme_examples"]["list"])
        mo.output.replace(mo.md(
            f"## {_spec['problem_number']}. {_spec['problem_title']}\n\n"
            f"{_spec['readme_description']}\n\n"
            f"### Examples\n\n{_examples}\n\n"
            f"### Constraints\n\n{_spec['readme_constraints']}"
        ))
    else:
        mo.output.replace(mo.md("Select a problem row to read its statement."))
    return


@app.cell(hide_code=True)
def workflow(mo):
    mo.md("""
    ## Solve and take notes

    1. Open a problem notebook and read its statement.
    2. Implement the unfinished methods in the **Your solution** cell.
    3. Press **Run tests** to run the full problem test bank against your notebook code.
    4. Add Markdown cells for your approach, complexity, and edge cases.

    Reference answers remain in the adjacent `solution.py` files. Practice notebooks do not import or run them.

    [Browse this repository's notebooks](/)
    """)
    return


if __name__ == "__main__":
    app.run()
