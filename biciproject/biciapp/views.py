import http
import json
from unicodedata import name
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotAllowed, HttpResponseBadRequest
from .models import Bike, Customers

# Create your views here.
def newCustomer(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body) 
            customer = Customers.objects.filter(customer_id = data['documento']).first()
            if (customer):
                return HttpResponseBadRequest("Ya existe un cliente con ese id") 
            customer = Customers(
                customer_id = data["documento"],
                first_name = data["primernombre"],
                middle_name = data["segundonombre"],
                first_surname = data["primerapellido"],
                second_surname = data["segundoapellido"],
                phone = data["telefono"],
                email = data["correo"],
                departament = data["departamento"],
                city = data["ciudad"],
                neighborhood = data["barrio"],
                address = data["direccion"],
                password = data["contrasena"],
            )
            customer.save()
            return HttpResponse("Registro exitoso.")
        except:
            return HttpResponseBadRequest("Error en la data")
    else:
        return HttpResponseNotAllowed(['POST'], "Metodo invalid")
def getCustomers(request):
    if request.method == 'GET':
        customers = Customers.objects.all()
        allCustomersData = []
        for customer in customers:
            data = {
                "documento": customer.customer_id,
                "primernombre": customer.first_name,
                "segundonombre": customer.middle_name,
                "primerapellido": customer.first_surname,
                "segundoapellido": customer.second_surname,
                "telefono": customer.phone,
                "correo": customer.email,
                "departamento": customer.departament,
                "ciudad": customer.city,
                "barrio": customer.neighborhood,
                "direccion": customer.address,
                "contrasena": customer.password,
            }
            allCustomersData.append(data)
        dataJson = json.dumps(allCustomersData)
        resp = HttpResponse()
        resp.headers['Content-Type'] = "text/json"
        resp.content = dataJson
        return resp
    else:
        return HttpResponseNotAllowed(['GET'],"Metodo invalid")
def getOneCustomer(request, id):
    if request.method == 'GET':
        customer = Customers.objects.filter(customer_id = id).first()
        if (not customer):
            return HttpResponseBadRequest("El cliente no existe.")
        data = {
            "documento": customer.customer_id,
            "primernombre": customer.first_name,
            "segundonombre": customer.middle_name,
            "primerapellido": customer.first_surname,
            "segundoapellido": customer.second_surname,
            "telefono": customer.phone,
            "correo": customer.email,
            "departamento": customer.departament,
            "ciudad": customer.city,
            "barrio": customer.neighborhood,
            "direccion": customer.address,
            "contrasena": customer.password,
        }
        dataJson = json.dumps(data)
        resp = HttpResponse()
        resp.headers['Content-Type'] = "text/json"
        resp.content = dataJson
        return resp
    else:
        return HttpResponseNotAllowed(['GET'], "Método inválido")
def deleteCustomer(request, id):
    if request.method == 'DELETE':
        try:
            customer = Customers.objects.filter(customer_id = id).first()
            if (not customer):
                return HttpResponseBadRequest("No existe el cliente")
            customer.delete()
            return HttpResponse("Cliente Eliminado")
        except:
            return HttpResponseBadRequest("Error en la data")
    else:
        return HttpResponseNotAllowed(['DELETE'], "Method invalid")
def updateCustomer(request, id):
    if request.method == 'PUT':
        try:
            customer = Customers.objects.filter(customer_id = id).first()
            if (not customer):
                return HttpResponseBadRequest("EL cliente no existe")
            data = json.loads(request.body)
            customer.first_name = data["primernombre"]
            customer.middle_name = data["segundonombre"]
            customer.first_surname = data["primerapellido"]
            customer.second_surname = data["segundoapellido"]
            customer.phone = data["telefono"]
            customer.email = data["correo"]
            customer.departament = data["departamento"]
            customer.city = data["ciudad"]
            customer.neighborhood = data["barrio"]
            customer.address = data["direccion"]
            customer.password = data["contrasena"]
            customer.save()
            return HttpResponse("Cliente Actualizado")
        except:
            return HttpResponseBadRequest("Error en la data")
    else:
        return HttpResponseNotAllowed(['PUT'],"Method invalid")       

#Bikes

def newBike(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            bike = Bike.objects.filter(bike_id = data['codigo']).first()
            if (bike):
                return HttpResponseBadRequest("producto repetido") 
            bike = Bike(
                bike_id = data["codigo"],
                bike_name = data["nombre"],
                description = data["descripcion"],
                bike_category = data["categoria"],
                country = data["pais"],
                bike_image = data["imagen"],
                brand = data["marca"],
                color = data["color"],
                size_rin = data["tallarin"],
                size_frame = data["tallamarco"],
                brake_system = data["sistemafrenos"],
                year = data["anio"],
                bike_price = data["preciounitario"],
                stock = data["stock"],
            )
            bike.save()
            return HttpResponse("Registro exitoso")
        except:
            return HttpResponseBadRequest
    else:
        return HttpResponseNotAllowed(['POST'], "Method invalid")
def getAllBikes(request):
    if request.method == 'GET':
        bikes = Bike.objects.all()
        allBikesData = []
        for bike in bikes:
            data = {
                "codigo": bike.bike_id,
                "nombre": bike.bike_name,
                "descripcion": bike.description,
                "categoria": bike.bike_category,
                "pais": bike.country,
                "imagen":bike.bike_image,
                "marca": bike.brand,
                "color": bike.color,
                "tallarin": bike.size_rin,
                "tallamarco": bike.size_frame,
                "sistemafrenos": bike.brake_system,
                "anio": str(bike.year),
                "preciounitario": float(bike.bike_price),
                "stock": bike.stock
            }
            allBikesData.append(data)
        dataJson = json.dumps(allBikesData)
        resp = HttpResponse("Consulta exitosa")
        resp.headers['Content-Type'] = "text/json"
        resp.content = dataJson
        return resp
    else:
        return HttpResponseNotAllowed(['GET'],"Method invalid")
def getOneBike(request, id):
    if request.method == 'GET':
        bike = Bike.objects.filter(bike_id = id).first()
        if (not bike):
            return HttpResponseBadRequest("El producto no existe")
        data = {
            "codigo": bike.bike_id,
            "nombre": bike.bike_name,
            "descripcion": bike.description,
            "categoria": bike.bike_category,
            "pais": bike.country,
            "imagen":bike.bike_image,
            "marca": bike.brand,
            "color": bike.color,
            "tallarin": bike.size_rin,
            "tallamarco": bike.size_frame,
            "sistemafrenos": bike.brake_system,
            "anio": str(bike.year),
            "preciounitario": float(bike.bike_price),
            "stock": bike.stock
        }
        dataJson = json.dumps(data)
        resp = HttpResponse()
        resp.headers['Content-Type'] = "text/json"
        resp.content = dataJson
        return resp
    else:
        return HttpResponseNotAllowed(['GET'],"Method invalid")

def updateBike(request, id):
    if request.method == 'PUT':
        try:
            bike = Bike.objects.filter(bike_id = id).first()
            if (not bike):
                return HttpResponseBadRequest("El producto no existe")
            data = json.loads(request.body)
            bike.bike_name = data["nombre"]
            bike.description = data["descripcion"]
            bike.bike_category = data["categoria"]
            bike.country = data["pais"]
            bike.bike_image = data["imagen"]
            bike.brand = data["marca"]
            bike.color = data["color"]
            bike.size_rin = data["tallarin"]
            bike.size_frame = data["tallamarco"]
            bike.brake_system = data["sistemafrenos"]
            bike.year = data["anio"]
            bike.bike_price = data["preciounitario"]
            bike.stock = data["stock"]
            bike.save()
            return HttpResponse("Producto actualizado")
        except:
            return HttpResponseBadRequest("Error en la data")
    else:
        return HttpResponseNotAllowed(['PUT'], "Method invalid")
def deleteBike(request, id):
    if request.method == 'DELETE':
        try:
            bike = Bike.objects.filter(bike_id = id).first()
            if (not bike):
                return HttpResponseBadRequest("El producto no existe")
            bike.delete()
            return HttpResponse("Producto eliminado")
        except:
            return HttpResponseBadRequest("Error en la data")
    else:
        return HttpResponseNotAllowed(['DELETE'],"Method invalid")