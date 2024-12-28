# # books/views.py
# from rest_framework.views import APIView
# from rest_framework.response import Response
# from django_elasticsearch_dsl.search import Search
# from .documents import BookDocument
# from .serializers import BookDocumentSerializer

# class BookSearchAPIView(APIView):
#     def get(self, request, *args, **kwargs):
#         query = request.query_params.get('q', '')  # Search query
#         search = BookDocument.search().query("multi_match", query=query, fields=['title', 'author', 'description'])
#         results = search.execute()
#         total = len(results)
#         print(query, " --------------")
#         # Serialize results
#         serializer = BookDocumentSerializer(results, many=True)
#         return Response({ "len": total,"data":serializer.data})




# books/views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from .documents import BookDocument
from .serializers import BookDocumentSerializer

class BookSearchAPIView(APIView):
    def get(self, request, *args, **kwargs):
        query = request.query_params.get('q', '')  # Search query

        # Match all fields specified in `fields` where the query term exists
        search = BookDocument.search().query(
            "multi_match",
            query=query,
            fields=['title', 'author', 'description'],  # Search in these fields
            fuzziness="auto",  # Optional: Enables fuzzy matching for typos
    

        ).extra(size=100)

        # Execute the search query
        results = search.execute()

        # Convert search hits to list of dictionaries
        hits = [hit.to_dict() for hit in results]
        res = {
           
            "len" : len(hits),
             "hit":hits, 
        }
        return Response(res)
