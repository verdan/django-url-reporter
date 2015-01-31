import sys
import operator


class HtmlReportPresenter(object):
    def __init__(self, item):
        self.item = item
        self.content_of_page = self.item.get_text()
        self.words_list = self.content_of_page.split()

    def create_unique_word_dict(self):
        freq_dict = {}
        for word in self.words_list:
            word = word.lower()
            if word.isalnum() and word in freq_dict.keys():
                freq_dict[word] += 1
            else:
                freq_dict[word] = 1

        return freq_dict

    @property
    def title(self):
        return self.item.title.string

    @property
    def size(self):
        bytes = sys.getsizeof(self.content_of_page, int)
        kilobytes = bytes / 1024
        return '%.2fKb' % kilobytes

    @property
    def words_count(self):
        return len(self.words_list)

    @property
    def unique_words_count(self):
        unique_words = set(self.words_list)
        return len(unique_words)

    @property
    def common_words(self):
        freq_dict = self.create_unique_word_dict()
        freq_sorted = sorted(freq_dict.items(), key=operator.itemgetter(1), reverse=True)
        top_five = [item[0] for item in freq_sorted[:5]]
        return top_five

    @property
    def links(self):
        links_list = []
        links_on_page = self.item.find_all('a')
        for link in links_on_page:
            if link.text:
                links_list.append('Link Text:%s | Link URL:%s' % (link.text, link.attrs.get('href')))
        return links_list

    @property
    def metas(self):
        metas_list = []
        metas = self.item.find_all('meta', hidden=True)
        for meta in metas:
            meta_name = meta.attrs.get('name')
            if meta_name:
                metas_list.append(meta.attrs.get('name'))
        return metas_list


