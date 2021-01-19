# Template generator from csv file

According to the name of the variables in the `.csv` files, templates will be filled up and saved on the output folder.

The script iterates through the lines of the `.csv` file and saves a version for each line.

## Usage

Create the `.csv` table with the variables you want to use as columns names.
Write `.txt` templates with those variable names in curly brackets ({}).
Attention: do not type spaces before or after the variable name.

After that setup, just run the main.py file.

To run the file with the option to choose which field will be used to discriminate the output files, type the name of the field as one of the arguments when running from the terminal. In the mock file, we would have, if we wanted to use the column titled "Name B" as a reference when saving the output files, we should type this on the terminal:

```
    python3 main.py "Name B"
```

Otherwise, the script will just consider the first column of the .csv file as a reference.

## Dependencies

Libraries used:

- Pandas
- OS
- Sys

Only _Pandas_ need to be installed.
To install:

```
    pip install pandas
```

## Authors

**[Sthefano Carvalho](https://github.com/sthefanoc)**
