from django.shortcuts import render
from cart.models import Product
from rest_framework.response import Response
from rest_framework.views import APIView


# Create your views here.


def index(request):
    product = Product.objects.all()
    return render(request, 'index.html',{'product_list':product})


def cart(request):
    try:

        product_data = request.session['product_data']
    except Exception as error:
        product_data = {}
    print(product_data)
    product_list = {}
    for product in product_data:
        print(product_data[product]['product_name'])
        total_price = product_data[product]['price'] * int(product_data[product]['qty'])
        product_data[product]['total']= total_price
    return render(request,'cart.html', {'product_list':product_data})

class Addtocart(APIView):
    "this method is used for add product to cart"
    def post(self, request):
        data = request.data
        total = 0
        status = 1
        try:

            product_data = request.session['product_data']
        except Exception as error:
            product_data = {}
        
        msg = 'Product added to cart'
        if 'product_id' in data and data['product_id'] != '':
            print('helllo')
            
            if data['product_id'] in product_data:
                if 'product_qty' in data:
                    qty = int(data['product_qty'])
                else:
                    qty = product_data[data['product_id']]['qty'] + 1
                total = product_data[data['product_id']]['price'] * qty
                product_data[data['product_id']]['qty'] = qty
                if qty == 0:
                        del product_data[data['product_id']]
                        status = 2
                        msg = 'Product remove from cart'
            else:
                product_detail = Product.objects.get(id=data['product_id'])

                product_data[data['product_id']] = {
                    'product_name' : product_detail.product_name,
                    'category' : product_detail.category,
                    'subcategory' : product_detail.subcategory,
                    'price' : product_detail.price,
                    'desc' : product_detail.desc,
                    'id' : product_detail.id,
                    'qty': 1
                }
                # product_data[data['product_id']]['qty'] = 1
                
        request.session['product_data'] = product_data
        print(product_data)
        return Response({"message":msg, 'error':0, 'total':total, 'status':status})
        
        
        
        
        