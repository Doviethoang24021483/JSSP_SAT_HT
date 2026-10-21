"""Dinh nghia CHUNG cho moi file ket qua (CSV).

Ca hai thanh vien dung ham append_result() de ghi ket qua, khong tu ghi tay.
"""
import csv
import os

COLUMNS = [
    "instance",    # vd: ft06
    "method",      # crawford | crawford_window | timeindexed | cpsat | cplex_cp | cplex_mip | gurobi
    "solver",      # cadical153 | glucose4 | maplechrono | minisat22 | cryptominisat | kissat | -
    "strategy",    # linear_up | linear_down | binary | none (baseline)
    "incremental", # 1 / 0
    "L_final",     # makespan tot nhat tim duoc (hoac toi uu)
    "status",      # OPTIMAL | FEASIBLE | TIMEOUT | MEMOUT | ERROR
    "time",        # tong thoi gian (giay)
    "encode_time", # thoi gian sinh CNF (giay), baseline de trong
    "n_calls",     # so lan goi solver
    "vars",        # so bien (SAT) / so bien (MIP/CP)
    "clauses",     # so clause (SAT) / so rang buoc (MIP/CP)
    "mem",         # MB dinh bo nho (neu do duoc)
    "seed",
    "note",
]


def append_result(path, row):
    """Ghi them 1 dong vao CSV (tu tao header neu file chua co)."""
    os.makedirs(os.path.dirname(path) or ".", exist_ok=True)
    new = not os.path.exists(path)
    full = {c: row.get(c, "") for c in COLUMNS}
    with open(path, "a", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=COLUMNS)
        if new:
            w.writeheader()
        w.writerow(full)
