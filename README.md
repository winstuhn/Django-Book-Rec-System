# Django-Book-Rec-System
Displays book recommendations based on user input
- Provides users with up to five recommendations per book

- Utilizes this dataset: https://www.kaggle.com/datasets/jealousleopard/goodreadsbooks
    - Contains information on 10k+ books

Utitlized Pandas and Numpy to analyze and aggregate data based on content-based filtering
    - Compared genres and titles of books
    - used cosine similarity to obtain similarity index
    
In order to run application:

- Navigate to page holding manage.py
- Use start command: py manage.py runserver
- Visit url: http://127.0.0.1:8000/
- Ensure that book is inside CSV and input into form

Sample user input:
![image](https://user-images.githubusercontent.com/95652335/219508607-ab9f6c85-1254-426b-bd51-08cdcfb1c97b.png)

Sample response:
![image](https://user-images.githubusercontent.com/95652335/219508640-ec611fa9-9ae5-47a1-bbe0-ef8bffbb0883.png)
