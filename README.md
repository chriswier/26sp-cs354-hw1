# hw01-starting-with-sql

**Course:** CS354 — Database Management Systems  
**Assignment:** HW01 — Starting with SQL  
**Topics:** SELECT, WHERE, ORDER BY, DISTINCT, LIKE, BETWEEN, AND, OR, NOT

---

## Learning Objectives

By completing this assignment you will be able to:

- Write basic `SELECT` queries to retrieve specific columns from a table
- Filter rows using `WHERE` with comparison operators (`=`, `<>`, `>`, `<`, `>=`, `<=`)
- Sort result sets with `ORDER BY` (ascending and descending)
- Eliminate duplicate rows with `DISTINCT`
- Match string patterns with `LIKE`
- Filter numeric and date ranges with `BETWEEN … AND …`
- Combine multiple conditions with `AND`, `OR`, and `NOT`

---

## Prerequisites

Install the following tools before you start:

| Tool | Purpose |
|------|---------|
| [Docker Desktop](https://www.docker.com/products/docker-desktop/) | Runs the local PostgreSQL 16 database |
| [VSCode](https://code.visualstudio.com/) | Code and SQL editor |
| [SQLTools extension](https://marketplace.visualstudio.com/items?itemName=mtxr.sqltools) | Run SQL queries from inside VSCode |
| [SQLTools PostgreSQL Driver](https://marketplace.visualstudio.com/items?itemName=mtxr.sqltools-driver-pg) | PostgreSQL support for SQLTools |

---

## Setup

### 1. Clone the repository

```bash
git clone <your-classroom-repo-url>
cd hw01-starting-with-sql
```

### 2. Create and activate a virtual environment

**macOS / Linux**
```bash
python3 -m venv venv
source venv/bin/activate
```

**Windows**
```powershell
python -m venv venv
venv\Scripts\activate
```

### 3. Install Python dependencies

```bash
pip install -r requirements.txt
```

### 4. Start the database

```bash
docker compose up -d
```

This command starts a PostgreSQL 16 container named `manga_db`, creates the
`manga` database, and automatically loads the schema and seed data.  
The database will be ready in a few seconds.

### 5. Connect VSCode SQLTools

The `.vscode/settings.json` file pre-configures a connection named
**"manga (local)"**.

1. Open the SQLTools panel (the database icon in the left sidebar, or
   **View → SQLTools**).
2. Click **"manga (local)"** to connect.
3. Open any `q[N].sql` file and click **▶ Run on Active Connection**
   (or press `Ctrl+E Ctrl+E` / `Cmd+E Cmd+E`) to execute your query and
   view results inside VSCode.

### 6. Write your queries

Open each `q01.sql` … `q20.sql` file and write your SQL query below the
comment block. Each file tells you exactly which columns your result set
must contain.

### 7. Check your score locally

```bash
python grade.py
```

The script prints ✅ or ❌ for every question and a total score.  
Fix any failing queries, then re-run before submitting.

### 8. Reset the database (if needed)

```bash
docker compose down -v   # removes the container and its data volume
docker compose up -d     # recreates everything from scratch
```

---

## Submitting

```bash
git add q01.sql q02.sql q03.sql q04.sql q05.sql \
        q06.sql q07.sql q08.sql q09.sql q10.sql \
        q11.sql q12.sql q13.sql q14.sql q15.sql \
        q16.sql q17.sql q18.sql q19.sql q20.sql
git commit -m "Complete hw01"
git push
```

GitHub Actions will run the autograder automatically.  
Open the **Actions** tab in your repository to see your score.

---

## Database Schema

The database contains a single table:

```
manga
├── id             SERIAL PRIMARY KEY
├── title          VARCHAR(255)
├── author         VARCHAR(255)
├── genre          VARCHAR(100)
├── status         VARCHAR(50)      -- 'Ongoing' | 'Completed'
├── avg_rating     NUMERIC(3,1)     -- may be NULL for unrated titles
├── volumes        INTEGER
└── year_published INTEGER
```

---

## Grading

| Item | Points |
|------|--------|
| Q01 — Alphabetical title list | 5 |
| Q02 — Title and author of all manga | 5 |
| Q03 — Distinct genres | 5 |
| Q04 — Titles ordered by rating | 5 |
| Q05 — Ongoing manga | 5 |
| Q06 — Manga with more than 20 volumes | 5 |
| Q07 — Manga published 2010 or later | 5 |
| Q08 — Manga with rating exactly 5.0 | 5 |
| Q09 — Shonen manga | 5 |
| Q10 — Completed manga, alphabetical | 5 |
| Q11 — Distinct statuses | 5 |
| Q12 — Manga published before 2000 | 5 |
| Q13 — High rating and many volumes | 5 |
| Q14 — Titles starting with 'N' | 5 |
| Q15 — Single-volume manga | 5 |
| Q16 — Non-Shonen manga by genre | 5 |
| Q17 — Published 2000–2010 | 5 |
| Q18 — Ratings between 3.0 and 4.0 | 5 |
| Q19 — Author contains 'Oda' | 5 |
| Q20 — Completed or high-rated | 5 |
| **Total** | **100** |

Grading compares your query's **result set** against the expected result set —
not the query text itself.  As long as your query returns the correct rows and
columns (and the correct row order when required), you receive full credit.
