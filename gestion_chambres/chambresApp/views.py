# # chambresApp/views.py
# from django.http import JsonResponse
# import requests

# def informations_chambres(request):
#     search_city = request.GET.get('search_city')
#     check_in = request.GET.get('check_in')
#     check_out = request.GET.get('check_out')
#     currency = request.GET.get('currency')
#     token = request.GET.get('token')

#     api_url = f"/hotel/api/v2/cache.json?location={search_city}&checkIn={check_in}&checkOut={check_out}&currency={currency}&limit=100&token={token}"

#     try:
#         response = requests.get(api_url)
#         response.raise_for_status()
#         data = response.json()
#         return JsonResponse(data, safe=False)
#     except requests.exceptions.RequestException as e:
#         return JsonResponse({'error': str(e)}, status=500)
