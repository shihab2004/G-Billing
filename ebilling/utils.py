from io import BytesIO
from django.http import HttpResponse,Http404
from django.template.loader import get_template
from ebilling.models import Company
from xhtml2pdf import pisa

from ebilling.models import History

def render_to_pdf(template_src, context_dict={}):
    template = get_template(template_src)
    html  = template.render(context_dict)
    result = BytesIO()
    pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result)
    if not pdf.err:
        return HttpResponse(result.getvalue(), content_type='application/pdf')
    return None

def Log(request,task):
    return History.objects.create(user=request.user,task=task,company=request.user.getCompany.get())


def check_permission(name=""):
    def _viewFunc(function):
        def main(request,*args, **kwargs):
            if request.user.getPermissions.filter(task=name).exists():
                pass
            elif request.user.is_staff:
                pass
            else:
                raise Http404()
            return function(request,*args, **kwargs)
        return main
    return _viewFunc