# Uni Survival Kit - Flask Web Application

A web-based platform developed using Flask to help university students discover and explore the best campus spots for studying, dining, relaxing, and taking photos.

The group set out to create an application that would ease the transition to university life for first-year students. The Uni Survival Kit helps students discover ideal study spots that are quiet, food places that offer great value, picture-worthy locations with the best atmosphere, and university organizations with welcoming communities. Users can also leave their own reviews, rate locations on factors such as accessibility, crowdedness, value, and overall experience, and comment on specific spots.

We hope this becomes a valuable tool for students at the University of Western Australia, making it easier to explore both the campus and the wider Perth area.
---

## 📁 Project Structure

```
CITS3403/
├── app.py
├── config.py
├── exts.py
├── forms.py
├── models.py
├── requirements.txt
├── static/
├── templates/
├── BluePrint/
├── migrations/
├── project_tests/
│   ├── selenium_tests/
│   └── unit_tests/
└── README.md
```

---

## 🚀 How to Run the Application

### 1. Clone the Repository
```bash
git clone (https://github.com/undergraduateuwa/CITS3403)

```


### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Run the Application
```bash
python app.py
```

Visit the app in your browser: [http://127.0.0.1:5000/](http://127.0.0.1:5000/)

---

## 🧪 Running Tests

This project includes both unit tests and Selenium-based UI tests.
Note: This project was tested on macOS. The selenium runs right on macOS. 

To run unit tests:
```bash
python -m unittest discover project_tests/unit_tests
```

To run Selenium tests:
```bash
python -m unittest discover project_tests/selenium_tests
```

### Platform Compatibility

All unit tests were successfully run on both **macOS** and **Windows** without any issues.

However, **Selenium tests were only executed on macOS** due to platform-specific constraints. In particular, the following line was required on macOS to avoid a `multiprocessing` error:

```python
multiprocessing.set_start_method("fork")
```

This resolves the error:

```
AttributeError: Can't pickle local object 'Flask.__init__.<locals>.<lambda>'
```

The `"fork"` start method is only supported on macOS, which is why the Selenium tests are not compatible with Windows without modification.
---

## ✨ Key Features

- 🧑‍🎓 User Registration & Login
- 🗺️ Interactive campus spot browsing
- ❤️ Like, collect, and comment on locations
- 🏆 Awards page: best-reviewed spots for Study, Grub, Snap, and Fun
- 👥 Friend request and social profile system
- 📊 Like trends visualized with charts
- ✅ Complete test coverage (unit & functional tests)

---

## 🗃️ Database

- Uses SQLite (`u_pay.sqlite3`) for simplicity

---

---

## 👨‍💻 Authors

Name	         Student ID	    github
Johen Ciu	     24369572	      Purplesun1989
Johan llagan	 23832843       jcarlo-mabini
Layla V.	     24230713       laylaVanStaden
