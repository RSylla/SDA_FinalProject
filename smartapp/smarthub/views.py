from django.shortcuts import render
from django.views.generic import FormView
from django.urls import reverse_lazy
<<<<<<< HEAD
<<<<<<< HEAD
=======
from smarthub.forms import SmartAppForm
from smarthub.a_tickets import remove_extra, count_characters
from smarthub.k_tickets import punctuation_removal, text_upper, text_lower, remove_new_line, word_summary
=======
>>>>>>> Anneli
from .forms import SmartAppForm
from .a_tickets import remove_extra, count_characters, spell_check, remove_stopwords
from .k_tickets import punctuation_removal, text_upper, text_lower, remove_new_line, word_summary
from string import punctuation
<<<<<<< HEAD
=======
from smarthub.forms import SmartAppForm
from smarthub.a_tickets import remove_extra, count_characters
from smarthub.k_tickets import punctuation_removal, text_upper, text_lower, remove_new_line, word_summary
>>>>>>> Anneli
=======
>>>>>>> 1e8946203ccb68e38738d3840b19f600bc11bcae
>>>>>>> Anneli
"""Raivo added 2 sampleviews for UI.
Later it will be automatically generated by class FormView"""


class SmartAppView(FormView):
    template_name = 'index.html'
    form_class = SmartAppForm
    success_url = reverse_lazy('guide')

    def form_valid(self, form):
        global form_data
        form_data = form.cleaned_data
        return super().form_valid(form)



def guideView(request):
    changed_data = {}
    text = form_data['text']
    edited_text = text
    if bool(form_data['gen_word_summary']):
        changed_data['Generate Summary Of a Word:'] = word_summary(text)
        edited_text = word_summary(text)
        text = edited_text
    if bool(form_data['remove_punctuations']):
        changed_data['Remove Punctuations:'] = punctuation_removal(text, punctuation)
        edited_text = punctuation_removal(edited_text, punctuation)
    if bool(form_data['upper_case']):
        changed_data['Upper Case:'] = text_upper(text)
        edited_text = text_upper(edited_text)
    if bool(form_data['lower_case']):
        changed_data['Lower Case:'] = text_lower(text)
        edited_text = text_lower(edited_text)
    if bool(form_data['new_line_remove']):
        changed_data['New Line Remove:'] = remove_new_line(text)
        edited_text = remove_new_line(edited_text)
    if bool(form_data['extra_space_remove']):
        changed_data['Extra Space Remove:'] = remove_extra(text)
        edited_text = remove_extra(edited_text)
    if bool(form_data['count_characters']):
        changed_data['Count Characters:'] = " ".join(count_characters(text))
    if bool(form_data['spell_check']):
        changed_data['Spell Check:'] = spell_check(text)[1]
        edited_text = spell_check(edited_text)[0]
    if bool(form_data['remove_stop']):
        changed_data['Remove Stop Words of your Paragraph:'] = remove_stopwords(str(text))
        edited_text = remove_stopwords(str(edited_text))

    context = {
        'edited_text': edited_text,
        'content': changed_data
    }
    return render(request, template_name='guide.html', context=context)

