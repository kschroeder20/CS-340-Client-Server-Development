# CS-340-Client-Server-Development

#### How do you write programs that are maintainable, readable, and adaptable? Especially consider your work on the CRUD Python module from Project One, which you used to connect the dashboard widgets to the database in Project Two. What were the advantages of working in this way? How else could you use this CRUD Python module in the future?

Keeping programs maintainable, readable, adaptable mainly comes down to keeping a program simple. The methods of the application should be well-commented and have logical naming conventions. Methods should be kept as short as possible and as simple as possible so that it's easy for an outsider to determine what the method accomplishes. The CRUD module was a great example of where methods had a singular purpose and were kept short. I'd use more of the CRUD methods in the future like create, update, and delete.

#### How do you approach a problem as a computer scientist? Consider how you approached the database or dashboard requirements that Grazioso Salvare requested. How did your approach to this project differ from previous assignments in other courses? What techniques or strategies would you use in the future to create databases to meet other client requests?

I tried to keep my callback methods on the dashboard and the CRUD methods as flexible as possible. For example, I handled every possible parameter that could be sent to the readAll method of my CRUD module. I did a lot of thinking on this last project in particular about how a user could potentially break the system. I made sure to add error handling so that the entire program doesn't completely crash. I'd make sure to be as diligent about error handling in the future.

#### What do computer scientists do, and why does it matter? How would your work on this type of project help a company, like Grazioso Salvare, to do their work better?

Data analytics is massively important to a company like Grazioso Salvare. However, numbers are only useful if people can read them and customize them to satisfy their questions. My dashboard allows the employees to do just that and there is a lot of potential to expand this dashboard to allow the viewers to gain quick insights.
