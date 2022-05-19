# Inventory Tracker
## Instructions
To view this application in [Replit](https://replit.com/@davidalliger/inventorytracker), first click the RUN button at the top of the page. Then click <a href="https://inventorytracker.davidalliger.repl.co/" target="_blank">here</a> to view the app in a separate window. You can click on links to navigate through the app, and buttons to add, edit or delete items and warehouses.
## Description
This is a simple inventory tracker web application. Users can add items, edit items, delete items, view items in a list, and inspect the details of a particular item. 
They can also add warehouses, edit warehouses, delete warehouses, view warehouses in a list, inspect the details of a particular warehouse, and assign items to warehouses...
as long as they fit! A warehouse's remaining capacity (current capacity) will update as items are added and/or removed, and will be displayed on the warehouse detail page.
## Technologies
This application utilizes the following technologies:
- PostgreSQL
- Python
- Flask
- Flask-SQLAlchemy
- Alembic
- Jinja
## Implementation
While working on this application, I ran into a number of interesting challenges. When users create items, I wanted them to be able to assign those items to specific warehouses by selecting from a dropdown menu. I also wanted to give them the option to allow items to remain unassigned to a warehouse. This posed a problem at first, because even though an item's warehouse_id column is nullable, I wasn't sure at first what value to assign the "Unassigned" option from the dropdown. I realized that I needed to insert NULL into the column, but I also wanted the form to pass validation, so I needed the value to be a number. I ended up going with zero, since I knew that wouldn't actually be a valid warehouse id. Then, inside the post route for warehouses, I could check to see if the warehouse_id is '0' and, if so, replace that with null. This worked quite well.
![inventory-4](https://user-images.githubusercontent.com/88861592/169152261-9b6ff2d3-55bb-4f94-902a-2056e33f3511.PNG)
![inventory-3](https://user-images.githubusercontent.com/88861592/169152292-0a8c9da8-9a5f-4e20-9f79-3a596a12e2a8.PNG)
I also created a custom validator that calculates the item's volumen and the selected warehouse's remaining capacity and raises a validation error if the item will not fit in the selected warehouse:
![inventory-1](https://user-images.githubusercontent.com/88861592/169152765-ff940ac5-78e0-44a4-8016-990811fd1df9.PNG)
## Screenshots
![inventory-5](https://user-images.githubusercontent.com/88861592/169153600-02a27bb6-edf2-4ea5-a8e5-7725b5436643.PNG)
![inventory-7](https://user-images.githubusercontent.com/88861592/169153681-aa066c4a-576a-42b9-b157-56fb2888f29d.PNG)
![inventory-6](https://user-images.githubusercontent.com/88861592/169153728-61a28653-0cf9-4173-89cd-cdc90c9b7dbe.PNG)
## Possible future features
In the future, it might be interesting to make category its own table in the database, so that users can create, edit, and delete categories as needed. It also might be neat to add a shipments feature, so that users can assign items to shipments, and warehouse inventory would be adjusted automatically.
