# JSSP bang SAT Encoding (BTL so 2 - Cac van de hien dai KHMT)

Giai Job-Shop Scheduling Problem bang SAT encoding (Crawford & Baker; Koshimura et al., IEICE 2010),
so sanh voi CP-SAT, CPLEX CP, CPLEX MIP, Gurobi.

Nhom: <Ten A> (SAT side), <Ten B> (baseline + analysis side)

## Cai dat

```bash
python -m venv .venv
source .venv/bin/activate          # Windows: .venv\Scripts\activate
pip install -r requirements.txt
python check_env.py                # phai in "MOI TRUONG SAN SANG"
```

CPLEX / Gurobi can license hoc thuat (xem phan cuoi), bo comment trong `requirements.txt` sau khi co.

## Cau truc

```
data/          instance OR-Library + best_known.csv (instance, n, m, LB, UB)
src/           ma nguon (instance, verify, encodings/, baselines/, search, ...)
experiments/   script chay batch
results/       CSV tho do script ghi (KHONG sua tay)
figures/       script ve hinh (cnsplots) + hinh xuat ra
report/        bao cao LaTeX (cas-sc)
tests/         test
```

## Quy uoc ket qua (CSV)

Moi ket qua ghi bang `src.schema.append_result(path, row)`. Cot:

| Cot | Y nghia |
|---|---|
| instance | ten instance, vd `ft06` |
| method | `crawford`, `crawford_window`, `timeindexed`, `cpsat`, `cplex_cp`, `cplex_mip`, `gurobi` |
| solver | `cadical153`, `glucose4`, `maplechrono`, `minisat22`, `cryptominisat`, `kissat`, `-` |
| strategy | `linear_up`, `linear_down`, `binary`, `none` |
| incremental | 1 / 0 |
| L_final | makespan tot nhat tim duoc |
| status | `OPTIMAL`, `FEASIBLE`, `TIMEOUT`, `MEMOUT`, `ERROR` |
| time / encode_time | giay (tong / rieng phan sinh CNF) |
| n_calls | so lan goi solver |
| vars / clauses | kich thuoc mo hinh |
| mem | MB |
| seed, note | tuy chon |

Quy tac chung: moi bang/hinh trong bao cao sinh tu CSV bang script, khong lam tay.

## Quy uoc lam viec nhom

- Nhanh: `main` chi nhan code da review. Moi nguoi lam tren nhanh `a/...` hoac `b/...`, mo Pull Request, nguoi kia review.
- `verify.py` la "trong tai": moi lich (tu SAT hay baseline) deu phai qua no.
- Moc kiem tra: ft06 = 55, ft10 = 930.
- Hop nhanh 15 phut moi 2-3 ngay.

## Data Availability

Ma nguon va ket qua thuc nghiem: <link GitHub cua nhom>

## Xin license hoc thuat

- CPLEX: IBM Academic Initiative (can email truong .edu)
- Gurobi: Academic license (cap qua mang truong)
