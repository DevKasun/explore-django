from django.http import JsonResponse

def products_list(request):
    products = [
        {'id': 1, 'product_name': 'iPhone 12', 'category': 'Smartphone'},
        {'id': 2, 'product_name': 'Samsung Galaxy S21', 'category': 'Smartphone'},
        {'id': 3, 'product_name': 'Google Pixel 5', 'category': 'Smartphone'}
    ]
    return JsonResponse({'products': products})
