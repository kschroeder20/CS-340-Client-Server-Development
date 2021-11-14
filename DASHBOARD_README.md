# CS-340-Client-Server-Development

## Functionality
Grazioso Salvare required 3 charts for their dashboard: a data table, a geolocation chart, and a chart of my choosing where I used a vertical bar chart.

**Starting state picture:**
<img width="1498" alt="Screen Shot 2021-11-12 at 4 37 19 PM" src="https://user-images.githubusercontent.com/46656090/141660297-c7e58296-3fcf-42b2-b03d-00021600c747.png">

All of the charts had to be filterable by rescue type so that Grazioso Salvare could quickly analyze the dogs available for specific rescue missions. Screenshots below display what the charts look like with each filter. If a user clicks the ‘x’ at the far right of the filter bar, the charts will reset to the starting state.

**Water Rescue Filter:**
<img width="1447" alt="Screen Shot 2021-11-12 at 4 37 40 PM" src="https://user-images.githubusercontent.com/46656090/141660316-039d0f0b-a3c8-45a3-9a3d-c0f57b783403.png">

**Mountain or Wilderness Rescue Filter:**
<img width="1467" alt="Screen Shot 2021-11-12 at 4 37 51 PM" src="https://user-images.githubusercontent.com/46656090/141660325-ece7d4d4-129c-4463-b890-d19eab167d42.png">

**Disaster or Individual Tracking Filter:**
<img width="1502" alt="Screen Shot 2021-11-12 at 4 38 01 PM" src="https://user-images.githubusercontent.com/46656090/141660338-7002f3c0-9d77-4431-986f-c1e8b911eb9b.png">

## Tools
#### MongoDB
MongoDB’s document model allowed me to store any kind of data structure and easily retrieve the information. I was able to store each animal as a dictionary in the database that can have different attributes for each animal. Mongo also interacts with python easily using the PyMongo library. This library allowed me to easily connect a CRUD API written in python with our MongoDB database.

#### Dash
I used the Dash framework to implement my controller and view structure of the dashboard. Dash allows users to implement callback functions that fire on a specific action and act on the input data (controllers). These functions will then communicate with the front end (view) to change the charts accordingly.

#### Jupyter Notebook
I used Jupyter Notebook as my IDE for this project because it interprets python code very easily and properly idsplays the charts.

[PyMongo](https://pymongo.readthedocs.io/en/stable/)

[MongoDB](https://www.mongodb.com/)

[Dash](https://plotly.com/dash/)

[Jupyter Notebook](https://jupyter.org/)

## Production Steps
1. I imported the sample data into a MongoDB database called ‘AAC’ and a collection called ‘animals.’
2. Created a user that had read and write credentials to the AAC database.
3. Created a CRUD application in python with properly functioning create, read, update, and delete functions.
4. Using Jypter Notebook I created a .ipynb file to create the dashboard.
5. Connected the dashboard to our CRUD API and our database with the user credentials set up in step 2.
6. Used the Dash framework to build the basic layout components such as a header, unique identifier, and logo. 
7. Used the Dash framework to create 3 empty charts: a data table with filter options, a geolocation chart, and a horizontal bar chart. I used the MongoDB connection and the readAll method in my CRUD API to pull all data from the database, creating the initial state.
8. Then, I used Dash callback functions to respond to a filter selection and edit the charts to filter for client-requested specifications. The callbacks would take in the input of the filter choice and query the database using the readAll method in my CRUD API.

## Challenges
My biggest challenge was learning how to debug in Jupyter Notebook. I am used to programming in systems that have easily-accessible error logs that document anything that would prevent the system from running. Jupter Notebook has that functionality, but it took me a while to find it. My code would run, but filters wouldn’t work because of a bug that was unrelated to the filters. The SNHU-provided way to see error logs didn’t work for me for some reason. I searched on Google and found out that I could access the logs through Jupyter Lab. Once I was able to track down the error logs, I was able to move much faster in the development process.

## CRUD API
To view more infomration about the CRUD API used in this project, please download the [project README](https://github.com/kschroeder20/CS-340-Client-Server-Development/files/7532847/Animals.CRUD.Module.README.1.docx)

