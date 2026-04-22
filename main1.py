# import pandas as pd

# # Load Excel file
# df = pd.read_excel("student_raw_data.xlsx")

# # Total Marks
# df["Total"] = df[["Maths", "Science", "English", "Hindi", "SST"]].sum(axis=1)

# # Percentage
# df["Percentage"] = (df["Total"] / 500) * 100

# # Grade Function
# def get_grade(p):
#     if p >= 90:
#         return "A"
#     elif p >= 75:
#         return "B"
#     elif p >= 60:
#         return "C"
#     else:
#         return "Fail"

# df["Grade"] = df["Percentage"].apply(get_grade)

# # Topper
# topper = df.loc[df["Total"].idxmax()]

# print("Topper Student:")
# print(topper)

# # Save new file
# df.to_excel("student_report.xlsx", index=False)

# print("Report Generated Successfully ✅")

# import pandas as pd

# # Load Excel file
# df = pd.read_excel("student_raw_data.xlsx")

# # Total Marks
# df["Total"] = df[["Maths", "Science", "English", "Hindi", "SST"]].sum(axis=1)

# # Percentage
# df["Percentage"] = (df["Total"] / 500) * 100

# # Grade Function (33% pass rule)
# def get_grade(p):
#     if p >= 90:
#         return "A"
#     elif p >= 75:
#         return "B"
#     elif p >= 50:
#         return "C"
#     elif p >= 33:
#         return "D"
#     else:
#         return "Fail"

# # Apply Grade
# df["Grade"] = df["Percentage"].apply(get_grade)

# # Pass/Fail Column (clear understanding ke liye)
# df["Result"] = df["Percentage"].apply(lambda x: "Pass" if x >= 33 else "Fail")

# # Topper
# topper = df.loc[df["Total"].idxmax()]

# print("🏆 Topper Student:")
# print(topper[["Name", "Total", "Percentage", "Grade"]])

# # Top 5 Students
# top5 = df.sort_values(by="Total", ascending=False).head(5)

# # Fail Students (<33%)
# fail_students = df[df["Percentage"] < 33]

# # Save all files
# df.to_excel("student_report1.xlsx", index=False)
# top5.to_excel("top5_students.xlsx", index=False)
# fail_students.to_excel("fail_students.xlsx", index=False)

# print("\n✅ Report Generated Successfully")
# print("📁 Files Created:")
# print("1. student_report.xlsx")
# print("2. top5_students.xlsx")
# print("3. fail_students.xlsx")

# import pandas as pd

# # Load Excel
# df = pd.read_excel("student_raw_data.xlsx")

# # Total
# df["Total"] = df[["Maths", "Science", "English", "Hindi", "SST"]].sum(axis=1)

# # Percentage
# df["Percentage"] = (df["Total"] / 500) * 100

# # Grade
# def get_grade(p):
#     if p >= 90:
#         return "A"
#     elif p >= 75:
#         return "B"
#     elif p >= 50:
#         return "C"
#     elif p >= 33:
#         return "D"
#     else:
#         return "Fail"

# df["Grade"] = df["Percentage"].apply(get_grade)

# # Result
# df["Result"] = df["Percentage"].apply(lambda x: "Pass" if x >= 33 else "Fail")

# # Save
# df.to_excel("student_report3.xlsx", index=False)

# print("✅ Data Processed Successfully")

import pandas as pd

# -------------------------------
# 📂 LOAD RAW DATA
# -------------------------------
df = pd.read_excel("student_raw_data.xlsx")

# -------------------------------
# 🧮 DATA PROCESSING
# -------------------------------
df["Total"] = df[["Maths", "Science", "English", "Hindi", "SST"]].sum(axis=1)

df["Percentage"] = (df["Total"] / 500) * 100

# Grade Function
def get_grade(p):
    if p >= 90:
        return "A"
    elif p >= 75:
        return "B"
    elif p >= 50:
        return "C"
    elif p >= 33:
        return "D"
    else:
        return "Fail"

df["Grade"] = df["Percentage"].apply(get_grade)

# Result Column
df["Result"] = df["Percentage"].apply(lambda x: "Pass" if x >= 33 else "Fail")

# -------------------------------
# 📊 EXTRA FILES
# -------------------------------

# Top 5 Students
top5 = df.sort_values(by="Total", ascending=False).head(5)

# Fail Students
fail_students = df[df["Percentage"] < 33]

# -------------------------------
# 💾 SAVE FILES (3 FILES)
# -------------------------------
df.to_excel("student_report4.xlsx", index=False)
top5.to_excel("top5_students4.xlsx", index=False)
fail_students.to_excel("fail_students10.xlsx", index=False)

# -------------------------------
# 🖨️ OUTPUT MESSAGE
# -------------------------------
print("✅ Report Generated Successfully")
print("📁 Files Created:")
print("1. student_report10.xlsx")
print("2. top5_students8.xlsx")
print("3. fail_students8.xlsx")