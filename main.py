# Smart home will accomplish station crafting dynamically, and will then dynamically set prices on each sale when open orders are available.
import requests


# Check if refuel needs to happen. Purchase and stock fuel if necessary.
def refuel_check():
    pass
    # Simple true/false check.
    # If true, buy a fuel can and place in the generator.
    # If false, do nothing.

# Check API for best station craft to focus on.
def update_station_craft(query):
    pass
    response = requests.post('https://tarkov-tools.com/graphql', json={'query': query})
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception("Query failed to run by returning code of {}. {}".format(response.status_code, query))
    # Returns the most profitable recipe at the designated station

# Check Stations if they are busy or finished.
def station_check(station_name):
    pass
    # Return boolean

# Using a dictionary, we will store all craft results as a key, then pair the ingredients as values.
def craft_start(craft_name):
    # Will acquire materials and start a craft. 
    pass


# Calculate and display profit_per_hour as program is running.
def profit_per_hour():
    # Calculate profit based on conditions to be determined by testing.
    pass
    # Return profit per hour
  
# Simple janitorial function, move all crafted items to a designated junkbox. Will likely run on a timer as a catch-all to keep top of stash clear.
def move_to_junkbox():
    pass

# From our junkboxes, pull out the requisite items and make a sell posting based on current prices. *args allows for dynamic number of params to pass to it. Will likely make it fill orders until a) the list of orders runs out, or b) no more orders can be put up. Will look deeper into this functionality.
def flea_sell_orders(*args):
    pass


# Logic to execute our functions.
if __name__ == "__main__":
    print('Placeholder, nothing implemented.')

    new_query = """
{
    itemsByName(name: "m995") {
        id
        name
        shortName
        basePrice
    }
}
"""

    result = update_station_craft(new_query)
    print(result)