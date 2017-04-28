from django import forms
from datetimewidget.widgets import DateTimeWidget, DateWidget, TimeWidget
from .models import Event

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ('eventType','title','day','start','end','street','city','state','description')
        dateOptions = {
            'format': 'yyyy-mm-dd',
            'autoclose': True,
        }
        timeOptions = {
            'format': 'hh:ii',
            'autoclose': True,
            'showMeridian': True,
            'minuteStep': 30
        }
        widgets = {
            'day': DateWidget(options=dateOptions),
            'start': TimeWidget(options=timeOptions),
            'end': TimeWidget(options=timeOptions)
        }

