"""Provides untility classes"""


class MongoQuery:
    """Utility class used with mongo db for ease of querying."""

    def __init__(self, collection):
        self.collection = collection

    def get_by_name(self, name_input):
        """Search database for strain by name"""

        query_results = []
        query = self.collection.find(
            {"Name": {"$regex": f".*{name_input}.*"}}, {"_id": None})

        for result in query:
            if result not in query_results:
                query_results.append(result)

        return query_results

    def get_by_type(self, type_input):
        """Search database for strain by type(indica, hybrid, sativa)"""

        query_results = []
        query = self.collection.find(
            {"Type": {"$regex": f".*{type_input}.*"}}, {"_id": None})

        for result in query:
            if result not in query_results:
                query_results.append(result)

        return query_results

    def get_by_effect(self, effect_input):
        """Search database for strain by effects"""

        query_results = []
        query = self.collection.find(
            {"Effects": {"$regex": f".*{effect_input}.*"}}, {"_id": None})

        for result in query:
            if result not in query_results:
                query_results.append(result)

        return query_results

    def get_by_flavor(self, flavor_input):
        """Search database for stain by flavor"""

        query_results = []
        query = self.collection.find(
            {"Flavors": {"$regex": f".*{flavor_input}.*"}}, {"_id": None})

        for result in query:
            if result not in query_results:
                query_results.append(result)

        return query_results
