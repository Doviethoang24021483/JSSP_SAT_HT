"""Kiem tra moi truong. Chay: python check_env.py
Ca hai thanh vien phai thay 'OK' o cac muc BAT BUOC."""
import importlib
import platform
import sys

print(f"Python {sys.version.split()[0]} on {platform.platform()}")
ok_all = True


def check(label, mod, required=True):
    global ok_all
    try:
        m = importlib.import_module(mod)
        ver = getattr(m, "__version__", "")
        print(f"[OK]   {label} {ver}")
        return m
    except Exception as e:  # noqa
        tag = "FAIL" if required else "skip"
        print(f"[{tag}] {label}: {type(e).__name__}: {e}")
        if required:
            ok_all = False
        return None


if sys.version_info < (3, 10):
    print("[FAIL] Can Python >= 3.10")
    ok_all = False

pysat = check("python-sat", "pysat")
ortools = check("ortools", "ortools")
check("numpy", "numpy")
check("pandas", "pandas")
check("matplotlib", "matplotlib")
check("psutil", "psutil")

# Thu giai that: SAT solver va CP-SAT
if pysat:
    try:
        from pysat.solvers import Cadical153, Glucose4

        for S in (Cadical153, Glucose4):
            with S(bootstrap_with=[[1, 2], [-1, 2], [-2, 3]]) as s:
                assert s.solve(), S.__name__
                # kiem tra assumption (can cho Incremental SAT)
                assert not s.solve(assumptions=[-3]), S.__name__
        print("[OK]   PySAT: Cadical153 + Glucose4 (ho tro assumptions)")
    except Exception as e:  # noqa
        print(f"[FAIL] PySAT solver: {type(e).__name__}: {e}")
        ok_all = False

if ortools:
    try:
        from ortools.sat.python import cp_model

        m = cp_model.CpModel()
        x = m.NewIntVar(0, 10, "x")
        m.Add(x >= 3)
        m.Minimize(x)
        s = cp_model.CpSolver()
        assert s.Solve(m) == cp_model.OPTIMAL and s.Value(x) == 3
        print("[OK]   OR-Tools CP-SAT giai duoc bai thu")
    except Exception as e:  # noqa
        print(f"[FAIL] CP-SAT: {type(e).__name__}: {e}")
        ok_all = False

# Tuy chon (can license)
check("docplex (CPLEX CP)", "docplex", required=False)
check("gurobipy", "gurobipy", required=False)
check("cnsplots", "cnsplots", required=False)

print()
print("MOI TRUONG SAN SANG" if ok_all else "CON LOI: sua cac muc [FAIL] o tren")
sys.exit(0 if ok_all else 1)
