# Student Grading Report (Pencarian Nilai)
<p>I use VS Code for local deploy. This project is how to deploy a website in order to see the final record of the student. Each student need to enter the <b>Course Name, Student ID and Password</b> to see their own report. We create this project to deploy ONSITE into <a href="https://pythonanywhere.com" target="_blank">Pythonanywhere</a>. See <a href="https://adeclintonsitepu.pythonanywhere.com" target="_blank">This Demo</a> for the reference.</p>
<p>
  YouTube video tutorial: <a href="https://youtu.be/5SBoeVgORzo" target="_blank">https://youtu.be/5SBoeVgORzo</a>
</p>

<h2>Cloning the repository</h2>

Clone the repository using the command below :
```bash
git clone https://github.com/adeclintonsitepu/Pencarian-Nilai.git

```

Move into the directory where we have the project files : 
```bash
cd Pencarian-Nilai

```

Create a virtual environment :
```bash
# Let's install virtualenv first
pip install virtualenv

# Then we create our virtual environment
virtualenv envname

```

Activate the virtual environment :
```bash
envname\scripts\activate

```

<div>
Requirements: <br />
<ul>
  <li><bold></b>Python 3.10.*</bold></b> (Type "python --ver" from yor CMD to see your version)</li>
  <li>

```bash
pip install flask

```
    
  </li>
  <li>
    
```bash
pip install gspread

```
    
  </li>
  <li>Give <b>editorservieaccount@website-396012.iam.gserviceaccount.com</b> mail to access your google spreadsheet file</li>
</ul>
</div>

<h2>Running the App</h2>

To run the App, we use :
```bash
python app.py

```

> ⚠ Then, the development server will be started at http://127.0.0.1:5000/
