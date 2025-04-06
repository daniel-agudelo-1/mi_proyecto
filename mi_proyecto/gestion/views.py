from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from .forms import ClienteForm
from .models import Cliente
import csv
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, TableStyle, Paragraph, Table, TableStyle
from reportlab.lib import colors 
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.pdfgen import canvas
from openpyxl import Workbook
# gestion/views.py
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from .serializers import ClienteSerializer


def index(request):
    return render(request, 'index.html')

def clientes(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('clientes')
    else:
        form = ClienteForm()

    lista_clientes = Cliente.objects.all()
    return render(request, 'clientes.html', {'form': form, 'clientes': lista_clientes})



# Editar cliente
def editar_cliente(request, id):
    cliente = get_object_or_404(Cliente, id=id)
    if request.method == 'POST':
        form = ClienteForm(request.POST, instance=cliente)
        if form.is_valid():
            form.save()
            return redirect('clientes')
    else:
        form = ClienteForm(instance=cliente)
    return render(request, 'editar_cliente.html', {'form': form})

# Eliminar cliente
def eliminar_cliente(request, id):
    cliente = get_object_or_404(Cliente, id=id)
    if request.method == 'POST':
        cliente.delete()
        return redirect('clientes')
    return render(request, 'confirmar_eliminar.html', {'cliente': cliente})

# Exportar clientes a CSV
def exportar_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="clientes.csv"'
    writer = csv.writer(response)
    writer.writerow(['Documento', 'Nombres', 'Apellidos', 'Teléfono', 'Correo'])
    clientes = Cliente.objects.all()
    for cliente in clientes:
        writer.writerow([cliente.documento, cliente.nombres, cliente.apellidos, cliente.telefono, cliente.correo])
    return response


"""# Exportar clientes a PDF
def exportar_pdf(request):
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="clientes.pdf"'
    p = canvas.Canvas(response, pagesize=letter)
    p.drawString(100, 750, "Lista de Clientes")
    clientes = Cliente.objects.all()
    y = 730
    for cliente in clientes:
        p.drawString(100, y, f"{cliente.documento} - {cliente.nombres} {cliente.apellidos} - {cliente.telefono} - {cliente.correo}")
        y -= 20
    p.showPage()
    p.save()
    return response  
"""
#exportar clientes a pdf 
def exportar_pdf (request):
    response  = HttpResponse(content_type='aplicacion/pdf')
    response  ['content-Disposition'] = 'attachment; filename="clientes.pdf"'
    doc = SimpleDocTemplate(response, pagesize = letter)
    elements = []
    
    styles = getSampleStyleSheet ()
    title = Paragraph ("lista de Clientes", styles ['Title'])
    elements.append(title)
    
    #encabezado de la tabla
    data =[["Documento", "Nombre", "Apellido", "Teléfono","Correo electrónico"]]

    clientes = Cliente.objects.all()
    for cliente in clientes:
        data.append([
            cliente.documento,
            cliente.nombres,
            cliente.apellidos,
            cliente.telefono,
            cliente.correo
        ])
    table = Table(data, colWidths=[80, 100, 100, 80, 150])
    
    style = TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.grey),  # fondo encabezado
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),  # texto encabezado
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),  # fuente encabezado
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),  # espacio abajo del encabezado
        ('GRID', (0, 0), (-1, -1), 1, colors.black),  # bordes
    ])
    table.setStyle(style)

    elements.append(table)
    doc.build(elements)

    return response
    
    
# Exportar clientes a Excel
def exportar_excel(request):
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="clientes.xlsx"'
    wb = Workbook()
    ws = wb.active
    ws.append(['Documento', 'Nombres', 'Apellidos', 'Teléfono', 'Correo'])
    clientes = Cliente.objects.all()
    for cliente in clientes:
        ws.append([cliente.documento, cliente.nombres, cliente.apellidos, cliente.telefono, cliente.correo])
    wb.save(response)
    return response

class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer
    permission_classes = [IsAuthenticated]
    
def autor(request):
    return render(request, 'autor.html')
