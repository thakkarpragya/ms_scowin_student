# from django.shortcuts import render,HttpResponse
# from django.http import JsonResponse

# # Create your views here.

# from health_check.views import MainView
# class HealthCheckCustomView(MainView):

#     def get(self, request, *args, **kwargs):
#         plugins = []
#         # print("error        =>   " + self)
#         status = 500 if self.errors else 200 # needs to be filled status you need
#         # ...
#         if 'application/json' in request.META.get('HTTP_ACCEPT', ''):
#             return self.render_to_response_json(plugins, status)
#         return self.render_to_response(plugins, status)
#     def render_to_response(self, plugins, status): # customize HTML output
#         return HttpResponse('HEALTHY' if status == 200 else 'NOT HEALTHY', status=status)
#     def render_to_response_json(self, plugins, status): # customize JSON output
#         return JsonResponse(
#     {str(p.identifier()): 'HEALTHY' if status == 200 else 'NOT HEALTHY' for p in
#      plugins},
#     status=status
# )