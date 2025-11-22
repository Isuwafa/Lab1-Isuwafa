# Individual Coding Lab – Grade Generator & CSV Archiver

**Author: Suwafa Iradukunda**
**Course: Introduction to Python Programming and Databases**


## This project contains two main components:

grade-generator.py
An interactive Python program that:

Collects assignment information (name, category, grade, and weight)

Validates all user input

Computes weighted formative (FA) and summative (SA) scores

Calculates final grade and GPA

Determines Pass/Fail status for each category and overall

Identifies required resubmissions based on failed formative assessments

Export all data into grades.csv

## organizer.sh
A Bash shell script that:

Archives CSV files in the current folder

Generates timestamps for each archived file

Writes detailed logs into organizer.log

Moves renamed CSV files into an archive/ directory

Is fully executable in a bash environment (Git Bash / Linux / WSL)

## How to Run the Python Program

Make sure Python is installed. 
Then run:
```python 

python3 grade-generator.py

``` 
Follow the prompts to input:

Assignment name

Category (FA/SA)

Grade

Weight

The program will automatically generate:

A grade summary

Pass/Fail status

Resubmission requirements

A grades.csv file

How to Run the Archive Shell Script

The shell script must be executable.


- Step 1 — Open Git Bash in the project folder

Right-click inside the folder → “Git Bash Here”

- Step 2 — Make the script executable

```bash
chmod +x organizer.sh
```

- Step 3 — Run the script
```bash
./organizer.sh
```

Expected Result After Running the Script
Before running:

```bash
.
├── grade-generator.py
├── grades.csv
└── organizer.sh

```

After running:

```bash
.
├── archive
│   └── grades-20251120-175500.csv
├── organizer.log
├── grade-generator.py
└── organizer.sh

```

Files Included        File	Description
grade-generator.py    Python program that calculates grades
organizer.sh          Executable Bash script to archive CSV files
grades.csv            Generated CSV containing assignment input
organizer.log         Log file updated by the shell script
archive/	Folder       containing archived timestamped CSVs
README.md             Documentation file


