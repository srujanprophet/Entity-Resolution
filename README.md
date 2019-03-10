# Entity-Resolution

## Description
This is an approach to solving the entity resolution problem in NLP. We are given three inputs of entity and a search query,
and we want to find the occurrences of the entity when the query is searched in google.

## Installation
1. Ensure that you have python installed on your system, if not, [Install python first](https://www.python.org/downloads/)   
2. Install virtualenv,create and activate new environment
  ``` pip install virtualenv
      virtualenv venv
      source venv/bin/activate
  ```
3. Install Dependencies
  ``` pip install -r requirements.txt
  ```
  
## Usage
- Run the code :   `python entity_res.py `
- Provide the name, location and organization along with the search query.
- The output will be all the links retrieved from google search that contain the entity mentions.

