# grade-anonymizer
Grade anonymizer built for UNL Software Engineering Teaching Assistants to publish anonymized versions of lab grades.

Use instructions:
  Requires two input files to operate.
  1. NUID.csv
  2. gradefile.txt

  NUID.csv should be filled with students' names and ID numbers, following the example format given in the repository copy of NUID.csv.
    Each row should be the student's name, followed by a comma, followed by a newline.
    The first row of the file should read "Name, NUID"
  gradefile.txt should be filled with students' names and grades, following the example given in the repository copy of gradefile.txt. (It is set up to allow copy-pasting directly from Google sheets.)
    The first row of the file should be "Student Name\t1\t2\t..." where \t represents a tab character and category names are added separated by tab characters.
    Each subsequent row should be "Student Name\tTRUE\tFALSE\tTRUE..." where each TRUE and FALSE category corresponds to completion or non-completion of each category in the first row.

  Then run the python file anonymizer.py.
  The script will output to anonymized_grades.csv, in a format that is ready to be opened in Excel.
