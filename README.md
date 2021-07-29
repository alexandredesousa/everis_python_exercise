# Description
Project to develop for the everis python exercise

# Due
Friday, 30th July, 2021

# Python packages used
if any
???

# Instructions


# ASSUMPTIONS
- If understood correctly, the goal is to develop a function `get_tend('XPI')` which computes the result in the table
with that head.

  - to compute that, I will need to use the `AUX`, `XPI`, and `WWW` tables (allegedly, because from formulas inspection,
to compute the results in head `XPI` only tables `XPI` and `AUX`  are required, being that `AUX` also depends on table `XPI` - 
see file [data_own_calculations.xlsx](docs/data_own_calculations.xlsx) (sheet `XPI_computation`) where I computed those records, and checked if they are
equal to source (they are), using only the tables `XPI` and `AUX`.

- Considering the challenge clearly states all columns must be used, I'll assume the previous point is not correct
(either misinterpretation or incorrect in the problem statement?).
Considering the other heads in the table containing computed elements, specifically, `FIXED`, `XPI`, `XPI+1.0%`, `XPI+2.0%`,
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
    where the C columns refers to XPI column.

- ** The formula in that column was specifically chosen to present here.
Even though the formula points to `D$10` it is my belief it is a mistake - as that leads to a circular formula for the
year 1992 (cell D10) - see [raw_data_circularity.png](docs/raw_data_circularity.png) file.
The same is true for column `XPI+2.0%` (i.e. pointing to cell `E$10`, in this case).
   - I believe that should instead point to cell `D$5` and `E$5` respectively, that is, pointing to the respective
   percentage values.
   - What I point to be the correct case, is what happens in the `WWW` calculations - i.e. point to the percentage
   points rather than some value in the middle of the calculations that leads to a circular computation
   when that cell is reached.
   - based on that [data_own_calculations.xlsx](docs/data_own_calculations.xlsx) (sheet `corrected formulas`) presents
   what I consider to be the correct formulas - basically, apply the same type of formula as to the
   `WWW+x%` columns to the `XPI+x%` columns, and thus avoiding circularity for year 1992.
   - the values obtained are coherent to the raw data received (file [python_assessment_data.xlsx](docs/python_assessment_data.xlsx))
   
Assuming all the points presented, four types of functions, which apply to the headers as presented,
the four types of computations will be developed in order to reproduce the .xlsx file with python code.  