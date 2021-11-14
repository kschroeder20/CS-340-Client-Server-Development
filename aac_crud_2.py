import datetime
import json
from bson import json_util
from pymongo import MongoClient
from bson.objectid import ObjectId
from bson.json_util import dumps, loads


class AnimalShelter(object):
    """ CRUD operations for Animal collection in MongoDB """

    def __init__(self, username, password):
        try:
            # Initializing the MongoClient. This helps to 
            # access the MongoDB databases and collections.             
            self.client = MongoClient('mongodb://%s:%s@localhost:43363/?authMechanism=DEFAULT&authSource=AAC' % (username, password))
            self.database = self.client['AAC']
            self.collection = self.database['animals']
        except:
            return{'Success': 'false'}

    # Complete this create method to implement the C in CRUD.
    def create(self, data):
      try:
        if data is not None:
            # insert method
            self.collection.insert_one(data)
            message = {'Success' : 'true'}
        else:
            message = {'Success': 'false'}

        # print json response
        json_data = dumps(message, indent=2)
        parsed = json.loads(json_data)
        return json.dumps(parsed, indent=4, sort_keys=True)
      except:
        return {'Error', 'something went wrong'}

    # Read method to implement the R in CRUD. 
    def read(self, data):
        return "Made it"
        try:
            if data is not None:
                if self.collection.count_documents(data) != 0:
                    # Returns cursor of all entries with specified data
                    results_cursor = self.collection.find(data)
                    error_message = None
                    # Print out the data
                    json_data = dumps(list(results_cursor), indent=2)
                    parsed = json.loads(json_data)
                    return json.dumps(parsed, indent=4, sort_keys=True)               
                else:
                    error_message = {'Error': 'No results found'}
            else:
                results_cursor = self.collection.find()
                error_message = None
                # Print out the data
                json_data = dumps(list(results_cursor), indent=2)
                parsed = json.loads(json_data)
                return json.dumps(parsed, indent=4, sort_keys=True) 

            if error_message is not None:
                json_data = dumps(error_message, indent=2)
                parsed = json.loads(json_data)
                return json.dumps(parsed, indent=4, sort_keys=True)
        except Exception as e:
            return {'Error', str(e)}
    
    # Updates record in database
    def update(self, search_data, new_data):
      # Handle empty params
      if search_data is None:
        return {"Error", "search data parameter is empty"}
      if new_data is None:
        return {"Error", "new data parameter is empty"}
      # If at least one record exists, update all matching records
      # Else, return error message
      try:
        num_of_records = self.collection.count_documents(search_data)
        if num_of_records != 0:
          self.collection.update_many(search_data, {"$set": new_data})
          # Converting reuslts to the JSON
          records_updated = {'Records Updated': num_of_records}
          json_data = dumps(records_updated, indent=2)
          parsed = json.loads(json_data)
          return json.dumps(parsed, indent=4, sort_keys=True)
        else:
          return 'Error: record doesn\'t exist with entered search data'
      except:
        return {'Error', 'something went wrong'}

    # Deletes record in database
    def delete(self, search_data):
      # Handle empty params
      if search_data is None:
        return {'Error', 'search data parameter is empty'}
      try:
        # Find records
        num_of_records = self.collection.count_documents(search_data)
        if num_of_records != 0:
          self.collection.delete_many(search_data)
          # Converting reuslts to the JSON
          records_deleted = {'Records Deleted': num_of_records}
          json_data = dumps(records_deleted, indent=2)
          parsed = json.loads(json_data)
          return(json.dumps(parsed, indent=4, sort_keys=True))
        else:
          return {"Error", "record doesn't exist with entered search data"}
      except:
        return {'Error', 'something went wrong'}
    
    def readAll(self, data):
        if not data:            
            results_cursor = self.collection.find({},{'_id':0})
        else:
            results_cursor = self.collection.find({ 'breed': { '$in': data['breeds'] }, 'sex_upon_outcome': data['sex'], 'age_upon_outcome_in_weeks' : { '$gt': data['young_week'] }, 'age_upon_outcome_in_weeks' : { '$lt': data['old_week'] } },{'_id':0})    
        
        return results_cursor

