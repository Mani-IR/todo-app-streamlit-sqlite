# ---------------
#  Mani Ajorloo
# ---------------
import streamlit as st
import pandas as pd
from datetime import date, datetime, timedelta
from db.database import Database
from models.task import Task

# --------------------------------------
db = Database()
conn = db.connect()
db.execute("""
CREATE TABLE IF NOT EXISTS Task (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    description TEXT,
    status TEXT DEFAULT 'pending',
    due_date TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)
""")
db.execute("""
CREATE TABLE IF NOT EXISTS deleted_tasks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    description TEXT,
    status TEXT NOT NULL,
    created TEXT NOT NULL
)
""")
db.close()
# --------------------------------------



# --------------------------------------
if "last_deleted_task" not in st.session_state:
    st.session_state["last_deleted_task"] = None
# --------------------------------------


# --------------------------------------
tasks = Task.get_all(db)
today = date.today()
tomorrow = today + timedelta(days=1)
MAX_REMINDERS = 3
overdue_tasks = [t for t in tasks if t[4] and datetime.strptime(t[4], "%Y-%m-%d").date() < today and t[3] != "done"][:MAX_REMINDERS]
today_tasks = [t for t in tasks if t[4] and datetime.strptime(t[4], "%Y-%m-%d").date() == today][:MAX_REMINDERS]
tomorrow_tasks = [t for t in tasks if t[4] and datetime.strptime(t[4], "%Y-%m-%d").date() == tomorrow][:MAX_REMINDERS]
st.sidebar.subheader("⏰ یادآوری تسک‌ها")
if overdue_tasks:
    st.sidebar.warning("❌ تسک‌های گذشته:")
    for t in overdue_tasks:
        st.sidebar.markdown(f"- {t[1]} | سررسید: {t[4]}")
if today_tasks:
    st.sidebar.info("🟢 تسک‌های امروز:")
    for t in today_tasks:
        st.sidebar.markdown(f"- {t[1]} | سررسید: {t[4]}")
if tomorrow_tasks:
    st.sidebar.info("🟡 تسک‌های فردا:")
    for t in tomorrow_tasks:
        st.sidebar.markdown(f"- {t[1]} | سررسید: {t[4]}")
# --------------------------------------

# --------------------------------------
st.set_page_config(page_title="ToDo App", layout="centered")
st.title("📝 ToDo App (پروژه / تمرینی)")
st.subheader("مدیریت کارها با داشتن دیتابیس ")
# --------------------------------------


# ----------------------------------------------------------------------------
menu = ["ساخت لیست", "نمایش همه", "آپدیت", "پاک کردن", "بایگانی"]
choice = st.sidebar.selectbox("Menu", menu)
if choice == "ساخت لیست":
    st.header("ساخت لیست")
    with st.form("add_task_form", clear_on_submit=True):
        title = st.text_input("موضوع")
        desc = st.text_area("توضیحات")
        status = st.selectbox("وضعیت", ["در انتظار", "درحال انجام", "انجام شد"])
        due_date = st.date_input("تاریخ", date.today())
        submitted = st.form_submit_button("✅ اضافه کردن")
        if submitted:
            if title.strip() == "":
                st.error("عنوان نمی‌تواند خالی باشد.")
            else:
                db.connect()
                db.add_task(title, desc, status, due_date.strftime("%Y-%m-%d"))
                db.close()
                st.success(f"لیست <{title}> با موفقیت ساخته شد ✅")
# --------------------------------------
elif choice == "نمایش همه":
    st.header("📋 همه کارها")
    tasks = Task.get_all(db)
    if tasks:
        tasks_df = [t[:5] for t in tasks] 
        df = pd.DataFrame(tasks_df, columns=["آیدی", "موضوع", "توضیحات", "وضعیت", "تاریخ"])
        st.dataframe(df)
        total_tasks = len(tasks)
        done_tasks = len([t for t in tasks if t[3].lower() == "انجام شد"])
        progress = done_tasks / total_tasks if total_tasks > 0 else 0
        st.subheader("📊 درصد تکمیل پروژه")
        st.progress(progress)
        st.subheader("🔍 جزئیات لیست انتخابی")
        task_options = [f"{t[1]} ({t[3]})" for t in tasks]
        selected_task = st.selectbox("یک لیست را انتخاب کنید:", task_options)
        task = [t for t in tasks if f"{t[1]} ({t[3]})" == selected_task][0]
        with st.expander(f"{task[1]} ({task[3]})"):
            status = task[3].lower()
            if status == "انجام شد":
                status_color = "#000000FF"
                status_icon = "✅"
                status_text = "انجام شده"
            elif status == "درحال انجام":
                status_color = "#000000FF"
                status_icon = "⏳"
                status_text = "در حال انجام"
            else:
                status_color = "#3E3636FF"
                status_icon = "📝"
                status_text = "در انتظار"
            st.markdown(
                f"<div style='background-color:{status_color}; padding:10px; border-radius:8px;'>{status_icon} وضعیت: {status_text}</div>",
                unsafe_allow_html=True
            )
            st.markdown(f"**عنوان:** {task[1]}")
            st.markdown(f"**توضیح:** {task[2] if task[2] else 'ندارد'}")
            st.markdown(f"**وضعیت:** {task[3]}")
            st.markdown(f"**تاریخ تغییر:** {task[4]}")
            st.markdown(f"**تاریخ ایجاد:** {task[5]}")
# --------------------------------------
elif choice == "آپدیت":
    st.header("✏️ تغییر جزییات")
    tasks = Task.get_all(db)
    if tasks:
        task_titles = [t[1] for t in tasks]
        selected_task = st.selectbox("انتخاب لیست", task_titles)
        task = [t for t in tasks if t[1] == selected_task][0]
        new_title = st.text_input("موضوع", task[1])
        new_desc = st.text_area("توضیحات", task[2])
        new_status = st.selectbox("وضعیت", ["در انتظار", "درحال انجام", "انجام شد"],
        index=["در انتظار", "درحال انجام", "انجام شد"].index(task[3]))
        new_due = st.date_input("تاریخ", datetime.strptime(task[4], "%Y-%m-%d").date() if task[4] else date.today())
        if st.button("آپدیت لیست"):
            db.update_task(task[0], new_title, new_desc, new_status, new_due.strftime("%Y-%m-%d"))
            st.session_state["update_msg"] = f"لیست '{new_title}' با موفقیت بروزرسانی شد ✅"
            st.rerun()
        if "update_msg" in st.session_state:
            st.success(st.session_state["update_msg"])
            del st.session_state["update_msg"]
    else:
        st.info("هیچ تسکی برای آپدیت وجود ندارد.")
# --------------------------------------
elif choice == "پاک کردن":
    st.header("🗑️ پاک کردن لیست")
    tasks = Task.get_all(db)
    if tasks:
        task_titles = [t[1] for t in tasks]
        selected_task = st.selectbox("انتخاب تسک برای حذف", task_titles)
        if st.button("پاک کردن"):
            task = [t for t in tasks if t[1] == selected_task][0]
            st.session_state["last_deleted_task"] = {
                "title": task[1],
                "description": task[2],
                "status": task[3],
                "due_date": task[4],
                "created_at": task[5]
            }
            db.connect()
            db.execute(
                "INSERT INTO deleted_tasks (title, description, status, created) VALUES (?, ?, ?, ?)",
                (task[1], task[2], task[3], task[5])
            )
            db.delete_task(task[0])
            db.close()
            st.session_state["delete_msg"] = f"لیست '{task[1]}' با موفقیت پاک شد "
    # واسع برگردون دن لیستی که پاکش کردم
    if "delete_msg" in st.session_state:
        st.warning(st.session_state["delete_msg"])
        del st.session_state["delete_msg"]
    last_task = st.session_state.get("last_deleted_task")
    if last_task:
        if st.button("↩️برگردودن لیست"):
            db.connect()
            db.add_task(last_task["title"], last_task["description"], last_task["status"], last_task["due_date"])
            db.close()
            st.success(f"برگشت!'{last_task['title']}' لیست ")
            st.session_state["last_deleted_task"] = None
# --------------------------------------
elif choice == "بایگانی":
    st.header("🗂️ بایگانی کارها(تعداد نگهداری 30)")
    conn = db.connect()
    try:
        df_deleted = pd.read_sql_query("SELECT * FROM deleted_tasks ORDER BY id DESC", conn)
    except pd.io.sql.DatabaseError:
        st.warning("🛑 جدول deleted_tasks وجود ندارد!")
        df_deleted = pd.DataFrame()
    conn.close()
    st.dataframe(df_deleted)

