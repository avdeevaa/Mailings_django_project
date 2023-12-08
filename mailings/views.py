from django.shortcuts import render, reverse
from mailings.models import Message, Client
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView


class MessageListView(ListView):
    """ shows main page"""
    model = Message
    template_name = 'mailings/main_page.html'


class MessageDetailView(DetailView):
    """ shows one item (mailing message)"""
    model = Message
    template_name = 'mailings/message_detail.html'


class MessageUpdateView(UpdateView):
    """makes changes in the model Massage == UPDATE"""
    model = Message
    fields = ('subject', 'body', 'settings')
    template_name = 'mailings/message_form.html'

    def get_success_url(self):
        return reverse('mailings:main_page')


class MessageDeleteView(DeleteView):
    """deletes one model of Message"""
    model = Message
    template_name = 'mailings/message_confirm_delete.html'

    def get_success_url(self):
        return reverse('mailings:main_page')


class MessageCreateView(CreateView):
    model = Message
    fields = ('subject', 'body', 'settings')
    template_name = 'mailings/message_form.html'

    def get_success_url(self):
        return reverse('mailings:main_page')


class ClientListView(ListView):
    """ shows all clients"""
    model = Client
    template_name = 'mailings/client_list.html'


class ClientDetailView(DetailView):
    """ shows one item (one client)"""
    model = Client
    template_name = 'mailings/client_detail.html'


class ClientUpdateView(UpdateView):
    """makes changes in the model Client == UPDATE"""
    model = Client
    fields = ('name', 'fathers_name', 'surname', 'email', 'comment')
    template_name = 'mailings/client_form.html'

    def get_success_url(self):
        return reverse('mailings:all_clients')


class ClientCreateView(CreateView):
    model = Client
    fields = ('name', 'fathers_name', 'surname', 'email', 'comment')
    template_name = 'mailings/client_form.html'

    def get_success_url(self):
        return reverse('mailings:all_clients')


class ClientDeleteView(DeleteView):
    """deletes one model of Client"""
    model = Client
    template_name = 'mailings/client_confirm_delete.html'

    def get_success_url(self):
        return reverse('mailings:all_clients')


# def main_page(request):
#     # products_list = Product.objects.all()
#     # context = {
#     #     'object_list': products_list
#     # }
#     return render(request, 'mailings/main_page.html', )
# #
#
# def contact_page(request):
#     if request.method == "POST":
#         name = request.POST.get('name')
#         phone = request.POST.get('phone')
#         message = request.POST.get('message')
#         print(f"Форма обрабатывает {name}, {phone}, {message}")
#     return render(request, 'design/contact_page.html')
#
#
# def items_page(request):
#     products_list = Product.objects.all()
#     context = {
#         'object_list': products_list
#     }
#     return render(request, 'design/items_page.html', context)
#
#
# class ProductDetailView(DetailView):
#     """ replaces item_detail"""
#     model = Product
#     template_name = 'design/item_detail.html'
#
# #
# # def item_detail(request, pk):
# #     product = get_object_or_404(Product, pk=pk)
# #     context = {
# #         'product': product
# #     }
# #     return render(request, 'design/item_detail.html', context)


#
# class BlogListView(ListView):
#     model = Blog
#     template_name = 'design/blog_list.html'
#
#     def get_queryset(self, *args, **kwargs):
#         queryset = super().get_queryset()
#         queryset = queryset.filter(publication_sign=True)
#         return queryset
#
#
# class BlogDetailView(DetailView):
#     model = Blog
#     template_name = 'design/blog_detail.html'
#
#     def get_object(self, queryset=None):
#         self.object = super().get_object(queryset)
#         self.object.number_of_views += 1
#         self.object.save()
#         return self.object
