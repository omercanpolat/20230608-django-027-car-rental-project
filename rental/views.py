from django.shortcuts import render, HttpResponse, get_object_or_404
from rest_framework.response import Response
from .models import Car, Customer, Reservation
from .serializers import CarSerializer, CustomerSerializer, ReservationSerializer
from rest_framework import status
from rest_framework.decorators import api_view


def home(request):
    return HttpResponse('<h1>API Page</h1>')

@api_view(['GET', 'POST'])
def car_list(request):
    if request.method == 'GET':
        cars = Car.objects.all()
        serializer = CarSerializer(cars, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = CarSerializer(data=request.POST)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def car_detail(request, pk):
    car = get_object_or_404(Car, pk=pk)

    if request.method == 'GET':
        serializer = CarSerializer(car)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = CarSerializer(car, data=request.POST)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    elif request.method == 'DELETE':
        car.delete()
        return Response({'message': 'Car deleted successfully.'}, status=204)

# Similarly, define views for Customer and Reservation CRUD operations


@api_view(['GET', 'POST'])
def customer_list(request):
    if request.method == 'GET':
        customers = Customer.objects.all()
        serializer = CustomerSerializer(customers, many=True)
        return Response(serializer.data, safe=False)
    elif request.method == 'POST':
        serializer = CustomerSerializer(data=request.POST)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

@api_view(['GET', 'PUT', 'DELETE'])
def customer_detail(request, pk):
    customer = get_object_or_404(Customer, pk=pk)

    if request.method == 'GET':
        serializer = CustomerSerializer(customer)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = CustomerSerializer(customer, data=request.POST)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    elif request.method == 'DELETE':
        customer.delete()
        return Response({'message': 'Customer deleted successfully.'}, status=204)


@api_view(['GET', 'POST'])
def reservation_list(request):
    if request.method == 'GET':
        reservations = Reservation.objects.all()
        serializer = ReservationSerializer(reservations, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = ReservationSerializer(data=request.POST)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

@api_view(['GET', 'PUT', 'DELETE'])
def reservation_detail(request, pk):
    reservation = get_object_or_404(Reservation, pk=pk)

    if request.method == 'GET':
        serializer = ReservationSerializer(reservation)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = ReservationSerializer(reservation, data=request.POST)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    elif request.method == 'DELETE':
        reservation.delete()
        return Response({'message': 'Reservation deleted successfully.'}, status=204)
















# from django.http import JsonResponse
# from django.views.decorators.csrf import csrf_exempt

# @csrf_exempt
# def car_list(request):
#     if request.method == 'GET':
#         cars = Car.objects.all()
#         serializer = CarSerializer(cars, many=True)
#         return JsonResponse(serializer.data, safe=False)
#     elif request.method == 'POST':
#         serializer = CarSerializer(data=request.POST)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data, status=201)
#         return JsonResponse(serializer.errors, status=400)

# @csrf_exempt
# def car_detail(request, pk):
#     car = get_object_or_404(Car, pk=pk)

#     if request.method == 'GET':
#         serializer = CarSerializer(car)
#         return JsonResponse(serializer.data)

#     elif request.method == 'PUT':
#         serializer = CarSerializer(car, data=request.POST)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data)
#         return JsonResponse(serializer.errors, status=400)

#     elif request.method == 'DELETE':
#         car.delete()
#         return JsonResponse({'message': 'Car deleted successfully.'}, status=204)

# Similarly, define views for Customer and Reservation CRUD operations



# @csrf_exempt
# def customer_list(request):
#     if request.method == 'GET':
#         customers = Customer.objects.all()
#         serializer = CustomerSerializer(customers, many=True)
#         return JsonResponse(serializer.data, safe=False)
#     elif request.method == 'POST':
#         serializer = CustomerSerializer(data=request.POST)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data, status=201)
#         return JsonResponse(serializer.errors, status=400)

# @csrf_exempt
# def customer_detail(request, pk):
#     customer = get_object_or_404(Customer, pk=pk)

#     if request.method == 'GET':
#         serializer = CustomerSerializer(customer)
#         return JsonResponse(serializer.data)

#     elif request.method == 'PUT':
#         serializer = CustomerSerializer(customer, data=request.POST)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data)
#         return JsonResponse(serializer.errors, status=400)

#     elif request.method == 'DELETE':
#         customer.delete()
#         return JsonResponse({'message': 'Customer deleted successfully.'}, status=204)


# @csrf_exempt
# def reservation_list(request):
#     if request.method == 'GET':
#         reservations = Reservation.objects.all()
#         serializer = ReservationSerializer(reservations, many=True)
#         return JsonResponse(serializer.data, safe=False)
#     elif request.method == 'POST':
#         serializer = ReservationSerializer(data=request.POST)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data, status=201)
#         return JsonResponse(serializer.errors, status=400)

# @csrf_exempt
# def reservation_detail(request, pk):
#     reservation = get_object_or_404(Reservation, pk=pk)

#     if request.method == 'GET':
#         serializer = ReservationSerializer(reservation)
#         return JsonResponse(serializer.data)

#     elif request.method == 'PUT':
#         serializer = ReservationSerializer(reservation, data=request.POST)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data)
#         return JsonResponse(serializer.errors, status=400)

#     elif request.method == 'DELETE':
#         reservation.delete()
#         return JsonResponse({'message': 'Reservation deleted successfully.'}, status=204)