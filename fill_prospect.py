import json

data = {
  "places": [
    {
      "brand": "Coffee Shop",
      "name": "Olmsted",
      "address": "659 Vanderbilt Ave, Brooklyn, NY 11238"
    },
    {
      "brand": "Restaurant",
      "name": "Faun",
      "address": "606 Vanderbilt Ave, Brooklyn, NY 11238"
    },
    {
      "brand": "Bar",
      "name": "Weather Up",
      "address": "589 Vanderbilt Ave, Brooklyn, NY 11238"
    },
    {
      "brand": "Bookstore",
      "name": "Unnameable Books",
      "address": "615 Vanderbilt Ave, Brooklyn, NY 11238"
    },
    {
      "brand": "Coffee Shop",
      "name": "Little Skips East",
      "address": "1643 Broadway, Brooklyn, NY 11207"
    }
  ]
}

with open("data/prospect_heights.json", 'w') as f:
    json.dump(data, f, indent=2)

print("Updated data/prospect_heights.json")
