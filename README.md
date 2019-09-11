# Product Rating System
Let's say a customer rents 5 different products (furniture) from CasaOne. We need to capture the ratings from the customer for all of these products after customer starts using the furniture. We also need to display the ratings on the website next to the product. This product rating feature is similar to product ratings on Flipkart and Amazon


Here is what you can submit as part of the assignment

- How will you design the flow? Architecture diagram with an explanation will help. What will the user do and what will the system do

- Code for API to fetch ratings for the product. This should also return average product rating and count for individual ratings




## Steps to Buid  
You need to have Python3 and Pip 3 for this to run  
```
cd ratingSystem
virtualenv -p python3 venv
source venv/bin/activate
pip install -r requirements.txt
python manage.py runserver  
``` 
## APIs  
```
baseurl=http:127:0.0.1:8000 
```

## Get All Products     
Method = (get)
```
{{baseurl}}/api/products
```

## Get A Product's Rating
Method = (get)
```
{{baseurl}}/api/products/{{product_id}}
```
