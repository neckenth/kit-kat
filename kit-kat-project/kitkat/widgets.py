from django.forms import DateTimeInput


class XDSoftDateTimePickerInput(DateTimeInput):
    template_name = './templates/widgets/xdsoft_datetimepicker.html'
