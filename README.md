


FOR DEPLOYMENT THE Chunkr-Backend IS THE MAIN FOLDER, ALL THE FRONTEND HAS BEEN RENDERED THROUGH TEMPLATING IN THE BACKEND FOLDER

## Run locally
​
If you want to run locally, then you can use the following commands on your machine:
​
​

Clone the project
```
  git clone https://github.com/zuri-training/Chunk-File-Team-47.git
```
​
Go to the project directory
```
  cd Chunk-File-Team-47
```
Go to the backend directory
```
  cd Chunkr-Backend
```
​
Create a Virtual Environment 
```
python -m venv env
```
​
Activate Virtual Environment
```
env\scripts\activate
```
​
Install Dependencies
```
  pip install -r requirements.txt
  or
  pip install django django-crispy-forms
  then
  pip install crispy-bootstrap5
  pip install pandas
```
​

make migrations
```
python manage.py makemigrations chunkrio
```
​
Migrate the database
```
python manage.py migrate
```
​
create superuser 
```
python manage.py createsuperuser
```
​
Create a new branch to work with
```
git branch <new-branch>
```
​
switch to the new branch to make changes
```
git checkout <new-branch>
```
​
Finally, Start The Server.
```
python manage.py runserver
```















Chunkr.io
This is a platform that accepts CSV or JSON large files, and break them into smaller bits. Read below for better understanding. ⬇


DOCUMENTATION🚀

Introduction

A CSV file, as the name implies, typically separates information using commas. It's a way to exchange structured information, like the contents of a spreadsheet, among programs that can't necessarily talk to one another directly, While JSON is an open standard file format and data interchange format that uses human-readable text to store and transmit data objects consisting of attribute–value pairs and arrays (or other serializable values). These files exist in large formats in terms of size and properties, so we propose & created the flexibility of splitting into smaller sections to enable users of csv and json file work smarter and better, digest the informations below as we unleash the technical-know-how of this product and break down its complexities in simpler terms.

HOW IT WORKS
1. After signing up as a user, on your dashboard, you get to choose the type of file you want to split, either JSON or CSV.
2. The splitter takes in the uploaded file, split it asynchronously and return it back to the dashboard.
3. Users can either choose to save or download the chunked files. If they save it files will be stored in the database.

 Note: you have to be an authenticated user to use this product.😀

HOW TO USE
1. Sign up/ Create an account
2. Navigate to your dashboard
3. Click on the “Split” button and select the type of file you want to split
4. Upload your file and choose the number of files you want to split it to and split.
5. The splitter is going to return your chunked files to your dashboard
6. Download and use or save to download later.🙂

FAQ’s

1. What is Chunkr.io?

Chunkr.io is the easiest way to split CSV and JSON files into multiple pieces. You upload a file, specify how you want it chunked up, and boom! We give you the chunks you asked for.

2. Why does this exist?

To provide a clean, efficient, secure, simple way to split CSV and JSON files.

3. Can anybody access it?

Only authenticated users can access the splitting tool by signing up.

4. Do I need to sign up or create an account?

Yes. You need to create an account to let you split, track, save and download your file splits.

5. I want to do things with a CSV or JSON file or any other file that you don't do?

Contact us! Send us a message, or email us at team47@chunkr.io. We LOVE feature requests.

6. How long is my data retained?

Our default data retention policy is for all content (uploaded files and output files) to be deleted few mins after the split is complete. But you can choose to save it too.

7. I have another question not covered here?

Contact us! Send us a message here, or email us at team47@chunkr.io

PRESENTATION LINK
https://drive.google.com/file/d/1sEwix7vV4uR4hH5LHxX_bNMeaFReoiaI/view?usp=sharing
https://i4gxzuriprojectphase.slack.com/files/U03NZFL5FKR/F03RQK82A76/team47_chunk_file.mp4


