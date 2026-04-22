# import streamlit as st
# import pandas as pd

# df = pd.read_excel("student_report3.xlsx")

# st.title("🎓 Student Dashboard")

# st.subheader("📊 All Students Data")
# st.dataframe(df)

# # Topper
# topper = df.loc[df["Total"].idxmax()]
# st.subheader("🏆 Topper")
# st.write(topper)

# # Top 5
# top5 = df.sort_values(by="Total", ascending=False).head(5)
# st.subheader("🔥 Top 5 Students")
# st.dataframe(top5)

# # Chart
# st.subheader("📈 Chart")
# st.bar_chart(top5.set_index("Name")["Total"])

# # Fail Students
# fail = df[df["Percentage"] < 33]
# st.subheader("❌ Fail Students")
# st.dataframe(fail)

# import streamlit as st
# import pandas as pd

# df = pd.read_excel("student_report4.xlsx")

# st.title("🎓 Student Dashboard")

# # ✅ SUMMARY (ADD HERE - sabse upar)
# st.subheader("📊 Summary")

# col1, col2, col3 = st.columns(3)

# col1.metric("Total Students", len(df))
# col2.metric("Average %", round(df["Percentage"].mean(), 2))
# col3.metric("Top Score", df["Total"].max())

# # ✅ ALL DATA
# st.subheader("📊 All Students Data")
# st.dataframe(df)

# # ✅ TOPPER (IMPROVED)
# topper = df.loc[df["Total"].idxmax()]

# st.subheader("🏆 Topper")
# st.success(f"{topper['Name']} - {topper['Total']} marks")

# # ✅ TOP 5
# top5 = df.sort_values(by="Total", ascending=False).head(5)

# st.subheader("🔥 Top 5 Students")
# st.dataframe(top5)

# # ✅ CHART
# st.subheader("📈 Chart")
# st.bar_chart(top5.set_index("Name")["Total"])

# # ✅ FAIL STUDENTS (IMPROVED)
# fail = df[df["Percentage"] < 33]

# st.subheader("❌ Fail Students")

# if len(fail) > 0:
#     st.error("Some students failed")
#     st.dataframe(fail)
# else:
#     st.success("No Fail Students 🎉")

import streamlit as st
import pandas as pd

df = pd.read_excel("student_report4.xlsx")

st.title("🎓 Student Dashboard")

# -------------------------------
# 📊 SUMMARY
# -------------------------------
st.subheader("📊 Summary")

col1, col2, col3 = st.columns(3)

col1.metric("Total Students", len(df))
col2.metric("Average %", round(df["Percentage"].mean(), 2))
col3.metric("Top Score", df["Total"].max())

# -------------------------------
# 📊 ALL DATA
# -------------------------------
st.subheader("📊 All Students Data")
st.dataframe(df)

# -------------------------------
# 🏆 TOPPER
# -------------------------------
topper = df.loc[df["Total"].idxmax()]

st.subheader("🏆 Topper")
st.success(f"{topper['Name']} - {topper['Total']} marks")

# -------------------------------
# 🔥 TOP 5
# -------------------------------
top5 = df.sort_values(by="Total", ascending=False).head(5)

st.subheader("🔥 Top 5 Students")
st.dataframe(top5)

# -------------------------------
# 📈 CHART
# -------------------------------
st.subheader("📈 Chart")
st.bar_chart(top5.set_index("Name")["Total"])

# -------------------------------
# ❌ FAIL STUDENTS
# -------------------------------
fail = df[df["Percentage"] < 33]

st.subheader("❌ Fail Students")

if len(fail) > 0:
    st.error("Some students failed")
    st.dataframe(fail)
else:
    st.success("No Fail Students 🎉")

# -------------------------------
# 💾 DOWNLOAD BUTTONS (NEW 🔥)
# -------------------------------
st.subheader("⬇️ Download Reports")

# Full Report
st.download_button(
    label="📥 Download Full Report",
    data=df.to_csv(index=False),
    file_name="student_report.csv",
    mime="text/csv"
)

# Top 5
st.download_button(
    label="📥 Download Top 5 Students",
    data=top5.to_csv(index=False),
    file_name="top5_students.csv",
    mime="text/csv"
)

# Fail Students
st.download_button(
    label="📥 Download Fail Students",
    data=fail.to_csv(index=False),
    file_name="fail_students.csv",
    mime="text/csv"
)