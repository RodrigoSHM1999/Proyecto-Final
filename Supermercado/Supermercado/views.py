from django.http import HttpResponse

from django.views.generic import View

from django.template.loader import get_template
from market.models import Compra
from .utils import render_to_pdf

class GeneratePDF(View):
    def get(self,request, *args, **kwargs):
        template = get_template('invoice.html')
        context = {
            "invoice_id": 123,
            "customer_super":"Supermercado Todo al Paso",
            "customer_name": "David",
            "amount": 24,
            "today":"13/08/2020",
        }
        html = template.render(context)
        pdf = render_to_pdf('invoice.html', context)
        if pdf:
            response = HttpResponse(pdf, content_type='application/pdf')
            filename = "Invoice_%s.pdf" %("12341231")
            content = "inline; filename='%s'" %(filename)
            
            download = request.GET.get("download")
            if download:
                 content = "attachment; filename='%s'" %(filename)
            response['Content-Disposition'] = content
            return response
        return HttpResponse("Not found ")