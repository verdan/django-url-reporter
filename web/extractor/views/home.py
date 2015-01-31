import urllib2

from bs4 import BeautifulSoup

from report.libs.base_view import BaseView
from web.extractor.forms.url_form import UrlForm
from web.extractor.presenter import HtmlReportPresenter


class HomePageView(BaseView):
    template_name = 'extractor/home.html'

    @staticmethod
    def get_html_content(from_url):
        request_to_hit_url = urllib2.Request(from_url)
        try:
            response = urllib2.urlopen(request_to_hit_url)
            return response.read()
        except urllib2.URLError:
            return None

    def get_context_data(self, **kwargs):
        url_form = kwargs.get('url_form')
        report_url = url_form.cleaned_data.get('url').lower()

        html_content = self.get_html_content(from_url=report_url)
        if html_content:
            html_doc_dict = BeautifulSoup(html_content)
            kwargs.update({'report': HtmlReportPresenter(html_doc_dict)})
        else:
            url_form.add_error(field='url', message='There was an error trying to fetch data. Please try again.')

        return super(HomePageView, self).get_context_data(**kwargs)

    def get(self):
        return {'url_form': UrlForm()}

    def post(self):
        url_form = UrlForm(self.request.POST)
        if not url_form.is_valid():
            return {'url_form': url_form}

        return self.get_context_data(url_form=url_form)


def home_view(request):
    return HomePageView(request).respond_with()
