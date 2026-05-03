# python-csv-tools

Small CLI helpers for everyday CSV cleanup. Stdlib only.

## Scripts

- `dedupe_rows.py` — drop duplicate rows by selected columns
- `normalize_headers.py` — lowercase + snake_case headers
- `filter_rows.py` — keep rows where a column matches a value

## Examples

```bash
python dedupe_rows.py sample_data/people.csv -o out/unique.csv -k Email
python normalize_headers.py sample_data/people.csv -o out/headers.csv
python filter_rows.py sample_data/people.csv -o out/london.csv --column City --equals London
```

