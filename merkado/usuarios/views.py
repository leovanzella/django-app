from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.views.generic.base import View
from perfis.models import Perfil
from usuarios.forms import RegistrarUsuariosForm


class RegistrarUsuarioView(View):

    template_name = 'registrar.html'

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):

        form = RegistrarUsuariosForm(request.POST)

        if form.is_valid():
            dados_form = form.data

            usuario = User.objects.create_user(dados_form['nome'], dados_form['email'], dados_form['senha'])

            perfil = Perfil(nome=dados_form['nome'], telefone=dados_form['telefone'], nome_empresa=dados_form['nome_empresa'], usuario=usuario)

            perfil.save()

            return redirect('/')

        return render(request, self.template_name, {'form': form})
