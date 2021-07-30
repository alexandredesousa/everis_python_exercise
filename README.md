# Description
Project to develop for the everis python exercise.

# Due
Friday, 30th July, 2021.

# Instructions
A docker container to run the code was not created
as such the project dir must be added to the `PYTHONPATH` in the machine it is to be run,
if ran in the machine terminal/shell.

In case one wants to run the code to reproduce the results, pay attention to:
Python version used: **Python 3.7.9**.

Required packages: see `requirements.txt`
(may be useful to use `pip install -r requirements.txt` command from the root of the project).

## Notes on the project
### data dir
The [data](data) dir contains both the raw data provided ([python_assessment_data.xlsx](data/python_assessment_data.xlsx)),
as well as the raw data used in the code - according to the [instructions](docs/everisuk_python_assessment_v1.pdf),
should not use the file provided, "Your Python code can’t use the spreadsheet as a source, but you can create any other
external method as csv, txt, etc.."; as such, the routine presented in module [get_raw_data.py](src/get_raw_data.py)
provides the script to extract the required raw data from the original file, as well as saving the extracted tables
into .csv files also in the [data](data) dir, specifically [AUX_data.csv](data/AUX_data.csv), [PERC_data.csv](data/PERC_data.csv),
[WWW_data.csv](data/WWW_data.csv) and [XPI_data.csv](data/XPI_data.csv).

In addition to that, the [data](data) dir also contains the solutions, as per the [main.py](src/main.py) script run.

### docs dir
Contains the problem statement as well as some notes.

### src
There are 3 scripts:

- [main.py](src/main.py):
  
  The main script is a simple script that invokes the functions one.
  It can be used to **compute the complete solution** for the problem, i.e. given the raw data compute all the column data
  for all the years.
  
  The solutions are provided in the form of a pandas dataframe and are saved by default in the [data](data) dir as a `.csv`
  (both rounded to 2 decimal places, as presented in the problem statement, as well as not rounded).
  
  * Note: it is assumed that the raw data tables required for solution computation are available in the [data](data) dir.

- [get_raw_data.py](src/get_raw_data.py):
  Considering the problem statement refers that the spreadsheet provided must not be used as source, this script extracts
  the required raw data (as per the instructions) from the spreadsheet and saves the required tables as `.csv` in the
  [data](data).

- [functions.py](src/functions.py)
  This script contains the functions required to achieve the solution as in the .xlsx file, as well as an
  auxiliary function (compute_solution) that aggregates all in one, to allow for solution computation with a single call,
  provided the raw data (notice single call in the main to compute the solution).


# ASSUMPTIONS
- If understood correctly, the goal is to develop a function `get_tend('XPI')` which computes the result in the table
with that head, however some points do not seem to be clear:

  - Allegedly, to compute that, I will need to use the `AUX`, `XPI`, and `WWW` tables
  (as per documentation provided, "note that to achieve the results you will need to use the AUX, XPI, and WWW tables
  in order to apply all the necessary calculations as demonstrated.").
  - However, from formulas inspection, I notice that to compute the results in head `XPI`
  only tables `XPI` and `AUX`  are required, being that `AUX` also depends on table `XPI` so in the limit,
  only table `XPI` is required - see file [data_own_calculations.xlsx](data/data_own_calculations.xlsx)
  (sheet `XPI_computation`) where I computed those records, and checked if they are equal to source (they are),
  using only the tables `XPI` and `AUX`.

- Notwithstanding the previous point, the challenge clearly states all columns must be used,
as such I'll assume the previous point is not correct (either misinterpretation or incorrect in the problem statement?),
i.e. the goal is not just to compute the `XPI` column.
  - **I will assume all computable columns are to be computed**, not just column `XPI`.

- Considering the other heads in the table containing computed elements, specifically, `FIXED`, `XPI`, `XPI+1.0%`, `XPI+2.0%`,
`WWW`, `WWW+1.0%` and `WWW+2.0%` we see there are __four__ types of computations being performed:

  - Computation type no.1 (executed in the ``FIXED` column):
    - computes an increment from the next element, as: Fixed_t = Fixed_t+1*(1+percent_fixed)
    - see for instance first record formula on cell B8: `=B9*(1+$B$5)`
  
  - Computation type no.2 (executed in the `XPI` column):
    - for a given year, averages the values from table `XPI` for that same year. That values is divided by a constant
    computed previously.
    - see for instance first record formula on cell C8: `=$J$6/AVERAGEIF($L$4:$L$377;A8;$M$4:$M$377)`
    where J6 is the computed constant, $L$4:$M$377 defines the `XPI` table range.
  
  - Computation type no.3 (executed in the `WWW` column):
    - Just looks up two values on table `WWW` and divides them.
    - see for instance first record formula on cell F8: `=VLOOKUP($A$39;$O$4:$P$40;2;FALSE)/VLOOKUP($A8;$O$4:$P$40;2;FALSE)`
    where $O$4:$P$40 defines the `WWW` table range.
    - Notice the numerator never changes - all cells are locked.
  
  - Computation type no.4 (executed in the `XPI+1.0%`, `XPI+2.0%`, `WWW+1.0%` and `WWW+2.0%`):
    - For a given t, add to the corresponding XPI or WWW value for that same t the value of the XPI of the next t
    multiplied by a percentage, as:
      - XPI(1%)_t= XPI_t+XPI_t+1*percentage_1%
      - XPI(2%)_t= XPI(1%)_t+XPI(1%)_t+1*percentage_2%
    - see  for instance first record formula on cell D8: `=C9*(C8/C9+D$10)`**
    where the C columns refers to XPI column. The formulas presented above are simplified, based on this one, considering
    that `=C9*(C8/C9+D$10)` can be simplified as `=(C8+C9*D$10)` thus reducing the number of operations.

- ** The formula in that column was specifically chosen to present here.
Even though the formula points to `D$10` it is my belief it is a mistake - as that leads to a circular formula for the
year 1992 (cell D10) - see [raw_data_circularity.png](docs/raw_data_circularity.png) file.
The same is true for column `XPI+2.0%` (i.e. pointing to cell `E$10`, in this case).
   - I believe that should instead point to cell `D$5` and `E$5` respectively, that is, pointing to the respective
   percentage values.
   - What I point to be the correct case, is what happens in the `WWW` calculations - i.e. point to the percentage
   points rather than some value in the middle of the calculations that leads to a circular computation
   when that cell is reached.
   - based on that [data_own_calculations.xlsx](data/data_own_calculations.xlsx) (sheet `corrected formulas`) presents
   what I consider to be the correct formulas - basically, apply the same type of formula as to the
   `WWW+x%` columns to the `XPI+x%` columns, and thus avoiding circularity for year 1992.
   - the values obtained are coherent to the raw data received (file [python_assessment_data.xlsx](data/python_assessment_data.xlsx))
   
*Assuming all the points presented four types of functions, which apply to the headers as presented,
the four types of computations will be developed in order to reproduce the .xlsx file with python code, which is to compute
all the columns in the main table, not just the `XPI` column.*

# Development Notes
1. to satisfy the requirement "Your Python code __can’t__ use the spreadsheet as a source,
but you can create any other external method as csv, txt, etc..", a module was developed ([get_raw_data.py](src/get_raw_data.py))
to extract the raw data from the spreadsheet provided (available [here](data/python_assessment_data.xlsx)), and saves it
as .csv in the [data directory](data).
  1.  according to the document provided "note that to achieve the results you will need to use the
  AUX, XPI, and WWW tables in order to apply all the necessary calculations (...)
  and you must use all the percentual indexes.". The module extracts only these data and saves it as different csv files.
  
  
# Development notes
Used a python venv, with version: **Python 3.7.9**.

## Python packages used
The following packages are required (from `pip list`):

```
Package         Version
--------------- -------
et-xmlfile      1.1.0
numpy           1.21.1
openpyxl        3.0.7
pandas          1.3.1
pip             20.1.1
python-dateutil 2.8.2
pytz            2021.1
setuptools      47.1.0
six             1.16.0
```

Installed `Pandas` and optional to `Pandas`, but required to read .xlsx (raw data format provided), also installed `openpyxl`.
Other required packages were also installed automatically.

A `requirements.txt` was added (`pip freeze > requirements.txt`) to the root of the project.