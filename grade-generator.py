#!/usr/bin/env python3
"""
grade-generator.py
Interactive grade collector, calculator, summary printer, and CSV exporter.

Creates grades.csv with columns: Assignment,Category,Grade,Weight
"""

import csv
import sys

def input_nonempty(prompt):
    name = input(prompt).strip()
    return name if name else input_nonempty(prompt)
    
def input_category(prompt):
    while True:
        s = input(prompt).strip().upper()
        if s in ("FA", "SA"):
            return s
        print("Invalid category. Enter 'FA' (Formative) or 'SA' (Summative).")

def input_grade(prompt):
    while True:
        s = input(prompt).strip()
        try:
            g = float(s)
            if 0 <= g <= 100:
                return g
            else:
                print("Grade must be between 0 and 100.")
        except ValueError:
            print("Please enter a number for grade (0-100).")

def input_positive_number(prompt):
    while True:
        s = input(prompt).strip()
        try:
            v = float(s)
            if v > 0:
                return v
            else:
                print("Value must be a positive number.")
        except ValueError:
            print("Please enter a valid number.")

def yes_no(prompt):
    while True:
        s = input(prompt).strip().lower()
        if s in ("y", "n"):
            return s == "y"
        print("Enter 'y' or 'n'.")

def print_summary(assignments, total_fa_wg, total_sa_wg, total_fa_weight, total_sa_weight):
    total_grade = total_fa_wg + total_sa_wg
    gpa = (total_grade / 100.0) * 5.0

    print("\n--- RESULTS ---")

    print(f"Total Formative: {total_fa_wg:.2f} / {int(total_fa_weight)}")
    print(f"Total Summative: {total_sa_wg:.2f} / {int(total_sa_weight)}")
    print("-" * 27)

    print(f"Total Grade:        {total_grade:.2f} / {int(total_fa_weight + total_sa_weight)}")
    print(f"GPA:                {gpa:.4f}")
    
 # Pass/Fail check: must have >= 50% of category weight in each category
    def category_status(total_weighted, total_weight, name):
        if total_weight == 0:
            # No assignments in this category -> treat as failing (explicit message)
            return (False, f"No {name} assignments entered.")
        threshold = 0.5 * total_weight
        passed = total_weighted >= threshold
        return (passed, f"{'PASS' if passed else 'FAIL'} (needed >= {threshold:.2f}, got {total_weighted:.2f})")

    fa_ok, fa_msg = category_status(total_fa_wg, total_fa_weight, "FA")
    sa_ok, sa_msg = category_status(total_sa_wg, total_sa_weight, "SA")

    overall_pass = fa_ok and sa_ok

    print(f"Status:             {"PASS" if overall_pass else "FAIL"}")

    return {
        "total_grade": total_grade,
        "gpa": gpa,
        "overall_pass": overall_pass,
        "fa_ok": fa_ok,
        "sa_ok": sa_ok,
    }

def write_csv(filename, assignments):
    header = ["Assignment", "Category", "Grade", "Weight"]
    try:
        with open(filename, mode="w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=header)
            writer.writeheader()
            for a in assignments:
                # write only required columns (Grade and Weight preserved as numbers but CSV will write them)
                writer.writerow({
                    "Assignment": a["Assignment"],
                    "Category": a["Category"],
                    "Grade": a["Grade"],
                    "Weight": a["Weight"]
                })
        print(f"\nCSV file '{filename}' created successfully.")
    except Exception as e:
        print("Failed to write CSV:", e)

def main():
    print("Grade Generator - Enter assignment data. Type carefully; validations are enforced.")
    assignments = []
    total_fa_wg = 0.0
    total_sa_wg = 0.0
    total_fa_weight = 0.0
    total_sa_weight = 0.0

    while True:
        name = input_nonempty("\nAssignment Name: ")
        category = input_category("Category (FA/SA): ")
        grade = int(input_grade("Grade (0-100): "))
        weight = int(input_positive_number("Weight (e.g., 30): "))

        weighted = (grade / 100.0) * weight

        # store item
        assignments.append({
            "Assignment": name,
            "Category": category,
            "Grade": grade,
            "Weight": weight,
            "Weighted": weighted
        })

        # update totals
        if category == "FA":
            total_fa_wg += weighted
            total_fa_weight += weight
        else:  # SA
            total_sa_wg += weighted
            total_sa_weight += weight

        another = yes_no("\nAdd another assignment? (y/n): ")
        if not another:
            break

    # print summary
    results = print_summary(assignments, total_fa_wg, total_sa_wg, total_fa_weight, total_sa_weight)

    # write CSV
    write_csv("grades.csv", assignments)

    # optional: exit code reflect pass/fail? We'll just end.
    return

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nInterrupted by user. Exiting.")
        sys.exit(1)

