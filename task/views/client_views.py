from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from ..models import Client  # Ensure you import the 'Client' model

def add_client(request):
    if request.method == 'POST':
        name = request.POST.get('nome')
        cpf = request.POST.get('cpf')
        rg = request.POST.get('rg')
        birth_date = request.POST.get('data_nascimento')
        contact = request.POST.get('contato')
        email = request.POST.get('email')
        gender = request.POST.get('genero')
        whatsapp = request.POST.get('whatsapp')
        zip_code = request.POST.get('cep')
        address = request.POST.get('logradouro')
        house_number = request.POST.get('numero_casa')
        neighborhood = request.POST.get('bairro')

        # Validate house number as an integer
        try:
            house_number = int(house_number)
        except (ValueError, TypeError):
            messages.error(request, "Invalid house number.")
            return render(request, 'tasks/cliente.html')

        # Ensure all required fields are filled
        if not all([name, rg, cpf, contact, gender, birth_date, zip_code, address, neighborhood]):
            messages.error(request, "All required fields must be filled.")
            return render(request, 'tasks/cliente.html')

        # Try to create and save a new client
        try:
            new_client = Client(
                name=name,
                cpf=cpf,
                rg=rg,
                birth_date=birth_date,
                contact=contact,
                email=email,
                gender=gender,
                whatsapp=whatsapp,
                zip_code=zip_code,
                address=address,
                house_number=house_number,
                neighborhood=neighborhood
            )
            new_client.save()
            messages.success(request, "Client added successfully!")
            return redirect('add_client')
        except Exception as e:
            messages.error(request, f"An error occurred while adding the client: {e}")
            return render(request, 'tasks/cliente.html')

    clients = Client.objects.all()
    return render(request, 'tasks/cliente.html', {'clients': clients})

def edit_client(request, client_id):
    client = get_object_or_404(Client, id=client_id)

    if request.method == 'POST':
        client.name = request.POST.get('nome')
        client.cpf = request.POST.get('cpf')
        client.rg = request.POST.get('rg')
        client.birth_date = request.POST.get('data_nascimento')
        client.gender = request.POST.get('genero')
        client.contact = request.POST.get('contato')
        client.whatsapp = request.POST.get('whatsapp')
        client.email = request.POST.get('email')
        client.zip_code = request.POST.get('cep')
        client.address = request.POST.get('logradouro')
        client.house_number = request.POST.get('numero_casa')
        client.neighborhood = request.POST.get('bairro')
        client.pis_pasep = request.POST.get('pis_pasep')
        client.series = request.POST.get('serie')
        client.number = request.POST.get('numero')
        client.state = request.POST.get('uf')

        # Validate house number as an integer
        try:
            client.house_number = int(client.house_number)
        except (ValueError, TypeError):
            messages.error(request, "Invalid house number.")
            return render(request, 'tasks/edit_client.html', {'client': client})

        # Ensure all required fields are filled
        if not all([client.name, client.rg, client.cpf, client.contact, client.gender, client.birth_date, client.zip_code, client.address, client.neighborhood]):
            messages.error(request, "All required fields must be filled.")
            return render(request, 'tasks/edit_client.html', {'client': client})

        # Try to save the updated client
        try:
            client.save()
            messages.success(request, 'Client updated successfully!')
            return redirect('clients')
        except Exception as e:
            messages.error(request, f"Something went wrong: {e}")
            return render(request, 'tasks/edit_client.html', {'client': client})

    return render(request, 'tasks/edit_client.html', {'client': client})

def delete_client(request, client_id):
    client = get_object_or_404(Client, id=client_id)
    if request.method == 'POST':
        client.delete()
        messages.success(request, 'Client deleted successfully!')
    return render(request, 'tasks/client.html')
