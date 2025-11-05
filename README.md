![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![SQLite](https://img.shields.io/badge/SQLite-07405E?style=for-the-badge&logo=sqlite&logoColor=white)
![License](https://img.shields.io/github/license/Mani-IR/todo-app-streamlit-sqlite?style=for-the-badge)

---


# ToDo App / اپلیکیشن ToDo

A simple task management application (To-Do List) built with Streamlit and SQLite database. This project is designed for Python programming practice and includes basic features such as adding, viewing, editing, deleting, and archiving tasks. It also includes reminders for overdue, today's, and tomorrow's tasks, and an undo feature for the last deleted task.  
یک اپلیکیشن ساده مدیریت وظایف (To-Do List) ساخته‌شده با Streamlit و دیتابیس SQLite. این پروژه برای تمرین برنامه‌نویسی پایتون طراحی شده و قابلیت‌های پایه‌ای مانند اضافه کردن، نمایش، ویرایش، حذف و بایگانی وظایف را دارد. همچنین شامل یادآوری وظایف گذشته، امروز و فردا، و امکان undo برای آخرین وظیفه حذف‌شده است.

## Features / ویژگی‌ها
- **Add new task**: Enter title, description, status (pending, in progress, done) and due date.  
  **اضافه کردن وظیفه جدید**: وارد کردن عنوان، توضیحات، وضعیت (در انتظار، درحال انجام، انجام شد) و تاریخ سررسید.
- **View all tasks**: Display task list in a table using Pandas, with project progress (progress bar) and details of the selected task.  
  **نمایش همه وظایف**: نمایش لیست وظایف در جدول با استفاده از Pandas، همراه با پیشرفت پروژه (progress bar) و جزئیات وظیفه انتخابی.
- **Edit task**: Change title, description, status, and due date of an existing task.  
  **ویرایش وظیفه**: تغییر عنوان، توضیحات، وضعیت و تاریخ سررسید یک وظیفه موجود.
- **Delete task**: Delete a task and store it in the archive table (deleted_tasks) for history (up to 30 recent items).  
  **حذف وظیفه**: حذف وظیفه و ذخیره آن در جدول بایگانی (deleted_tasks) برای نگهداری تاریخچه (حداکثر ۳۰ مورد اخیر).
- **Archive deleted tasks**: Display table of deleted tasks.  
  **بایگانی وظایف حذف‌شده**: نمایش جدول وظایف حذف‌شده.
- **Reminders**: Display overdue, today's, and tomorrow's tasks in the sidebar (up to 3 per category).  
  **یادآوری‌ها**: نمایش وظایف گذشته، امروز و فردا در سایدبار (حداکثر ۳ مورد برای هر دسته).
- **Undo delete**: Ability to restore the last deleted task using session_state in Streamlit.  
  **Undo حذف**: امکان برگرداندن آخرین وظیفه حذف‌شده با استفاده از session_state در Streamlit.
- **SQLite Database**: Data storage in `yek.db` file with `Task` and `deleted_tasks` tables.  
  **دیتابیس SQLite**: ذخیره‌سازی داده‌ها در فایل `yek.db` با جداول `Task` و `deleted_tasks`.

## Live Demo / دموی زنده
[![Open in Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://mani-ir-todo-app-streamlit-sqlite.streamlit.app)

[Click here to try the app online](https://mani-ir-todo-app-streamlit-sqlite.streamlit.app)


## Prerequisites / پیش‌نیازها
- Python 3.8 or higher  
  Python 3.8 یا بالاتر
- Dependencies (in `requirements.txt` file):  
  وابستگی‌ها (در فایل `requirements.txt`):
  ```
  streamlit
  pandas
  sqlite3 (built-in در پایتون)
  ```

## Installation and Setup / نصب و راه‌اندازی
1. **Clone the project**:  
   **کلون کردن پروژه**:
   ```
   git clone <repository URL>
   cd TODO_APP
   ```

2. **Create virtual environment (optional but recommended)**:  
   **ایجاد محیط مجازی (اختیاری اما توصیه‌شده)**:
   ```
   python -m venv env
   source env/bin/activate  # Linux/Mac
   env\Scripts\activate  # Windows
   ```

3. **Install dependencies**:  
   **نصب وابستگی‌ها**:
   ```
   pip install -r requirements.txt
   ```

4. **Run the app**:  
   **اجرای اپ**:
   ```
   streamlit run src/app_streamlit.py
   ```
   The app will open in the browser (usually at http://localhost:8501).  
   اپ در مرورگر باز می‌شود (معمولاً در http://localhost:8501).

## Usage / استفاده
- **Sidebar Menu**: Select options like "Create List", "View All", "Update", "Delete", or "Archive".  
  **منو سایدبار**: انتخاب گزینه‌های "ساخت لیست"، "نمایش همه"، "آپدیت"، "پاک کردن" یا "بایگانی".
- **Create List**: Form to add a new task.  
  **ساخت لیست**: فرم برای اضافه کردن وظیفه جدید.
- **View All**: Task table, project progress, and expander for details.  
  **نمایش همه**: جدول وظایف، پیشرفت پروژه، و expander برای جزئیات.
- **Update**: Select task and edit fields.  
  **آپدیت**: انتخاب وظیفه و ویرایش فیلدها.
- **Delete**: Select task to delete, with undo option.  
  **پاک کردن**: انتخاب وظیفه برای حذف، با گزینه undo.
- **Archive**: Display deleted tasks in a table.  
  **بایگانی**: نمایش وظایف حذف‌شده در جدول.

### Example of Running the App / مثال اجرای اپ
After running, reminders are displayed in the sidebar. Tasks with different statuses are shown with icons and color-coding.  
پس از اجرا، در سایدبار یادآوری‌ها نمایش داده می‌شود. وظایف با وضعیت‌های مختلف با آیکون و رنگ‌بندی نشان داده می‌شوند.

## Project Structure / ساختار پروژه
- `src/app_streamlit.py`: Main Streamlit app file.  
  فایل اصلی اپ Streamlit.
- `db/database.py`: Database class for managing SQLite connection and operations.  
  کلاس Database برای مدیریت اتصال و عملیات SQLite.
- `models/task.py`: Task class for task model (methods: save, get_all, update, delete).  
  کلاس Task برای مدل وظیفه (متدهای save, get_all, update, delete).
- `yek.db`: Database file (automatically created).  
  فایل دیتابیس (به طور خودکار ساخته می‌شود).
- `requirements.txt`: List of dependencies.  
  لیست وابستگی‌ها.
- `README.md`: This file.  
  این فایل.

## Development Notes / نکات توسعه
- **Task Table**: Includes fields id, title, description, status, due_date, created_at.  
  **جدول Task**: شامل فیلدهای id, title, description, status, due_date, created_at.
- **deleted_tasks Table**: For archiving deleted tasks (id, title, description, status, created).  
  **جدول deleted_tasks**: برای بایگانی وظایف حذف‌شده (id, title, description, status, created).
- **Possible Improvements**: Add search, filters, or email integration for reminders.  
  **بهبودهای ممکن**: اضافه کردن جستجو، فیلترها، یا интеграция با ایمیل برای یادآوری.
- **Known Issues**: In the Task model, update_status method only updates title and description (needs fix for status). Use update_task method from Database.  
  **اشکالات شناخته‌شده**: در مدل Task، متد update_status فقط title و description را آپدیت می‌کند (نیاز به اصلاح برای status). از متد update_task در Database استفاده کنید.

#
<br>

Built by [ Mani Ajorloo ] - 2025 / ساخته‌شده توسط [ مانی آجرلو ] - ۲۰۲۵
