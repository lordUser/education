from django.http import HttpResponse
from django.db import connection
import logging


logger = logging.getLogger(__name__)


class QueryCountDebugMiddleware(object):
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):

        response = self.get_response(request)
        if response._content_type_for_repr.find('text/html') > 0: 
            if response.status_code == 200:
                total_time = 0

                for query in connection.queries:
                    query_time = query.get('time')
                    if query_time is None:
                        query_time = query.get('duration', 0) / 1000
                    total_time += float(query_time)

                querycount = '\n {} queries run, total {} seconds\n'.format(len(connection.queries), total_time)
                body = response.rendered_content.find("</body>")
                if body > 0:
                    start_content = response.rendered_content[:body]
                    end_content = response.rendered_content[body:]
                    content = start_content + querycount + end_content
                    response = HttpResponse(content)

        return response
